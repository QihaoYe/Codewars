#!/bin/bash


start=$(date +%s)
start_ms=${start:0:16}

nbMonths()
{
    a=$1
    b=$2
    c=0
    d=0
    e=$4
    while(($(echo "($a+$c-$b)/1" |bc) < 0))
    do
        a=$(echo "scale=3;$a*(100-$e)/100" |bc)
        b=$(echo "scale=3;$b*(100-$e)/100" |bc)
        c=$[$c+$3]
        d=$[$d+1]
        if [ $[$d%2] == 1 ]
        then
            e=$(echo "$e+0.5" |bc)
        fi
    done
    echo $d $(echo "($a+$c-$b+0.5)/1" |bc)
    # Round
}
nbMonths $1 $2 $3 $4

end=$(date +%s)
end_ms=${end:0:16}
echo -n "cost time is: "
echo "($end_ms - $start_ms)" | bc
