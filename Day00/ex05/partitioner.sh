#/bin/sh

if [ -z "$1" ]
  then
    INPUT_FILE="../ex03/hh_positions.csv"
  else
    INPUT_FILE="$1"
fi

awk -F '\",\"|T' 'NR == 1 { a=$0; next } { b=$2".csv" } !($2 in c) { c[$2]; print a > b } { print >> b }' $INPUT_FILE
