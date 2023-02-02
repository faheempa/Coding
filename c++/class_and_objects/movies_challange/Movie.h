#ifndef _MOVIE_H_
#define _MOVIE_H_
#include "Movies.h"
#include <string>

using std::string;

class Movie
{
        string name;
        float rating;
        int wcount;
        friend class Movies;

public:
        Movie(string name = "none", float rating = 0, int wcount = 0);
        void set_rating(float rating);
        float get_rating() const;
        void set_name(string name);
        string get_name() const;
        void set_wcount(int wcount);
        int get_wcount() const;
        ~Movie();
};

#endif

// create Movie.pp and cut paste the below
