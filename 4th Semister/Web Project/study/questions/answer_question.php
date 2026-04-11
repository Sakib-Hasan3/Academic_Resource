<?php
session_start();
include('../db.php');

if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

$question_id = isset($_GET['id']) ? (int) $_GET['id'] : 0;
if ($question_id <= 0) {
    die("Invalid question ID.");
}

// Fetch the question
$stmt = $conn->prepare("
  SELECT q.question, u.username 
  FROM questions q
  JOIN users u ON q.user_id = u.id
  WHERE q.id = ?
");
$stmt->execute([$question_id]);
$question = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$question) {
    die("Question not found.");
}

// Handle answer submission
$message = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty(trim($_POST['answer']))) {
    $answer = trim($_POST['answer']);
    $insert = $conn->prepare("INSERT INTO answers (question_id, user_id, answer) VALUES (?, ?, ?)");
    if ($insert->execute([$question_id, $_SESSION['user_id'], $answer])) {
        $message = "Answer posted successfully.";
    } else {
        $message = "Failed to post answer.";
    }
}

// Fetch all answers
$answers = $conn->prepare("
  SELECT a.answer, a.created_at, u.username 
  FROM answers a 
  JOIN users u ON a.user_id = u.id 
  WHERE a.question_id = ?
  ORDER BY a.created_at ASC
");
$answers->execute([$question_id]);
$answerList = $answers->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Answer Question – CSE Study Room</title>
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
  <h1 class="hero-title">Answer Question</h1>
  <p class="hero-subtitle">Help others by sharing your knowledge and experience.</p>
</section>

<div class="container">

  <div class="question-item">
    <div class="meta"><strong><?= htmlspecialchars($question['username']) ?></strong> asked:</div>
    <div class="text"><?= nl2br(htmlspecialchars($question['question'])) ?></div>
  </div>

  <div class="answers-section">
    <h3>Answers</h3>
    <?php if ($answerList): ?>
      <?php foreach ($answerList as $a): ?>
        <div class="answer-item">
          <p><?= nl2br(htmlspecialchars($a['answer'])) ?></p>
          <small>— <?= htmlspecialchars($a['username']) ?> on <?= date('M j, Y, g:i a', strtotime($a['created_at'])) ?></small>
        </div>
      <?php endforeach; ?>
    <?php else: ?>
      <p><em>No answers yet. Be the first to respond!</em></p>
    <?php endif; ?>

    <h3>Your Answer</h3>
    <form method="POST">
      <textarea name="answer" rows="4" placeholder="Write your answer..." required></textarea>
      <button type="submit" class="btn">Post Answer</button>
    </form>

    <?php if ($message): ?>
      <p class="message"><?= htmlspecialchars($message) ?></p>
    <?php endif; ?>

    <div class="section">
      <a href="questions_list.php" class="btn">Back to Question List</a>
    </div>
  </div>

</div>
</body>
</html>
