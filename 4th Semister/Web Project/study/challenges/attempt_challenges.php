<?php
// Include necessary files
include 'includes/db.php';
include 'includes/header.php';

// Check if challenge_id is set
if (isset($_GET['challenge_id'])) {
    $challenge_id = $_GET['challenge_id'];

    // Fetch the challenge details
    $query = "SELECT * FROM challenges WHERE id = $challenge_id";
    $result = mysqli_query($conn, $query);
    $challenge = mysqli_fetch_assoc($result);
} else {
    echo "Invalid challenge ID!";
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Capture user submission
    $user_id = 1; // Assuming logged-in user is with ID 1. You can fetch this from session
    $code = mysqli_real_escape_string($conn, $_POST['code']);
    $language = $_POST['language'];  // Language selected by user (e.g., PHP, Python, C++)

    // Insert submission into the database (Initially, status will be 'Pending')
    $query = "INSERT INTO submissions (user_id, challenge_id, code, language, status) 
              VALUES ($user_id, $challenge_id, '$code', '$language', 'Pending')";
    if (mysqli_query($conn, $query)) {
        echo "<p>Your submission has been received and is being processed!</p>";
    } else {
        echo "<p>Error: " . mysqli_error($conn) . "</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Attempt Challenge - <?php echo $challenge['title']; ?></title>
    <link rel="stylesheet" href="assets/css/courses.css">
</head>
<body>
    <div class="container">
        <h1><?php echo $challenge['title']; ?></h1>
        <p><strong>Category:</strong> <?php echo $challenge['category']; ?></p>
        <p><strong>Description:</strong> <?php echo $challenge['description']; ?></p>
        <p><strong>Input Example:</strong> <?php echo $challenge['input_example']; ?></p>
        <p><strong>Output Example:</strong> <?php echo $challenge['output_example']; ?></p>

        <form action="" method="POST">
            <label for="language">Choose Language:</label>
            <select name="language" id="language" required>
                <option value="C">C</option>
                <option value="C++">C++</option>
                <option value="Python">Python</option>
                <option value="PHP">PHP</option>
            </select>

            <label for="code">Your Code:</label>
            <textarea name="code" id="code" rows="10" required></textarea>

            <button type="submit" class="btn">Submit Code</button>
        </form>
    </div>
</body>
</html>
