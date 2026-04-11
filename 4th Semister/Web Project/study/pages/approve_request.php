<?php
session_start();
include('../db.php');  // adjust path if needed

// Redirect if not logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: ../auth/login.php');
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['request_id'])) {
    $requestId = intval($_POST['request_id']);

    // 1) Mark the mentorship request as approved
    $update = $conn->prepare("
        UPDATE mentorship_requests
           SET status = 'approved'
         WHERE id = ?
    ");
    $update->execute([$requestId]);

    // 2) Fetch the mentor_id and user_id for this request
    $select = $conn->prepare("
        SELECT mentor_id, user_id
          FROM mentorship_requests
         WHERE id = ?
    ");
    $select->execute([$requestId]);
    $row = $select->fetch(PDO::FETCH_ASSOC);

    if ($row) {
        $mentorId = (int)$row['mentor_id'];
        $userId   = (int)$row['user_id'];

        // 3) Insert into study_groups
        $insert = $conn->prepare("
            INSERT INTO study_groups (mentor_id, user_id)
            VALUES (?, ?)
        ");
        $insert->execute([$mentorId, $userId]);

        // 4) Redirect back to the mentor’s page
        header("Location: mentorship.php?mentor_id={$mentorId}");
        exit();
    }
}

// If accessed directly or something went wrong, redirect back
header('Location: mentorship.php');
exit();
