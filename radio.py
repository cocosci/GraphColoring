from sys import argv
import copy
script,	constraint = argv
freqs = ['A', 'B', 'C', 'D']
states=[]
neighbors={}
domain={}
A={}
numberofbacktracking=0

# Initialize states, neighbors, and domain.
txt1 = open("/Users/Kai/Documents/CS_PhD/551/zhenk-a4/adjacent-states")
for lines in txt1.readlines():
	splitline = lines.split( )
	states.append(splitline[0])
	domain[splitline[0]]= freqs
	neighbors[splitline[0]] = [] if len(splitline) == 1 else list(splitline[1:len(splitline)])
txt1.close()

# Update the domain
txt2 = open(constraint)
for lines in txt2.readlines():
	splitline = lines.split( )
	if len(splitline) is not 0:
		domain[splitline[0]]=list(splitline[1:len(splitline)])
txt2.close()

# two heuristic ideas are used here.
def pickWisely(reststates,neighbors,domain):
	# find those with fewest domain.
	freqCandidate = list(len(domain[i]) for i in reststates)
	candidate1 = list(i for i in reststates if len(domain[i]) == min(freqCandidate))
	# among candidate1, find those with the most number of neighbors.
	neighborsCandidate = list(len(neighbors[i]) for i in candidate1)
	candidate2 = list(i for i in candidate1 if len(neighbors[i]) == max(neighborsCandidate))
	return candidate2[0]
# rank the element in the domain[nextState]
def nextstateDomainRank(nextState,reststates,neighbors,domain):
	nextstateEffectiveNeighbor = list(i for i in neighbors[nextState] if i in reststates)
	howmanyEleKilled = {}
	for i in domain[nextState]:
		count = 0
		for j in nextstateEffectiveNeighbor:
			if i in domain[j]:
				count = count + 1
		howmanyEleKilled[i] = count
	return sorted(howmanyEleKilled,key = howmanyEleKilled.get)
# if there is collision between nextState and its neighbors in A.
def consistent(nextState,v,A,neighors):
	consistChecklist = list(i for i in neighors[nextState] if i in A)
	for i in consistChecklist:
		if v in A[i]:
			return False
	return True
# for all the neighors of nextState, we ignore those in A, and update the domain of the rest neibhnors.
def forwardchecking(A,nextState,v,neighbors,domain):
	theNeighbors = neighbors[nextState]
	theRestNeighbors = list(i for i in theNeighbors if i not in A)
	for i in theRestNeighbors:
		if v in domain[i]:
			domain[i]=list(set(domain[i])-set(v))
	return domain
# if domain of any reststate is zero, then return false;
def nozero(reststates,domain):
	keys = list(domain[i] for i in reststates)
	#print keys
	for i in range (len(keys)):
		if len(keys[i])==0:
			return False 
	return True
# the same algorithm covered in the lecture.	
def CSP_BACKTRACKING(A,domain):
	global numberofbacktracking
	if len(A)==50:
		return True
	# We choose the right states to proceed.
	nextState = pickWisely(list(set(states) - set(A.keys())),neighbors,domain)
	# We rank the order of color in each entry of the domain.
	freqsord = nextstateDomainRank(nextState,list(set(states) - set(A.keys())),neighbors,domain)
	for v in freqsord:
		# Choose one from head to the tail.
		if consistent(nextState,v,A,neighbors):
			A[nextState]=v
			domainbak = copy.deepcopy(domain)
			domain = forwardchecking(A,nextState,v,neighbors,domain)
			if nozero(list(set(states) - set(A.keys())),domain):
				result = CSP_BACKTRACKING(A,domain)
				if result is True:
					return True
				del A[nextState]
			else:
				domain = copy.deepcopy(domainbak)
	# If I ran out of choice, then backtraching will occur.
	numberofbacktracking = numberofbacktracking +1
	return False



def writeres(A):
	f = open('results.txt', 'w')
	for i in A:
		f.write(i + " " + A[i]+'\n')
	#f.write("Number of backtracks:"+str(numberofbacktracking))
	f.close()

#print A
CSP_BACKTRACKING(A,domain)
writeres(A)
print ("Number of backtracks:"+str(numberofbacktracking))
#print A
#print numberofbacktracking
