from tkinter import *
import requests
import time
 
 
canvas = Tk()
canvas.geometry("600x500")
canvas.resizable(0,0)
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold") 

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=06c921750b9a82d8f5d1294e1586276f"    
    json_data = requests.get(api).json()
   
    kelvin = 273.15 # value of kelvin    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - kelvin)
    feels_like = int(json_data['main']['feels_like'] - kelvin)
    min_temp = int(json_data['main']['temp_min'] - kelvin)
    max_temp = int(json_data['main']['temp_max'] - kelvin)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Feels_like: " + str(feels_like) + "°C" "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "%" "\n" +"Wind Speed: " + str(wind) + "km/h" "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

   

city_head= Label(canvas, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
textField = Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = Label(canvas, font=t)
label1.pack()
label2 = Label(canvas, font=f)
label2.pack()
canvas.mainloop()