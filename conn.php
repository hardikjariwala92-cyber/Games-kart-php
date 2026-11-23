<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

$hostname = getenv('DB_HOST') ?: "127.0.0.1";
$username = getenv('DB_USER') ?: "root";
$password = getenv('DB_PASS') !== false ? getenv('DB_PASS') : "";
$database = getenv('DB_NAME') ?: "kmart";
$port     = getenv('DB_PORT') ? (int)getenv('DB_PORT') : 3306;

// First attempt to connect to specified database (kmart)
$con = @mysqli_connect($hostname, $username, $password, $database, $port);

// If kmart fails, fallback to project database
if (!$con) {
    $con = @mysqli_connect($hostname, $username, $password, "project", $port);
}

// If still not connected, connect to server and attempt selecting kmart or project
if (!$con) {
    $con = @mysqli_connect($hostname, $username, $password, "", $port);
    if ($con) {
        if (!@mysqli_select_db($con, $database) && !@mysqli_select_db($con, "project")) {
            // neither database could be selected
        }
    }
}

if (!$con) {
    die("<div style='font-family:Arial,sans-serif;padding:20px;background:#1a1a2e;color:#fff;border-radius:8px;max-width:600px;margin:50px auto;text-align:center;'>
        <h2 style='color:#ff4757;'>⚠️ Database Connection Error</h2>
        <p>Could not connect to MySQL database.</p>
        <p style='color:#a4b0be;font-size:13px;'>Error: " . htmlspecialchars(mysqli_connect_error()) . "</p>
        <p style='font-size:14px;'>Make sure MySQL is running in XAMPP on port $port.</p>
    </div>");
}

mysqli_set_charset($con, "utf8mb4");
?>
