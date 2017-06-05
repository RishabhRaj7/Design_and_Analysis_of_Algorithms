def kar(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		n2 = int(n/2)
		a = int(x/10**(n2))
		b = int(x%10**(n2))
		c = int(y/10**(n2))
		d = int(y%10**(n2))
		ac = kar(a,c)
		bd = kar(b,d)
		ad_bc = kar(a+b,c+d) - ac - bd
		p = ac*(10**(n2*2)) + ad_bc*(10**(n2)) + bd
		return p

a = int(input("\nEnter the first no:"))
b = int(input("Enter the second no:"))
pr = kar(a,b)
print ("\nThe product of %d and %d is %d" %(a, b, pr))
