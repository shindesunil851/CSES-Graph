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
random.seed(0)
def dfs(x,y,vis,mv,dr):
        vis[x][y]=mv+1
        if mv==63:
            for i in range(8):
                for j in range(8):
                    print(vis[i][j],end=" ")
                print("")
            exit(0)
        dr=random.sample(dr,len(dr))
        next=[]
        for dx,dy in dr:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>7 or ny<0 or ny>7 or vis[nx][ny]!=0:
                continue
            next.append([nx,ny])
        random.shuffle(next)
        for a,b in next:
            dfs(a,b,vis,mv+1,dr)    
        
        vis[x][y]=0

def main():
    y,x=inps()
    y-=1
    x-=1
    vis=[[0]*8 for _ in range(8)]

    dr=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    

    dfs(x,y,vis,0,dr)








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