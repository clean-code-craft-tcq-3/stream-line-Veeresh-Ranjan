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
  readiings_list= [reading for reading in reading_list if reading]
  print (readiings_list)
  return calculate_statistics(get_SOC_reading(readings_list),get_temperature_readings(reading_list))
  
def get_SOC_reading(readings_list):
  for value in readiings_list:
    json_data= json.loads(value)
    SOC_readings.append(json_data["Battery"]["SOC"])
  return SOC_readings

def get_temperature_readings(reading_list):
  for value in readiings_list:
    json_data= json.loads(value)
    Temperature_readings.append(json_data["Battery"]["Temperature"])
  return Temperature_readings
  
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
  print_statistics(min_soc, max_soc, min_temp, max_temp, moving_avg_soc, moving_avg_temp)
  return min_soc, max_soc, min_temp, max_temp, moving_avg_soc, moving_avg_temp

def print_statistics(min_soc, max_soc, min_temp, max_temp, moving_avg_soc, moving_avg_temp):
  print("Minimum SOC : ", min_soc)
  print("Maximum SOC : ", max_soc)
  print("Minimum Temperature : ", min_temp)
  print("Maximum Temperature : ", max_temp)
  print("Moving average SOC : ", moving_avg_soc)
  print("Moving average Temperature : ", moving_avg_temp)

if __name__=="__main__":
  data= get_reading_from_sender()
  process_sender_data(data)
  
