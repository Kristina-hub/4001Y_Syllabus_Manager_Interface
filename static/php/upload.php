<!-- Programmer Name: 04     -->
<!-- Date: November 26, 2021 -->
<!-- Language: PHP           -->
<!-- Class: index page       -->

<?php
	$target_dir = "uploads/";
	$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
	$uploadOk = 1;
	$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
	$uploadOk = 1;
// 	Check if image file is a actual image or fake image
// 	if(isset($_POST["submit"])) {
// 	  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
// 	  if($check !== false) {
// 		echo "File is an image - " . $check["mime"] . ".";
// 		$uploadOk = 1;
// 	  } else {
// 		echo "File is not an image.";
// 		$uploadOk = 0;
// 	  }
// 	}
?>
