<?php
header('Content-Type: text/html; charset=UTF-8');
$s=$_GET['a'];
$left = 'left.jpg'; // 왼쪽 경로 출력 이미지
$right = 'right.jpg'; // 오른쪽 경로 출력 이미지
$answer = 'answer.jpg'; // 웹페이지에 출력할 이미지
unlink("answer.jpg");
if($s==1) {
  if(!copy($left, $answer)) {
  	
  }
  else if (file_exists($answer)) {
  }
}
else if($s==2) {
  if(!copy($right, $answer)) {
  }
  else if (file_exists($answer)) {
  }
}
echo "<img src = 'answer.jpg'/>";
echo "<img src = 'situ.jpg'/>";
?>
