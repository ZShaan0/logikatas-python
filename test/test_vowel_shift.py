from src.vowel_shift import vowel_shift

class TestVowelShift:
    def test_works_when_no_shift_specified(self):
        test_string = "foo"
        result = vowel_shift(test_string, 0)
        assert result == 'foo'
    
    def test_works_when_shift_less_than_length_of_string(self):
        test_string = "foo"
        result = vowel_shift(test_string, 1)
        assert result == 'foo'

        test_string2 = "hello"
        result2 = vowel_shift(test_string2, 1)
        assert result2 == 'holle'

        test_string3 = 'star nosed mole'
        result3 = vowel_shift(test_string3, 2)
        assert result3 == 'stor nesad mole'

    def test_works_when_shift_equal_to_num_of_vowels(self):
        test_string = 'funnily enough'
        result = vowel_shift(test_string, 5)
        assert result == 'funnily enough'

    def test_works_when_shift_greater_than_length_of_string(self):
        test_string = 'funnily enough'
        result = vowel_shift(test_string, 6)
        assert result == 'funnuly ineogh'