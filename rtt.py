# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
def test_fibo(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

test1= test_fibo(10)
for i in test1:
    print(i)

