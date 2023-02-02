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

class Path {
public:
        Path() {}
        Path(int vertex, int weight) {
                this->path.push_back(vertex);
                this->weight=weight;
        }
        void addPath(int vertex, int weight) {
                this->path.push_back(vertex);
                this->weight+=weight;
        }
        int weight=0;
        std::vector<int> path;
};

bool operator>(const Path& p1, const Path& p2) {
        return p1.weight > p2.weight;
}

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
                                        matrix[i][j] = UINT16_MAX;
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

        Path TSP(int x)
        {
                bool arr[this->V];
                for (int i = 0; i < this->V; i++)
                {
                        if (i == x)
                                arr[i] = false;
                        else
                                arr[i] = true;
                }
                return TSP_helper(x, arr);
        }

        Path TSP_helper(int current_vertex, bool to_be_called[])
        {
                bool done = true;
                std::priority_queue<Path,std::vector<Path>,std::greater<Path>> r_values; // proirity queue
                for (int i = 0; i < this->V; i++)
                { 
                        bool temp[this->V];
                        if (to_be_called[i])
                        {
                                done = false;
                                for (int j = 0; j < this->V; j++)
                                {
                                        if(j==i)
                                        {
                                                temp[j]=false;
                                                continue;
                                        }
                                        temp[j] = to_be_called[j];
                                }
                                Path cost1 = TSP_helper(i, temp);
                                cout << cost1.weight << "\t";
                                //Path cost2 = this->matrix[current_vertex][i];
                                cost1.addPath(i,this->matrix[current_vertex][i]);
                                cout << cost1.weight << endl;
                                r_values.push(cost1);
                        }
                }
                if (done)
                        return Path(0,matrix[current_vertex][0]);
                return r_values.top();
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
        g.addEdge(0, 1, 2);
        g.addEdge(0, 2, 5);
        g.addEdge(2, 1, 5);
        g.addEdge(3, 0, 7);
        g.addEdge(1, 3, 7);
        g.addEdge(2, 3, 3);
        g.addEdge(3, 2, 3);

        g.make_matrix();
        g.print_matrix();
        Path mp = g.TSP(0);
        cout << mp.weight << endl;
        for(auto i: mp.path) {
                cout << i << "\t";
        }
        // std::priority_queue<Path> p;
        // p.push(Path(0,10));
        // p.push(Path(1,12));
        // p.push(Path(2,6));
        // p.push(Path(3,7));
        // p.push(Path(4,1));
        // while(!p.empty()) {
        //         cout << p.top().weight << endl;
        //         p.pop();
        // }

        return 0;
}