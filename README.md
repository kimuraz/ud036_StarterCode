# ud036_StarterCode
Source code for a Movie Trailer website.

## Requirements

### Python
`python 2.x or 3.x`
### Web browser
Any web browser.
### Dependencies
Use pip and the `requirements.txt` for installing the project dependencies:

```shell
$ pip install -r requirements.txt
```
If you have more than one python project you might want to use
[VirtualEnvironments]('https://virtualenv.pypa.io/en/stable/')

## Running the program
```shell
$ python movie_page_data.py
```
This command will generate `fresh_tomatoes.html` file and open your browser,
rendering the movies instatiated in `movie_page_data.py`.

## Adding movies
If you want to add more movies just add a Movie instance according to the class in
`media.py` and put it `movies` array in `movie_page_data.py`.
