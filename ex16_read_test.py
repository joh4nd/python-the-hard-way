from sys import argv

script, filename = argv

txt = open(filename)

print("Read the text written in ex16.py:\n")
print(txt.read())
txt.close()
