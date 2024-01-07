    # TODO: Convert between C, F and K
    # ! Use functions

def fromCelcius():
    c = float(input("Enter temperature in Celcius: "))
    
    # * c/5 = (f - 32)/9
    # * 9*c/5 = f - 32
    # * f = (9*c/5) + 32
    
    # * k = c + 273
    
    f = float((9*c/5) + 32)
    k = float(c + 273)
    print("Temperature in Fahrenheit: ", f)
    print("Temperature in Kelvin: ", k)

def fromFahenheit():
    f = float(input("Enter temperature in Fahrenheit: "))
    
    # * c/5 = (f - 32)/9
    # * c = ((f - 32) * 5)/9

    # * k = c + 273
    
    c = float(((f - 32) * 5)/9)
    k = float(c + 273)
    print("Temperature in Celcius: ", c)
    print("Temperature in Kelvin: ", k)

def fromKelvin():
    k = float(input("Enter temperature in Kelvin: "))
    
    # * c = k - 273

    # * f = (9*c/5) + 32
    
    c = float(k - 273)
    f = float((9*c/5) + 32)
    print("Temperature in Celcius: ", c)
    print("Temperature in Fahrenheit: ", f)

            # ! Main Controller ! #

print("1. To convert from Celcius")
print("2. To convert from Fahrenheit")
print("2. To convert from Kelvin")

c = int(input("> "))
if(c == 1):
    fromCelcius()
elif(c == 2):
    fromFahenheit()
elif(c == 3):
    fromKelvin()