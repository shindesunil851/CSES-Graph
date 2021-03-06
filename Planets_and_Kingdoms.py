from heapq import *
from collections import *
import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
 



 
ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
 
from fractions import Fraction as F
def main():
    
    n,m=inps()
    dc=defaultdict(list)
    dc2=defaultdict(list)
    

    for i in range(m):
        a,b=inps()
        dc[a].append(b)
        dc2[b].append(a)

    vis=[0]*(n+1)
    ds=[]

    for i in range(1,n+1):
        if vis[i]==0:
            st=[[i,"en"]]

            while st:
                nd,fl=st.pop()
                #
                #print(nd,fl)
                if vis[nd]==2:
                    continue
                if fl=="ex":
                    ds.append(nd)
                 #   print("g")
                    vis[nd]=2
                    continue

                vis[nd]=1
                st.append([nd,"ex"])
                
                for nbr in dc[nd]:
                    if vis[nbr]==0:
                        st.append([nbr,"en"])

   # print("here",ds)          
    vis2=[0]*(n+1)
    ans=[]
    res=0

    pp=[-1 for i in range(n+1)]

    k=1
    while ds:
        ll=ds.pop()
        if not vis2[ll]:
            ans.append(ll)
            res+=1
            
            st=[(ll,ll)]
            k+=1
            #print("st",ll)
            while st:
                nd,prn=st.pop()
                vis2[nd]=1
                pp[nd]=prn
                for nbr in dc2[nd]:
                    if not vis2[nbr]:
                        pp[nbr]=prn
                       # print("g",nbr,nd)
                        #print(nbr,pp[nbr])
                        st.append((nbr,prn))
        
    #print(ds)
    # def find(u):
    #     while u!=pp[u]:
    #         pp[u]=pp[pp[u]]
    #         u=pp[u]
    #     return u
    print(len(ans))
    #print(ans)
    mp={}
    k1=1
    for nm in ans:
        mp[nm]=k1
        k1+=1

    for i in range(1,n+1):
        print(mp[pp[i]],end=" ")

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