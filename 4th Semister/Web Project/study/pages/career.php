<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: ../auth/login.php");
    exit();
}
$username = $_SESSION['username'] ?? 'User';

include('../db.php');

// Handle search query
$search = $_GET['search'] ?? '';
if (!empty($search)) {
    $stmt = $conn->prepare("SELECT * FROM career_roadmap WHERE career_name LIKE ? OR description LIKE ? ORDER BY id");
    $stmt->execute(["%$search%", "%$search%"]);
} else {
    $stmt = $conn->query("SELECT * FROM career_roadmap ORDER BY id");
}
$roadmaps = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Career Roadmap – CSE Study Room</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="../assets/css/career.css">
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

  <!-- Hero Section -->
  <header class="hero">
    <h1 class="hero-title">Career Roadmap</h1>
    <p class="hero-subtitle">
      Explore various career paths in Computer Science and Engineering (CSE).
    </p>
  </header>

  <!-- Search Bar -->
  <div class="search-form">
    <form method="GET">
      <input type="text" name="search" class="search-input" placeholder="Search career paths..." value="<?= htmlspecialchars($search) ?>">
      <button type="submit" class="search-btn">Search</button>
    </form>
  </div>

  <!-- Cards Grid -->
  <main class="grid">
    <?php if ($roadmaps): ?>
      <?php foreach ($roadmaps as $r): ?>
        <article class="card">
          <h2 class="card__title"><?= htmlspecialchars($r['career_name']) ?></h2>
          <p class="card__desc"><?= nl2br(htmlspecialchars($r['description'])) ?></p>

          <div class="card__section">
            <h3>Steps</h3>
            <ul>
              <?php foreach (explode("\n", $r['steps']) as $step): 
                $step = trim($step);
                if ($step): ?>
                  <li><?= htmlspecialchars($step) ?></li>
              <?php endif; endforeach; ?>
            </ul>
          </div>

          <div class="card__section">
            <h3>Resources</h3>
            <ul>
              <?php foreach (explode("\n", $r['resources']) as $res): 
                $res = trim($res);
                if ($res): ?>
                  <li><a href="<?= htmlspecialchars($res) ?>" target="_blank"><?= htmlspecialchars($res) ?></a></li>
              <?php endif; endforeach; ?>
            </ul>
          </div>
        </article>
      <?php endforeach; ?>
    <?php else: ?>
      <p class="no-results">No career paths found for "<?= htmlspecialchars($search) ?>". Try another search!</p>
    <?php endif; ?>
  </main>

</body>
</html>
