
#include "Player.h"

Player::Player(string name, int health)
    : name{name}, health{health}
{
}

Player::Player(const Player &source)
    : name{source.name}, health{source.health} {}

void Player::set_name(string name)
{
        this->name = name;
}

string Player::get_name()
{
        return this->name;
}

void Player::set_health(int health)
{
        this->health = health;
}

int Player::get_health()
{
        return this->health;
}
