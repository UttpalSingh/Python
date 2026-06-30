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
