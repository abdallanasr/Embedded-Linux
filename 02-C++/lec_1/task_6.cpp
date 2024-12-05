#include <iostream>
#include <string>


int main(){
    int num = 0, sum = 0;
    std::cout << "Enter an intger \n";
    std::cin >> num;

    std::string numStr = std::to_string(num);
    for(auto digitChar : numStr){
        int digit = digitChar - '0';
        std::cout << digit<< std::endl;
        sum += digit;
    }

    std::cout << "Sum of digits = " << sum << std::endl;
    return 0;
}