from sys import argv # argv = command line arguments

script, first, second, third = argv # when running the script from terminal, pass three arguments besides the script ex13.py; else python3 raises an error.

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

forgotten_arg = input("The forgotten input is: ")
input("Ohh I also forgot: ")


