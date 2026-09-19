import sys
import os

# Check the user gave both required arguments
if len(sys.argv) < 3:
    print("Usage: python new_writeup.py \"Challenge Name\" \"path/to/folder\"")
    sys.exit(1)

challenge_name = sys.argv[1]
save_path = sys.argv[2]

# Turn "Challenge Name" into a safe filename like "challenge-name.md"
filename = challenge_name.lower().replace(" ", "-") + ".md"

# Make sure the target folder exists adn creates it if it doesn't
os.makedirs(save_path, exist_ok=True)

# Combine folder + filename into the full file path
full_path = os.path.join(save_path, filename)

# The template used
template = f"""# {challenge_name} — {category}
Difficulty: 
Tools: 

What I was given: 
What worked: 
Steps: 
Things I learned: 
"""

# Make sure we don't overwrite an existing writeup by accident
if os.path.exists(filename):
    print(f"File '{filename}' already exists.")
    sys.exit(1)

# Write the file
with open(filename, "w") as f:
    f.write(template)

print(f"Created {filename}")
