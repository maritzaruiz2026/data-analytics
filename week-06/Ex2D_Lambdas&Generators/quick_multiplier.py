#doubler = lambda n: n * 2

#print(doubler(8))
#print(doubler(-4))
#print(doubler('banana'))

#tripler = lambda t: t * 3
#print(tripler(8))
#print(tripler(-4))
#print(tripler('banana'))

def times(n):
    return lambda x : x * n

quadrupler = times(4) 
quintupler = times(5) 
sextupler = times(6) 
septupler = times(7)
octupler = times(8)
nonupler = times(9)
decupler = times(10)

print(quadrupler(1))
print(quintupler(1))
print(sextupler(1))
print(octupler(1))
print(nonupler(1))
print(decupler(1))

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))