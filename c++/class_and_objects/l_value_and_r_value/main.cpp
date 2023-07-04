#include <iostream>

using std::cin;
using std::cout;
using std::endl;

void l_value_function(int &x)
{
        cout << "L value : " << x << endl;
}

void r_value_function(int &&x)
{
        cout << "R value :" << x << endl;
}

int main()
{
        int a=10;
        l_value_function(a);
        r_value_function(10);
        return 0;
}