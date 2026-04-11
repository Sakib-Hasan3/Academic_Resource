<?php
include '../includes/auth_chechk.php';
include '../includes/header.php';
?>
<h2>Upload Course</h2>
<form method="POST" action="">
    Course Name: <input type="text" name="name"><br>
    Instructor: <input type="text" name="instructor"><br>
    Description: <textarea name="description"></textarea><br>
    <input type="submit" name="submit" value="Upload">
</form>
<?php
if (isset($_POST['submit'])) {
    include '../db.php';
    $name = $_POST['name'];
    $instructor = $_POST['instructor'];
    $desc = $_POST['description'];
    $sql = "INSERT INTO courses (name, instructor, description) VALUES ('$name', '$instructor', '$desc')";
    if (mysqli_query($conn, $sql)) {
        echo "<p>Course uploaded successfully!</p>";
    } else {
        echo "<p>Error uploading course.</p>";
    }
}
include '../includes/footer.php';
?>
