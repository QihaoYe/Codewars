<?php 

function inArray($array1, $array2) 
{
    $result = array();
    foreach ($array1 as $x)
    {
        foreach ($array2 as $y)
        {
            if (strpos($y, $x) == true or $y == $x)
            {
                array_push($result, $x);
                break;
            }
        }
    }
    sort($result);
    return $result;
}

$a2 = ["lively", "alive", "harp", "sharp", "armstrong"];
$a1 = ["arp", "live", "strong"];

$start = microtime(true);

$output = inArray($a1, $a2);

$end = microtime(true);

foreach ($output as $i)
{
    echo $i;
    echo "\n";
}

printf("%f\n", $end - $start);

?>
