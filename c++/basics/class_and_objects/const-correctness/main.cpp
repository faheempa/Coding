#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class Player
{
    int hp;

public:
    Player(int hp = 100)
        : hp{hp} {}
    void set_hp(int hp);
    int get_hp() const;
};

void Player::set_hp(int hp)
{
    this->hp = hp;
}

//  compiler assumes that get_hp function will modufies the attributes (which is const), hence we need tell the compiler that this function will not modify the its attritubes
// hence we use 'const' with function protopyte.
int Player::get_hp() const
{
    return this->hp;
}

int main()
{
    const Player p;
    cout << p.get_hp() << endl;
    Player h;
    h.set_hp(50);
    cout << h.get_hp() << endl;
    return 0;
}
