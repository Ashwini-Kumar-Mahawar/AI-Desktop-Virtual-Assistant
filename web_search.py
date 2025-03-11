import webbrowser

def search_web(query):
    # Remove the "search" keyword from the query
    query = query.replace("search", "").strip()

    # Construct the Google search URL
    url = f"https://www.google.com/search?q={query}"

    # Open the URL in the default web browser
    webbrowser.open(url)
    print(f"Searching for: {query}")