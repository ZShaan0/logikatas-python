from src.sub_sequence_sum import sub_sequence_sum

class TestSubSequenceSum:
    def test_empty_sequence_returns_zero(self):
        test_seq = []
        result = sub_sequence_sum(test_seq)
        assert result == 0
    
    def test_sequence_of_positive_ints_returns_sum(self):
        test_seq = [5, 1, 2, 3, 4]
        result = sub_sequence_sum(test_seq)
        assert result == 15
    
    def test_sequence_negative_ints_returns_zero(self):
        test_seq = [-2, -3, -4]
        result = sub_sequence_sum(test_seq)
        assert result == 0

    def test_positive_and_negative_ints_excludes_negatives(self):
        test_seq = [5, 1, 2, -3, -4]
        result = sub_sequence_sum(test_seq)
        assert result == 8
    
    def test_positive_and_negative_ints_mixed_order_sums_subsequence(self):
        test_seq = [-2, 5, 1, -1, 2, -3]
        result = sub_sequence_sum(test_seq)
        assert result == 7
