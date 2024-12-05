#include <iostream>


int main(){
    bool isVowel = false;
    char c = 0;
    const char vowel[10] = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'};
    std::cout << "Enter a character" << std::endl;
    std::cin >> c;
    for(auto i : vowel){
        if(c == i){
            isVowel = true;
            break;
        }
    }
    if(true == isVowel){
        std::cout << c  << " is vowel \n";
    }
    else{
        std::cout << c << " isn't vowel \n";
    }
    return 0;
}