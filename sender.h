#include "sensor.h"

void callPrint(){
    string path = "readings.json";
    auto bufferPtr = readFromFile(path);
    printOnConsole(bufferPtr,cout);
}
 
