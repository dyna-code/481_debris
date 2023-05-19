#!/bin/bash

# Get the list of test cases to run
#test_cases=$1
original_coverage=36

# Clean up any previous coverage data
#find . -name "*.gcda" -exec rm -f {} \;
rm *.gcda pngout.png

#IFS=',' read -ra test_cases_array <<< "$test_cases"

echo hello

for test_case in *; do
    echo hello 
    #$test_case
    #./pngtest $test_case   
done

gcov *.c

# for test_case in "${test_cases_array[@]}"; do
#     ./pngtest "${test_case}.png"
#     gcov *.c
# done

# Generate coverage data
#gcov -b *.c >/dev/null 2>&1

# # Run pngtest for each test case
# #IFS=',' read -ra test_cases_array <<< "$test_cases"


# # Generate coverage data
# #gcov -b *.c >/dev/null 2>&1

# Calculate line coverage percentage

# total_lines=$(grep -hc -E "(#####|-):" *.c.gcov)
# uncovered_lines=$(grep -c "#####:" *.c.gcov)
# covered_lines=$((total_lines - uncovered_lines))
# line_coverage=$(echo "scale=2; $covered_lines * 100 / $total_lines" | bc)

# Check if the line coverage is the same as the original line coverage (36.19%)

# if [ $(echo "$line_coverage >= $original_coverage" | bc) -eq 1 ]; then
#     echo "1" # Interesting: same or better coverage
# else
#     echo "0" # Not interesting: lower coverage
# fi
