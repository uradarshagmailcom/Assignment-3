def factorial(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res
num=int(input("Enter a number: "))
print("Factorial of ",num,"is: ",factorial(num))