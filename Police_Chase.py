from heapq import *
from collections import *
import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
import random


ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
 
from fractions import Fraction as F
dc=defaultdict(list)
dc2=defaultdict(list)
e=[]

class edg:
    def __init__(self,u,v,c,r):
        self.u=u
        self.v=v
        self.c=c
        self.r=r

def dfs(nd,vis):
    vis[nd]=1
    for i in dc[nd]:
        if e[i].c and vis[e[i].v]==0:
            dfs( e[i].v,vis )





def main():
    
    n,m=inps()
   
    for  i in range(m):
        a,b=inps()
        c=1
        a-=1
        b-=1
        e.append(edg(a,b,c,2*i+1))
        e.append(edg(b,a,1,2*i))
        
        dc[a].append(2*i)
        dc[b].append(2*i+1)



    mxf=0
    md=pow(10,9)+7
    while True:
        
        f=inf
        par=[-1]*(n+1)
        q=deque([0])
        d=[inf]*(n+1)     
        d[0]=0
        
        while q:
            cn=q.popleft()
            for ed in dc[cn]:

                nbr=e[ed].v
                c=e[ed].c
                if d[nbr]>md and c>0:
                    #f=min(f,c)
                    par[nbr]=ed        
                    #vis[nbr]=1
                    d[nbr]=1+d[cn]
                    q.append(nbr)
            
        if d[n-1]>md:
            break    
        cn=n-1

        while cn:
            f=min(f,e[par[cn]].c)
            cn=e[par[cn]].u

        
        mxf+=f
            
        cn=n-1
        while cn:
            #f=min(f,e[par[cn]].c)
            
            e[par[cn]].c-=f
            e[e[par[cn]].r].c+=f
            cn=e[par[cn]].u

    
    print(mxf)

    vis=[0]*(n+1)

    dfs(0,vis)

    for i in range(2*m):
        if e[i].c==0 and vis[e[i].u] ^ vis[e[i].v]:
            print(e[i].u+1,e[i].v+1)
    print()












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