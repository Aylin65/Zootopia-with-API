import requests



def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  response = requests.get(
          "https://api.api-ninjas.com/v1/animals",
          headers={"X-Api-Key": API_KEY},
          params={"name": animal_name}
  )
  return response.json()

# def load_data_from_api(animal_name):
#     """gets animal data from the ninja animals API."""
#     response = requests.get(
#         "https://api.api-ninjas.com/v1/animals",
#         headers={"X-Api-Key": API_KEY},
#         params={"name": animal_name}
#     )
#     return response.json()