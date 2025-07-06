from api.endpoints.board_api import create_board, delete_board
from api.endpoints.list_api import create_list, delete_list

def test_create_and_delete_list():
    board = create_board("API Test Board")
    assert board.status_code == 201

    board_id = board.json().get("id")
    assert board_id

    lst = create_list(board_id, "Temp List")
    assert lst.status_code == 201

    list_id = lst.json().get("id")
    assert list_id

    assert delete_list(list_id).status_code == 200
    assert delete_board(board_id).status_code == 200