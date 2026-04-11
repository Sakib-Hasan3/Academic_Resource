<?php
// Include necessary files
include 'includes/db.php';
include 'includes/header.php';

// Fetch all available challenges from the database
$query = "SELECT * FROM challenges";
$result = mysqli_query($conn, $query);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coding Challenges</title>
    <link rel="stylesheet" href="assets/css/courses.css">
</head>
<body>
    <div class="container">
        <h1>Coding Challenges</h1>
        <div class="challenges-list">
            <?php while ($row = mysqli_fetch_assoc($result)) { ?>
                <div class="challenge-item">
                    <h3><?php echo $row['title']; ?></h3>
                    <p><strong>Category:</strong> <?php echo $row['category']; ?></p>
                    <p><strong>Description:</strong> <?php echo $row['description']; ?></p>
                    <a href="attempt_challenges.php?challenge_id=<?php echo $row['id']; ?>" class="btn">Start Challenge</a>
                </div>
            <?php } ?>
        </div>
    </div>
</body>
</html>
