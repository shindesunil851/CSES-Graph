INT_MAX =float('infinity')
n,m = list(map(int,input().split()))
graph = [[]for i in range(n+1)]
# for i in range(m):
#     a,b,w = list(map(int,input().split()))
#     graph[a].append((b,w))
 
 
# since bellman ford is required we require all the edges for the loop 
# therefore it is convinient to store all the edges in other format
 
# alo note that one of the test case has n = 2500 but they dont have many edges connected to them
# THis would cause the function to run many times therefore we assign INT_MAX to those nodes only which have edges 
 
edges = []
distance = [False for i in range(n+1)]
for i in range(m):
    a,b,w = list(map(int,input().split()))
    edges.append((a,b,w))
    distance[a] = INT_MAX
    distance[b]  = INT_MAX
 
 
 
 
visited = [False for i in range(n+1)]
parent = [-1 for i in range(n+1)]
 
def bellman_ford(source):
    # print(source,"--")
    for i in range(1,n):
        distance[source] = 0
        for a,b,w in edges:
            if distance[a]!=INT_MAX and distance[b]>distance[a]+w:
                distance[b] = distance[a]+w
                parent[b] = a
    
    for a,b,w in edges:
        if distance[a]!=INT_MAX and distance[b]>distance[a]+w:
            print("YES")
            # print(a,b)
            ans = [str(a)]
            temp = a
            a = parent[a]
            while a!=temp and str(a) not in ans:
                ans.append(str(a))
                a= parent[a]
            # print(ans,a)
            ans.append(str(a))
            # print(" ".join(ans[::-1]))
            print(" ".join(ans[ans.index(str(a)):][::-1]))
            return True
    return False
 
flag = True
for i in range(1,n+1):
    if distance[i]==INT_MAX:
        a = bellman_ford(i)
        if a:
            flag = False
            break
# print(parent)
if  flag:
    print("NO")
 
 