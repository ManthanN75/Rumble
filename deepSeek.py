# # deepSeek.py
# import requests

# api_key = "sk-0b5ed2fcc9aa4cbb839279976139a1f5"

# def search_deepseek(query, api_key):  # Accept both query and api_key
#     """
#     Sends a search query to the DeepSeek API and returns the results.
#     """
#     url = "https://api.deepseek.com/search"  # Replace with the correct endpoint
#     headers = {
#         "Authorization": f"Bearer {api_key}",  # Use the provided API key
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "query": query,
#         "max_results": 5  # Adjust based on your needs
#     }

#     try:
#         # Send POST request to DeepSeek API
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()  # Raise an error for bad status codes
#         results = response.json()  # Parse JSON response
#         return results
#     except requests.exceptions.RequestException as e:
#         print(f"DeepSeek API request failed: {e}")
#         return {"error": str(e)}