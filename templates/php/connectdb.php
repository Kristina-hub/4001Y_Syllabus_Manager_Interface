<?php
	$dbhost = "172.31.80.128";
	$dbuser= "root";
	// $dbpass = "cs3319";
	$dbname = "vetoffice";
	$connection = mysqli_connect($dbhost, $dbuser,$dbpass,$dbname);
	
	if (mysqli_connect_errno()) {
 		die("Error: database connection failed :" . 
 		mysqli_connect_error() . " (" . mysqli_connect_errno() . ")" );
 	} 
?>