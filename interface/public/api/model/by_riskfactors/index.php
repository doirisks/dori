<?php
/**
 * find all models for which a set of CUIs can fill all inputs
 * (accepts either array or associative array json input)
 *
 * DOES NOT SCREEN FOR INAPPROPRIATE POPULATIONS
 **/



// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

if ( (empty($posted_array['CUIs'])) ) {
    if (empty($_GET)) {
        $ans = ["error" => "no CUIs sent"];
        die(json_encode($ans));
    }
    $posted_CUIs = $_GET;
}
else {
    // supplies JUNK VALUES if CUIs are given in an array (without values) - TODO update to function properly...
    if ( is_array($posted_array) ) {
        foreach($posted_array as $CUI) {
            $replacement[$CUI] = 1;
        }
        $posted_array = $replacement;
    }
    $posted_CUIs = $posted_array;
}

// clean input, then expand CUIs via derived CUIs
$CUIs = array();
$CUI_vals = [];
prep_CUIs($CUIs,$CUI_vals,$posted_CUIs);

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
    $ans['error'] = 'query could not be constructed';
    echo json_encode($ans);
    exit();
}
//echo '<p>'.$to_query."</p>";

$models = query($to_query);
if ( count($models) == 0 ) {
    $ans['error'] = 'no applicable models';
    echo json_encode($ans);
    exit();
}
foreach($models as $model) {
    $ans[(string)$model['id']] = $model;
}

echo json_encode($ans);
?>
