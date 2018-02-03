<?php
    $con = mysqli_connect("localhost", "root", "12345");
    if(!$con)
    {
        echo "Not connected To Server";
    }
    if(!mysqli_select_db($con,"app"))
    {
        echo "Database not selected";
    }

  
    $username = $_POST["username"];
    $password = $_POST["password"];
	
	
    $statement = "SELECT username,password FROM users WHERE username='$username' AND password='$password'";
	
     if(!mysqli_query($con,$statement))
    {
        echo ("Not Loggedin: ". mysqli_error($con));
    }
    else
    {
        echo"logged in";
    } 
    header("refresh:30000; url=login.html");
?>