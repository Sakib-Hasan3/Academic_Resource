<?php
session_start();
include('../db.php');

if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

// Fetch all questions with usernames and answer count
$stmt = $conn->query("
  SELECT q.id AS question_id, q.question, q.created_at, u.username,
         (SELECT COUNT(*) FROM answers a WHERE a.question_id = q.id) AS answer_count
  FROM questions q
  JOIN users u ON q.user_id = u.id
  ORDER BY q.created_at DESC
");
$questions = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>All Questions – CSE Study Room</title>
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

<!-- Hero -->
<section class="hero">
  <h1 class="hero-title">All Questions</h1>
  <p class="hero-subtitle">Explore what others have asked or help by answering.</p>
</section>

<div class="container">

  <!-- Ask Your Own Question -->
  <div class="section ask-own">
    <h2>Ask Your Own Question</h2>
    <p>If you have a question, don’t hesitate to ask!</p>
    <a href="ask_questions.php" class="btn">Ask Now</a>
  </div>

  <!-- Questions List -->
  <?php foreach ($questions as $q): ?>
    <div class="question-item">
      <div class="meta">
        <strong><?= htmlspecialchars($q['username']) ?></strong>
        asked on <?= date('M j, Y, g:i a', strtotime($q['created_at'])) ?>
      </div>
      <div class="text"><?= nl2br(htmlspecialchars($q['question'])) ?></div>
      <div style="margin-top: 8px; font-size: 0.95rem; color: #666;">
        <?= $q['answer_count'] ?> <?= $q['answer_count'] == 1 ? 'Answer' : 'Answers' ?>
      </div>
      <a href="answer_question.php?id=<?= $q['question_id'] ?>" class="btn btn-answer">Answer</a>
    </div>
  <?php endforeach; ?>

</div>

</body>
</html>
