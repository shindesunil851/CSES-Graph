#pragma warning disable warning-list
from heapq import heapify,heappop,heappush
from collections import defaultdict,Counter,deque
import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
from bisect import bisect_left,bisect_right
from math import inf
import random


ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
 
from fractions import Fraction as F
mch=[-1]*(10000000)


def dfs(u,vis,dc):
    vis[u]=1
    for v in dc[u]:
        if mch[v]<0 or vis[mch[v]]==0 and dfs(mch[v],vis,dc):
            mch[v]=u
            return 1
    return 0


def main():
    
    n,m,k=inps()

    dc=defaultdict(list)
    for i in range(k):
        a,b=inps()
        dc[a].append(b)
    
    f=0
    for i in range(1,n+1):
        vis=[0]*(n+1)
        f+=dfs(i,vis,dc)

    
    print(f)
    for i in range(1,m+1):
        if mch[i]!=-1:
            print(mch[i],i)













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