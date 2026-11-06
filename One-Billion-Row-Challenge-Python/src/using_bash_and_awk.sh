#!/usr/bin/env bash

if [ ! -f data/measurements.txt ]; then
    echo "Arquivo data/measurements.txt não encontrado."
    exit 1
fi


if [ -z "$1" ]; then
    QTD="$(wc -l < data/measurements.txt)"
else
    QTD="$1"
fi

echo "Quantidade de Registros: ${QTD}"

SECONS=0
#head -n $QTD data/measurements.txt | pv -p -e -t -l -s $QTD | awk -F ";" \
head -n $QTD data/measurements.txt | awk -F ";" \
'{
	if (!($1 in cnts)){
		mins[$1] = $2 
		maxs[$1] = $2 
	}
	else{
		mins[$1] = $2<mins[$1] ? $2 : mins[$1]
		maxs[$1] = $2>maxs[$1] ? $2 : maxs[$1]
	}
	cnts[$1] += 1;
	sums[$1] += $2;
} END { for (v in cnts) print v ";" maxs[v] ";" mins[v] ";" sums[v]/cnts[v] }' | sort

TEMPO=$SECONDS

printf "\n"
printf "====================================\n"
printf "Tempo de processamento: %02d:%02d:%02d\n" \
    $((TEMPO / 3600)) \
    $((TEMPO % 3600 / 60)) \
    $((TEMPO % 60))
printf "====================================\n"