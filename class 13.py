# n=int(input("enter a number"))
# sum=0
# i=1
# while i<=n:
#       sum=sum+i
#       i+=1
# print("the sum is",sum)    



n=int(input("enter a number:"))
fac=0
while n>0:
    fac=fac+n
    n=n-1 
print("the fac is",fac)

# start=1
# stop=5
# while start<stop:
#      print(start)
#      start=2**start
# n=int(input("enter a number"))
# sum=0
# i=1
# while i<=n:
#       sum=sum+i
#       i+=1
# print("the sum is",sum)    

# nums=[1,4,9,16,25,36,49,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
# i=0
# x=36
# while i<len(nums) :
#     if (nums[i]==x):
#     print("foud at x"i)
#     i+=1


# quantity=8
# price=120

# while quantity <=12:
#     total=quantity*price
#     discount=0
#     if quantity>10:
#         discountrate=0.1
#         discount=total*discountrate
#         total=total-discount
#         quantity= quantity+1
#         print(total) 
n=int(input("enter an integer"))
print("the divisors of the number are ")
for i in range(1,n+1):
    if(n%i==0):
        print(i)
       

        