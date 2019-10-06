def positiveCount(numbers):
#if the type of numbers is not a list it will raise a type error
    if type(numbers) != list:
        raise TypeError("Not a list")
    count = 0
    #if a number is greater than 0 then add 1
    for element in numbers:
        if element >0:
            count = count + 1
    return count

positiveCount ([0, 1, 2, 3, 4, 5])
positiveCount ("a, b, c, d, e, f")
