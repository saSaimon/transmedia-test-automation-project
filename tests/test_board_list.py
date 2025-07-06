import time
import pytest
from pages.home_page import HomePage
from pages.board_page import BoardPage

def test_create_board_and_delete_list(driver):
    board_title = "My Local Project"

    home = HomePage(driver)
    board = BoardPage(driver)

    home.click_create_new_board()
    home.enter_board_title(board_title)
    home.click_create_board()

    board.add_list("List 1")
    board.add_list("List 2")
    board.delete_first_list()

    time.sleep(3)
    print("\n✅ Test completed using POM.")
