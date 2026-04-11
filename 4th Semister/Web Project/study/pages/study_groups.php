<?php
session_start();
include('../db.php');

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
  header('Location: ../auth/login.php');
  exit();
}

// Fetch each mentor’s group and count
$stmt = $conn->query("
  SELECT 
    m.id AS mentor_id,
    m.full_name,
    m.course_name,
    COUNT(s.user_id) AS enrolled_count
  FROM study_groups s
  JOIN mentors m ON s.mentor_id = m.id
  GROUP BY s.mentor_id
  ORDER BY enrolled_count DESC
");
$groups = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Study Groups – CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/study_groups.css">
</head>
<body>

  <?php include('../includes/header.php'); ?>

  <section class="hero">
    <h1 class="hero-title">Study Groups</h1>
    <p class="hero-subtitle">
      See how many students have been approved into each mentor’s course.
    </p>
  </section>

  <div class="container">
    <?php if ($groups): ?>
      <div class="groups-list">
        <?php foreach ($groups as $g): ?>
          <div class="group-card">
            <h2><?= htmlspecialchars($g['course_name']) ?></h2>
            <p>Mentor: <?= htmlspecialchars($g['full_name']) ?></p>
            <p><strong>Enrolled:</strong> <?= $g['enrolled_count'] ?></p>
            <a href="mentorship.php?mentor_id=<?= $g['mentor_id'] ?>" class="btn">
              View Mentor
            </a>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p class="no-results">No study groups yet.</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>
</body>
</html>
