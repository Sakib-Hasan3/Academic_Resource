<?php 
session_start();
include('../db.php');

// Redirect if user is not logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// Fetch study tips and motivational quotes
$stmt = $conn->query("SELECT * FROM tips ORDER BY created_at DESC");
$tips = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Study Tips & Motivational Quotes - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/tips.css">
  <style>
    .hero img.hero-img {
      max-width: 100px;
      margin-bottom: 15px;
    }
  </style>
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

 <section class="hero">
  <img src="../assets/images/tips.png" alt="Tips" class="hero-img">
  <h1 class="hero-title">Study Tips & Motivational Quotes</h1>
  <p class="hero-subtitle">
    Boost your learning with curated tips and quotes to keep you focused and inspired.
  </p>
</section>


  <!-- Tips Cards -->
  <div class="container">
    <?php if ($tips): ?>
      <div class="tips-list">
        <?php foreach ($tips as $tip): ?>
          <div class="tip-item">
            <div class="tip-text"><?php echo nl2br(htmlspecialchars($tip['tip_text'])); ?></div>
            <?php if (!empty($tip['author'])): ?>
              <div class="tip-author">&mdash; <?php echo htmlspecialchars($tip['author']); ?></div>
            <?php endif; ?>
            <small class="tip-date">Added on: <?php echo date('F j, Y', strtotime($tip['created_at'])); ?></small>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p>No tips available at the moment. Check back soon!</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>

</body>
</html>
