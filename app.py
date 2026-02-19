from app import make_app
from app.routes.lucky_colour_routes import make_lucky_colours

app = make_app()
make_lucky_colours(app)

if __name__ == "__main__":
    app.run(debug=True)
