#include <iostream>
#include <map>
#include <fstream>
#include <string>
using namespace std;

int main(){

    std::map<char, int> my_map = {
    { 'A X', '1' },
    { 'B Z', '2' },
    { 'C Z', '3' }
};


    fstream data;
    data.open("inputv2.txt",ios::in);

    return 0;
}