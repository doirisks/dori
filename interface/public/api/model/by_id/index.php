<?php
// get query configurations and posted json
require('../../../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// make sure that request is valid
if ( (!isset($posted_array['ids'])) or (!is_array($posted_array['ids'])) or (count($posted_array['ids']) == 0) ) {
    if ((!isset($_GET['ids'])) or (!is_array($_GET['ids'])) or (count($_GET['ids']) == 0)) {
        $ans['error'] = 'no ids sent';
        die(json_encode($ans));
    }
    $model_ids = $_GET['ids'];
}
else {
    $model_ids = $posted_array['ids'];
}

// iterate through ids
$ans = [];
foreach( $model_ids as $id ) {
    // ensure that id is valid
    $id = (string)$id;
    if ( !ctype_digit($id) ) {
        $ans[$id]['error'] = 'invalid id';
    }

    // build and run query
    $to_query = "SELECT * FROM `models` WHERE id = " . $id ;
    $from_query = query($to_query);
    
    # handle query output
    if (count($from_query) == 0) {
        $ans[$id]['error'] = 'no models found';
    }
    else if (count($from_query) == 1) {
        $ans[$id] = $from_query[0];
    }
    else {
        $ans[$id]['error'] = 'duplicate models found!';
        $ans[$id]['models'] = $from_query;
    }
}

// send back the results
echo json_encode($ans);
?>
