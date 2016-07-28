<?php
// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// check that CUIs were sent (CUIs must be sent as an array!)
if ( (!isset($posted_array['CUIs'])) or (!is_array($posted_array['CUIs'])) or (count($posted_array['CUIs']) == 0)) {
    $ans['error'] = 'no CUIs sent';
    echo(json_encode($ans));
    exit();
}

$CUIs = $posted_array['CUIs'];

// iterate through CUIs
foreach($CUIs as $CUI) {

    // check for empty or dangerous CUIs
    if ( ($CUI == NULL) or ($CUI == "") or ( !ctype_alnum($CUI) ) ){
        $ans[$CUI]['error'] = 'bad CUI: ' . $CUI;
        continue;
    }
    // send the query
    $query_output = query( "SELECT * FROM `CUIs` WHERE CUI = '". htmlspecialchars ($CUI) ."'" )[0];
    
    // check that the response was valid
    if ( empty($query_output) ) {
        $ans[$CUI]['error'] = 'no CUI found: ' . $CUI;
        continue;
    }
    
    // store the data in the answer variable
    $ans[$CUI] = $query_output;
}

// send back the data!
echo json_encode($ans);

?>
