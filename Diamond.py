n=int(raw_input("Enter the order of diamond: "))
for i in range (2*n-1):
    if i<n:
        print " "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1)
    else:
        print " "*(i-(n-1))+"*"*(2*(2*(n-1)-i)+1)+" "*(i-(n-1))
