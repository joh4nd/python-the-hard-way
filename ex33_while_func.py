def listed_numbers(limit = int(input("Enter limit: ")), increment = int(input("Enter increment: "))):
    """
    To be run from terminal:
    $ python3 -c 'from ex33_while_func import listed_numbers; listed_numbers()'
    """
    
    i = 0
    numbers = []
    
    while i < limit:
        print("At the top i is %d" % i)
        numbers.append(i)
        
        i = i + increment
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)

