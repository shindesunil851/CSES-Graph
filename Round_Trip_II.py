from heapq import *
from collections import *
import os
import sys
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
    
    for i in range(m):
        a,b=inps()
        dc[a].append(b)
   
    
    #vis=[0]*(n+1)
    parent=[0]*(n+1)
    found=False
    active=[0]*(n+1)
    # for i in range(1,n+1):
    #     if vis[i]==0:
    #         dfs(vis,active,i,dc,parent)

    for i in range(1,n+1):
        if active[i]==0:
            #vis[i]=1
            st=[(i,"Enter")]
            
            while st:
                #print(st)
                
                curNode,status=st.pop()
                if status=="Exit":
                    active[curNode]=2
                    continue
                st.append((curNode,"Exit"))
                active[curNode]=1
                for nbr in dc[curNode]:
                    if active[nbr]==1:
                        #print("GOT")
                        parent[nbr]=curNode
                        node=nbr
                        found=True
                        break
                    #print(curNode,nbr)
                    if active[nbr]==0:
                        parent[nbr]=curNode
                     #   active[nbr]=1
                        st.append((nbr,"Enter"))

               


                if found==True:

                    ls=[node]
                    node1=node
                    while node1!=parent[node]:
                        ls.append(parent[node])
                        node=parent[node]
                    ls.append(node1)
                    
                    print(len(ls))
                    for nm in ls[::-1]:
                        print(nm,end=" ")
                    # fs=""
                    # fs=" ".join(map(str,ls[::-1]))
                    # print(fs)
                    print("")
                    return
        
    print("IMPOSSIBLE")


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