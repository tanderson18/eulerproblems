def sum_of_squares(limit):
    total = 0
    for i in range (limit+1):
        total += i**2
    return total

def square_of_sum(limit):
    total = 0
    for i in range (limit+1):
        total += i
    return total**2

s1 = sum_of_squares(100)
s2 = square_of_sum(100)

print("Answer: " + str(s2-s1))
