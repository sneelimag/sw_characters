import fire
import search_api

def search(name='luke'):
  characters = search_api.search(name)
  if characters is not None:
    parse_char_list(characters)
  else:
    print(f'Cannot find the character "{name}"')

def parse_char(char):
  char_name = search_api.parse_name(char)
  planet= search_api.parse_planet(char)
  film_list = search_api.parse_films(char)
  titles = search_api.format_titles(film_list)
  description = search_api.person_description(char_name, planet, titles)
  return description

def parse_char_list(chars):
  for char in chars:
    char_name = search_api.parse_name(char)
    planet= search_api.parse_planet(char)
    film_list = search_api.parse_films(char)
    titles = search_api.format_titles(film_list)
    description = search_api.person_description(char_name, planet, titles)
    print(description)

if __name__ == '__main__':
  fire.Fire(search)