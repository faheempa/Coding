#ifndef _PLAYER_H_
#define _PLAYER_H_

#include <string>
#include <iostream>
using std::string;

class Player
{
        string name;
        int health;

public:
        Player(string name = "player", int health = 100);
        Player(const Player &source);
        void set_name(string name);
        string get_name();
        void set_health(int health);
        int get_health();
};

#endif

