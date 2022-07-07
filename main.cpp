#include"sender.h"
#include<assert.h>

void callTest(){
    vector<int> SOC;
    vector<int> Temperature;
    stringstream stringStreamBuffer,DummyBuffer;
    Temperature = {45,36,32,11,29,34,18,28};
    SOC = {42,41,23,19,37,38,26,15};

    testPrint(SOC,Temperature,DummyBuffer);
    string expectedOutput = DummyBuffer.str();
    Sensor sensor1,sensor2;
    cout<<"Test 1"<<endl;
    sensor1.setBatteryParameters(Temperature,SOC);
    sensor1.printOnConsoleStub(stringStreamBuffer);
    cout<<stringStreamBuffer.str()<<endl;
    assert(stringStreamBuffer.str() == expectedOutput);
    cout<<"Test 1 pass"<<endl;

    cout<<"Test 2"<<endl;
    stringStreamBuffer.str("");
    DummyBuffer.str("");
    testPrint(sensor2.getSOC(),sensor2.getTemperature(),DummyBuffer);
    expectedOutput = DummyBuffer.str();
    sensor2.printOnConsoleStub(stringStreamBuffer);
    cout<<stringStreamBuffer.str()<<endl;
    assert(stringStreamBuffer.str() == expectedOutput);
    cout<<"Test 2 pass"<<endl;

}

int main(){
    void (*funcPtr)();
    funcPtr = &callTest;
    funcPtr();
    funcPtr = &callPrint;
    funcPtr();
}
