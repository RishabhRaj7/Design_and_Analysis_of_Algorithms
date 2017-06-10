def input_points():
	temp=[]
	n=int(input("Enter number of points:"))
	print("Enter the points:")
	for i in range(n):
		x=int(input("x:"))
		y=int(input("y:"))
		temp.append((x,y))
	return temp

def closestpair(Points):

	def square(x):
		return x*x

	def sqdist(p,q):
		return square(p[0]-q[0])+square(p[1]-q[1])

	best =[(sqdist(Points[0],Points[1]))**0.5, (Points[0],Points[1])]

	def testpair(p,q):
		d=(sqdist(p,q))**0.5
		if d<best[0]:
			best[0]=d
			best[1]=p,q

	def mergey(A,B):
		i=0
		j=0
		temp=[]
		while i<len(A) or j<len(B):
			if j>=len(B) or (i<len(A) and A[i][1]<=B[j][1]):
				temp.append(A[i])
				i+=1
			else:
				temp.append(B[j])
				j+=1
		return temp

	def recur(Points):
		if len(Points)<2:
			return Points
		split=len(Points)/2
		splitx=Points[split][0]
		Points=list(mergey(recur(Points[:split]),recur(Points[split:])))
		E=[p for p in Points if abs(p[0]-splitx)<best[0]]
		for i in range(len(E)):
			for j in range(1,8):
				if i+j<len(E):
					testpair(E[i],E[i+j])
		return Points

	def mergex(A,B):
		i=0
		j=0
		temp=[]
		while i<len(A) or j<len(B):
			if j>=len(B) or (i<len(A) and A[i][0]<=B[j][0]):
				temp.append(A[i])
				i+=1
			else:
				temp.append(B[j])
				j+=1
		return temp

	def sort_p(Points):
		if len(Points)<2:
			return Points
		else:
			m=len(Points)/2
			Pointsl=sort_p(Points[:m])
			Pointsr=sort_p(Points[m:])
			return mergex(Pointsl,Pointsr)

	Points=sort_p(Points)
	recur(Points)
	return best

Points=input_points()
print(closestpair(Points))
