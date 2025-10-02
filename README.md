# Ex.05 Design a Website for Server Side Processing
# Date:2/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
power.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .calc{
            font-family: algerian;
            font-size: x-large;
            color: #E0EEC6;
        }
        body{
            background-image: url("https://img.freepik.com/premium-photo/light-bulb-with-dark-background-blue-background_777078-2360.jpg");
            background-size: cover;
        }
    </style>
    <title>Power calculator</title>
</head>
<body>

    <p style="text-align: center;font-size: xx-large;font-family: algerian;background-color: rgba(62, 225, 247, 0.5);color: #E4FDE1;text-shadow:
       0 0 1px #00ff3c,  /* very tight yellow glow */
      0 0 2px #00ff15,
      0 0 3px #9efd60,
      0 0 4px #87fc5c;">POWER CALCULATOR</p>
    <center><form method="post">
        {%csrf_token%}
        <div class="calc">
        <label for="I">Enter Current value(in amperes):</label>
        <input type="number" name="I" placeholder="Current"><br><br><br>
        <label for="R">Enter Resistance value(in ohm):</label>
        <input type="number" name="R" placeholder="Resistance"><br><br><br>
       <i><button type="submit" style="border-radius: 40px;background-color: aqua;font-size: xx-large;">Calculate</button></i>
        </div>
    </form>
    
    </center>
</body>
</html>

result.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
    <style>
        body{
            background-image: url("https://img.freepik.com/premium-photo/light-bulb-with-dark-background-blue-background_777078-2360.jpg");
            background-size: cover;
        }
    </style>
</head>
<body>
    <center style="background-color: rgba(84, 238, 249, 0.351);font-size: xx-large;">
    <h1 style="font-family: brush script mt;color:rgb(0, 255, 255)">RESULT</h1>
    <p style="color: lightgoldenrodyellow;"> Power = {{power}} W</p>
    </center>
</body>
</html>

views.py
from django.shortcuts import render
def calculator(request):
    power= None
    if request.method == "POST":
        I=float(request.POST.get("I"))
        R=float(request.POST.get("R"))
        power=I**2 *R
        print(f"Enter Current value(in amperes): {I}, Enter Resistance value(in ohm): {R}, Power={power:.2f}")
        return render(request, 'result.html', {'power': power, 'I': I, 'R': R})
    return render(request, 'power.html', {'power':power})

urls.py
from django.contrib import admin
from django.urls import path
from powerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculator, name='calculator'),
]


```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-02 211248.png>)

# HOMEPAGE:
![alt text](<Screenshot 2025-10-02 210712.png>)
![alt text](<Screenshot 2025-10-02 210726.png>)

# RESULT:
The program for performing server side processing is completed successfully.
