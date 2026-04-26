res = lambda a: print("pair") if a % 2 == 0 else print("impair")
res(10)
res(3)

divisible =  lambda a, b: f"{a} est divisible par {b}" if a % b == 0 else f"{a} n'est pas divisible par {b}"
print(divisible(10, 5))
print(divisible(10, 3))


