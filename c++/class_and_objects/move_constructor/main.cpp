#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

class Move
{
        int *data;

public:
        Move(int data)
        {
                this->data = new int;
                *this->data = data;
                cout<< "Constructor for "<<data <<endl;
        }

        Move(const Move &source) // deep copy
            : Move(*source.data)
        {
                cout<< "Copy Constructor for "<<*this->data <<endl;
        }

        Move(Move &&source) noexcept // move constructor
            : data{source.data}
        {
                source.data=nullptr;
                cout<< "Move Constructor for " <<*this->data<<endl;
        }

        void set_data(int data);
        int get_data();

        ~Move()
        {
                cout<< "Destructor for "<<this->data <<endl<<endl;
                delete data;
        }
};

void Move::set_data(int data)
{
        *this->data = data;
}

int Move::get_data()
{
        return *this->data;
}

int main()
{
        vector<Move> vec;
        vec.push_back(Move{10});
        vec.push_back(Move{15});
        vec.push_back(Move{20});
        return 0;
}