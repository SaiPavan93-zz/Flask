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

    $email = $_POST["email"];
    $username = $_POST["username"];
    $password = $_POST["password"];
	$age=$_POST["age"];
	$name=$_POST["name"];

    $statement = "INSERT INTO users (email, username, password, age, name) VALUES ('$email','$username','$password',$age, '$name')";
    if(!mysqli_query($con,$statement))
    {
        echo "Not Inserted";
    }
    else
    {
		header("refresh:2; Location=149.162.139.76:3000\login.html");
       //echo "Successfully Registered";
    }
    //header("refresh:2; Location=149.162.139.76:3000\login.html");
?>