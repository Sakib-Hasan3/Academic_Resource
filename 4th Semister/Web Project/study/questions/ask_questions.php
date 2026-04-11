<?php
session_start();
include('../db.php');

if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// Handle new question submission
$message = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty(trim($_POST['question']))) {
    $stmt = $conn->prepare("INSERT INTO questions (user_id, question) VALUES (?, ?)");
    if ($stmt->execute([ $_SESSION['user_id'], trim($_POST['question']) ])) {
        $message = "Your question has been posted!";
    } else {
        $message = "Failed to post. Please try again.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Ask a Question – CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/questions.css">
</head>
<body>

<!-- Navigation Bar -->
<nav class="nav">
  <div class="nav__brand">CSE Study Room</div>
  <ul class="nav__links">
    <li><a href="../pages/dashboard.php">Dashboard</a></li>
    <li><a href="../pages/courses.php">Courses</a></li>
    <li><a href="../pages/jobs.php">Jobs</a></li>
    <li><a href="../pages/mentorship.php">Mentorship</a></li>
    <li><a href="../auth/logout.php" class="nav__logout">Logout</a></li>
  </ul>
</nav>

<!-- Hero Banner -->
<section class="hero">
  <h1 class="hero-title">Ask a Question</h1>
  <p class="hero-subtitle">Stuck on a topic? Ask your CSE-related question and get help from others.</p>
</section>

<div class="container">

  <!-- Question Form -->
  <div class="question-form-card">
    <h2>Ask a New Question</h2>
    <form method="POST">
      <textarea name="question" rows="4" placeholder="Type your question here..." required></textarea>
      <button type="submit" class="btn">Post Question</button>
    </form>
    <?php if ($message): ?>
      <p class="message"><?= htmlspecialchars($message) ?></p>
    <?php endif; ?>
  </div>

  <!-- Button to View All Questions -->
  <div class="section">
    <a href="questions_list.php" class="btn">View All Questions</a>
  </div>

</div>
</body>
</html>
