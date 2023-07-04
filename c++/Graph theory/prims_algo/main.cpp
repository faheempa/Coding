#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Graph
{
        vector<pair<int, int>> *nbrs;
        int V;

public:
        Graph(int v)
        {
                this->V = v;
                nbrs = new vector<pair<int, int>>[V];
        }

        void addEdge(int i, int j, int w)
        {
                nbrs[i].push_back({j, w});
                nbrs[j].push_back({i, w});
        }

        int prims_algo()
        {
                // priority queue that provides smallest element (using min heap)
                priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q; // (weight, nbr_element)
                vector<bool> visited(this->V, false);
                q.push({0, 0});
                int weight, to, mst = 0;

                while (!q.empty())
                {
                        auto best = q.top();
                        q.pop();

                        weight = best.first;
                        to = best.second;

                        if (visited[to])
                                continue;

                        mst += weight;

                        visited[to] = true;
                        for (auto e : nbrs[to])
                        {
                                if (!visited[e.first])
                                {
                                        q.push({e.second, e.first});
                                }
                        }
                }
                return mst;
        }
};

int main()
{
        Graph g(4);
        g.addEdge(0, 1, 1);
        g.addEdge(0, 3, 2);
        g.addEdge(0, 2, 2);
        g.addEdge(1, 2, 2);
        g.addEdge(1, 3, 3);
        g.addEdge(2, 3, 3);

        cout << g.prims_algo() << endl;

        return 0;
}

