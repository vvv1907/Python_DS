#/bin/sh

if [ -z "$1" ]
  then
    OUTPUT_FILE="./concatenator.csv"
  else
    OUTPUT_FILE="$1"
fi

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $OUTPUT_FILE

cat 2022-09*.csv | sed -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p' >> $OUTPUT_FILE
