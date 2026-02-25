# Horoscope API

This is my fun Horoscope API where users will be able to find out information about their own zodiacs (or someone else's). I have built this project using the four important ones: Python, Flask, Flask‑RESTx, and MySQL.

## Project Overview

This Horoscope API brings together Flask, MySQL, and Swagger to create a clean, beginner‑friendly, and actually fun little system. Everything is structured neatly using Blueprints and documented with Swagger UI. The whole thing runs smoothly, returns tidy JSON, and is easy to explore whether you're a developer or just curious about the stars and their stories.

## My Goal

My goal was first, to be dancing for joy to create something. But also to:

- Build an API using Flask  
- Structure a project in a professional and clear way, to get me career‑ready  
- Use Git + GitHub to keep a good track of my project  
- Display my API using Flask‑RESTx (Swagger)  
  - (Anybody else start thinking about the song by Cher Lloyd when they see this, or just me)

## The Features

Currently, the API can:

- Return all 12 zodiac signs  
- Show zodiac details: name, date range, and element (Fire, Earth, Air, Water)  
- Fetch a specific sign  
- Work out a sign from a birthdate  
- Return lucky colours for each sign (from MySQL)  
- Check compatibility between two signs using elemental logic  

## Where My Tech At

- Python  
- Flask  
- Flask‑RESTx (for Swagger UI)  
- MySQL  
- Git + GitHub

## How to Run the Tests

This project uses **pytest** to make sure all the zodiac code and info is playing nice. To run the tests: 
1. Activate your virtual environment
2. In the project folder, run: pytest


You’ll see the tests zip by, and pytest will let you know if everything is aligned with the stars or if something needs a little cosmic adjustment. All tests live inside the `app/tests` folder, and they cover things like:

- Working out the correct zodiac sign  
- Boundary dates (the “is this Aries or Pisces?” moments)  
- Invalid dates and friendly error messages  

It keeps the project stable, predictable, and beginner‑friendly — just how I like it.

## This is the structure (but again, so far! Rome was not built in a day!)

    horoscope_api/
         app/
            __init__.py
            routes/
               signs_routes.py
               lucky_colour_routes.py
               compatibility_routes.py
           models/
               air_signs.py
               base_sign.py
               earth_signs.py
               fire_signs.py
               water_signs.py
    database/
         horoscope_setup.sql
    venv/  (not committed, even though I kept accidentally putting things inside it)
    requirements.txt
    app.py
    config.py
    README.md

## Completed

These are the things I’ve already built and polished:

- Added Blueprints and moved routes into their own files  
- Added a homepage route  
- Connected MySQL and returned real data  
- Added lucky colours table and endpoint  
- Added compatibility logic and endpoint  
- Added Swagger documentation  
- Added error handling  
- Added birthdate → sign logic  
- Structured routes using Blueprints  
- Kept testing and refining  

## Twiddly Bits Yet To Come

These are the last little bits of polish I’ll be adding to finish the API properly:

- Give the code a final tidy and clean‑up  
- Make naming consistent across files  
- Add clear docstrings so everything is easy to understand  
- Finish the README sections:
  - How to set things up  
  - How to run the app  
  - How to run the tests  
  - A simple list of all endpoints  
  - What the error messages look like  
  - A quick look at how the data is organised  
  - A beginner‑friendly note on how the sign classes relate to each other  
- Update the project board  
- Double‑check all endpoints  
- Run all tests again  
- Final commit and push  

After that, the API will be fully polished, documented, and ready to hand in.

## Thank You

I cannot wait for what is next.
