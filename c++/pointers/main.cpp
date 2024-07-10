#include <iostream>
#include <iostream>

using namespace std;

void print(int (&a)[5][4])
{
    for (int j = 0; j < 4; j++)
    {
        for (int i = 0; i < 5; i++)
            cout << a[i][j] << " ";
        cout << endl;
    }
}

int main()
{
    int a[5][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    print(a);
    return 0;
}