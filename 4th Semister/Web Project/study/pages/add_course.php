<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Add New Course - CSE Study Room</title>
  <link rel="stylesheet" href="../assets/css/courses.css">
  <style>
    body { font-family: Arial; padding: 20px; background: #f4f4f4; }
    form { background: #fff; padding: 20px; max-width: 600px; margin: auto; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    label { display: block; margin-top: 10px; font-weight: bold; }
    input, select, textarea { width: 100%; padding: 8px; margin-top: 5px; border-radius: 4px; border: 1px solid #ccc; }
    button { margin-top: 20px; padding: 10px 20px; background: #007bff; color: #fff; border: none; border-radius: 5px; cursor: pointer; }
    button:hover { background: #0056b3; }
  </style>
</head>
<body>

  <h2>Add New Course</h2>

  <form action="upload_course.php" method="POST" enctype="multipart/form-data">
    <label>Course Title:</label>
    <input type="text" name="title" required>

    <label>Description:</label>
    <textarea name="description" rows="4" required></textarea>

    <label>Content Type:</label>
    <select name="content_type" id="content_type" onchange="toggleFields()" required>
      <option value="">-- Select Type --</option>
      <option value="link">External Link</option>
      <option value="pdf">PDF File</option>
      <option value="video">Video File</option>
      <option value="html">HTML Content</option>
    </select>

    <div id="file_input" style="display:none;">
      <label>Upload File (PDF or MP4):</label>
      <input type="file" name="course_file" accept=".pdf,video/mp4">
    </div>

    <div id="html_input" style="display:none;">
      <label>HTML Content or Link:</label>
      <textarea name="course_html" rows="6" placeholder="For 'link' type, paste course URL here. For 'html' type, write HTML content here."></textarea>
    </div>

    <button type="submit">Add Course</button>
  </form>

  <script>
    function toggleFields() {
      const type = document.getElementById('content_type').value;
      document.getElementById('file_input').style.display = (type === 'pdf' || type === 'video') ? 'block' : 'none';
      document.getElementById('html_input').style.display = (type === 'link' || type === 'html') ? 'block' : 'none';
    }
  </script>

</body>
</html>
