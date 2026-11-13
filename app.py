import unittest

def add(a,b):
  return a+b

def aubtract(a,b):
  return a-b

def multilpy(a,b):
  return a*b

class TestCalculator(unittest.TestcCase):

  def test_add(self):
    self.assertEqual(add(20,20),40)

 def test_subtract(self):
    self.assertEqual(subtract(30,10),10)
   
 def test_multiply(self):
    self.assertEqual(multiply(30,10),10)

if__name__ == "__main__":

  print("Student Cl)
  print("Add : ",add(20,20))
  print("Subtarct : ",subtract(20,10))
  print("Multiply : ",multiply(5,4))     

print("\nExecuting Automated Tests>>>\n")
unittest.main(argv=['first-arg-is-ignored'],exit=False)        
