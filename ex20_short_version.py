from sys import argv

def print_a_line(line_count = 1, f = open(argv[1])):
    """Prints three lines starting from 1"""
    print("Let's print three lines:")
    while 0 < line_count < 4:
        print(line_count, f.readline())
        line_count += 1

    f.seek(0)
    f.close()

print_a_line(1)
