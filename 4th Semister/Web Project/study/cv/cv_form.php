<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: ../auth/login.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Generate CV – CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/cv_form.css">
</head>
<body>
  <div class="container">
    <h1>Build Your CV</h1>

    <form id="cvForm" method="POST" action="cv_generate.php">
      <div class="section">
        <label for="position">Desired Job Position</label>
        <input type="text" name="position" id="position" required>
      </div>

      <div class="section">
        <h3>Personal Details</h3>
        <input type="text" name="first_name" placeholder="First Name" required>
        <input type="text" name="last_name" placeholder="Last Name" required>
        <input type="text" name="headline" placeholder="Headline">
        <input type="email" name="email" placeholder="Email" required>
        <input type="text" name="phone" placeholder="Phone">
        <textarea name="address" placeholder="Address"></textarea>
      </div>

      <div class="section-buttons">
        <button type="button" onclick="addSection('Education')">+ Education</button>
        <button type="button" onclick="addSection('Experience')">+ Experience</button>
        <button type="button" onclick="addSection('Skills')">+ Skills</button>
        <button type="button" onclick="addSection('Languages')">+ Languages</button>
        <button type="button" onclick="addSection('Hobbies')">+ Hobbies</button>
        <button type="button" onclick="addSection('Certificates')">+ Certificates</button>
      </div>

      <div id="dynamicSections"></div>

      <div class="submit-section">
        <button type="submit">Generate CV</button>
      </div>
    </form>
  </div>

  <script src="../assets/js/cv_form.js"></script>
</body>
</html>
