#ifndef _MOVIES_H_
#define _MOVIES_H_

#include "Movie.h"
#include <vector>
#include <iostream>
using std::cout;
using std::endl;
using std::vector;
using std::string;


class Movies
{
        vector<class Movie> list;

public:
        void add_movie(string name, float rating, int wcount);
        void print_details_of_moives() const;
        void increment_wcount(string name);
        void change_rating(string name, float rating);
};

#endif
