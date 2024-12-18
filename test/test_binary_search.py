from src.binary_search import binary_search

class TestBinarySearch:
    def test_returns_minus_one_when_not_found(self):
        test_list = [1,2,3,4,5,6]

        result = binary_search(test_list, 8)
        assert result == -1

        result2 = binary_search(test_list, 0)
        assert result2 == -1

    def test_returns_index_when_target_at_start_or_end_of_list(self):
        test_list = [1,2,3,4,5,6]

        result = binary_search(test_list, 1)
        assert result == 0

        result2 = binary_search(test_list, 6)
        assert result2 == 5
    
    def test_returns_index_when_target_in_list(self):
        test_list = [1,2,3,4,5,6,7,10,100]

        result = binary_search(test_list, 5)
        assert result == 4

        result2 = binary_search(test_list, 4)
        assert result2 == 3

        result3 = binary_search(test_list, 10)
        assert result3 == 7