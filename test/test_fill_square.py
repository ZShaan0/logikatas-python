from src.fill_square import fill_square

class TestFillSquare:
    def test_pads_sublists_when_num_of_sublists_equals_length_of_max_row(self):
        test_list = [[1, 2, 3], [1, 2], [1]]
        result = fill_square(test_list)
        assert result == [[1, 2, 3],
                        [1, 2, None],
                        [1, None, None]]
    
    def test_pads_sublists_when_num_of_sublists_less_than_length_of_max_row(self):
        test_list = [[1, 2, 3], [1, 2, 3, 4, 5, 6], [1]]
        result = fill_square(test_list)
        assert result == [[1, 2, 3, None, None, None],
                          [1, 2, 3, 4, 5, 6],
                          [1, None, None, None, None, None],
                          [None, None, None, None, None, None],
                          [None, None, None, None, None, None],
                          [None, None, None, None, None, None]]
    
    def test_pads_sublists_when_num_of_sublists_more_than_length_of_max_row(self):
        test_list = [[1, 2, 3], [1, 2, 3], [1], [], [1, 2, 3], [1]]
        result = fill_square(test_list)
        assert result == [[1, 2, 3, None, None, None],
                          [1, 2, 3, None, None, None],
                          [1, None, None, None, None, None],
                          [None, None, None, None, None, None],
                          [1, 2, 3, None, None, None],
                          [1, None, None, None, None, None]]