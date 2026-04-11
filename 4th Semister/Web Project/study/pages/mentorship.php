<?php
session_start();
include('../db.php');

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// If we're viewing one mentor's profile
if (isset($_GET['mentor_id'])) {
    $mentor_id = intval($_GET['mentor_id']);

    // Fetch mentor info
    $mStmt = $conn->prepare("SELECT * FROM mentors WHERE id = ?");
    $mStmt->execute([$mentor_id]);
    $mentor = $mStmt->fetch(PDO::FETCH_ASSOC);
    if (!$mentor) {
        die("Mentor not found.");
    }

    // Handle the student request form
    $message = '';
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message'])) {
        $user_id = $_SESSION['user_id'];
        $note    = htmlspecialchars($_POST['message']);
        $iStmt   = $conn->prepare(
            "INSERT INTO mentorship_requests (mentor_id, user_id, message) 
             VALUES (?, ?, ?)"
        );
        if ($iStmt->execute([$mentor_id, $user_id, $note])) {
            $message = "Your request has been sent!";
        } else {
            $message = "Failed to send request. Please try again.";
        }
    }

    // Fetch pending requests for this mentor
    $rStmt = $conn->prepare("
        SELECT r.id, r.message, r.created_at, u.username 
          FROM mentorship_requests r
          JOIN users u ON r.user_id = u.id
         WHERE r.mentor_id = ? 
           AND r.status = 'pending'
         ORDER BY r.created_at ASC
    ");
    $rStmt->execute([$mentor_id]);
    $requests = $rStmt->fetchAll(PDO::FETCH_ASSOC);
    ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mentor Profile – <?= htmlspecialchars($mentor['full_name']) ?></title>
  <link rel="stylesheet" href="../assets/css/mentorship.css">
</head>
<body>

  <!-- NAVBAR -->
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

  <!-- HERO -->
  <section class="hero">
    <h1 class="hero-title">Mentor Profile</h1>
    <p class="hero-subtitle">Connect one-on-one with industry experts.</p>
  </section>

  <div class="container">

    <!-- Mentor Details -->
    <div class="mentor-card profile">
      <img
        src="../assets/images/mentors/<?= htmlspecialchars($mentor['photo']) ?>"
        alt="<?= htmlspecialchars($mentor['full_name']) ?>"
        class="mentor-photo"
      >
      <h2><?= htmlspecialchars($mentor['full_name']) ?></h2>
      <p class="mentor-expertise"><strong>Expertise:</strong> <?= htmlspecialchars($mentor['expertise']) ?></p>
      <p class="course-name"><?= htmlspecialchars($mentor['course_name']) ?></p>
      <p class="course-desc"><?= nl2br(htmlspecialchars($mentor['course_description'])) ?></p>
      <p>
        <a href="<?= htmlspecialchars($mentor['profile_link']) ?>"
           target="_blank"
           class="btn">View Full Profile</a>
      </p>
    </div>

    <!-- Request Form -->
    <div class="mentor-card">
      <h3>Request Mentorship</h3>
      <form method="POST">
        <textarea name="message" rows="5" placeholder="Your message..." required></textarea>
        <button type="submit" class="btn">Send Request</button>
      </form>
      <?php if ($message): ?>
        <p class="message"><?= $message ?></p>
      <?php endif; ?>
    </div>

    <!-- Pending Requests -->
    <div class="mentor-card">
      <h3>Pending Student Requests</h3>
      <?php if ($requests): ?>
        <div class="requests-list">
          <?php foreach ($requests as $req): ?>
            <div class="request-item">
              <p>
                <strong><?= htmlspecialchars($req['username']) ?></strong>
                <em>(<?= date('M j, Y g:ia', strtotime($req['created_at'])) ?>)</em><br>
                <?= nl2br(htmlspecialchars($req['message'])) ?>
              </p>
              <form method="POST" action="approve_request.php" class="inline-form">
                <input type="hidden" name="request_id" value="<?= $req['id'] ?>">
                <button type="submit" class="btn">Approve</button>
              </form>
            </div>
          <?php endforeach; ?>
        </div>
      <?php else: ?>
        <p><em>No pending requests.</em></p>
      <?php endif; ?>
    </div>

    <div class="section">
      <a href="mentorship.php" class="btn">Back to Mentors List</a>
    </div>
  </div>
</body>
</html>
    <?php
    exit;
}

// Otherwise, list all mentors
$stmt    = $conn->query("SELECT * FROM mentors ORDER BY created_at DESC");
$mentors = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mentorship – CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/mentorship.css">
</head>
<body>

  <!-- NAVBAR -->
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

  <!-- HERO -->
  <section class="hero">
    <h1 class="hero-title">Available Mentors</h1>
    <p class="hero-subtitle">Browse mentors and request personalized guidance.</p>
  </section>

  <div class="container">
    <?php if ($mentors): ?>
      <div class="mentors-list">
        <?php foreach ($mentors as $m): ?>
          <div class="mentor-card">
            <img
              src="../assets/images/mentors/<?= htmlspecialchars($m['photo']) ?>"
              alt="<?= htmlspecialchars($m['full_name']) ?>"
              class="mentor-photo"
            >
            <h2><?= htmlspecialchars($m['full_name']) ?></h2>
            <p class="mentor-expertise"><?= htmlspecialchars($m['expertise']) ?></p>
            <p class="course-name"><?= htmlspecialchars($m['course_name']) ?></p>
            <a href="mentorship.php?mentor_id=<?= $m['id'] ?>" class="btn">Request</a>
          </div>
        <?php endforeach; ?>
      </div>
    <?php else: ?>
      <p class="no-results">No mentors available at the moment.</p>
    <?php endif; ?>

    <div class="section">
      <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
  </div>
</body>
</html>
