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
    if ( (!isset($_GET['models'])) or (empty($_GET['models'])) ) {
        $ans['error'] = 'no models sent';
        die(json_encode($ans));
    }
    // store 'models' element in its own variables from the query string
    $models = $_GET['models'];
}
else {
    // store 'models' element in its own variables from the cURL style input
    $models = $posted_array['models'];
}

$CUIs['models'] = null;  

// clean input, then expand CUIs via derived CUIs
$CUIs = array();
$CUI_vals = [];
prep_CUIs($CUIs,$CUI_vals,$posted_array);

# debugging
#echo json_encode($CUI_vals) . "\n";

// a variable for the response
$ans = [];

// iterate through models sent
foreach ($models as $id) {
    $ans[$id] = score_id($id, $CUI_vals);
}

echo json_encode($ans);
?>
