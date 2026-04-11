<?php
include '../includes/auth_chechk.php';
include '../includes/header.php';
?>
<h2>Manage Users</h2>
<table border="1">
    <tr><th>Username</th><th>Email</th><th>Role</th><th>Actions</th></tr>
    <?php
    include '../db.php';
    $result = mysqli_query($conn, "SELECT * FROM users");
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td>{$row['username']}</td><td>{$row['email']}</td><td>{$row['role']}</td><td><a href='edit_user.php?id={$row['id']}'>Edit</a> | <a href='delete_user.php?id={$row['id']}'>Delete</a></td></tr>";
    }
    ?>
</table>
<?php include '../includes/footer.php'; ?>