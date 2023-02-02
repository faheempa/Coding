#include "Movie.h"

Movie::Movie(string name, float rating, int wcount)
    : name{name}, rating{rating}, wcount{wcount}
{
}

void Movie::set_rating(float rating)
{
    this->rating = rating;
}

float Movie::get_rating() const
{
    return this->rating;
}

void Movie::set_name(string name)
{
    this->name = name;
}

string Movie::get_name() const
{
    return this->name;
}

void Movie::set_wcount(int wcount)
{
    this->wcount = wcount;
}

int Movie::get_wcount() const
{
    return this->wcount;
}

Movie::~Movie()
{
}