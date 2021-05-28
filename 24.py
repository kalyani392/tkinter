#24.Temperature converter

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit=ent_temperature.get()
    celsius=(5/9)*(float(fahrenheit)-32)
    lbl_result["text"]=f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
