DAY=$1

mkdir "day_$1"
touch "day_$1/__init__.py"
cp template.py "day_$1/main.py"
touch "day_$1/puzzle_input.txt"
touch "tests/test_day_$1.py"