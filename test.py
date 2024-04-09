def decorator_example(func):
    print("example")
    c = 1
    def wrapper(name, x=c):
        func(name)
        return print("inner_one", name,  x)
  
    return wrapper

# @decorator_example
def say(name):
    return print("HELLO")

# say("David")

y = decorator_example(say)
y("David")


# decorator_example(say)("David")

# a = [1,2,3,4,]
# print(*a)

# b = {"a": 1, "f":3}
# print(b)

# def my_gen(n):
#     for i in range(n):
#         print(f"i before yield {i}")
#         yield i
#         print(f"N={n} i={i}")

# for i in my_gen(3):
#     print(i)
        
# q = my_gen(3)
# print(next(q))
# print(next(q))
# print(next(q))



