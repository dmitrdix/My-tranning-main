def is_prime(func):
    def wrapper(*args):
        result=func(*args)
        if result <=1:
            print('Составное')
        for i in range(2,int(result**0.5)+1):
            if result%i ==0:
                print('Составное')
        else:
            print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)
result = sum_three(2, 3, 6)
print(result)