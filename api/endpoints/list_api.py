import requests

BASE_URL = "http://localhost:3000/api"

def create_list(board_id, title):
    payload = {"boardId": board_id, "title": title}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/lists", json=payload, headers=headers)
    print("Create list:", response.status_code, response.text)
    return response

def delete_list(list_id):
    response = requests.delete(f"{BASE_URL}/lists/{list_id}")
    print("Delete list:", response.status_code, response.text)
    return response