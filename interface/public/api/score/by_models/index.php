<?php
/** 
 * scores a set of CUIs by a set of models
 * e.g:
 * {
 *   'models' : [
 *     6,
 *     17
 *   ],
 *   'C000001': True,
 *   'C000001': False
 * }
 */
 
// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// guarantee that model ids were sent
if ( (!isset($posted_array['models'])) or (empty($posted_array['models'])) ) {
    $ans['error'] = 'no models sent';
    die(json_encode($ans));
}

// store 'models' element in its own variables
$models = $posted_array['models'];
$CUIs['models'] = null;  

// clean input, then expand CUIs via derived CUIs
$CUIs = array();
$CUI_vals = [];
prep_CUIs($CUIs,$CUI_vals,$posted_array);

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
        $ans[$id]['error'] = "no response from model";
    } else {
        // record the score!
        $ans[$id]['score'] = $modeloutput[0];
    }
}

echo json_encode($ans);
?>
