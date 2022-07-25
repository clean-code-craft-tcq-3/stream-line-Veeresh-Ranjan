#include "sensorStub.h"

void testPrint(vector<int> SOC, vector<int> Temperature, std::ostream& output){
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
