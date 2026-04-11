<?php
session_start();

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: ../auth/login.php");
    exit();
}

include('../db.php'); 

// Fetch internships & jobs
$sql = "SELECT * FROM jobs ORDER BY created_at DESC";
$stmt = $conn->query($sql);
$jobs = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Internships & Jobs - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/jobs.css">
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
    <h1 class="hero-title">Internships &amp; Jobs</h1>
    <p class="hero-subtitle">
      Browse the latest internship and job openings curated for CSE students and fresh graduates.
    </p>
  </section>

  <!-- Job Cards -->
  <div class="container">
    <?php if ($jobs): ?>
      <div class="jobs-list">
        <?php foreach ($jobs as $job): ?>
          <div class="job-item">
            <h3>
              <?php echo htmlspecialchars($job['position']); ?>
              <span class="at">at</span>
              <?php echo htmlspecialchars($job['company']); ?>
            </h3>
            <div class="location"><strong>Location:</strong> <?php echo htmlspecialchars($job['location']); ?></div>
            <div class="description"><?php echo nl2br(htmlspecialchars($job['description'])); ?></div>
            <a href="<?php echo htmlspecialchars($job['apply_link']); ?>"
               target="_blank"
               class="btn">Apply Now</a>
            <small>Posted on: <?php echo date('F j, Y', strtotime($job['created_at'])); ?></small>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p>No job opportunities available at the moment. Check back soon!</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>

</body>
</html>
