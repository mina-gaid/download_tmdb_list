# Download TMDB watchlist or a specific list by ID

This Python script allows you to download your TMDB watchlist or a specific list by ID, and save the content to an Excel file.

## Prerequisites

- Python 3
- `tmdbsimple` and `pandas` packages installed. If not, install them using pip:

```
pip install tmdbsimple pandas
```

## Usage

1. Open a terminal or command prompt.
2. Clone or download this repository to your local machine.
3. Navigate to the directory containing the script.
4. Run the script by entering the following command:

```
python download_tmdb_list.py
```

5. Enter your TMDB API key when prompted.
6. Select whether you want to download your watchlist or a specific list by entering 'w' or 'l' respectively.
7. If you selected 'l', enter the ID of the list you want to download.
8. Wait for the script to finish running. It will create an Excel file in the same directory containing the content of the list.

## Note

- If you select to download a specific list, you must have created the list on TMDB website beforehand.

