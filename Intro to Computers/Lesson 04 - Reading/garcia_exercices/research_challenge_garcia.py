# Scenario: You need to build a small Python script that:

# 1. Fetches data from a public API (JSONPlaceholder)
# 2. Parses the JSON response
# 3. Saves specific fields to a file
# 4. Handles errors gracefully

# # import requests and json
import requests
import json

# Define the API URL and the file to save the data
url = "https://jsonplaceholder.typicode.com/posts/1"
file_name = "research_challenge_saved_file_garcia.json"

def fetch_and_save_data():
    try:
        # Fetches data from a public API (JSONPlaceholder)
        response = requests.get(url)
        
        # Raise an exception for HTTP
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract fields
        parsed_data = {
            "title": data.get("title"),
            "body": data.get("body")
        }
        
        # Save to a file
        with open(file_name, "w") as file:
            json.dump(parsed_data, file, indent=4)
        print(f"Data successfully saved to {file_name}")

    # Handle errors
    except requests.exceptions.RequestError as err:
        print(f"Network error occurred: {err}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except json.JSONDecodeError:
        print(f"Error: The API response was not valid JSON.")
    except IOError as err:
        print(f"File writing error: {err}")

# Call the function
if __name__ == "__main__":
    fetch_and_save_data()