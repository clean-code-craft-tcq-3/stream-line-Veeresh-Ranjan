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
  return 

def get_min_temperature(Temperature_readings):
  return min(Temperature_readings)

def get_max_temperature(Temperature_readings):
  return max(Temperature_readings)

def get_min_SOC(SOC_readings):
  return min (SOC_readings)

def get_max_SOC(SOC_readings):
  return max(SOC_readings)

def calculate_moving_avg(parameter_reading):
  moving_vag=[]
  index=0;
  

