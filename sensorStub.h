#include <iostream>
#include <vector>
using namespace std;

class Sensor{
    vector<int> Temperature;
    vector<int> SOC;
public:
    Sensor(){
        Temperature = {3,-8,10,19,-19,-31,-38,-42,-23,-26};
        SOC = {45,31,14,38,6,42,22,19,27};
    }
    vector<int> getTemperature(){
        return this->Temperature;
    }
    vector<int> getSOC(){
        return this->SOC;
    }
    void setBatteryParameters(vector<int> Temperature, vector<int> SOC){
        this->Temperature = Temperature;
        this->SOC = SOC;
    }
    void printOnConsoleStub(std::ostream& output){
        output<<"Temperature :";
        for(unsigned int i=0; i < Temperature.size(); i++){
            output<<Temperature[i]<<",";
        }
        output<<"\nSOC :";
        for(unsigned int i=0; i < SOC.size(); i++){
            output<<SOC[i]<<",";
        }
        output<<"\n";
    }
};


