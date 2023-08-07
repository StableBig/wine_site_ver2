from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import pandas as pd

def get_year_form(num):
    if 11 <= num % 100 <= 20:
        return "лет"
    else:
        if num % 10 == 1:
            return "год"
        elif 2 <= num % 10 <= 4:
            return "года"
        else:
            return "лет"

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")

excel_table_df = pd.read_excel("wine.xlsx")

wine_characteristics = excel_table_df.to_dict(orient="records")

current_year = datetime.now().year
winery_age = current_year - 1920
year_form = get_year_form(winery_age)

rendered_page = template.render(
    winery_age=f"{winery_age} {year_form}",
    wine_characteristics=wine_characteristics
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
