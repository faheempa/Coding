#include "Movies.h"

void Movies::add_movie(string name, float rating, int wcount)
{
        for (const Movie &movie : list)
        {
                if (movie.get_name() == name)
                {
                        cout << "Movie already exist in the list" << endl;
                        return;
                }
        }
        Movie obj{name, rating, wcount};
        list.push_back(obj);
}

void Movies::print_details_of_moives() const
{
        for (const Movie &movie : list)
        {
                cout << "Name : " << movie.get_name() << endl;
                cout << "Rating : " << movie.get_rating() << endl;
                cout << "Watch count : " << movie.get_wcount() << endl;
                cout << "-------------------------------------------" << endl;
        }
        return;
}

void Movies::increment_wcount(string name)
{
        for (Movie &movie : list)
        {
                if (movie.get_name() == name)
                {
                        movie.set_wcount(movie.get_wcount() + 1);
                        return;
                }
        }
        cout << "So such movie exist in the movie list" << endl;
        return;
}

void Movies::change_rating(string name, float rating)
{
        for (Movie &movie : list)
        {
                if (movie.get_name() == name)
                {
                        movie.set_rating(rating);
                        return;
                }
        }
        cout << "So such movie exist in the movie list" << endl;
        return;
}