<?php
session_start();
require '../db.php';

// Ensure the user is an admin
if ($_SESSION['role'] !== 'admin') {
    header("Location: ../auth/login.php");
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - CSE Study Room</title>
    <link rel="stylesheet" href="../assets/css/dashboard.css">
</head>
<body>
    <div class="admin-dashboard">
        <h1>Welcome, Admin</h1>
        <div class="dashboard-cards">
            <div class="card">
                <h3>Total Users</h3>
                <p>
                    <?php
                    // Get the total number of users
                    $stmt = $conn->query("SELECT COUNT(*) FROM users");
                    $totalUsers = $stmt->fetchColumn();
                    echo $totalUsers;
                    ?>
                </p>
            </div>
            <div class="card">
                <h3>Total Courses</h3>
                <p>
                    <?php
                    // Get the total number of courses
                    $stmt = $conn->query("SELECT COUNT(*) FROM courses");
                    $totalCourses = $stmt->fetchColumn();
                    echo $totalCourses;
                    ?>
                </p>
            </div>
            <div class="card">
                <h3>Total Reports</h3>
                <p>
                    <?php
                    // Get the total number of reports
                    $stmt = $conn->query("SELECT COUNT(*) FROM reports");
                    $totalReports = $stmt->fetchColumn();
                    echo $totalReports;
                    ?>
                </p>
            </div>
        </div>
        <div class="admin-links">
            <a href="manage_courses.php">Manage Courses</a>
            <a href="manage_users.php">Manage Users</a>
            <a href="view_reports.php">View Reports</a>
        </div>
    </div>
</body>
</html>
