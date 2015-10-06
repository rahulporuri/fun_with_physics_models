'''
for i in range(0,4):
	for j in range(0,4):
		for k in range(0,4):
			for l in range(0,4):
				if i!=j :
					if k!=l :
						print i,j,k,l
'''
counter = 0
for i in range(0,2):
	for j in range(0,2):
		for k in range(0,2):
			for l in range(0,2):
				if i == k:
					if counter == 0:
						print 'checked'
						if i!=j:
							if k!=l :
								print i,j,k,l
								print counter
								counter += 1
				if i == l:
					if counter == 0:        
						print 'checked'
						if i!=j:
							if k!=l :
								print i,j,k,l
								print counter
								counter += 1
				if j == k:
					if counter == 0:
						print 'checked'
						if i!=j:
							if k!=l :
								print i,j,k,l
								print counter
								counter += 1
				if j == l:
					if counter == 0:        
						print 'checked'
						if i!=j:
							if k!=l :
								print i,j,k,l
								print counter
								counter += 1
				else :
					if i!=j:
						if k!=l :
							print i,j,k,l
							print counter
