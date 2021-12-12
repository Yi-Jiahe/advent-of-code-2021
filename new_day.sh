if [[ -z $1 ]]; then
  echo "Please provide a day"
  exit 1
fi

day=$1

if [ -d "day_${day}" ]; then
  echo "Directory already exists for day ${day}"
  exit 1
fi

mkdir "day_${day}"
touch "day_${day}/__init__.py"
cp template.py "day_${day}/main.py"
touch "day_${day}/puzzle_input.txt"
touch "tests/test_day_${day}.py"