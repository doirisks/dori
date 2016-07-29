<?php
// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// make sure that request is valid
if ( (!isset($posted_array['ids'])) or (!is_array($posted_array['ids'])) or (count($posted_array['ids']) == 0) ) {
    if ( (!isset($_GET['ids'])) or (!is_array($_GET['ids'])) or (count($_GET['ids']) == 0) ) {
        $ans['error'] = 'improper request';
        echo json_encode($ans);
        exit();
    }
    $DOIs = $_GET['ids'];
}
else {
    $DOIs = $posted_array['ids'];
}

// iterate through DOIs
$ans = [];
foreach( $DOIs as $DOI ) {
    // ensure that DOI is valid
    if ( (strpos($DOI,"'") !== false) or (strpos($DOI,'"') !== false) ) {
        $ans[$DOI]['error'] = 'invalid DOI';
    }

    // build, run, and store query
    $to_query = "SELECT `id` FROM `models` WHERE DOI = '" . $DOI . "'";
    $ans[$DOI] = query($to_query);
    
    if ( empty($ans[$DOI]) ) {
        $ans[$DOI]['error'] = 'no models found';
    }
}

// send back the results
echo json_encode($ans);
?>
