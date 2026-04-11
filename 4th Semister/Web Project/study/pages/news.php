<?php
session_start();
include('../db.php'); // updated path to db.php

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// Fetch CSE news entries
$stmt = $conn->prepare("SELECT * FROM news ORDER BY created_at DESC");
$stmt->execute();
$newsItems = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSE News & Updates - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/news.css">
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
    <h1 class="hero-title">CSE News &amp; Updates</h1>
    <p class="hero-subtitle">
      Stay updated with the latest developments, research, and events in Computer Science & Engineering.
    </p>
  </section>

  <!-- News Cards -->
  <div class="container">
    <?php if ($newsItems): ?>
      <div class="news-list">
        <?php foreach ($newsItems as $news): ?>
          <div class="news-item">
            <h3><?php echo htmlspecialchars($news['title']); ?></h3>
            <small>Published on <?php echo date('F j, Y, g:i a', strtotime($news['created_at'])); ?></small>
            <p><?php echo nl2br(htmlspecialchars(substr($news['content'], 0, 300))); ?><?php echo strlen($news['content']) > 300 ? '...' : ''; ?></p>
            <?php if (!empty($news['link'])): ?>
              <a href="<?php echo htmlspecialchars($news['link']); ?>"
                 target="_blank"
                 class="btn">Read Full Article</a>
            <?php endif; ?>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p>No news updates available at the moment. Check back soon!</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>

</body>
</html>
