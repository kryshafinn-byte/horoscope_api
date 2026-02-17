# Horoscope API
This is my fun Horoscope API. Users will be able to find out information about their own zodiacs (or someone else's).
I have built this project using the four important ones!
**Python**, **Flask**, **Flask-RESTx**, and **MySQL**.

# My Goal?
My goal was first, to be dancing for joy to create something! But also to:
- Build an API using Flask
- Strtucture a project in a professional and clear way, to get me career-ready!
- Use Git + GitHub for being able to keep a good track of my project!
- Display my API using Flask-RESTx (Swagger) - *Anybody else start thinking about the song by Cher Lloyd when they see this, or just me?*

# The Features
Currently, we have it that:
- 12 zodiac signs will show and return back to us
- Zodiac details shows the name, date range and if they are Fire, Earth, Air, or Water!

# WIP (Work In Progress)
It is just early days for now, but I want to be adding on lucky colours, compatability, a person to just get their indivdual sign, some query parameters and some Swagger info documented!

# Where my Tech at?
- **Python**
- **Flask**
- **Flask-RESTx** (for my Swagger UI)
- **MySQL**
- **Git + GitHub**

This is the structure (but again, so far! Rome was not built in a day!)

    Horoscope_api/
        app/
            __init__.py
            routes/
            services/
            models/
        database/
            horoscope_setup.sql   # My horoscope 12 signs table
    venv/   # My virtual environment (not committed though, even though I did keep on accidentally putting folders inside my venv)
    requirements.txt   # Installed my Python packages - yay!
    README.md   # Got to keep that project tracked and documented!
    app/
  
## Blueprints Added (Session 2 Progress)
I’ve now moved my /signs endpoint into its own Blueprint inside app/routes/signs_routes.py so that it can be clean and work well in the professional setting.
The Flask app now can register this Blueprint inside that of app/__init__.py, which makes it so much nicer!

# Now, how's it going?
Well, first things first, got to keep this project tracked! So, I have used the lovely *GitHub Project Board!*
Moving my tasks from To Do --> In Progress --> Done! Has been so satisfying!

My future things and twiddly bits will be coming soon!
- Add lucky colours table
- Add compatability table
- Add endpoints for each sign
- Add query parameters
- Get that SWAGGER documentation!
- Add in those error handling!
- Add unit tests (and keep on testing!)

Thank you, and I cannot wait for what is next!
    
