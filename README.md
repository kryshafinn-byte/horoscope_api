# Horoscope API

This is my fun Horoscope API where users will be able to find out information about their own zodiacs (or someone else's). I have built this project using the four important ones! **Python, Flask, Flask‑RESTx, and MySQL.**

## My Goal?

My goal was first, to be dancing for joy to create something! But also to:

- Build an API using Flask  
- Structure a project in a professional and clear way, to get me career‑ready!  
- Use Git + GitHub for being able to keep a good track of my project!  
- Display my API using Flask‑RESTx (Swagger)  - Anybody else start thinking about the song by Cher Lloyd when they see this, or just me?

## The Features

Currently, we have it that:

- **12 zodiac signs** will show and return back to us  
- Zodiac details show the **name**, **date range**, and if they are **Fire, Earth, Air, or Water!**

## 🛠 Where my Tech at?

- Python  
- Flask  
- Flask‑RESTx (for my Swagger UI)  
- MySQL  
- Git + GitHub  

## This is the structure (but again, so far! Rome was not built in a day!)

Horoscope_api/
app/
    init.py
routes/
    signs_routes.py
models/
    air_signs.py
    base_sign.py
    earth_signs.py
    fire_signs.py
    water_signs.py
database/
horoscope_setup.sql   # My horoscope 12 signs table
venv/   # My virtual environment (not committed though, even though I did keep on accidentally putting folders inside my venv)
requirements.txt   # Installed my Python packages - yay!
app.py
config.py
README.md   # Got to keep that project tracked and documented!

## Blueprints Added (Day 2)

I’ve now moved my `/signs` endpoint into its own Blueprint inside  
`app/routes/signs_routes.py` so that it can be clean and work well in the professional setting.

The Flask app now can register this Blueprint inside `app/__init__.py`, which makes it so much nicer!

I also added a **homepage route (`/`)** that returns a welcome message.

MySQL is now fully connected, and the `/signs` endpoint successfully returns data from the database.

## Now, how's it going?

Well, first things first, got to keep this project tracked!  
So, I have used the lovely GitHub Project Board!  
Moving my tasks from **To Do → In Progress → Done** has been so satisfying!

## My future things and twiddly bits will be coming soon!

- Add lucky colours table  
- Add compatability table  
- Add endpoints for each sign  
- Add query parameters  
- Get that SWAGGER documentation!  
- Add in those error handling!  
- Add unit tests (and keep on testing!)  

---

## 💫 Thank you, and I cannot wait for what is next!
