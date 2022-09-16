#!/bin/sh

API="https://api.hh.ru/vacancies"

VACANCY_NAME="${1/ /+}"

VACANCY_AMOUNT="20"

JQ="/Users/hcolumbu/homebrew/Cellar/jq/1.6/bin/jq"

OUTPUT_FILE="./hh.json"

curl -k -H "User-Agent: api-test-agent" -G "$API?text=$VACANCY_NAME&per_page=$VACANCY_AMOUNT" | $JQ > $OUTPUT_FILE
