import tkinter as tk   # for the UI
import requests     # I was having problems with the PIP on on my desktop It worked on my laptop      But I test it on  the replit IDE. 

def getWeather(canvas):
    # zip = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?zip=90210,us&appid=09d000cd760c041414c09bede4f3eb27"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
 #  The Json file provides the temp in kelvin, so to  use in US Fahrenheit I use the formula to convert it . f+ K * 1.8 - 459.67

    temp = int(json_data['main']['temp'] * 1.8 - 459.67 )
    min_temp = int(json_data['main']['temp_min'] * 1.8 - 459.67)
    max_temp = int(json_data['main']['temp_max'] * 1.8 - 459.67)

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°F" + "\n" + "Max Temp: " + str(max_temp) + "°F" + "\n\n\n" + " by  Mario Montenegro"

    
    label1.config(text=final_info)
    label2.config(text=final_data)
    

canvas = tk.Tk()
canvas.geometry("700x500")
canvas.title("Leidos Weather App By Zip code")
f = ("Times", 20, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()