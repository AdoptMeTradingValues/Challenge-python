import requests

def extract_data_from_api():
    url = "http://security.mercurywork.shop/api"

    try:
        response = requests.get(url)
        data = response.json()
        
        for key, value in data.items():
            print(f"{key}: {value}")
    
    except Exception as e:
        print(f"Error extracting data: {e}")

extract_data_from_api()
