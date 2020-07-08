from heapq import *
from collections import *
import os
import sys
sys.setrecursionlimit(1<<31-1)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
 
dp=[0]*1000000

mod=pow(10,9)+7
def dfs(act,cur,dc,res,p):
    if cur==len(act)-1:
        dp[cur]=1
    else:
        dp[cur]=0
    act[cur]=1
    for nbr in dc[cur]:
        if act[nbr]==1:

            print("IMPOSSIBLE")
            exit(0)
        if act[nbr]==0:
            
            dfs(act,nbr,dc,res,p)
        
        dp[cur]+=dp[nbr]
        dp[cur]=dp[cur]%mod
    act[cur]=2
    #res.append(cur)
 

dp2=[0]*1000000

mod=pow(10,9)+7
def dfs2(act,cur,dc,res,p):
    if cur==len(act)-1:
        dp2[cur]=1
    else:
        dp2[cur]=inf
    act[cur]=1
    for nbr in dc[cur]:
        if act[nbr]==1:

            print("IMPOSSIBLE")
            exit(0)
        if act[nbr]==0:
            
            dfs2(act,nbr,dc,res,p)
        
        if dp2[cur]>dp2[nbr]+1:
            dp2[cur]=dp2[nbr]+1
        #dp[cur]+=dp[nbr]
        #dp[cur]=dp[cur]%mod
    act[cur]=2
    #res.append(cur)




dp3=[0]*1000000

mod=pow(10,9)+7
def dfs3(act,cur,dc,res,p):
    if cur==len(act)-1:
        dp3[cur]=1
    else:
        dp3[cur]=-inf
    act[cur]=1
    for nbr in dc[cur]:
        if act[nbr]==1:

            print("IMPOSSIBLE")
            exit(0)
        if act[nbr]==0:
            
            dfs3(act,nbr,dc,res,p)
        
        if dp3[cur]<dp3[nbr]+1:
            dp3[cur]=dp3[nbr]+1
        #dp[cur]+=dp[nbr]
        #dp[cur]=dp[cur]%mod
    act[cur]=2
    #res.append(cur)






ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
 
from fractions import Fraction as F
def main():
    
    n,m=inps()
    dc2=defaultdict(list)
    dc=defaultdict(list)

    for i in range(m):
        a,b,c=inps()
        dc2[a].append((b,c))
    

    


    d=[inf]*(n+1)
    d[1]=0
    mh=[(0,1)]
    
    while mh:
        dist,nd=heappop(mh)
        if d[nd]<dist:
            continue
        for nbr,cost in dc2[nd]:
            if d[nbr]>cost+d[nd]:
                d[nbr]=cost+d[nd]
                heappush(mh,(d[nbr],nbr))
    


    print(d[n],end=" ")
    

    for i in range(1,n+1):
        for b,c in dc2[i]:
            if d[i]+c==d[b]:
                dc[i].append(b)

    #vis=[0]*(n+1)
    res=[]
    p=[-1]*(n+1)
    active=[0]*(n+1)
    #vis=[0]*(n+1)

    dfs(active,1,dc,res,p)
    print(dp[1],end=" ")

    res=[]
    p=[-1]*(n+1)
    active=[0]*(n+1)
    
    dfs2(active,1,dc,res,p)
    print(dp2[1]-1,end=" ")
    
    res=[]
    p=[-1]*(n+1)
    active=[0]*(n+1)
    

    dfs3(active,1,dc,res,p)
    print(dp3[1]-1)
    








BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()
# import threading,sys
# sys.setrecursionlimit(1000000)
# threading.stack_size(1024000)
# thread=threading.Thread(target=main)
# thread.start()
