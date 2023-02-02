#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class Player
{
        int hp;
        static int no_of_players;

public:
        Player(int hp = 100)
            : hp{hp}
        {
                no_of_players++;
        }

        ~Player()
        {
                no_of_players--;
        }

        // static function can only access static attributes
        static int get_no_of_players()
        {
                return no_of_players;
        }
};

int Player::no_of_players{0};

int main()
{
        Player p1;
        Player p2;
        Player p3;
        cout << Player::get_no_of_players() << endl;
        Player p4;
        cout << Player::get_no_of_players() << endl;
        p1.~Player();
        cout << Player::get_no_of_players() << endl;
        p2.~Player();
        p3.~Player();
        p4.~Player();
        cout << Player::get_no_of_players() << endl;

        Player *p5 = new Player(200);
        cout << Player::get_no_of_players() << endl;
        delete p5;
        cout << Player::get_no_of_players() << endl;
        

        return 0;
}