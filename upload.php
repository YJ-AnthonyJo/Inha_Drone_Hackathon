<?php
 
// 설정
$uploads_dir = './';
$allowed_ext = array('mp4','jpg','jpeg','png`');
 
// 변수 정리
$error = $_FILES['myfile']['error'];
$name = $_FILES['myfile']['name'];

if (file_exists('situ.jpg')){
  unlink('situ.jpg');
}


$t = explode('.', $name);
$ext=array_pop($t);
 
// 오류 확인
if( $error != UPLOAD_ERR_OK ) {
    switch( $error ) {
        case UPLOAD_ERR_INI_SIZE:
        case UPLOAD_ERR_FORM_SIZE:
            echo "too big ($error)";  
            break;
        case UPLOAD_ERR_NO_FILE:
            echo "not uploaded ($error)";
            break;
        default:
            echo "just error ($error)";
    }
    exit;
}
 
// 확장자 확인
if( !in_array($ext, $allowed_ext) ) {
    echo "unallowed";
    exit;
}
 
// 파일 이동
move_uploaded_file( $_FILES['myfile']['tmp_name'], "$uploads_dir/$name");
 
// 파일 정보 출력
/*echo "<h2>파일 정보</h2>
 <ul>
        <li>파일명: $name</li>
        <li>확장자: $ext</li>
        <li>파일형식: {$_FILES['myfile']['type']}</li>
        <li>파일크기: {$_FILES['myfile']['size']} 바이트</li>
    </ul>";*/
?>
