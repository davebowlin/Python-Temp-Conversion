#######################################################
#  This code snippet converts temperatures from       #
#  C to F, and F to C                                 #
#######################################################

def convert(t, temp):
    if t == "C":
        # convert to Celsius
        return round((temp - 32) * 5/9, 1)
    else:
        # convert to Fahrenheit
        return round((temp * 9/5) + 32, 1)

while True:
    t = input("Convert temperature to (F)ahrenheit or (C)elsius, or (q) to quit: ").upper()
    if t not in ["F", "C", "Q"]:
        print("That is not a valid choice, try again.")
    else:
        if t == "Q":
            break
        
        temp = float(input("Enter the temperature: "))
        
        print(f"The temperature converted to {t} is: {convert(t, temp)}")
