#include <iostream>
#include <vector>
#include <climits>
#include <list>
#include <queue>

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
        int starting_vertex;

public:
        Graph(int v, int x = 0)
        {
                this->V = v;
                nbrs = new vector<pair<int, int>>[V];
                starting_vertex = x;
        }
        void addEdge(int i, int j, int wt, bool undir = false)
        {
                nbrs[i].push_back(pair(j, wt));
                if (undir)
                        nbrs[j].push_back(pair(i, wt));
        }
        void make_matrix()
        {
                this->matrix = new int *[this->V];
                for (int i = 0; i < this->V; i++)
                {
                        matrix[i] = new int[this->V];
                }
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

        pair<int, vector<int>> TSP()
        {
                bool arr[this->V];
                for (int i = 0; i < this->V; i++)
                {
                        if (i == this->starting_vertex)
                                arr[i] = false;
                        else
                                arr[i] = true;
                }
                return TSP_helper(this->starting_vertex, arr);
        }

        pair<int, vector<int>> TSP_helper(int current_vertex, bool to_be_called[])
        {
                bool done = true;
                std::priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, std::greater<pair<int, vector<int>>>> r_values; // proirity queue
                for (int i = 0; i < this->V; i++)
                {
                        bool temp[this->V];
                        if (to_be_called[i])
                        {
                                done = false;
                                for (int j = 0; j < this->V; j++)
                                {
                                        if (j == i)
                                        {
                                                temp[j] = false;
                                                continue;
                                        }
                                        temp[j] = to_be_called[j];
                                }
                                auto cost1 = TSP_helper(i, temp);
                                int cost2 = this->matrix[current_vertex][i];
                                int total_cost = cost1.first + cost2;
                                cost1.second.push_back(current_vertex);
                                r_values.push({total_cost, cost1.second});
                        }
                }
                if (done)
                {
                        vector<int> path;
                        path.push_back(current_vertex);
                        return {matrix[current_vertex][0], path};
                }
                return r_values.top();
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
        int n = 4;
        Graph g(n);
        g.addEdge(0, 1, 2);
        g.addEdge(0, 2, 5);
        g.addEdge(2, 1, 5);
        g.addEdge(3, 0, 7);
        g.addEdge(1, 3, 7);
        g.addEdge(2, 3, 3);
        g.addEdge(3, 2, 3);

        g.make_matrix();
        g.floyd_warshall_algo();
        auto min_cost = g.TSP();
        cout << "MINIMUM COST: " << min_cost.first << endl;
        cout << "PATH: ";
        for (int i = n - 1; i >= 0; i--)
        {
                cout << min_cost.second.at(i) << " ---> ";
        }
        cout << 0 << endl;
        return 0;
}