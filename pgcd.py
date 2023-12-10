print ("PGCD(A,B)")
A =int(input ("A ==> "))
B =int(input ("B ==> "))
if A > B :
	min = B
else :
	min = A
for i in range(1,min+1):
	if A % i == 0 and B % i == 0 :
		R = i
print ("PGCD (",A,",",B,") =",R)

