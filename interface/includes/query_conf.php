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
    define("SERVER", "dori_mysql");

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
     * Check upper and lower bounds of an integer- or float-valued CUI, 
     * 
     * compares the 'value' with 'low' and 'upp', returns error message
     * append CUI after error message!
     */
    function check_bounds ($value, $low, $upp) {
        if ( ($low != null) and ($value < $low)) {
            return('bad CUI - value ' . $value . ' below bound of ' . $low . ': ');  // CUI below acceptable range
        }
        if ( ($upp != null) and ($value > $upp)) {
            return('bad CUI - value ' . $value . ' above bound of ' . $upp . ': ');  // CUI above acceptable range
        }
        else {
            return($value);
        }
    }
    
    
    /**
     * Cleans input, expands known CUIs to find directly derived CUIs
     */
    function prep_CUIs(&$CUIs, &$CUI_vals, $QUERYDATA) {// cleaning (and debugging)
        $allegedCUIs = array_keys($QUERYDATA);
        // accept only real CUIs
        $to_query = "SELECT `CUI`, `datatype`, `defaultlower`, `defaultupper`, `derivable` FROM `CUIs` WHERE CUI = '";
        foreach ($allegedCUIs as $CUI) {
            if ( ctype_alnum($CUI) ) {
                $to_query .= $CUI;
                $to_query .= "' OR CUI = '";
            }
        }
        $to_query .= "'";
        // break off without any effect if no CUIs were accepted
        if (strcasecmp($to_query,"SELECT `CUI`, `datatype`, `defaultlower`, `defaultupper`, `derivable` FROM `CUIs` WHERE CUI = '") == 0) {
            return(1);
        }
        // debug here
        #echo htmlspecialchars($to_query) . "\n";
        
        // query
        $data = query($to_query);
        
        // handle data
        $derivable = array();   // CUIs which may be derivable afterwards
        foreach( $data as $datum ) {
            // make sure a CUI value exists
            if (!isset($QUERYDATA[$datum['CUI']])) {
                $CUI_vals[$datum['CUI']] = 'bad CUI - no value given: ' . $datum['CUI'];  // identify a missing CUI
                continue;
            }

            // get the CUI's alleged value
            $arg = $QUERYDATA[$datum['CUI']];
            
            // bools
            if ($datum['datatype'] == 'bool') { 
                if (is_bool($arg)) {
                    // no action
                } else if ( ($arg == "true") or ($arg === 1) ) {    // recognize improper forms of "true"
                    $arg = true;
                } else if (($arg == "false") or ($arg === 0) ) {    // recognize improper forms of "false
                    $arg = false;
                } else if ( $arg == 'C28421' ) {
                    if (strcasecmp($arg, "male") == 0) {
                        $arg = true;
                    } else if (strcasecmp($arg, "female") == 0) {
                        $arg = false;
                    } else {
                        $CUI_vals[$datum['CUI']] = 'bad boolean CUI: ' . $datum['CUI'] . " = " . (string)$arg ;  // identify a bad bool
                        continue;
                    }
                } else {
                    $CUI_vals[$datum['CUI']] = 'bad boolean CUI: ' . $datum['CUI'] . " = " . (string)$arg ;  // identify a bad bool
                    continue;
                }
                // check for possibly derivable CUIs
                if ($datum['derivable'] != '[]') {
                    foreach (json_decode($datum['derivable']) as $maybe) {
                        array_push($derivable, $maybe);
                    }
                }
            } 
            // integers
            else if ($datum['datatype'] == 'integer' or $datum['datatype'] == 'int') { 
                if (is_string($arg)){
                    if ( ctype_digit($arg) ) {
                        $arg = (int)$arg;
                    } else if ( ctype_digit(str_replace('.','',$arg)) ) { // only non-numbers are decimal points
                        if ( substr_count($arg,'.') == 1 && strlen($arg) > 1 ) { 
                            // if there is only one decimal point, round to nearest integer
                            $arg = (string)round((float)$arg);
                        } else {
                            // otherwise, error
                            $CUI_vals[$datum['CUI']] = 'bad integer CUI: ' . $datum['CUI'];  // identify a bad CUI
                            continue;
                        }
                    } else {
                        $CUI_vals[$datum['CUI']] = 'bad integer CUI: ' . $datum['CUI'];  // identify a bad CUI
                        continue;
                    }
                } else if (is_float) { 
                    $arg = (int)round((float)$arg);
                } else if (!is_int($arg)) {
                    $CUI_vals[$datum['CUI']] = 'bad integer CUI: ' . $datum['CUI'];  // identify a bad CUI
                }
                
                // check upper and lower bounds
                $arg = check_bounds($arg,(int)$datum['defaultlower'],(int)$datum['defaultupper']);
                if (is_string($arg)){
                    $CUI_vals[$datum['CUI']] = $arg . $datum['CUI'];
                    continue;
                }
            } 
            // floats ($datatypes[$datum] == 'float')
            else  { 
                if (is_string($arg)) {   
                    if ( ctype_digit($arg) ) {
                        // if already integer, tell code it is a float
                        $arg = (float)$arg;
                    } else if (ctype_digit(str_replace('.','',$arg)) ) {
                        if (substr_count($arg,'.') == 1 && strlen($arg) > 1 ) {
                            $arg = (float)$arg;
                        }
                        else {
                            $CUI_vals[$datum['CUI']] = 'bad float CUI: ' . $datum['CUI'] . " = " . (string)$arg;  // identify a bad float
                            continue;
                        }
                    } else {
                        $CUI_vals[$datum['CUI']] = 'bad float CUI: ' . $datum['CUI'] . " = " . (string)$arg;  // identify a bad float
                        continue;
                    } 
                }
                else if (is_int($arg)){
                    $arg = (float)$arg;
                }
                else if (!is_float($arg)){
                    $CUI_vals[$datum['CUI']] = 'bad float CUI: ' . $datum['CUI'] . " = " . (string)$arg;  // identify a bad float
                }
                // check upper and lower bounds
                $arg = check_bounds($arg,(float)$datum['defaultlower'],(float)$datum['defaultupper']);
                if (is_string($arg)){
                    $CUI_vals[$datum['CUI']] = $arg . $datum['CUI'];
                    continue;
                }
            }
            
            // add verified CUIs
            array_push($CUIs,$datum['CUI']);
            $CUI_vals[$datum['CUI']] = $arg;
        }
        
        // expanding known CUIs
        // sex (m/f)
        if (in_array('C28421', $CUIs)) {
            array_push($CUIs,'C0086582');               //male sex CUI
            //array_push($CUIs,'');                       //female sex CUI
            if ($CUI_vals['C28421']) {
            // boolean true => male
                $CUI_vals['C0086582'] = true;
                //$CUI_vals['???'] = false;               //female sex
            }
            else {
                $CUI_vals['C0086582'] = false;
                //$CUI_vals['???'] = true;                //female sex
            }
        }

        // BMI
        if (in_array('heightCUI',$CUIs) && in_array('weightCUI',$CUIs)) {
            array_push($CUIs,'BMI_CUI');
            $CUI_vals['BMI_CUI'] = $CUI_vals['BMI_CUI']; #TODO
        }
        
        // add derivable boolean CUIs
        // build a query
        $to_query = "SELECT `CUI`, `derivedfrom` FROM `CUIs` WHERE CUI = '";
        foreach ($derivable as $maybe) {
            $to_query .= $maybe;
            $to_query .= "' OR CUI = '";
        }
        // only use the query if something was added to it
        if (strcasecmp($to_query,"SELECT `CUI`, `derivedfrom` FROM `CUIs` WHERE CUI = '") == 0) {
            // do nothing
        }
        else {
            $to_query .= "'";
            // debug here
            #echo htmlspecialchars($to_query) . "\n";
            $data = query($to_query);
            foreach( $data as $datum ) {
                // determine whether CUIs are really derivable and determine their value
                // supports only pure disjunction and conjunction
                
                // conjunction
                if ( stristr($datum['CUI'],"and") ) {
                    $depends = json_decode($datum['derivedfrom']);
                    // arg stores the potential for the conjunction to be true
                    $arg = true;
                    // iterate through possible derivers
                    foreach ($depends as $dep) {
                        // if any dependencies are false, the conjunction is false
                        if ( ($CUI_vals[$dep] === false) ) {
                            array_push($CUIs,$datum['CUI']);
                            $CUI_vals[$datum['CUI']] = false;
                            $arg = false;
                            break;
                        }
                        // if the conjunction still might be true, check for missing data
                        if ( $arg === true ) {
                            $arg = $CUI_vals[$datum['CUI']];
                        }
                    }
                    // if the argument stayed true for all dependencies, the conjunction is true
                    if ( $arg === true ) {
                        array_push($CUIs,$datum['CUI']);
                        $CUI_vals[$datum['CUI']] = true;
                    }
                    
                // disjunction
                } else if ( stristr($datum['CUI'],"or") ) {
                    $depends = json_decode($datum['derivedfrom']);
                    // arg stores the potential for the disjunction to be false
                    $arg = false;
                    // iterate through possible derivers
                    foreach ($depends as $dep) {
                        // if any dependencies are true, the disjunction is true
                        if ( ($CUI_vals[$dep] === true) ) {
                            array_push($CUIs,$datum['CUI']);
                            $CUI_vals[$datum['CUI']] = true;
                            $arg = true;
                            break;
                        }
                        // if the conjunction still might be false, check for missing data
                        if ( $arg === false ) {
                            $arg = $CUI_vals[$datum['CUI']];
                        }
                    }
                    // if the argument stayed false for all dependencies, the disjunction is false
                    if ( $arg === false ) {
                        array_push($CUIs,$datum['CUI']);
                        $CUI_vals[$datum['CUI']] = false;
                    }
                // singles
                } else {
                    $depends = json_decode($datum['derivedfrom']);
                    // iterate through possible derivers
                    foreach ($depends as $dep) {
                        // disjunctions - if false, then all components are false
                        if ( (stristr($dep,"or")) and ($CUI_vals[$dep] === false) ) {
                            $datum['CUI'] = false;
                            break;
                        // conjunctions - if true, then all components are true
                        } else if ( (stristr($dep,"and")) and ($CUI_vals[$dep] === true) ) {
                            array_push($CUIs,$datum['CUI']);
                            $CUI_vals[$datum['CUI']] = true;
                            break;
                        }
                    }
                }
            }
        } // end of derivable handling
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
        
        // check population criteria
        // TODO

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
            
            // bool, convert to integer
            if ($datatypes[$index] == 'bool') { 
                if ($arg === true) {
                    $arg = '1';
                } else if ($arg === false) {
                    $arg = '0';
                } else {
                    $resp['error'] = 'bad boolean CUI: ' . $CUI;  // identify a bad bool
                    return($resp);
                }
            } 
            // integer
            else if ($datatypes[$index] == 'integer' or $datatypes[$index] == 'int') { 
                // ensure that argument is an integer
                if ( !is_int($arg) ) {
                    $resp['error'] = 'bad integer CUI: ' . $CUI;  // identify a bad CUI
                    return($resp);
                }
                // check upper and lower bounds
                $arg = check_bounds($arg,(int)$lowers[$index],(int)$uppers[$index]);
                if (is_string($arg)){
                    $resp['error'] = $arg . $CUI;
                    return($resp);
                }
                $arg = (string)$arg;
            } 
            // float ($datatypes[$index] == 'float')
            else  {    
                if ( !is_float($arg) ) {
                    $resp['error'] = 'bad float CUI: ' . $CUI;  // identify a bad CUI
                    return($resp);
                }
                // check upper and lower bounds
                $arg = check_bounds($arg,(float)$lowers[$index],(float)$uppers[$index]);
                if (is_string($arg)){
                    $resp['error'] = $arg . $CUI;
                    return($resp);
                }
                $arg = (string)$arg;
                // if it looks like an integer, tell code it is a float
                if ( ctype_digit($arg) ) {
                    $arg .= '.0';
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
