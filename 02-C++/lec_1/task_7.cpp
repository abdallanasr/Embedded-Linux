#include <iostream>
#include <bitset>


int main(){
    
    int num = 0;
    std::cout << "Enter a Number \n";
    std::cin >> num;
    std::bitset<8> binary(num);
    std::string Strbinary = binary.to_string();
    std::cout<< Strbinary << std::endl;

    return 0;
}