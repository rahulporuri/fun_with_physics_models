import sympy

r, phi = sympy.symbols('r phi')

gmn= sympy.Matrix([[1,0],[0,r**2]])
gMN= gmn**(-1)

sum = 0
for o in [r, phi]:
	if o == r:
		j = 0
		print (1./2)*gMN[2*0+j]*(sympy.diff(gmn[2*1+j],r) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*1+1],r))
		sum += (1./2)*gMN[2*0+j]*(sympy.diff(gmn[2*1+j],r) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*1+1],r))
	if o == phi:
		j = 1
		print (1./2)*gMN[2*0+j]*(sympy.diff(gmn[2*1+j],phi) +sympy.diff(gmn[2*1+j],phi) -sympy.diff(gmn[2*1+1],phi))
		sum += (1./2)*gMN[2*0+j]*(sympy.diff(gmn[2*1+j],phi) +sympy.diff(gmn[2*1+j],phi) -sympy.diff(gmn[2*1+1],phi))

print sum

sum = 0
for o in [r, phi]:
        if o == r:
                j = 0
                print (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],r))
		sum += (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],r))
        if o == phi:
                j = 1
		sum += (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],phi)) 
                print (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],phi))
print sum


