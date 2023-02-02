#include <iostream>
#include <vector>
#include <set>
#include <climits>

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
                nbrs[i].push_back(pair(j, w));
                nbrs[j].push_back(pair(i, w));
        }

        vector<int> dijkstrasAlgo(int x)
        {
                vector<int> distance(V, INT_MAX);
                set<pair<int, int>> s; // wieght , nbr

                s.insert(pair(0, x));
                distance[x] = 0;

                while (!s.empty())
                {
                        auto edge = s.begin();
                        s.erase(edge);
                        int distanceUntilNow = edge->first;
                        int currentNode = edge->second;

                        for (auto nbr : nbrs[currentNode])
                        {
                                int toNode = nbr.first;
                                int weight = nbr.second;

                                if (distance[toNode] > weight + distanceUntilNow)
                                {
                                        auto present = s.find(pair(weight, toNode));
                                        if (present != s.end()) 
                                        // checking whether {wieght,toEdge} is present in set or not
                                                s.erase(pair(weight, toNode));
                                        distance[toNode] = weight + distanceUntilNow;
                                        s.insert(pair(distance[toNode], toNode));
                                }
                        }
                }
                return distance;
        }
};

int main()
{
        Graph g(5);

        g.addEdge(0, 1, 2);
        g.addEdge(0, 4, 4);
        g.addEdge(0, 2, 1);
        g.addEdge(2, 4, 2);
        g.addEdge(2, 3, 1);

        vector<int> distanceFromZero = g.dijkstrasAlgo(0);
        for (int i = 0; i < 5; i++)
        {
                cout << "distance to " << i << " : " << distanceFromZero[i] << endl;
        }
        return 0;
}