#include <iostream>
#include "Graph.h"

using std::cin;
using std::cout;
using std::endl;

int main()
{
        int n = 4;
        Graph g(4, 0);
        g.addEdge(0, 1, 2);
        g.addEdge(0, 2, 5);
        g.addEdge(2, 1, 5);
        g.addEdge(3, 0, 7);
        g.addEdge(1, 3, 7);
        g.addEdge(2, 3, 3);
        g.addEdge(3, 2, 3);

        g.make_matrix();
        g.min_distance_using_floyd_warshall_algo();
        g.print_matrix();
        auto min_cost = g.TSP();
        cout << "MINIMUM COST: " << min_cost.first << endl;
        cout << "PATH: ";
        for (int i = n - 1; i >= 0; i--)
        {
                cout << min_cost.second.at(i) << " ---> ";
        }
        cout << 0 << endl;
        vector<int> distanceFromZero = g.min_distance_using_dijkstrasAlgo(0);
        for (int i = 0; i < 5; i++)
        {
                cout << "distance to " << i << " : " << distanceFromZero[i] << endl;
        }

}
