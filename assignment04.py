# Assignment 04
# Question no 1 
#  (Calculate age)
def age(birth_year,current_year):
    age = current_year - birth_year
    print(age)
age(2004,2024)


# Question no 2
#  (Calculate Area of Rectangle)
def AreaofRectangle(length,width):
    AreaofRectangle = length * width 
    print(AreaofRectangle)
AreaofRectangle(30,10)

# Question no 3 
#  (Calculate Area of Circle)
def AreaofCircle(pie,radius):
    AreaofCircle = pie * radius**2
    print(AreaofCircle)
AreaofCircle(3.14,7)

# Question no 4
#  (Calculate Area of CUBE)
a = 9
def AreaofCube(a):
    AreaofCube = 9 * a**2
    print(AreaofCube)
AreaofCube(9)



# Question no 5 
#  (Convert Celsius into fahrenheit & vice versa) 
def C_to_F(Celsius , fahrenheit):
     C_to_F = (  Celsius * 9/5 ) + 32 
     print(C_to_F)
C_to_F(43,7)
def F_to_C(Celsius , fahrenheit):
     F_to_C = (fahrenheit - 32) * 5/9
     print(F_to_C)
C_to_F(43,7)


# Question no 6 
# (Convert minutes into seconds & seconds_to_minutes)
def  minutes_to_seconds(seconds , minutes):
     minutes_to_seconds = minutes * 60
     print(minutes_to_seconds)
minutes_to_seconds(300 , 20)
def seconds_to_minutes(seconds,minutes):
    seconds_to_minutes = seconds / 60
    print(seconds_to_minutes)
seconds_to_minutes(300 , 20)



# Question no 7 
# (Calculate Percentage)
def percentage(obtained , total):
    percentage = obtained / total * 100
    print(percentage)
percentage(700 , 1100)



# Question no 8
#  (Calculate BMI)
def BMI(weight , height):
     BMI = weight / (height * height) 
     print(BMI)
BMI(80 , 20)



# Question no 9
#  (Volume of cylinder)
def Volume_of_cylinder(pie , radius , height):
    Volume_of_cylinder = pie * radius**2 * height
    print(Volume_of_cylinder)
Volume_of_cylinder(3.14,6,10)


