#include <iostream>
#include "Movie.h"
#include "Movies.h"

using std::cin;
using std::cout;
using std::endl;

int main()
{
        Movies movie_list;
        movie_list.add_movie("m1", 4, 2);
        movie_list.add_movie("m2", 4.5, 5);
        movie_list.add_movie("m3", 3.7, 1);
        movie_list.change_rating("m1",5.0);
        movie_list.increment_wcount("m2");
        movie_list.increment_wcount("m3");
        movie_list.print_details_of_moives();
        movie_list.increment_wcount("m4");
        movie_list.add_movie("m3", 3, 34);

        return 0;
}