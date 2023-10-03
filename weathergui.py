import tkinter as tk
import requests
api_key = 'YOUR_API_KEY'
def get_weather(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] == "404":
            return "City not found. Please check the city name."
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"Weather in {city_name}:\nDescription: {weather_description.capitalize()}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def fetch_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        result_label.config(text=weather_info)
    else:
        result_label.config(text="Please enter a city.")
root = tk.Tk()
root.title("Weather App")
city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=fetch_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()
