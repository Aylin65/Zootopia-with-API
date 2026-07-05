import json
import requests

API_KEY = "F1VH1NjfjZPoJdfDcXu6loDmleH3BpcMS4vyokYC" #kommt später in .env

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def load_html_template(filepath):
    """Loads data from the html file """
    with open(filepath, "r", encoding="utf-8") as handle:
        return handle.read()


def load_data_from_api(animal_name):
    """gets animal data from the ninja animals API."""
    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )
    return response.json()


def serialize_animal(animal_obj):
    """Serializes a single animal into an HTML card."""
    output = ''
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'

    output += '<p class="card__text">\n'

    if "diet" in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += "</p>\n"
    output += "</li>\n"

    return output


def get_information(animals_data):
    """Creates HTML for all animal cards."""
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    return output

animal_name = input("Enter the animal name to get the information: ")

animals_data = load_data_from_api(animal_name)


html_template = load_html_template("animals_template.html")

output = get_information(animals_data)

html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)


def create_html(html):
    """Writes the HTML content to animals.html."""
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)
create_html(html)
