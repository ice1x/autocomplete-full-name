# autocomplete-full-name
Full name autocomplete micro service based on prefix tree with FastAPI and deployment to Heroku

## API methods:

* Suggest
Allows to get name suggestions by prefix
https://autocomplete-full-name.herokuapp.com/suggest/%D0%B0%D0%BD%D1%82%D0%BE%D0%BD&10

* Parse
Allows to get name tokens by abstract text string
https://autocomplete-full-name.herokuapp.com/parse/%D0%BE%D0%B4%D0%B8%D0%BD%20%D0%B8%D0%B2%D0%B0%D0%BD%20%D0%B4%D0%B2%D0%B0%20%D0%B8%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%20%D1%82%D1%80%D0%B8%20%D0%B8%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87

## Changelog:
* Python Prefix Trie inherited from https://github.com/ice1x/Python-Prefix-Tree
* Integrated with FastAPI
* Added deployment to Heroku
* Fixed problem with Cyrillic UTF-8 text
* Added Parse API method
