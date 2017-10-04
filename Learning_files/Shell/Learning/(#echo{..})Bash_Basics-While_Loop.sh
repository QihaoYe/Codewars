#!/bin/bash


start=$(date +%s)
start_ms=${start:0:16}


echo "Count: "{1..20}
# for i in `seq 20`; do echo "Count: $i"; done


end=$(date +%s)
end_ms=${end:0:16}
echo -n "cost time is: "
echo "($end_ms - $start_ms)" | bc
