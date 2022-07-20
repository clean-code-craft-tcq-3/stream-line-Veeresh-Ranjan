import json
import sys


#Read the sender data

def get_reading_from_sender():
  readings= sys.stdin.read()
  return readings

#process the sender data to compute the statistics

def process_sender_data(readings):
  reading_list= readings.split("\n")
  SOC_readings= []
  Temperature_readings=[]
  readiings_list= [reading for reading reading_list]
  print readiings_list
  for value in readiings_list:
    json_data= json.loads(value)
    SOC_readings.append(json_data["Battery"]["SOC"])
    Temperature_readings.append(json_data["Battery"]["Temperature"])
  return calculate_statistics(SOC_readings,Temperature_readings)
  
def get_min_temperature(Temperature_readings):
  return min(Temperature_readings)

def get_max_temperature(Temperature_readings):
  return max(Temperature_readings)

def get_min_SOC(SOC_readings):
  return min (SOC_readings)

def get_max_SOC(SOC_readings):
  return max(SOC_readings)

def calculate_moving_avg(parameter_reading):
  sum= (parameter_reading[-1]+parameter_reading[-2]+parameter_reading[-3]+parameter_reading[-4]+parameter_reading[-5])
  return round((sum/5), 2)

def calculate_statistics(SOC_readings, Temperature_readings):
  min_soc= get_min_SOC(SOC_readings)
  max_soc= get_max_SOC(SOC_readings)
  min_temp= get_min_temperature(Temperature_readings)
  max_temp= get_max_temperature(Temperature_readings)
  moving_avg_soc= calculate_moving_avg(SOC_readings)
  moving_avg_temp= calculate_moving_avg(Temperature_readings)
  
  return min_soc, max_soc, min_temp, max_temp, moving_avg_soc, moving_avg_temp
  

if __name__=="__main__":
  data= get_reading_from_sender()
  process_sender_data(data)
  
