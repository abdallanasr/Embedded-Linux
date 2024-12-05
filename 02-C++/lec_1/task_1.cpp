#include <iostream>


int main(){
    std::cout << "| Char | ASCII |" << std::endl;
    for (int i = 0; i <= 255; i++)
    {
        std::cout << "| " << char(i) << " |" << "| " << int(i) << " |" << std::endl;
    }
        return 0;
}