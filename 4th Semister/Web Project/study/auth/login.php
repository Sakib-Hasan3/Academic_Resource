<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login - CSE Study Room</title>
    <link rel="stylesheet" href="../assets/css/login.css">
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri&display=swap" rel="stylesheet">
</head>
<body>
<div class="login-wrapper">
    <!-- Left Section -->
    <div class="login-left">
        <div class="login-content">
            <img src="../assets/images/login.png" alt="CSE Study Room" class="animated-img">
            <div class="login-text">
                <h2>Welcome to <span class="highlight">CSE Study Room</span></h2>
                <p>Explore, Learn, and Build. This platform is your all-in-one portal for CSE learning, mentorship, and collaboration. Start your academic journey with confidence.</p>
            </div>
        </div>
    </div>

    <!-- Right Section -->
    <div class="login-right">
        <div class="form-box">
            <h2>🔐 Login</h2>
            <?php 
            session_start();
            include('../db.php');
            $message = "";

            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $email = htmlspecialchars($_POST['email']);
                $password = $_POST['password'];
                $sql = "SELECT * FROM users WHERE email = ?";
                $stmt = $conn->prepare($sql);
                $stmt->execute([$email]);
                $user = $stmt->fetch(PDO::FETCH_ASSOC);

                if ($user && password_verify($password, $user['password'])) {
                    $_SESSION['user_id'] = $user['id'];
                    $_SESSION['email'] = $user['email'];
                    header("Location: ../pages/dashboard.php");
                    exit();
                } else {
                    $message = "Invalid email or password.";
                }
            }
            ?>

            <?php if (!empty($message)): ?>
                <p class="error"><?php echo htmlspecialchars($message); ?></p>
            <?php endif; ?>

            <form method="POST" action="">
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>

            <p class="register-text">Don't have an account? <a href="register.php">Register here</a></p>
        </div>
    </div>
</div>
</body>
</html>