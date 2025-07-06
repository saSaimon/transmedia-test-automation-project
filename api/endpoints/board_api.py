import requests

BASE_URL = "http://localhost:3000/api"

def create_board(name):  # <== previously 'title'
    payload = {"name": name}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/boards", json=payload, headers=headers)
    print("Create board:", response.status_code, response.text)
    return response

def delete_board(board_id):
    response = requests.delete(f"{BASE_URL}/boards/{board_id}")
    print("Delete board:", response.status_code, response.text)
    return response