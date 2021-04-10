def say_hello():
    print('hello')

print(say_hello)

def say_something(some_func):
    for _ in range(3):
        some_func()

say_something(say_hello)
    
        