from screen_time import too_much_screen_time

def test_screen_time():
    assert too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) == False
    assert too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) == False
    assert too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) == False
    assert too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) == True
    assert too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) == True
    assert too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) == True
    assert too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) == True
