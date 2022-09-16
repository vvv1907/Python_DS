#/bin/sh

if [ -z "$1" ]
  then
    INPUT_FILE="../ex00/hh.json"
  else
    INPUT_FILE="$1"
fi

JQ="/Users/hcolumbu/homebrew/Cellar/jq/1.6/bin/jq"

FILTER_FILE="filter.jq"

OUTPUT_FILE="hh.csv"

cat $INPUT_FILE | $JQ -rf $FILTER_FILE > $OUTPUT_FILE
