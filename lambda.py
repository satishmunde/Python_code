# This is the one way to define function as we know,
# def fun1(a):
#     return a + 6

# define a function using lambda
# it is function which is created using expression

fun1 = lambda a:a+6
square =  lambda a:a*a
sum = lambda a,b:a+b
a=5
print(fun1(a))
print(square(a))
print(sum(a,10))