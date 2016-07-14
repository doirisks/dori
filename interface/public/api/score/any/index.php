<?php
/**
 * find all models for which a set of CUIs can fill all inputs AND SCORE them
 *
 * DOES NOT SCREEN FOR INAPPROPRIATE POPULATIONS
 **/



// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// clean input, then expand CUIs via derived CUIs
$CUIs = array();
$CUI_vals = [];
prep_CUIs($CUIs,$CUI_vals,$posted_array);

// build a query to get must, mustnot, and input columns for each CUI
$to_query = "SELECT `CUI`,`must`,`mustnot`,`input` FROM `CUIs` WHERE CUI = '";
foreach($CUIs as $CUI) {
    $to_query .= htmlspecialchars ($CUI);
    $to_query .= "' OR CUI = '";
    // debug submitted CUIs
    //echo $CUI . "<br>";
}
$to_query .= "'";

// debug query
//echo "<p>" . htmlspecialchars($to_query) . "</p>";

// send query
$CUI_data = query($to_query);

// debug reply
/*foreach($CUI_data as $CUI_datum) {
    echo "<p>" . $CUI_datum['CUI'].": ". $CUI_datum['input'] . "</p>";
}*/

// count up the inputs for each id
$inputIDcounts = [];
foreach ($CUI_data as $datum) {
    $inputIDs = json_decode($datum['input']);
    foreach ($inputIDs as $ID) {
        if ( array_key_exists($ID,$inputIDcounts) ) {
            $inputIDcounts[$ID] += 1;
        }
        else {
            $inputIDcounts[$ID] = 1;
        }
    }
}


$modelIDs = array_keys($inputIDcounts);     // this line used in debug AND in actual code
// debug counting
/*foreach( $modelIDs as $modelID ) {
    echo "<p>". $modelID . ": " . $inputIDcounts[$modelID]."</p>\n";
}*/

// build query to get models
$to_query = "SELECT `id` FROM `models` WHERE ( id = ";
foreach ($modelIDs as $id) {
    $to_query .= htmlspecialchars($id);
    $to_query .= " AND numofinputs = ";
    $to_query .= htmlspecialchars ($inputIDcounts[$id]);
    $to_query .= " ) OR ( id = ";
}

// trim query or report emptiness without bothering database
if (strlen($to_query) > 134) {
    $to_query = substr($to_query,0, -11);
}
else {
    $ans['error'] = 'no models suggested';
    echo json_encode($ans);
    exit();
}

// check if there is insufficient data for any models
$models = query($to_query);
if ( count($models) == 0 ) {
    $ans['error'] = 'no models received';
    echo json_encode($ans);
    exit();
}

// turn query output into an array
$replacement = Array();
foreach($models as $model) {
    array_push($replacement, $model['id']);
}
$models = $replacement;

// a variable for the response
$ans = [];

// iterate through models sent
foreach ($models as $id) {
    
    // check that id is numerical
    if ( !ctype_digit((string)$id) ){
        $ans[$id]['error'] = 'bad id';
        continue;
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
            $ans[$id]['error'] = 'missing CUI: ' . $CUI;  // identify a missing CUI
            break;
        }
    
        // get the CUI's value
        $arg = $CUI_vals[$CUI];
        
        // check that CUI's value is in valid range (unnecessary for bools!)
        if (!empty($lowers[$index]) and ($arg < $lowers[$index])) {
            $ans[$id]['error'] = 'CUI below acceptable range: ' . $CUI;  // CUI below acceptable range
            break;
        }
        if (!empty($uppers[$index]) and ($arg > $uppers[$index])) {
            $ans[$id]['error'] = 'CUI above acceptable range: ' . $CUI;  // CUI above acceptable range
            break;
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
                $ans[$id]['error'] = 'bad boolean CUI: ' . $CUI;  // identify a bad bool
                break;
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
                    $ans[$id]['error'] = 'bad integer CUI: ' . $CUI;  // identify a bad CUI
                    break;
                }
            } else {
                $ans[$id]['error'] = 'bad integer CUI: ' . $CUI;  // identify a bad CUI
                break;
            }
        } 
        else  {    // float ($datatypes[$index] == 'float')
            if (ctype_digit($arg) ) {
                // if already integer, tell python it is a float
                $arg .= '.0';
            } else if (ctype_digit(str_replace('.','',$arg)) ) {
                if (substr_count($arg,'.') == 1 && strlen($arg) > 1 ) {
                    // arg is already fine
                }
                else {
                    $ans[$id]['error'] = 'bad float CUI: ' . $CUI;  // identify a bad float
                    break;
                }
            } else {
                $ans[$id]['error'] = 'bad float CUI: ' . $CUI;  // identify a bad float
                break;
            }
        }
        array_push($modelargs,$arg);
    }
    // make sure that no errors occurred
    if (isset($ans[$id]['error'])) {
        continue;
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
        //TODO
    } else if ( strtolower($model['language']) == 'sas' ) {
        //TODO
    }

    // calculate risk score
    $modeloutput = array();
    exec($command,$modeloutput);
    if (count($modeloutput) < 1) {
        $ans[$id]['error'] = "no response from model";
    } else {
        // record the score!
        $ans[$id]['score'] = $modeloutput[0];
    }
}

echo json_encode($ans);
?>
