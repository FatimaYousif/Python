#task 1

def factorial(n) :
    if(n==1):
        return n
    else:
        return n*factorial(n-1)
factorial(int(5))
