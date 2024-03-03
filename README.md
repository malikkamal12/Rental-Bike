# Rental Bike Dashboard
**Tugas Akhir Proyek Analisis Data**

## Setup environment
```
conda create --name python=3.9
conda activate --name
pip install numpy pandas matplotlib seaborn streamlit 
```

## Run steamlit app
```
streamlit run dashboard.py
```

## Dataset overview
### Introduction
This dataset consists of information about bike sharing rentals recorded over a period of two years. It includes various features such as date, weather conditions, and rental counts.

## Data Structure
- `instant`: Sequential unique identifier for each row.
- `dteday`: Date of the recorded data.
- `season`: season (1:springer, 2:summer, 3:fall, 4:winter)
- `yr`: year (0: 2011, 1:2012)
- `mnth`: month (1 to 12)
- `hr`: hour (0 to 23)
- `holiday`: Binary feature indicating whether it's a holiday or not.
- `weekday`: Day of the week (0: Sunday, 1: Monday, ..., 6: Saturday).
- `workingday`: Binary feature indicating whether it's a working day or not.
- `weathersit`: Weather situation :
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- `temp`: Normalized temperature in Celsius. The values are divided by 41 (max)
- `atemp`: Normalized feeling temperature in Celsius. The values are divided by 50 (max)
- `hum`: Normalized humidity. The values are divided by 100 (max)
- `windspeed`: Normalized wind speed. The values are divided by 67 (max)
- `casual`: count of casual users
- `registered`: count of registered users
- `cnt`: Total count of bike rentals (casual + registered).
