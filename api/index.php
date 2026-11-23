<?php
// Vercel Serverless Entry Point & Front-Controller for GameKart
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$file = ltrim($uri, '/');

$rootDir = realpath(__DIR__ . '/..');

// Default landing page
if (empty($file) || $file === 'index.php') {
    chdir($rootDir);
    require $rootDir . '/index.php';
    exit;
}

$target = $rootDir . '/' . $file;
if (file_exists($target) && pathinfo($target, PATHINFO_EXTENSION) === 'php') {
    chdir($rootDir);
    require $target;
    exit;
}

// Fallback to index.php
chdir($rootDir);
require $rootDir . '/index.php';
