import os
from rag_utils import generate_review_and_fix  # Assuming this function is defined in rag_utils.py

# Path to the code sample (buggy_code.py) inside the 'code_samples' folder
buggy_code_path = "code_samples/buggy_code.py"

# Read the buggy code from the file
with open(buggy_code_path, "r") as file:
    buggy_code = file.read()

# Generate review and fix the code
review, fixed_code = generate_review_and_fix(buggy_code)

# Optional: Print the review and fixed code to the console
print("### Code Review:")
print(review)
print("\n### Auto-fixed Code:")
print(fixed_code)
