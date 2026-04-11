<?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

include('../db.php'); // Database connection

// Fetch questions from the database
$sql = "SELECT questions.id, questions.question, questions.created_at, users.username
        FROM questions
        JOIN users ON questions.user_id = users.id
        ORDER BY questions.created_at DESC";
$stmt = $conn->query($sql);
$questions = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Community Answers - CSE Study Room</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
    <h2>Community Questions</h2>

    <!-- Display all community questions -->
    <div class="community-questions">
        <?php if ($questions): ?>
            <?php foreach ($questions as $question): ?>
                <div class="question">
                    <p><strong>Asked by:</strong> <?php echo htmlspecialchars($question['username']); ?></p>
                    <p><strong>Question:</strong> <?php echo htmlspecialchars($question['question']); ?></p>
                    <p><strong>Asked on:</strong> <?php echo date('F j, Y, g:i a', strtotime($question['created_at'])); ?></p>
                    
                    <!-- Link to answer the question -->
                    <a href="answer_question.php?question_id=<?php echo $question['id']; ?>" class="btn">Answer This Question</a>
                </div>
                <hr>
            <?php endforeach; ?>
        <?php else: ?>
            <p>No questions available in the community.</p>
        <?php endif; ?>
    </div>

    <!-- Go Back to Dashboard -->
    <div class="section">
        <a href="dashboard.php" class="btn">Back to Dashboard</a>
    </div>
</div>
</body>
</html>
