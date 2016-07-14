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

// iterate through ids
$ans = [];
foreach( $posted_array as $id ) {
    // ensure that id is valid
    $id = (string)$id;
    if ( !ctype_digit($id) ) {
        $ans[$id]['error'] = 'invalid id';
    }

    // build, run, and store query
    $to_query = "SELECT * FROM `models` WHERE id = " . $id ;
    $ans[$id] = query($to_query);
    
    if ( empty($ans[$id]) ) {
        $ans[$id]['error'] = 'no models found';
    }
}

// send back the results
echo json_encode($ans);
?>
