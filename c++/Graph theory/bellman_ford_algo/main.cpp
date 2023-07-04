#include <iostream>
#include <vector>
#include <climits>

using std::cin;
using std::cout;
using std::vector;
using std::endl;

int vertices = 5;
vector<vector<int>> edges;
vector<int> distance(vertices, INT_MAX);

bool bellman_ford_algo(int src)
{
        distance.at(src) = 0;
        for (int i = 0; i < vertices; i++)
        {
                for (auto edge : edges)
                {
                        int u = edge.at(0);
                        int v = edge.at(1);
                        int wt = edge.at(2);

                        if (distance.at(u) != INT_MAX and distance.at(u) + wt < distance.at(v))
                               distance.at(v) = distance.at(u) + wt;
                }
        }
        for (int i = 0; i < vertices; i++)
        {
                for (auto edge : edges)
                {
                        int u = edge.at(0);
                        int v = edge.at(1);
                        int wt = edge.at(2);

                        if (distance.at(v) != INT_MAX and distance.at(u) + wt < distance.at(v))
                        {
                                cout<<"Negative cycle detected";
                                return false;
                        }
                        
                }
        }
        return true;
}

int main()
{
        edges.push_back({0, 3, 5});
        edges.push_back({2, 3, 3});
        edges.push_back({0, 4, 4});
        edges.push_back({2, 4, 2});
        edges.push_back({0, 1, 2});
        edges.push_back({0, 2, 1});

        if(bellman_ford_algo(0))
                for (int i = 0; i < vertices; i++)
                {
                        cout << "distance to " << i << " : " << distance.at(i) << endl;
                }

        return 0;
}

