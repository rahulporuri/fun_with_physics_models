import sympy

r, phi = sympy.symbols('r phi')

gmn= sympy.Matrix([[1,0],[0,r**2]])
gMN= gmn**(-1)
indices = {0:'r', 1:'phi'}

for i in [0,1]:
	for j in [0,1]:
		for k in [0,1]:
			sum = 0
			for o in [r, phi]:
				if o == r:
					l = 0
			#                print (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],r))
					sum += (1./2)*gMN[2*k+l]*(sympy.diff(gmn[2*j+l],indices[i]) +sympy.diff(gmn[2*i+l],indices[j]) -sympy.diff(gmn[2*i+j],indices[l]))
				if o == phi:
					l = 1
					sum += (1./2)*gMN[2*k+l]*(sympy.diff(gmn[2*j+l],indices[i]) +sympy.diff(gmn[2*i+l],indices[j]) -sympy.diff(gmn[2*i+j],indices[l]))
			#                print (1./2)*gMN[2*1+j]*(sympy.diff(gmn[2*0+j],phi) +sympy.diff(gmn[2*1+j],r) -sympy.diff(gmn[2*0+1],phi))
			print 'gamma',i,j,k,sum
