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
    $isVercel = getenv('VERCEL') !== false || isset($_SERVER['VERCEL']);
    $hostMsg = $isVercel 
        ? "<b>Running on Vercel:</b> Please configure your Cloud MySQL database environment variables (<code>DB_HOST</code>, <code>DB_USER</code>, <code>DB_PASS</code>, <code>DB_NAME</code>, <code>DB_PORT</code>) in your Vercel Project Settings." 
        : "Make sure MySQL is running in XAMPP on port $port.";

    die("<div style='font-family:Arial,sans-serif;padding:30px;background:#17121a;color:#fff;border-radius:12px;max-width:650px;margin:50px auto;text-align:center;border:1px solid #ce5cff;box-shadow:0 8px 30px rgba(206,92,255,0.2);'>
        <h2 style='color:#ce5cff;margin-bottom:12px;'>🎮 GameKart Database Setup</h2>
        <p style='color:#e2e8f0;font-size:15px;'>Could not connect to MySQL database.</p>
        <p style='color:#a0aec0;font-size:13px;background:rgba(255,255,255,0.05);padding:10px;border-radius:6px;word-break:break-all;'>Error: " . htmlspecialchars(mysqli_connect_error()) . "</p>
        <p style='font-size:14px;color:#cbd5e1;line-height:1.6;'>$hostMsg</p>
    </div>");
}

mysqli_set_charset($con, "utf8mb4");
?>
