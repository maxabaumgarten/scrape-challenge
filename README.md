# scrape-challenge

A challenge to scrape http://books.toscrape.com/ 

## Details

- Written in Python
- Parses product information from the Science and Poetry categories
- Saves data in a csv file

## Requirements

```sh
pip install -r requirements.txt
```

## Run

```sh
python main.py
```
View the generated CSV file for the data

## Issues 🤬

- This currently does not work
- Issue is due to not understanding how BeautifulSoup parses href links.
- Currently the program is returning "..//../" instead of the actual links causing it to fail
