<?php

// test.php파일을 복사본 test.phps로 만듭니다.
$oldfile = 'left.jpg'; // 원본파일
$newfile = 'answer.jpg'; // 복사파일

// file_exists 실제 존재하는 파일인지 체크
if(file_exists($oldfile)) {
     if(!copy($oldfile, $newfile)) {
           echo "파일 복사 실패";
     } else if (file_exists($newfile)) {
           echo "파일 복사 성공";
     }
}
?>
