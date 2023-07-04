#include<iostream>
#include<list>
#include<vector>
#include<queue>
#include<stack>

using namespace std;

class Graph
{
    int v;
    list <int> *l;
    stack <int> S;
    public:

    Graph(int v)
    {
        this->v=v;
        l=new list<int>[v];
    }

    void addEdge(int i, int j)
    {
        this->l[i].push_back(j);
    }

   void bfs_tsort()
    {
       vector<int> indegree(v,0);
       vector<bool> visited(v,false);
       for(int i=0;i<v;i++)
       {
           for(auto nbr: l[i])
           {
               indegree[nbr]++;
           }
       }
        queue <int> Q;
        for(int i=0;i<v;i++)
        {
            if(indegree[i]==0)
                Q.push(i);   
        }
        while(!Q.empty())
        {
            int x=Q.front();
            Q.pop();
            visited[x]=true;
            cout<<x<<" ";

            for(auto nbr: l[x])
            {
                indegree[nbr]--;
                if(indegree[nbr]==0)
                {
                    Q.push(nbr);
                }
            }
        }

       
    }

    void dfs(int x, vector<bool> &visited)
    {
        if(visited[x]==false)
        {
            visited[x]=true;
            for(auto nbr: l[x])
            {
                if(!visited[nbr])
                {
                    dfs(nbr,visited);
                }
            }
            S.push(x);
        }
    }

    void dfs_tsort()
    {
        vector<bool> visited(v,false);
        for(int i=0; i<v; i++)
        {
            dfs(i,visited);
        }

        while(!S.empty())
        {
            int x=S.top();
            cout<<x<<" ";
            S.pop();
        }
    }


};

int main()
{
    Graph g(6);

    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,3);
    g.addEdge(3,5);
    g.addEdge(4,5);

    g.bfs_tsort();
    cout<<endl;
    g.dfs_tsort();
}