<?php
session_start();
include('../../db.php');

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: ../../auth/login.php');
    exit();
}

// Fetch all questions ordered by newest first
$stmt = $conn->query("SELECT q.id, q.title, q.description, q.created_at, u.username 
                      FROM questions q 
                      LEFT JOIN users u ON q.user_id = u.id
                      ORDER BY q.created_at DESC");
$questions = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Community Forum - CSE Study Room</title>
  <link rel="stylesheet" href="../../assets/css/questions.css" />
</head>
<body>

<?php include('../../includes/nav.php'); ?>

<section class="hero">
  <h1>Community Q&A Forum</h1>
  <p>Ask questions, help others, and grow together.</p>
</section>

<div class="container">
  <a href="ask_questions.php" class="btn">Ask a Question</a>

  <?php if ($questions): ?>
    <?php foreach ($questions as $question): ?>
      <div class="question-card">
        <h3><?= htmlspecialchars($question['title']) ?></h3>
        <p><?= nl2br(htmlspecialchars($question['description'])) ?></p>
        <p><small>Asked by: <?= htmlspecialchars($question['username'] ?? 'Unknown') ?> on <?= date('F j, Y, g:i a', strtotime($question['created_at'])) ?></small></p>
        <a href="answer_question.php?id=<?= $question['id'] ?>" class="btn">View / Answer</a>
      </div>
    <?php endforeach; ?>
  <?php else: ?>
    <p>No questions found. Be the first to <a href="ask_questions.php">ask a question</a>!</p>
  <?php endif; ?>
</div>

</body>
</html>
