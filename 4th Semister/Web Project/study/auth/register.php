<?php
session_start();
require '../db.php';

// Initialize message variable
$message = "";
$success = false;

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and trim input
    $email = trim(htmlspecialchars($_POST['email']));
    $username = trim(htmlspecialchars($_POST['username']));
    $password = trim(htmlspecialchars($_POST['password']));
    $confirm_password = isset($_POST['confirm_password']) ? trim(htmlspecialchars($_POST['confirm_password'])) : '';

    // Check if email already exists
    $stmt = $conn->prepare("SELECT id FROM users WHERE email = ?");
    $stmt->execute([$email]);

    if ($stmt->rowCount() > 0) {
        $message = "This email is already registered. Please choose another one.";
    } elseif ($password !== $confirm_password) {
        $message = "Passwords do not match. Please try again.";
    } elseif (!preg_match("/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/", $password)) {
        // Check password strength: minimum 8 characters, at least one letter and one number
        $message = "Password must be at least 8 characters long and contain at least one letter and one number.";
    } else {
        // Hash the password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $conn->prepare("INSERT INTO users (email, password, username, created_at) VALUES (?, ?, ?, NOW())");

        if ($stmt->execute([$email, $hashedPassword, $username])) {
            $message = "Registration successful. You can now <a href='login.php'>log in</a>.";
            $success = true;
            // Redirect to login after successful registration
            header("Location: login.php");
            exit();
        } else {
            $message = "Error: Could not complete registration.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register - CSE Study Room</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .message {
            text-align: center;
            margin: 10px 0;
            font-weight: bold;
        }
        .message.error {
            color: red;
        }
        .message.success {
            color: green;
        }
        .login-link {
            text-align: center;
            margin-top: 10px;
        }
        .login-link a {
            color: #4CAF50;
            text-decoration: none;
        }
        .login-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Register</h2>

    <?php if (!empty($message)): ?>
        <p class="message <?= $success ? 'success' : 'error' ?>"><?= $message ?></p>
    <?php endif; ?>

    <form method="POST" action="register.php">
        <input type="email" name="email" placeholder="Enter your email" required>
        <input type="text" name="username" placeholder="Enter your username" required>
        <input type="password" name="password" placeholder="Enter your password" required>
        <input type="password" name="confirm_password" placeholder="Confirm your password" required>
        <button type="submit">Register</button>
    </form>

    <div class="login-link">
        <p>Already have an account? <a href="login.php">Login here</a></p>
    </div>
</div>

</body>
</html>
