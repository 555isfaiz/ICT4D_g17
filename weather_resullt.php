<?php
$weather = shell_exec("python3 weather.py");
echo "<?xml version=\"1.0\"?>\n";
?>

<vxml version = "2.1" application="xxxxxx">
    <form>
        <block>
            <var name="weather" expr="'<?=$weather?>'"/>
            <prompt>The weather will be: <value expr="weather"/>.</prompt>
        </block>
    </form>
</vxml>