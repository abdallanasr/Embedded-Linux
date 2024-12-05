#include <iostream>


int main(){
    int x = 10, y = 20, z = 14;
    std::cout << "Enter X, Y and Z" << std::endl;
    std::cin >> x >> y >> z;
    if (x > y)
    {
        if(x > z){
            std::cout << "X Is Maximum Number, X = " << x << std::endl;
        }
        else if(x < z){
            std::cout << "Z Is Maximum Number, Z = " << z << std::endl;
        }
    }
    else if(x < y){
        if(y > z){
            std::cout << "Y Is Maximum Number, Y = " << y << std::endl;
        }
        else if(y < z){
            std::cout << "Z Is Maximum Number, Z = " << z << std::endl;
        }
    }
    return 0;
}