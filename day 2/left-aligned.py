n = int(input("Enter Number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i), end = "*"*i)
    print()