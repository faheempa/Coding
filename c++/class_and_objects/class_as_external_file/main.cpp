#include <iostream>
#include <string>
#include "Player.h"

using std::cin;
using std::cout;
using std::endl;

void print_details(Player obj)
{
        cout<<"name : "<<obj.get_name()<<endl;
        cout<<"health : "<<obj.get_health()<<endl;
}

int main()
{
        Player p1;
        Player p2(p1);
        print_details(p1);
        return 0;
}
