from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# study drills

# 6 python3 refers to fileinput, not file. q
# close the openings
txt.close()
print(txt.close())
txt_again.close()
print(txt_again.close())
