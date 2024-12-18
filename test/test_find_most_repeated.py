from src.find_most_repeated import find_most_repeated

class TestFindMostRepeated:
    def test_returns_empty_result_if_passed_empty_list(self):
        test_list = []
        result = find_most_repeated(test_list)
        assert result == {'elements': [], 'repeats': None}
    
    def test_returns_empty_result_if_no_repeats(self):
        test_list = ["hi"]
        result = find_most_repeated(test_list)
        assert result == {'elements': [], 'repeats': None}

    def test_returns_single_item_list_with_count_2(self):
        test_list = ["hi", "hi"]
        result = find_most_repeated(test_list)
        assert result == {'elements': ['hi'], 'repeats': 2}
    
    def test_returns_multiple_repeating_items(self):
        test_list = ["foo", "foo", 1, 2, 3, "bar", 2, 3, 4, "bar", "bar", "foo"]
        result = find_most_repeated(test_list)
        assert result == {'elements': sorted(["foo", "bar"]), "repeats": 3}

    def test_purity_does_not_mutate_parameter(self):
        test_list = ["hi", "hi"]
        result = find_most_repeated(test_list)
        assert test_list == ["hi", "hi"]