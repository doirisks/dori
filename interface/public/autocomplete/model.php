<?php
// get query configurations and posted json
require('../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// make sure that request is valid
if ( (!is_array($posted_array)) or (count($posted_array) == 0) ) {
    $ans['error'] = 'improper request';
    exit();
}

// get all valid keywords
$keywords = array();
foreach ($posted_array as $keyword) {
    if (ctype_alnum($keyword)){
        array_push($keywords, $keyword);
    }
}
if (count($keywords) == 0) {
    $data = array();
    echo json_encode($data);
    exit();
}

// build query
$to_query = "SELECT `id`, `papertitle`, `modeltitle`, `outcome`,  FROM `CUIs` WHERE ";
foreach ($keywords as $keyword) {
    $to_query .= "( `outcome` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`papertitle` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`modeltitle` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`outcometime` LIKE '%" . $keyword . "%' ) ";
}

/** TODO
 * ignore models which the requester already has
foreach ($already as $model) {
    $to_query .= " AND NOT ( `id` = '" . $model . "' ) "
}
 */

$data = query($to_query);
echo json_encode($data);

?>
