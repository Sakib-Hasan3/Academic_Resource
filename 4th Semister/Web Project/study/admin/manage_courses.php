<?php
include '../includes/auth_chechk.php';
include '../includes/header.php';
include '../db.php';
?>

<h2>Manage Courses</h2>
<a href="upload_course.php">Upload New Course</a>
<table border="1">
    <tr>
        <th>Course Title</th>
        <th>Provider</th>
        <th>Actions</th>
    </tr>
    <?php
    $result = mysqli_query($conn, "SELECT * FROM courses");
    if (!$result) {
        die("Query Failed: " . mysqli_error($conn));
    }
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr>
                <td>{$row['title']}</td>
                <td>{$row['provider']}</td>
                <td>
                    <a href='edit_course.php?id={$row['id']}'>Edit</a> |
                    <a href='delete_course.php?id={$row['id']}'>Delete</a>
                </td>
              </tr>";
    }
    ?>
</table>

<?php include '../includes/footer.php'; ?>
