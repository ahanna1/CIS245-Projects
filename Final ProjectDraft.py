#Alex Hanna
#05/15/2021
#Final Project


import requests,json   #import requests and json modules


def get_city (): # function for searching by city
    api_key = "b74a6c2d77519aba9e7d0062c4650ee9" # key provided by open weather
    url = "http://api.openweathermap.org/data/2.5/weather?" # open weather url
    city = input("Enter the City: ")
    full_url = url + "appid=" + api_key+ "&q="+ city #complete url needed for api call
    
    forecast = requests.get(full_url) # get method from requests pulls info from open weather
    data = forecast.json() # converts data from json to python format
    display_forecast(data) # calls display_forecast and passes data
    
    prompt = input("Another search?") # prompt asks user if they want to do another search
    if prompt == "y":
        main()
    if prompt == "n":
        print("Program has ended")
        exit()
  
def get_zip (): # function for searching by zip code
    api_key = "b74a6c2d77519aba9e7d0062c4650ee9"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    zip = input ("Enter Zip Code:")
    full_url = url + "appid=" + api_key+ "&zip=" + zip
    forecast = requests.get(full_url)
    data = forecast.json()
    display_forecast(data)
    prompt = input("Another search?")
    if prompt == "y":
        main()
    if prompt == "n":
        print("Program has ended")
        exit()

    
def display_forecast(data):
    
    temp = data["main"]["temp"]
    temp = int(round(temp * 1.8) - 459.67) 
    feels_like= data["main"]["feels_like"]
    feels_like = int(round(feels_like * 1.8) - 459.67)
    min_temp = data["main"]["temp_min"]
    min_temp = int(round(min_temp * 1.8) - 459.67)
    max_temp = data["main"]["temp_max"]
    max_temp = int(round(max_temp * 1.8) - 459.67)
    description = data["weather"][0]["description"] # stores description at 0 index of weather

    #forecast details are accessed by corresponding dictionary keys
    # temps are in kelvin units and converted to F, also rounded up
    
    print("Connection sucessfull, one moment...")
    print()
    
    print(f"Weather condition: {description}")
    print(f"Current Temperature(fahrenheit): {temp}")
    print(f"Feels Like(fahrenheit): {feels_like}")
    print(f"Low Temperature(fahrenheit): {min_temp}")
    print(f"High Temperature(fahrenheit): {max_temp}")

def main ():
    
    while True:
        welcome = input ("Enter 'zip' to search forecast by zip code or 'city' to search by city: " )

        if welcome == "city":
            try:
                get_city()
            except:
                print("That city was not found, try again")
        if welcome == "zip":
            try:
                get_zip()
            except:
                print("That city was not found, try again")

    # while loop with try blocks, that call get_city or get_zip depending on user's input
  

main()








