import tmdbsimple as tmdb
import pandas as pd

# Prompt the user for their API key
api_key = input("Enter your TMDB API key: ")

# Set up the TMDB client with the API key
tmdb.API_KEY = api_key

# Ask the user whether they want to download their watchlist or a specific list by ID
list_type = input("Do you want to download your watchlist (w) or a specific list by ID (l)? ")

if list_type == "w":
    # Download the user's watchlist
    account = tmdb.Account()
    watchlist = account.watchlist().get(language="en-US", page=1)
    list_name = "watchlist"
else:
    # Ask the user for the list ID
    list_id = input("Enter the ID of the list you want to download: ")
    # Download the specified list
    client = tmdb.Client(api_key)
    list_details = client.lists.get(list_id)
    list_items = client.lists.items(list_id, language="en-US")
    list_name = list_details["name"]
    watchlist = list_items["results"]

# Convert the watchlist to a Pandas DataFrame
df = pd.DataFrame(watchlist)

# Write the DataFrame to an Excel file
filename = f"{list_name}.xlsx"
df.to_excel(filename, index=False)

print(f"{len(watchlist)} items written to {filename}")
