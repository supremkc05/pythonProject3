# using generators
# generators in python are special type of function which can be used to generate the function one by one as you iterate over it 
def my_generator():
    for i in range(50000):
        # complex computations here...
        yield i * 2
        # yield i
gen= my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# for j in gen:
#     print(j)
# it will generate up to 50000 elements, but stop at the first breakpoint.