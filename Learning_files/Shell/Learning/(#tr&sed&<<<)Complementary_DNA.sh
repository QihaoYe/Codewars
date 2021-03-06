#!/bin/bash


start=$(date +%s)
start_ms=${start:0:16}

# echo $1 | tr 'ATCG' 'TAGC'
# echo $1 | tr [ATCG] [TAGC]
# echo $1 | sed y/ATCG/TAGC/
tr ATCG TAGC <<< $1

end=$(date +%s)
end_ms=${end:0:16}
echo -n "cost time is: "
echo "($end_ms - $start_ms)" | bc
