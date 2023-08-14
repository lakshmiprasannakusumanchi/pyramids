import sys
def high_pyramid(num):
    return sum([x * x for x in range(num + 1)])
   
def low_even_pyramid(num):
    if num % 2 == 0 and num > 2:
        return sum([x * x for x in range(2,  num + 1,  2)])
    return -1
   
def low_odd_pyramid(num):
    if num %2 != 0 and num > 1:
        return sum([x * x for x in range(1, num + 1, 2)])
    return -1
   
def base1(cubes):
    i = 2
    while(high_pyramid(i) <= cubes):
        i += 1
    return i - 1
   
def possible_pyramids(cubes, j):
    if high_pyramid(j) <= cubes and high_pyramid(j) > 0:
        m.append(str(j) + "H")
        cubes -= high_pyramid(j)
    if low_even_pyramid(j) <= cubes and low_even_pyramid(j) > 0:
        m.append(str(j) + "L")
        cubes -= low_even_pyramid(j)
    if low_odd_pyramid(j) <= cubes and low_odd_pyramid(j) > 0:
        m.append(str(j) + "L")
        cubes -= low_odd_pyramid(j)
    return cubes
def print_possible_pyramids(x, cubes):
    global m
    m = []
    for i in range(x, 1, -1):
        cubes = possible_pyramids(cubes, i)
    if cubes != 0:
        print("impossible")
    else:
        print(" ".join(m))
cubes = int(sys.argv[1])
x = base1(cubes)
print_possible_pyramids(x, cubes)
