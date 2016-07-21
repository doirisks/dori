<?php
    /**
     * constants.php
     *
     * DOI Risk Interface
     *
     * Global constants.
     */

    // your database's name
    define("DATABASE", "doiarchive");

    // your database's password
    define("PASSWORD", "bitnami");

    // your database's server
    define("SERVER", "localhost");

    // your database's username
    define("USERNAME", "doirisks");
    
    define("MODELROOT","/src/models/");

    /**
     * Executes SQL statement, possibly with parameters, returning
     * an array of all rows in result set or false on (non-fatal) error.
     *
     * code from cs50 course materials
     */
    function query(/* $sql [, ... ] */)
    {
        // SQL statement
        $sql = func_get_arg(0);

        // parameters, if any
        $parameters = array_slice(func_get_args(), 1);

        // try to connect to database
        static $handle;
        if (!isset($handle))
        {
            try
            {
                // connect to database
                $handle = new PDO("mysql:dbname=" . DATABASE . ";host=" . SERVER, USERNAME, PASSWORD);

                // ensure that PDO::prepare returns false when passed invalid SQL
                $handle->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); 
            }
            catch (Exception $e)
            {
                // trigger (big, orange) error
                trigger_error($e->getMessage(), E_USER_ERROR);
                exit;
            }
        }

        // prepare SQL statement
        $statement = $handle->prepare($sql);
        if ($statement === false)
        {
            // trigger (big, orange) error
            trigger_error($handle->errorInfo()[2], E_USER_ERROR);
            exit;
        }

        // execute SQL statement
        $results = $statement->execute($parameters);

        // return result set's rows, if any
        if ($results !== false)
        {
            return $statement->fetchAll(PDO::FETCH_ASSOC);
        }
        else
        {
            return false;
        }
    }
    
    /**
     * Cleans input, expands known CUIs to find directly derived CUIs
     */
    function prep_CUIs(&$CUIs, &$CUI_vals, $QUERYDATA) {// cleaning (and debugging)
        $CUIs = array_keys($QUERYDATA);
        $CUI_vals = [];
        foreach ($CUIs as $CUI) {
            $CUI = htmlspecialchars ($CUI);
            $CUI_vals[$CUI] = $QUERYDATA[$CUI];
            // debugging CUIs passed
            //echo "<p>" . $CUI . ", ". $_GET[$CUI] . "</p>\n";
        }
        
        // expanding known CUIs
        // sex (m/f)
        if (in_array('C28421', $CUIs)) {
            array_push($CUIs,'C0086582');               //male sex CUI
            //array_push($CUIs,'');                       //female sex CUI
            if (strcasecmp($CUI_vals['C28421'],'male') == 0) {
                $CUI_vals['C0086582'] = 'true';
                //$CUI_vals['???'] = 'false';               //female sex
            }
            else {
                $CUI_vals['C0086582'] = 'false';
                //$CUI_vals['???'] = 'true';                //female sex
            }
        }

        // BMI
        if (in_array('heightCUI',$CUIs) && in_array('weightCUI',$CUIs)) {
            array_push($CUIs,'BMI_CUI');
            $CUI_vals['BMI_CUI'] = $CUI_vals['BMI_CUI']; #TODO
        }
        
        // add disjunctive CUIs ("CUIs" with OR in them)
        // build a query
        $to_query = "SELECT `CUI` FROM `CUIs` WHERE (CUI != '";
        foreach ($CUIs as $CUI) {
            if ( $CUI_vals[$CUI] === true ) {
                $to_query .= $CUI;
                $to_query .= "' AND CUI LIKE '%";
                $to_query .= $CUI;
                $to_query .= "%') OR ( CUI != '";
            }
        }
        // only use the query if something was added to it
        if (strcasecmp($to_query,"SELECT `CUI` FROM `CUIs` WHERE (CUI != '") == 0) {
            // do nothing
        }
        else {
            $to_query = substr($to_query,0,-14);
            // debug here
            #echo htmlspecialchars($to_query) . "\n";
            $data = query($to_query);
            foreach( $data as $datum ) {
                array_push($CUIs,$datum['CUI']);
                $CUI_vals[$datum['CUI']] = "true";
            }
        }
    }
    
    
    /**
     * Scores an id based on [already expanded] CUI value table
     */
    function score_id($id, $CUI_vals) {
        // response variable
        $resp = [];
    
        // check that id is numerical
        if ( !ctype_digit((string)$id) ){
            $resp['error'] = 'bad id';
            return($resp);
        }

        // get model data
        $model = query("SELECT `DOI`, `compiled`, `uncompiled`, `language`, `inpCUI`, `inpdatatype`, `upper`, `lower`  FROM `models` WHERE `id` = " . $id )[0];

        // unpack model data
        $inputs = json_decode($model['inpCUI']);
        $datatypes = json_decode($model['inpdatatype']);
        $uppers = json_decode($model['upper']);
        $lowers = json_decode($model['lower']);

        // assemble and CHECK model arguments
        $modelargs = array();
        foreach ($inputs as $index => $CUI) {               // TODO check CUIs and arguments

            // make sure a CUI value exists
            if (!isset($CUI_vals[$CUI])) {
                $resp['error'] = 'missing CUI: ' . $CUI;  // identify a missing CUI
                return($resp);
            }

            // get the CUI's value
            $arg = $CUI_vals[$CUI];
            
            // check that CUI's value is in valid range (unnecessary for bools!)
            if (!empty($lowers[$index]) and ($arg < $lowers[$index])) {
                $resp['error'] = 'CUI below acceptable range: ' . $CUI;  // CUI below acceptable range
                return($resp);
            }
            if (!empty($uppers[$index]) and ($arg > $uppers[$index])) {
                $resp['error'] = 'CUI above acceptable range: ' . $CUI;  // CUI above acceptable range
                return($resp);
            }
            
            if ($datatypes[$index] == 'bool') {     // bool, convert to integer
                if ($arg === true) {
                    $arg = '1';
                } else if ($arg === false) {
                    $arg = '0';
                } else if ($arg == "true") {
                    $arg = '1';
                } else if ($arg == "false") {
                    $arg = '0';
                } else {
                    $resp['error'] = 'bad boolean CUI: ' . $CUI;  // identify a bad bool
                    return($resp);
                }
            } 
            else if ($datatypes[$index] == 'integer' or $datatypes[$index] == 'int') { // integer
                if ( ctype_digit($arg) ){
                    // argument is already okay
                } else if ( ctype_digit(str_replace('.','',$arg)) ) { // only non-numbers are decimal points
                    if ( substr_count($arg,'.') == 1 && strlen($arg) > 1 ) { 
                        // if there is only one decimal point, round to nearest integer
                        $arg = (string)round((float)$arg);
                    } else {
                        // otherwise, error
                        $resp['error'] = 'bad integer CUI: ' . $CUI;  // identify a bad CUI
                        return($resp);
                    }
                } else {
                    $resp['error'] = 'bad integer CUI: ' . $CUI;  // identify a bad CUI
                    return($resp);
                }
            } 
            else  {    // float ($datatypes[$index] == 'float')
                if (ctype_digit($arg) ) {
                    // if already integer, tell code it is a float
                    $arg .= '.0';
                } else if (ctype_digit(str_replace('.','',$arg)) ) {
                    if (substr_count($arg,'.') == 1 && strlen($arg) > 1 ) {
                        // arg is already fine
                    }
                    else {
                        $resp['error'] = 'bad float CUI: ' . $CUI;  // identify a bad float
                        return($resp);
                    }
                } else {
                    $resp['error'] = 'bad float CUI: ' . $CUI;  // identify a bad float
                    return($resp);
                }
            }
            array_push($modelargs,$arg);
        }

        // calculate risk score
        $command = null;
        if ( strtolower($model['language']) == 'python' or strtolower($model['language']) == 'py') {
            $command = 'python ../../../../scripts/pythonrisk.py "' . MODELROOT . '" "' . $model['DOI'] . '"';
            $command .= " " . json_decode($model['uncompiled'])[0];
            foreach( $modelargs as $arg) {
                $command .= " " . $arg;
            }
        } else if ( strtolower($model['language']) == 'r' ) {
            $command = 'Rscript ../../../../scripts/Rrisk.R "' . MODELROOT . '" "' . $model['DOI'] . '"';
            $command .= " " . json_decode($model['compiled'])[0];
            foreach( $modelargs as $arg) {
                $command .= " " . $arg;
            }
        } else if ( strtolower($model['language']) == 'sas' ) {
            //TODO
        }

        // calculate risk score
        $modeloutput = array();
        exec($command,$modeloutput);
        if (count($modeloutput) < 1) {
            $resp['error'] = "no response from model";
        } else {
            // record the score!
            $resp['score'] = $modeloutput[0];
        }
        return($resp);
    }
?>
