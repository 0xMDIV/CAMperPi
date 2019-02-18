<!--
# Config Parser for the CAMperPi Project
# Made by MDIV
# Version 0.0.1
# Use xampp to use it local or reach me here: ariz0na.de/contact
-->
<?php 
    include('php/functions.php');

    $startInstallation = false;
    $pin = "";
    $pwmClock = 192;
    $pwmRange = 2000;
    $i2cAdress = 0x48;
    $poti = 0x00;
    $setupSleepTime = 1;

    $configWebsite = "";
    $livestreamUrl = "";

    $databaseAdress = "";
    $databaseUser = "";
    $databasePassword = "";

    if(isset($_POST['pin'])) {
        $pin = $_POST['pin'];
        //add ghere all values from downunder
        createCfg($pin);
    }
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CAMperPi Config Creator</title>
</head>

<body>
<h1>Configurieren der CFG</h1>
    <form id="login" action="">
    <fieldset style="width:150px">
        <label><b>Main settings</b></label>
        <br>
        Pin: <input type="number" min="1" max="2" name="pin"><br>
        PWM Clock: <input type="number" min="1" max="4" name="pwmClock"><br>
        PWM Range: <input type="number" min="1" max="5" name="pwmRange"><br>
        i2c Adresse: <input type="number" min="1" max="5" name="i2cAdress"><br>
        Potentiometer Adresse: <input type="number" min="1" max="5" name="poti"><br>
        SleepTimer: <input type="number" min="1" max="2" name="setupSleepTime"><br>
    </fieldset>
    <fieldset style="width:150px">
        <label><b>Stream Settings</b></label>
        Config Website URL: <input type="url" min="3" max="50" name="cfgURL"><br>
        Livestream Website URL: <input type="url" min="1" max="50" name="streamURL"><br>
    </fieldset>
    <fieldset style="width:150px">
        <label><b>Database Settings</b></label>
        Database Adress: <input type="url" min="3" max="20" name="dbAdresse"><br>
        Database User: <input type="text" min="3" max="20" name="dbUser"><br>
        Database Password: <input type="password" min="3" max="20" name="dbPassword"><br>
    </fieldset>
    Config erstellen <input type="submit"> 
    </form>
</body>

</html>