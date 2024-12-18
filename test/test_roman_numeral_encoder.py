from src.roman_numeral_encoder import roman_numeral_encoder

class TestRomanNumeralEncoder:
    def test_single_digit_nums(self):

        test_num = 3
        result = roman_numeral_encoder(test_num)
        assert result == 'III'

        test_num2 = 4
        result2 = roman_numeral_encoder(test_num2)
        assert result2 == 'IV'

        test_num3 = 5
        result3 = roman_numeral_encoder(test_num3)
        assert result3 == 'V'

        test_num4 = 9
        result4 = roman_numeral_encoder(test_num4)
        assert result4 == 'IX'

        test_num5 = 10
        result5 = roman_numeral_encoder(test_num5)
        assert result5 == 'X'

    def test_multiple_digit_nums(self):

        test_num = 16
        result = roman_numeral_encoder(test_num)
        assert result == 'XVI'

        test_num2 = 60
        result2 = roman_numeral_encoder(test_num2)
        assert result2 == 'LX'

        test_num3 = 75
        result3 = roman_numeral_encoder(test_num3)
        assert result3 == 'LXXV'

        test_num4 = 91
        result4 = roman_numeral_encoder(test_num4)
        assert result4 == 'XCI'

        test_num5 = 812
        result5 = roman_numeral_encoder(test_num5)
        assert result5 == 'DCCCXII'

        test_num6 = 949
        result6 = roman_numeral_encoder(test_num6)
        assert result6 == 'CMXLIX'

        test_num7 = 1111
        result7 = roman_numeral_encoder(test_num7)
        assert result7 == 'MCXI'

        test_num8 = 1994
        result8 = roman_numeral_encoder(test_num8)
        assert result8 == 'MCMXCIV'