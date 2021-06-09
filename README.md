# Full name autocomplete micro service on FastAPI

## API methods:

* Suggest
Allows to get name suggestions by prefix using option: query and count (suggestion list max size - 10 by default)
https://autocomplete-full-name.herokuapp.com/suggest/?query=%D0%B0%D0%BD%D1%82%D0%BE%D0%BD&count=10

* Parse
Allows to get name tokens by abstract text string using option: query
https://autocomplete-full-name.herokuapp.com/parse/?query=%D0%BE%D0%B4%D0%B8%D0%BD%20%D0%B0%D0%BD%D1%82%D0%BE%D0%BD%20%D0%B4%D0%B2%D0%B0%20%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%B8%D1%87%20%D1%82%D1%80%D0%B8%20%D1%87%D0%B5%D1%85%D0%BE%D0%B2

## Changelog:
* Moved Python Prefix Trie to separate pypi repo: https://pypi.org/project/prefix-tree/
* Python Prefix Trie inherited from https://github.com/ice1x/Python-Prefix-Tree
* Integrated with FastAPI
* Added deployment to Heroku
* Added test coverage
* Fixed problem with Cyrillic UTF-8 text (affected Safari OSX/iOS)
* Added Parse API method

## Known issues:
* Only russian names supported
* Suggestions and parsing based of name list so if the name is absent in list it will not be parsed and suggested
