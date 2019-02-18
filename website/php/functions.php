<?php 
function createCfg($pin)
{
    if ($pin == 0)
        return;

    $varsToCheck = array('pwmClock', 'pwmRange', 'i2cAdress', 'poti', 'setupSleepTime', 'configWebsite', 'livestreamUrl', 'databaseAdress', 'databaseUser', 'databasePassword');

    // wenn es klappt brauch ich die foreach unten nicht hehe
    // ach ja es ist 3:01 wenn du morgen/bald/gleich nicht mehr weißt was du machen wolltest
    // du wolltest ne website erstellen auf der man mit html elements in einer index.php die cfg erstellen kann für das kamera projekt
    // muss man als .cfg speichern damit der python cfg parser es parsen kann alles dazu hier: https://docs.python.org/3.4/library/configparser.html
    foreach ($varsToCheck as $var) {
        if (isset($_POST[$var])) {
            $var = $_POST[$var];
        }
        var_dump($var);
    }

    if (isset($_POST['pwmClock'])) {
        $pwmClock = $_POST['pwmClock'];
    }
    if (isset($_POST['pwmRange'])) {
        $pwmRange = $_POST['pwmRange'];
    }
    if (isset($_POST['i2cAdress'])) {
        $i2cAdress = $_POST['i2cAdress'];
    }
    if (isset($_POST['poti'])) {
        $poti = $_POST['poti'];
    }
    if (isset($_POST['setupSleepTime'])) {
        $setupSleepTime = $_POST['setupSleepTime'];
    }
    if (isset($_POST['configWebsite'])) {
        $configWebsite = $_POST['configWebsite'];
    }
    if (isset($_POST['livestreamUrl'])) {
        $livestreamUrl = $_POST['livestreamUrl'];
    }
    if (isset($_POST['databaseAdress'])) {
        $databaseAdress = $_POST['databaseAdress'];
    }
    if (isset($_POST['databaseUser'])) {
        $databaseUser = $_POST['databaseUser'];
    }
    if (isset($_POST['databasePassword'])) {
        $databasePassword = $_POST['databasePassword'];
    }

    return $cfg = array(
        'General' => array(
            
        ),
        'Stream' => array(

        ),
        'database' => array(

        )
    );
}
?>