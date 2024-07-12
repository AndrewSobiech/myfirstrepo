# Functions

# define a function
def greet():

    # Code block for my functions
    ## 
    print("Hello User! How are you?")

# call the greet function
greet()

#function with parameters
def add(a, b):

    return a + b

# call the add function
result = add(5, 9)
print(result)

# function with a default parameter
def greet(name='Guest'):

    print(f"hello, {name}")

greet()
greet("Andrew")

# function with multiple returns
def sum_product(a, b):
    return a+b, a*b
sum_result, product_result = sum_product(5,6)
print(sum_result, product_result)