"""Taks 1"""


# add15 = lambda x : 15 + x

# print(add15(1))
# print(add15(-2))


"""Task 2"""

# isOdd = lambda x : bool(x % 2)
# isEven = lambda x : not bool(x % 2)
# getParity = lambda x, parity : parity == 'odd' if bool(x % 2) else parity == 'even'




# print(isOdd(2), isEven(2))
# print(isOdd(1), isEven(1))
# print(getParity(2, 'odd'), getParity(2, 'even'))
# print(getParity(1, 'odd'), getParity(1, 'even'))


"""Task 3"""

# starts_with_p = lambda x : x.lower().startswith('p')

# starts_with_p = lambda x : x.startswith('p') or x.startswith('P')

# print(starts_with_p("Python"))
# print(starts_with_p("JavaScript"))
# print(starts_with_p("pirate"))



"""Task 4"""

numbers = [2, 4, 5, 7, 9, 14]
factor = 2



multiplication = map(lambda x : x * factor, numbers)


print(list(multiplication))

