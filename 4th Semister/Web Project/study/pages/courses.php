<?php
session_start();
include('../db.php'); 

if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// Fetch all online courses
$stmt = $conn->query("SELECT * FROM courses ORDER BY created_at DESC");
$courses = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Online Courses - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/courses.css">
</head>
<body>

  <!-- Top Navigation -->
  <nav class="nav">
    <div class="nav__brand">CSE Study Room</div>
    <ul class="nav__links">
      <li><a href="dashboard.php">Dashboard</a></li>
      <li><a href="courses.php">Courses</a></li>
      <li><a href="jobs.php">Jobs</a></li>
      <li><a href="mentorship.php">Mentorship</a></li>
      <li><a href="../auth/logout.php" class="nav__logout">Logout</a></li>
    </ul>
  </nav>

  <!-- Hero Banner -->
  <section class="hero">
    <h1 class="hero-title">Online Courses</h1>
    <p class="hero-subtitle">
      Browse and enroll in hand-picked Computer Science & Engineering courses,
      curated to help you level up your skills.
    </p>
  </section>

  <!-- Course Cards -->
  <div class="container">
    <?php if ($courses): ?>
      <div class="courses-list">
        <?php foreach ($courses as $course): ?>
          <div class="course-item">
            <h3><?php echo htmlspecialchars($course['title']); ?></h3>
            <div class="provider">Provider: <?php echo htmlspecialchars($course['provider']); ?></div>
            <div class="description"><?php echo nl2br(htmlspecialchars($course['description'])); ?></div>
            <a href="<?php echo htmlspecialchars($course['link']); ?>"
               target="_blank"
               class="btn">Go to Course</a>
            <small>Added on: <?php echo date('F j, Y', strtotime($course['created_at'])); ?></small>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p>No courses available at the moment. Check back soon!</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>

</body>
</html>
