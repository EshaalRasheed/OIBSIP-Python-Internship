print("............This is a BMI Calculator..............")
try:
 wieght=float(input("Enter your  weight in kilograms : "))
 height=float(input("Enter your height in meters :"))
 BMI=wieght/(height**2)
 if(height<0):
  print("Height must be greator than zero")
 elif (BMI<18.5):
  print(f"BMI: {BMI:.2f}")
  print("BMI is below 18.5 and you are underwieght") 
 elif (BMI>=18.5 and BMI<=24.9):
  print(f"BMI: {BMI:.2f}")
  print("Congratulations you are a normal wieght person")
 elif (BMI>=25.0 and BMI<=29.9):
  print(f"BMI: {BMI:.2f}")
  print("You are an overwieght person according to your BMI")
 elif (BMI>=30.0):
  print(f"BMI: {BMI:.2f}")
  print("You are an obese person (obesity)")
 else:
  print("Error")
except ValueError:
 print("Invalid Input. Please enter numeric values for wieght and height")

           
