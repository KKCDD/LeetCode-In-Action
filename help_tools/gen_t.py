import os

problems = [
    ("6", "ZigZag Conversion")
]

for problem_number, problem_name in problems:
    # Format the problem number with leading zeros
    problem_number = problem_number.zfill(4)

    # Replace spaces with underscores for filename
    filename = f"{problem_number}_{problem_name.replace(' ', '_')}.md"

    with open(filename, 'w') as f:
        f.write(f"# Leetcode {problem_number}. {problem_name}\n\n")
        f.write("## Problem Description\n\n")
        f.write("## Solution\n\n")