import time
#Decorators in Python(@)

#Problem1(Timing Function Execution)
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer 
def example_function(n):
    time.sleep(n)
    print("Hloo world")

# example_function(2)#example_function ran in 2.0001697540283203 time

#Problem2(Debugging Function Calls)
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}"for k,v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper


@debug
def greet(name,greeting="Hello"):
    print(f"{greeting},{name}")

greet("Modi Ji",greeting="Prime Minister of India") # calling : greet with args Modi Ji and kwargs greeting=Prime Minister of India