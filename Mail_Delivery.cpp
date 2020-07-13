/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include<bits/stdc++.h>
#include <iostream>
#include<vector>
using namespace std;


int v1[2000000];
int v2[2000000];
vector<int>res;

vector<int>adj[2000000];
int vis[2000000];

void dfs(int u)
{
    while(adj[u].size())
    {
        int e=adj[u].back();
        
        adj[u].pop_back();
        if(vis[e])
            continue;
        
        vis[e]=1;

        dfs(v1[e]^v2[e]^u);
        res.push_back(u);
        
    }
}

int main()
{
    int m,n;
    cin>>n>>m;
    
    for(int i=0;i<m;i++)
    {
        cin>>v1[i]>>v2[i];
        
        adj[v1[i]].push_back(i);
        adj[v2[i]].push_back(i);
        
    }
    
    
    for(int i=1;i<n+1;i++)
    {
        if(adj[i].size()&1)
            {
                cout<<"IMPOSSIBLE";
                return 0;
            }
            
        
    }
    
    res.push_back(1);
    dfs(1);
    if(res.size()^m+1)
        {
            cout<<"IMPOSSIBLE";
            return 0;
        }
    for(auto nm : res)
    {
        cout<<nm<<" ";
    }
    
  //  cout<<endl;
    
    return 0;
}
