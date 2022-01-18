<!-- Programmer Name: 04     -->
<!-- Date: November 26, 2021 -->
<!-- Language: PHP           -->
<!-- Class: index page       -->

<?php
	$dbhost = "172.31.80.128";
	$dbuser= "root";
	$dbpass = "syllabus";
	$dbname = "accounts";
	$connection = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
	
	if (mysqli_connect_errno()) {
 		die("Error: database connection failed :" . 
 		mysqli_connect_error() . " (" . mysqli_connect_errno() . ")" );
 	} 
?>
