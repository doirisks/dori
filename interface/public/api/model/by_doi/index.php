<?php
// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// make sure that request is valid
if ( (!is_array($posted_array)) or (count($posted_array) == 0) ) {
    var_dump($posted_array);
    $ans['error'] = 'improper request';
    exit();
}

// iterate through DOIs
$ans = [];
foreach( $posted_array as $DOI ) {
    // ensure that DOI is valid
    if ( (strpos($DOI,"'") !== false) or (strpos($DOI,'"') !== false) ) {
        $ans[$DOI]['error'] = 'invalid DOI';
    }

    // build, run, and store query
    $to_query = "SELECT * FROM `models` WHERE DOI = '" . $DOI . "'";
    $ans[$DOI] = query($to_query);
    
    if ( empty($ans[$DOI]) ) {
        $ans[$DOI]['error'] = 'no models found';
    }
}

// send back the results
echo json_encode($ans);
?>
