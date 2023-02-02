#include<iostream>
#include<list>

using namespace std;

class Graph
{
    int v;
    list<pair<int,int>>edge;

    public:
    Graph(int v)
    {
        this->v=v;
    }

    void addEdge(int i,int j)
    {
        edge.push_back(make_pair(i,j));
    }

    int find(int x, int parent[])
    {
        if(parent[x]==-1)
            return x;
        return find(parent[x], parent);
    }

    bool union_fun(int x, int y, int parent[])
    {
        int s1=find(x,parent);
        int s2=find(y,parent);

        if(s1!=s2)
            parent[s1]=s2;
        else 
            return true;
        return false;
    }

    bool is_cycle()
    {
        int parent[v];
        for(int i=0; i<v; i++)
            parent[i]=-1;
        for(auto edg : this->edge)
        {
            int a= edg.first;
            int b= edg.second;
            bool cyclic = union_fun(a,b, parent);
            if(cyclic)
                return true;
        }
        return false;
    }

};

int main()
{
    Graph g1(4);

    g1.addEdge(0,1);
    g1.addEdge(1,2);
    g1.addEdge(2,3);
    g1.addEdge(3,0);

    cout<<boolalpha<<g1.is_cycle()<<endl; // true

    Graph g2(4);
    g2.addEdge(0,1);
    g2.addEdge(1,2);
    g2.addEdge(2,3);

    cout<<boolalpha<<g2.is_cycle()<<endl; // false

}