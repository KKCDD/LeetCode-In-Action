import os

problems = [
    ("27", "Remove elements"),
    ("179", "Largest Number"),
    ("75", "Sort Colors"),
    ("215", "Kth Largest Element"),
    ("4", "Median of Two Sorted Arrays"),
    ("206", "Reverse Linked List"),
    ("876", "Middle of the Linked List"),
    ("160", "Intersection of Two Linked Lists"),
    ("141", "Linked List Cycle"),
    ("92", "Reverse Linked List II"),
    ("328", "Odd Even Linked List")
]

for problem_number, problem_name in problems:
    # Replace spaces with underscores for filename
    filename = f"{problem_number}_{problem_name.replace(' ', '_')}.md"

    with open(filename, 'w') as f:
        f.write(f"# Leetcode {problem_number}. {problem_name}\n\n")
        f.write("## Problem Description\n\n")
        f.write("## Solution\n\n")