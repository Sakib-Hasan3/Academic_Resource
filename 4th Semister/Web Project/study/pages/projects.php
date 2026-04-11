<?php
session_start();
include('../db.php');

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: ../auth/login.php");
    exit();
}

// Handle search query
$search = '';
$params = [];
$sql = "SELECT * FROM projects";
if (!empty($_GET['search'])) {
    $search = trim($_GET['search']);
    $sql .= " WHERE title LIKE :q OR description LIKE :q OR technologies LIKE :q";
    $params[':q'] = "%{$search}%";
}
$sql .= " ORDER BY created_at DESC";

$stmt = $conn->prepare($sql);
$stmt->execute($params);
$projects = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Projects – CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/projects.css">
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
      <li><a href="projects.php">Projects</a></li>
      <li><a href="../auth/logout.php" class="nav__logout">Logout</a></li>
    </ul>
  </nav>

  <!-- Hero Banner -->
  <section class="hero">
    <h1 class="hero-title">CSE Projects</h1>
    <p class="hero-subtitle">
      Explore student and community projects showcasing Computer Science &amp; Engineering skills.
    </p>
  </section>

  <div class="container">
    <!-- Search Form -->
    <form class="search-form" method="GET" action="projects.php">
      <input
        type="text"
        name="search"
        class="search-input"
        placeholder="Search projects..."
        value="<?php echo htmlspecialchars($search); ?>"
      >
      <button type="submit" class="search-btn">Search</button>
    </form>

    <!-- Projects Grid -->
    <?php if ($projects): ?>
      <div class="projects-list">
        <?php foreach ($projects as $project): ?>
          <div class="project-item">
            <h3><?php echo htmlspecialchars($project['title']); ?></h3>
            <p><strong>Description:</strong> <?php echo htmlspecialchars($project['description']); ?></p>
            <p><strong>Technologies Used:</strong> <?php echo htmlspecialchars($project['technologies']); ?></p>
            <a href="<?php echo htmlspecialchars($project['link']); ?>"
               target="_blank"
               class="btn">View Project</a>
            <small>Added on: <?php echo date('F j, Y', strtotime($project['created_at'])); ?></small>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p class="no-results">No projects found. Try a different search term.</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>

</body>
</html>
