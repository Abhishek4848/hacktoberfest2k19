print("Python program to display prime factors of a given number")
a=int(input("enter a number=")
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n =n// i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
f=prime_factors(a)
print ("Prime factors of ",a,"=",f)      
      
