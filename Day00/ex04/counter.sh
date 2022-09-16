#/bin/sh

if [ -z "$1" ]
  then
    INPUT_FILE="../ex03/hh_positions.csv"
  else
    INPUT_FILE="$1"
fi

OUTPUT_FILE="hh_uniq_positions.csv"

echo '"name","count"' > $OUTPUT_FILE

cat $INPUT_FILE | tail -n +2 | awk \
	'BEGIN { FS = OFS = "," }
    {
		if (index($3, "Junior"))
            JUNIOR++
        if (index($3, "Middle"))
            MIDDLE++
        if (index($3, "Senior"))
            SENIOR++
    }
    END { print "\"Junior\"", 
            JUNIOR "\n\"Middle\"", 
            MIDDLE "\n\"Senior\"",
			SENIOR
	}' \
| sort -t "," -rnk2 >>  $OUTPUT_FILE
