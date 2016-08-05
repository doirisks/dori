<?php
// get query configurations and posted json
require('../../includes/query_conf.php'); 
$str_json = file_get_contents('php://input');
$posted_array = json_decode($str_json, true);

// make sure that request is valid
if ( (!is_array($posted_array)) or (count($posted_array) == 0) ) {
    if ((!is_array($_GET['words'])) or (count($_GET['words']) == 0)) {
        $ans['error'] = 'improper request';
        exit();
    }
    $posted_array = $_GET['words'];
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
$to_query = "SELECT `CUI`, `name1` FROM `CUIs` WHERE ";
foreach ($keywords as $keyword) {
    $to_query .= "( `name1` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`name2` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`name3` LIKE '%" . $keyword . "%' OR ";
    $to_query .= "`CUI` LIKE '%" . $keyword . "%' ) ";
}

/** TODO
 * ignore CUIs which the requester already has
foreach ($already as $CUI) {
    $to_query .= " AND NOT ( `CUI` = '" . $CUI . "' ) "
}
 */

$data = query($to_query);
echo json_encode($data);

?>
