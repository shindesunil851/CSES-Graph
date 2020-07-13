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

int vin[2000000];
int vout[2000000];


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
        //adj[v2[i]].push_back(i);
        vin[v2[i]]+=1;
        vout[v1[i]]+=1;

    }
    
    
    int oc=0;
    for(int i=1;i<n+1;i++)
    {

        if(i==1 && vin[1]+1!=vout[1])
        {
            cout<<"IMPOSSIBLE";
            return 0;

        }
        else if(i==n && vout[n]+1!=vin[n])
        {
                cout<<"IMPOSSIBLE";
               return 0;
        }
        

        else if((i!=1 && i!=n) && vin[i]!=vout[i])
            {
              
               cout<<"IMPOSSIBLE";
               return 0;
            }
            
        
    }
    

   // res.push_back(1);
    
    dfs(1);
    
    if(res.size()^m)
            {
              
               cout<<"IMPOSSIBLE";
               return 0;
            }
    reverse(res.begin(),res.end());

    
    //cout<<"1 ";
    for(int nm : res)
    {
        cout<<nm<<" ";
    }

    cout<<n;
  //  cout<<endl;
    
    return 0;
}
