def caching_fibonacci():
    cache={}
    def fibonacci(n):
        print(cache)
        
        if n == 1:
          return 1
        if n<=0:
            return 0
        if n in cache:
            return cache[n]
        else:
            cache[n]= fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci

fib=caching_fibonacci()
print(fib(10))
print(fib(15))
print(fib(7))

def fibonacci(n, cache={}):
    print(cache)

    if n == 1:
        return 1
    if n<=0:
        return 0
    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(7))