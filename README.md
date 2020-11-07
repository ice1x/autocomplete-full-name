# Full name autocomplete micro service

## API methods:

* Suggest
Allows to get name suggestions by prefix
https://autocomplete-full-name.herokuapp.com/suggest/?query=%D0%B0%D0%BD%D1%82%D0%BE%D0%BD&count=10

* Parse
Allows to get name tokens by abstract text string
https://autocomplete-full-name.herokuapp.com/parse/?query=%D0%B0%D0%BD%D1%82%D0%BE%D0%BD

## Changelog:
* Python Prefix Trie inherited from https://github.com/ice1x/Python-Prefix-Tree
* Integrated with FastAPI
* Added deployment to Heroku
* Added test coverage
* Fixed problem with Cyrillic UTF-8 text (affected Safari OSX/iOS)
* Added Parse API method
