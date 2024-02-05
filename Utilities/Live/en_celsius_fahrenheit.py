def convert_temperature(temperature, scale):
    try:
        temperature = float(temperature)
        if scale.upper() == 'C':
            result = (temperature * 9/5) + 32
            return result, 'F'
        elif scale.upper() == 'F':
            result = (temperature - 32) * 5/9
            return result, 'C'
        else:
            return "Invalid scale. Enter 'C' or 'F'", None
    except ValueError:
        return "Error: Enter a valid temperature as a number", None

# Example of usage
try:
    temperature_input = input("Enter the temperature: ")
    scale_input = input("Enter the scale (C or F): ")

    result, new_scale = convert_temperature(temperature_input, scale_input)

    if new_scale:
        print(f"{temperature_input}°{scale_input} is equal to {result:.2f}°{new_scale}")
    else:
        print(result)

except Exception as e:
    print(f"Error: {e}")
