import sys
input = sys.stdin.readline
 
n, q = map(int, input().split())
T = list(map(lambda s: int(s)-1, input().split()))
 
M = 0
while 1 << M <= n: M += 1
 
jump = [T]
for i in range(1, M+1):
	jump.append([jump[i-1][jump[i-1][j]] for j in range(n)])
 
comps = []
comp = [-1] * n
V = [0] * n
for s in range(n):
	if V[s]: continue
	V[s] = 1
	P = [s]
	while V[T[s]] == 0:
		s = T[s]
		P.append(s)
		V[s] = 1
 
	if V[T[s]] == 1:
		C = [P.pop()]
		while C[-1] != T[s]:
			C.append(P.pop())
 
		for i in C:
			comp[i] = len(comps)
			V[i] = 2
 
		comps.append({j: i for i, j in enumerate(reversed(C))})
 
	for i in reversed(P):
		comp[i] = len(comps)
		comps.append({i: 0})
		V[i] = 2
 
def up(x, k):
	i = 0
	while k:
		if k&1:
			x = jump[i][x]
 
		k >>= 1
		i += 1
	return x
 
def dist2comp(x, c):
	if comp[x] == c: return x, 0
 
	dist = 1
	for i in range(M, -1, -1):
		if comp[jump[i][x]] > c:
			x = jump[i][x]
			dist += 1 << i
	return T[x], dist
 
R = []
for _ in range(q):
	a, b = map(int, input().split())
	a -= 1; b -= 1
 
	ac, bc = comp[a], comp[b]
	if comp[jump[-1][a]] != comp[jump[-1][b]] or ac < bc:
		R.append('-1')
		continue
 
	e1, d1 = dist2comp(a, bc)
	if comp[e1] != bc:
		R.append('-1')
		continue
 
	C = comps[bc]
	p1, p2 = C[e1], C[b]
	r = d1 + (p2 - p1 if p1 <= p2 else len(C) - p1 + p2)
	R.append(str(r))
 
print('\n'.join(R))