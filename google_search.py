# google_search.py
import requests

def search_google(query, api_key, cx):
    """
    Sends a search query to the Google Custom Search JSON API and returns the results.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query
    }

    try:
        # Send GET request to Google Custom Search API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        results = response.json()  # Parse JSON response
        return results
    except requests.exceptions.RequestException as e:
        print(f"Google API request failed: {e}")
        return {"error": str(e)}