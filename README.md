# Horoscope API

A fun little Horoscope API where you can look up zodiac signs, find lucky colours, check compatibility, and even work out someone’s sign from their birthdate. Built with **Python**, **Flask**, **Flask‑RESTx**, and **MySQL**.

## Project Overview

This API is designed to be clean, beginner‑friendly, and easy to explore. Routes are organised into simple files, everything returns tidy JSON, and Swagger UI makes it smooth to navigate whether you’re a developer or just curious about the stars.

## My Goal

I wanted to build something joyful while learning how to structure a project professionally, use Git + GitHub properly, and document everything clearly with Swagger!

## Features

- All 12 zodiac signs  
- Sign details: name, element, date range  
- Find a sign by name  
- Work out a sign from a birthdate  
- Lucky colours (from MySQL)  
- Compatibility between two signs  

## Tech

- Python  
- Flask  
- Flask‑RESTx  
- MySQL  
- Git + GitHub  

## Setup, Running, Testing, and Using the API

### Setup
1. Create and activate a virtual environment  
   - Git Bash: `source venv/Scripts/activate`  
   - CMD: `venv\Scripts\activate`
2. Install dependencies:  pip install -r requirements.txt
3. Set up the database: SOURCE horoscope_setup.sql;
4. Add your MySQL details to 'config.py'

## Run that App
    flask run
Visit: `http://127.0.0.1:5000/`  
Swagger UI will show all endpoints.

### Run the tests
    pytest

### Endpoints
- `/` — Welcome message  
- `/signs` — All zodiac signs  
- `/signs/<name>` — One sign  
- `/signs/by-date?date=YYYY-MM-DD` — Sign from birthdate  
- `/lucky-colour/<name>` — Lucky colours  
- `/compatibility/<sign1>/<sign2>` — Compatibility  

### Error responses
- Missing date → `400`  
- Invalid date → `400`  
- Unknown sign → `404`  
- Unknown compatibility sign → `404`  

### How the data works
Two simple MySQL tables:
- `signs` (name, element, date_range)  
- `lucky_colours` (sign_name, colour1, colour2, colour3)

### How the classes work
- `BaseSign` holds shared attributes  
- `FireSign`, `EarthSign`, `AirSign`, `WaterSign` inherit from it  
- Keeps everything clean and avoids repeating code  

---

## Project Structure

      horoscope_api/
         app/
            routes/
               signs_routes.py
               lucky_colour_routes.py
               compatibility_routes.py
            models/
               base_sign.py
               fire_signs.py
               earth_signs.py
               air_signs.py
               water_signs.py
            utils/
               sign_calculator.py
         database/
            horoscope_setup.sql
         requirements.txt
         app.py
         pytest.ini
         config.py
         README.md

## Done and dusted

- Clean route structure  
- MySQL connection + real data  
- Lucky colours endpoint  
- Compatibility logic  
- Birthdate → sign logic  
- Swagger documentation  
- Error handling  
- Tests with pytest  
- Code tidy‑up + docstrings  
- Updated README  
- Updated project board  

## Thank You

I cannot wait for what is next.

