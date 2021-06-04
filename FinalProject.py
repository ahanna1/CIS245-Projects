#Alex Hanna
#06/03/2021
#Final Project


import requests,json   #import requests and json modules


def get_city (): # function for searching by city
    api_key = "b74a6c2d77519aba9e7d0062c4650ee9" # key provided by open weather
    url = "http://api.openweathermap.org/data/2.5/weather?" # open weather url
    city = input("Enter the City: ")
    full_url = url + "appid=" + api_key+ "&q="+ city +"&units=imperial" #complete url needed for api call in imperial units
    
    forecast = requests.get(full_url) # get method from requests pulls info from open weather

    if forecast.status_code == 200: # if status code = 200 and is successfull will tell user of successful connection
        print("Connection successful!")
    
    else: # if status code does not equal 200 or is unsuccessful
        print("Connection not successfull")
    
    data = forecast.json() # converts data from json to python format
    display_forecast(data) # calls display_forecast and passes data
    
    prompt = input("Another search? If yes enter 'y' or enter any other key to exit.") # prompt asks user if they want to do another search
    if prompt == "y":
        main()
    else:
        print("Program has ended")
        
        
  
def get_zip (): # function for searching by zip code
    api_key = "b74a6c2d77519aba9e7d0062c4650ee9"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    zip = input ("Enter Zip Code:")
    full_url = url + "appid=" + api_key+ "&zip=" + zip +"&units=imperial"
    forecast = requests.get(full_url)

    if forecast.status_code == 200:
        print("Connection successful!")
    else:
        print("Connection not successfull")

    data = forecast.json()
    display_forecast(data)
    prompt = input("Another search? If yes enter 'y' or enter any other key to exit.")
    if prompt == "y":
        main()
    else: 
        print("Program has ended")
        
        
def display_forecast(data):
    
    temp = data["main"]["temp"]
    feels_like= data["main"]["feels_like"]
    min_temp = data["main"]["temp_min"]
    max_temp = data["main"]["temp_max"]
    description = data["weather"][0]["description"] # stores description at 0 index of weather

    #forecast details are accessed by corresponding dictionary keys
    
    
    print()
    
    print(f"Current Weather condition: {description}")
    print(f"Current Temperature(fahrenheit): {temp}")
    print(f"Feels Like(fahrenheit): {feels_like}")
    print(f"Low Temperature(fahrenheit): {min_temp}")
    print(f"High Temperature(fahrenheit): {max_temp}")
    print()

def main ():
    
    
        welcome = input ("Enter 'zip' to search forecast by zip code or 'city' to search by city: " )
        
        if welcome == "city":
            try:
                get_city()
            except:
                print("That city was not found, try again")
                get_city()
        if welcome == "zip":
            try:
                get_zip()
            except:
                print("That zip code was not found, try again")
                get_zip()

# while loop with try blocks, that call get_city or get_zip depending on user's input
  

main()