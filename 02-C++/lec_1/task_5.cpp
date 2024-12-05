#include <iostream>


int main(){
    for (int i = 1; i < 13; i++){
        for (int j = 1; j < 13; j++){
            std::cout << i << "*" << j << "=" << i * j << "  ";
        }
        std::cout << std::endl;
    }
        return 0;
}