import os
import pandas as pd
import argparse
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from config import FOUNDING_YEAR, WINE_LIST_PATH, SPECIAL_WINES

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

parser = argparse.ArgumentParser(description="Укажите путь к файлу с данными.")
parser.add_argument("--file", type=str, default=WINE_LIST_PATH,
                    help="Путь к файлу с данными. По умолчанию из файла конфигурации.")
args = parser.parse_args()

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")

current_year = datetime.now().year
winery_age = current_year - FOUNDING_YEAR
year_form = get_year_form(winery_age)

wine_characteristics = pd.read_excel(args.file)
wine_characteristics = wine_characteristics.fillna("")

grouped_characteristics = defaultdict(list)
for _, row in wine_characteristics.iterrows():
    grouped_characteristics[row["Категория"]].append(row.to_dict())

rendered_page = template.render(
    winery_age=f"{winery_age} {year_form}",
    grouped_characteristics=grouped_characteristics,
    special_wines=SPECIAL_WINES
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
