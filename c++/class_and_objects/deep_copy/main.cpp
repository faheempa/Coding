#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class Deep
{
        int *data;

public:
        Deep(int data)
        {
                this->data = new int;
                *this->data = data;
        }

        Deep(const Deep &source) // deep copy
                :Deep(*source.data) {}
                
        void set_data(int data);
        int get_data();

        ~Deep()
        {
                delete data;
        }
};

void Deep::set_data(int data)
{
        *this->data = data;
}

int Deep::get_data()
{
        return *this->data;
}

void display(Deep obj)
{
        cout<<"data: "<<obj.get_data() <<endl;
}

int main()
{
        Deep d(10);
        cout<<"data : "<<d.get_data()<<endl;

        display(d);
        return 0;
}