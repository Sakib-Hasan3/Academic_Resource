<?php
$host = 'localhost';  
$dbname = 'cse_study_room';  
$username = 'root'; 
$password = '';  
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conn->exec("SET NAMES 'utf8'");
} 
catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>
