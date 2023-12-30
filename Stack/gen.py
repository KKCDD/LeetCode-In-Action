import os

problems = [
    ("155", "Min Stack"),
    ("232", "Implement Queue using Stacks"),
    ("150", "Evaluate Reverse Polish Notation"),
    ("224", "Basic Calculator II"),
    ("20", "Valid Parentheses"),
    ("1472", "Design Browser History"),
    ("1209", "Remove All Adjacent Duplicates in String II"),
    ("1249", "Minimum Remove to Make Valid Parentheses"),
    ("735", "Asteroid Collision")
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