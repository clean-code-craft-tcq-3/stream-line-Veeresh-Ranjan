#include <iostream>
#include <vector>
#include <typeinfo>
#include <cstdlib>
#include <string>
#include "include/json.hpp"
#include <fstream>
#include"senderStub.h"

using namespace std;

auto readFromFile(string path){
    ifstream jsonFilePtr(path);
    stringstream readBuffer;
    readBuffer << jsonFilePtr.rdbuf();
    auto bufferPtr = nlohmann::json::parse(readBuffer.str());
    return bufferPtr;
}

void printOnConsole(auto bufferPtr, std::ostream& output)
{
    auto bufferSOC = bufferPtr["Battery"]["SOC"];
    auto bufferTemperature = bufferPtr["Battery"]["SOC"];
    output << "\nBattery Monitoring Results: "<<endl;
    output<<"SOC :"<<bufferSOC<<endl;
    output<<"Temperature :"<<bufferTemperature<<endl;
}
