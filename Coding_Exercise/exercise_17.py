# Student Scores Report
# You’re building a simple student report generator that combines names and scores.

# Tasks:
#   - Define a function generate_score_report that takes two lists — one with student names and one with their scores.
#   - Use the zip() function to pair each student with their score.
#   - Return a list of strings in the format "Name scored X marks"

names = ["Akash", "Sushant", "Rohit", "Rahul", "Ramesh"]
scores = [50, 70, 40, 60, 80]

for name, score in zip(names, scores):
    print(f"{name} scored {score} marks")


# return [f"{name} scored {score} marks" for name, score in zip(names, scores)]