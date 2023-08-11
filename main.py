import os
import pandas as pd
import argparse
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from dotenv import load_dotenv


def get_year_form(num):
    if 11 <= num % 100 <= 20:
        return "лет"

    if num % 10 == 1:
        return "год"
    elif 2 <= num % 10 <= 4:
        return "года"

    return "лет"


def main():
    load_dotenv()

    founding_year = int(os.environ.get("FOUNDING_YEAR", 1920))
    wine_table_path = os.environ.get("WINE_LIST_PATH", "wine.xlsx")

    parser = argparse.ArgumentParser(description="Скрипт для генерации веб-страницы на основе данных о винах из файла Excel. Запускает веб-сервер для отображения результата.")
    parser.add_argument("--file", type=str, default=wine_table_path,
                        help="Путь к файлу Excel с данными о винах. По умолчанию используется путь из файла конфигурации.")
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"])
    )

    template = env.get_template("template.html")

    current_year = datetime.now().year
    winery_age = current_year - founding_year
    year_form = get_year_form(winery_age)

    wine_characteristics = pd.read_excel(args.file)
    wine_characteristics = wine_characteristics.fillna("")

    grouped_characteristics = defaultdict(list)
    for _, row in wine_characteristics.iterrows():
        grouped_characteristics[row["Категория"]].append(row.to_dict())

    rendered_page = template.render(
        winery_age=f"{winery_age} {year_form}",
        grouped_characteristics=grouped_characteristics,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
