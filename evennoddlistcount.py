evens=0;odds=0;list=[]
n=int(input("Enter no of elements in list:"))
for i in range(0,n):
    ele=int(input())
for val in list:
    if val % 2 == 0:
        evens+=val
    else:
        odds+=val
print(f"List :{list}")
print(f"Sum of Even Numbers:{evens}")
print(f"Sum of Odd Numbers:{odds}")