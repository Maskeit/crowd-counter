import requests

# URL de la API
api_url = 'http://127.0.0.1:5000/data'

def send_person_count(person_count):
    payload = {'cantidad': person_count}
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        print(f'Successfully sent person count: {person_count}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to send person count: {e}')