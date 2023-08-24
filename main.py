from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    films = [
        {"name": "Blade Runner", "director": "Ridley Scott"},        
    ]
    print(films)
    context = {"request": request, "films": films}
    return templates.TemplateResponse("index.html", context)

@app.get("/films", response_class=HTMLResponse)
def get_films(request: Request):
    print("Got Request")
    filmsFromDB = [
        {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
        {"name": "Mulholland Drive", "director": "David Lynch"},
    ]
    context = {"request": request, "filmsFromDB": filmsFromDB}
    return templates.TemplateResponse("films.html", context)