#/bin/sh

if [ -z "$1" ]
  then
    INPUT_FILE="../ex01/hh.csv"
  else
    INPUT_FILE="$1"
fi

OUTPUT_FILE="hh_sorted.csv"

cat $INPUT_FILE | head -n 1 > $OUTPUT_FILE

cat $INPUT_FILE | tail -n +2 | sort -t "," -k2 -k1 >> $OUTPUT_FILE
