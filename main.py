import pandas as pd
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

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

current_year = datetime.now().year
winery_age = current_year - 1920
year_form = get_year_form(winery_age)

wine_characteristics = pd.read_excel("wine2.xlsx")
wine_characteristics = wine_characteristics.fillna("")

grouped_characteristics = defaultdict(list)
for _, row in wine_characteristics.iterrows():
    grouped_characteristics[row["Категория"]].append(row.to_dict())

rendered_page = template.render(
    winery_age=f"{winery_age} {year_form}",
    grouped_characteristics=grouped_characteristics
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
