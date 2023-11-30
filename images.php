<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Motion Sensing Camera Images</title>
</head>
<body>

<h1>Motion Sensing Camera Images</h1>
<br>
<P>To recieve email notifications when motion is detected, input your email below.<P>
<form>
    <input id="email-address" type="text">
    <button id="enter-button" type="button">Submit</button>
</form>

<h3 id="user_email"></h3>

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="/static/collect_email.js"></script>

<P>Images Captured:<P>
<!--php code taken from https://stackoverflow.com/questions/33588691/put-all-images-from-directory-into-html-->
<?php
    $files = scandir('/home/james/Desktop/CS2210/FINAL_PROJECT/images/');
    foreach($files as $file) {
        if($file !== "." && $file !== "..") {
            echo "<img src='$file' />";
        }
    }
?>

</body>
</html>
