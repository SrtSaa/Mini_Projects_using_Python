from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk



root = Tk()
root.title("Weather App")
root.geometry("630x550+400+150")
root.resizable(False, False)


def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # extract weather data
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2008de9c33ececb4edd412f69368b95a"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        feels_like = int(json_data['main']['feels_like'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        cloud = json_data['clouds']['all']
        visibility = round(json_data['visibility']/1000, 2)

        # use data
        maxmin.config(text=("Day: "+str(max_temp)+"°↑ • Night: "+str(min_temp)+"°↓"))
        t.config(text=(str(temp)+"°"))
        c.config(text=(condition+" | Feels like "+str(feels_like)+"°"))
        w.config(text=str(wind)+" m/sec")
        h.config(text=str(humidity)+"%")
        cl.config(text=str(cloud)+"%")
        p.config(text=str(pressure)+" mb")
        v.config(text=str(visibility)+" km")
        d.config(text=description)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!!")



# search box
image = Image.open("X:\Project\WebApp\pics\search.png").resize((450,80))
search_image = ImageTk.PhotoImage(image)
myimage = Label(image=search_image).place(x=90, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=150, y=40)
textfield.focus()

search_icon = PhotoImage(file="X:\Project\WebApp\pics\search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather).place(x=450,y=34)


# logo
logo_image = PhotoImage(file="X:\Project\WebApp\pics\logo.png")
logo = Label(image=logo_image).place(x=130, y=110)


# bottom box
image = Image.open("X:\Project\WebApp\pics\\box.png").resize((610,200))
frame_image = ImageTk.PhotoImage(image)
frame_myimage = Label(image=frame_image).place(x=10, y=340)


# time
name = Label(root, font=("arial",17,"bold"), fg="#C53D46")
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica",17))
clock.place(x=30, y=130)


# labels
label1 = Label(root, text="Wind", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=55, y=390)
label2 = Label(root, text="Humidity", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=150, y=390)
label3 = Label(root, text="Cloud", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=270, y=390)
label4 = Label(root, text="Pressure", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=360, y=390)
label4 = Label(root, text="Visibility", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=485, y=390)
label5 = Label(root, text="Description:", font=("Helvetica",17,"bold"),fg="white",bg="#1ab5ef").place(x=55, y=460)

maxmin = Label(font=("arial",13,"bold"))
maxmin.place(x=380, y=145)
t = Label(font=("arial",70,"bold"), fg="#ee666d")
t.place(x=380, y=170)
c = Label(font=("arial",15,"bold"))
c.place(x=380, y=280)

w = Label(text="       ...", font=("arial",15,"bold"), bg="#1ab5ef")
w.place(x=35, y=420)
h = Label(text=" ...", font=("arial",15,"bold"), bg="#1ab5ef")
h.place(x=185, y=420)
cl = Label(text=" ...", font=("arial",15,"bold"), bg="#1ab5ef")
cl.place(x=290, y=420)
p = Label(text="     ...", font=("arial",15,"bold"), bg="#1ab5ef")
p.place(x=370, y=420)
v = Label(text="    ...", font=("arial",15,"bold"), bg="#1ab5ef")
v.place(x=500, y=420)
d = Label(text="...", font=("arial",15,"bold"), bg="#1ab5ef")
d.place(x=200, y=465)





root.mainloop() 