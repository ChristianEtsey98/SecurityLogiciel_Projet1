<?php
  $host="localhost";
  $user="boss";
  $password="boss";
  $db_name="seculogi";
  
  $con = mysqli_connect($host,$user,$password,$db_name);
  
  if(mysqli_connect_errno()){
	  die("Failed to connect with MYSQL:".mysqli_connect_error());

  }       
?>

