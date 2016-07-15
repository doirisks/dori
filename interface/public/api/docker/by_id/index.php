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
    // ensure that id is numerical
    $id = (string)$id;
    if ( !ctype_digit($id) ) {
        $ans[$id]['error'] = 'invalid id';
    }

    // build command
    $command = '../../../../scripts/makedockerfolder.py ' . (string)$id;
    
    // execute and handle command
    $modeloutput = array();
    exec($command,$modeloutput);
    if (count($modeloutput) < 1) {                          // ensure an answer came back
        $ans[$id]['error'] = "no response from script";
    } else if ( (!ctype_digit($modeloutput[0])) or ($modeloutput[0] == "") ) {             // ensure that the answer was a numerical hash
        $ans[$id]['error'] = $modeloutput[0];
    } else {                                                // record the hash
        $ans[$id]['hash'] = $modeloutput[0];
    }
}

// send back the results
echo json_encode($ans);
?>
