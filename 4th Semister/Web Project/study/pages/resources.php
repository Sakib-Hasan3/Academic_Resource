<?php
session_start();
include('../db.php');

// Redirect if user is not logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: ../auth/login.php");
    exit();
}

// Handle search query
$search = '';
$params = [];
$sql = "SELECT * FROM resources";
if (!empty($_GET['search'])) {
    $search = trim($_GET['search']);
    $sql .= " WHERE title LIKE :q OR type LIKE :q OR description LIKE :q";
    $params[':q'] = "%{$search}%";
}
$sql .= " ORDER BY created_at DESC";

$stmt = $conn->prepare($sql);
$stmt->execute($params);
$resources = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSE Study Resources - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/resources.css">
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

  <!-- Hero Banner with background image -->
  <section class="hero">
    <h1 class="hero-title">CSE Study Resources</h1>
    <p class="hero-subtitle">
      A curated collection of tutorials, books, tools, and links to boost your Computer Science &amp; Engineering journey.
    </p>
  </section>

  <div class="container">

    <!-- Search Form -->
    <form class="search-form" method="GET" action="resources.php">
      <input
        type="text"
        name="search"
        class="search-input"
        placeholder="Search resources..."
        value="<?php echo htmlspecialchars($search); ?>"
      >
      <button type="submit" class="search-btn">Search</button>
    </form>

    <!-- Resources Grid -->
    <?php if ($resources): ?>
      <div class="resources-list">
        <?php foreach ($resources as $res): ?>
          <div class="resource-item">
            <h3><?php echo htmlspecialchars($res['title']); ?></h3>
            <div class="res-type"><strong>Type:</strong> <?php echo htmlspecialchars($res['type']); ?></div>
            <div class="res-desc"><?php echo nl2br(htmlspecialchars($res['description'])); ?></div>
            <a href="<?php echo htmlspecialchars($res['link']); ?>"
               target="_blank"
               class="btn">Access Resource</a>
            <small>Added on: <?php echo date('F j, Y', strtotime($res['created_at'])); ?></small>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p class="no-results">No resources found. Try a different search term.</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>

  </div>
</body>
</html>
