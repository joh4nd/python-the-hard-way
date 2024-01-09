def listed_numbers(limit = int(input("Enter limit: "))):
    """
    To be run from terminal:
    $ python3 -c 'from ex33_for_func import listed_numbers; listed_numbers()'
    """
    
    numbers = []
    
    for i in range(0, limit):
        print("At the top i is %d" % i)
        numbers.append(i)
        
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)
