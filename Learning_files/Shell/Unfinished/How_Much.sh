#!/bin/bash


start=$(date +%s)
start_ms=${start:0:16}


howmuch()
{
	if [ $1 -gt $2 ]
	then
		l=$[($2-37)/63+1]
		r=$[($1-37)/63]
	else
		l=$[($1-37)/63+1]
    	r=$[($2-37)/63]
    fi
    for k in $(seq $l $r)
    do
    	str=["M: $[63*$k+37]","B: $[9*$k+5]","C: $[7*$k+4]"]
    	echo $str
    done
}
howmuch 1 100

echo $[(1-37)/63]

# howmuch(1, 100) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]

end=$(date +%s)
end_ms=${end:0:16}
echo -n "cost time is: "
echo "($end_ms - $start_ms)" | bc
