""" Write a program to create "BCA.txt" file which contain information about BCA course. 
   count and print the total number of lines starting with ‘A’, ‘B’, and ‘C’ in "intro.txt" file."""
# Create the BCA.txt file with BCA course information
bca_info = """
BCA Course Information:

- BCA stands for Bachelor of Computer Applications.
- It is a 3-year undergraduate program in the field of computer applications.
- The course covers various aspects of computer science and programming.
- Graduates of BCA can pursue careers in software development, IT consulting, etc.
"""

with open("BCA.txt", "w") as f:
    f.write(bca_info)

# Count lines starting with 'A', 'B', and 'C' in intro.txt file
file = "intro.txt"
a = 0
b = 0
c = 0

with open(file, "r") as f:
    for line in f:
        if line.strip().startswith('A'):
            a += 1
        elif line.strip().startswith('B'):
            b += 1
        elif line.strip().startswith('C'):
            c += 1

# Print the counts
print("Number of lines starting with 'A':", a)
print("Number of lines starting with 'B':", b)
print("Number of lines starting with 'C':", c)
