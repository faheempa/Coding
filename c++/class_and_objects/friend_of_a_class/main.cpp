#include<iostream>

using std::cin;
using std::cout;
using std::endl;

class Player
{
        int hp;
        friend void display(Player obj); // granting friendship

public:

        Player(int hp = 100)
        : hp{hp} {}

        
};

// since this function is freind of player class, it can access all the attributes and function of the class(instance)
void display(Player obj)
{
        cout<<obj.hp<<endl;
}

int main()
{
        Player p;
        display(p);
        return 0;
}