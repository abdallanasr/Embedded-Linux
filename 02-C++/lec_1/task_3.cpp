#include <cmath>
#include <iostream>


int main(){
    int a, b, c;
    std::cout << "Enter a, b and c of Triangle" << std::endl;
    std::cout << "A = ";
    std::cin >> a;
    std::cout << "B = ";
    std::cin >> b;
    std::cout << "C = ";
    std::cin >> c;
    a = std::pow(a, 2);
    b = std::pow(b, 2);
    c = std::pow(c, 2);
    if(c == (a+b)){
        std::cout << "Triangle is Right Angle Triangle" << std::endl;
    }
    else{
        std::cout << "Isn't" << std::endl;
    }
    return 0;
}