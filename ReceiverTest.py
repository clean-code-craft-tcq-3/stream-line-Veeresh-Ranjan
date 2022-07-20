import unittest
import Receiver

data='''{"Battery" 
  {"Temperature": [1,2,3,4,5,6,7,8,9,9]
  "SOC": [1,2,3,4,5,6,7,8,9,9]
  }
  }'''

class receiver_test(unittest.TestCase):
  def test_get_min_temperature(self):
    self.assertTrue(Receiver.get_min_temperature([23,34,56,67,54,32,21])==21)
    
  def test_get_max_temperature(self):
    self.assertTrue(Receiver.get_max_temperature([23,34,56,67,54,32,21])==67)
  
  def test_get_min_SOC(self):
    self.assertTrue(Receiver.get_min_SOC([40,20,30,42,23,35])==20)
    
  def test_get_max_SOC(self):
    self.assertTrue(Receiver.get_max_SOC([40,20,30,42,23,35])==42)
    
  def test_calculate_moving_avg(self):
    self.assertTrue(Receiver.calculate_moving_avg([40,23,56,54,65,55,52,50])==55.2)
  
  def test_calculate_statistics(self):
    self.assertTrue(Receiver.calculate_statistics([10,20,30,40,50,60,70],[15,20,25,30,35,40,45,50])==(10,70,15,50,50.0,40.0))
    
    
    
if __name__=='__main__':
  unittest.main()
