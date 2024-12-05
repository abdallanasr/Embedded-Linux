#include <iostream>

#define a 5
int global_var = 5;
int global_var_a = 0;

int main()
{
    //Range loop
    int arr[5] = {1, 2, 3, 4, 5};
    for(auto i : arr){
        std::cout << i << std::endl ;
    }
    /*
    int local_var;
    std::cout << local_var << std::endl;
    std::cout << global_var_a << std::endl;
    std::cout << std::hex
            << "showbase: " << std::showbase << a << '\n'
            << "noshowbase: " << std::noshowbase << a << '\n';
    */
    return 0;
}