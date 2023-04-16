<?php
$plant = shell_exec("python3 plant.py");
echo "<?xml version=\"1.0\"?>\n";
?>

<vxml version = "2.1" application="xxxxxx">
    <form>
        <block>
            <var name="plant" expr="'<?=$plant?>'"/>
            <prompt>Recommended plant is: <value expr="plant"/>.</prompt>
        </block>
    </form>
</vxml>