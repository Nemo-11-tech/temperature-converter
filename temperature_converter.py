temp_fahrenheit=float(input("enter temperature in fahrenheit:"))
def convert_to_celsius(temp_fahrenheit):
    temp_celcius=5/9*(temp_fahrenheit-32)
    return temp_celcius
def convert_to_kelvin(temp_celcius):
    temp_kelvin=temp_celcius+273.15
    return temp_kelvin
def convert_temp():
    temp_celcius=convert_to_celsius(temp_fahrenheit)
    temp_kelvin=convert_to_kelvin(temp_celcius)
print(f" the temperature in kelvins is={temp_kelvin}")  
print(f"the temperature in celcius is={temp_celcius}")
convert_temp()
