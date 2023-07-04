#include <iostream>
#include <vector>
#include <climits>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::pair;
using std::vector;

class Graph
{
        vector<pair<int, int>> *nbrs;
        int V;
        int **matrix;

public:
        Graph(int v)
        {
                this->V = v;
                matrix = new int *[v];
                for (int i = 0; i < v; i++)
                {
                        matrix[i] = new int[v];
                }
                nbrs = new vector<pair<int, int>>[V];
        }

        void addEdge(int i, int j, int wt)
        {
                nbrs[i].push_back(pair(j, wt));
        }

        void make_matrix()
        {
                for (int i = 0; i < V; i++)
                {
                        for (int j = 0; j < V; j++)
                        {
                                if (i == j)
                                        matrix[i][j] = 0;
                                else
                                        matrix[i][j] = INT_MAX;
                        }
                }
                for (int i = 0; i < V; i++)
                {
                        for (auto nbr : nbrs[i])
                        {
                                matrix[i][nbr.first] = nbr.second;
                        }
                }
        }

        void floyd_warshall_algo()
        {
                for (int k = 0; k < this->V; k++)
                {
                        for (int i = 0; i < this->V; i++)
                        {
                                for (int j = 0; j < this->V; j++)
                                {
                                        if (this->matrix[i][j] > this->matrix[i][k] + this->matrix[k][j] and this->matrix[i][k] != INT_MAX and this->matrix[k][j] != INT_MAX)
                                        {
                                                this->matrix[i][j] = this->matrix[i][k] + this->matrix[k][j];
                                        }
                                }
                        }
                }
        }

        void print_matrix()
        {

                for (int i = 0; i < V; i++)
                {
                        for (int j = 0; j < V; j++)
                        {
                                cout << this->matrix[i][j] << "\t";
                        }
                        cout << endl;
                }
        }

        ~Graph()
        {
                delete[] nbrs;
                delete[] matrix;
        }
};

int main()
{
        Graph g(4);
        g.addEdge(0,1,2);
        g.addEdge(0,2,5);
        g.addEdge(2,1,5);
        g.addEdge(3,0,7);
        g.addEdge(1,3,7);
        g.addEdge(2,3,3);
        g.addEdge(3,2,3);

        g.make_matrix();
        g.floyd_warshall_algo();
        g.print_matrix();

        return 0;
}