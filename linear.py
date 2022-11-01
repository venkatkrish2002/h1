a=[33,4,55,67,22,88]
key=int(input("enter the search:"))
for i in range(len(a)):
    if key==a[i]:
        print("found at index",i)
        break
else:
    print("not found")
