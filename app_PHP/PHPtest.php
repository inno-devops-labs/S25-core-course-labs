<?php

date_default_timezone_set('Europe/Moscow'); // Setting the timezone

$current_time = date('Y-m-d H:i:s');

// The HTML document itself
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        h1 {
            font-size: 2em;
            color: #333;
        }
        p {
            font-size: 1.5em;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Current Time in Moscow</h1>
    <p><?php echo $current_time; ?></p>
</body>
</html>