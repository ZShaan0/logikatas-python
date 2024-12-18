import pytest
from src.simplify_directions import simplify_directions

class TestSimplifyDirections:
    def test_raises_error_when_misgiven_directions(self):
        test_directions = ["Up", "down"]
        with pytest.raises(ValueError):
            simplify_directions(test_directions)

    def test_returns_directions_when_cant_simplify(self):
        test_directions = ["SOUTH", "WEST"]
        result = simplify_directions(test_directions)
        assert result == ["SOUTH", "WEST"]

    def test_simplifes_directions_where_possible(self):
        test_directions = ["NORTH", "EAST", "SOUTH", "WEST", "NORTH", "NORTH"]
        result = simplify_directions(test_directions)
        assert result == ["NORTH", "NORTH"]

        test_directions2 = ["NORTH", "EAST", "SOUTH", "WEST", "NORTH", "NORTH", "SOUTH", "SOUTH"]
        result2 = simplify_directions(test_directions2)
        assert result2 == []

        test_directions3 = ["NORTH", "EAST", "SOUTH", "WEST", "NORTH", "NORTH", "SOUTH", "SOUTH", "EAST", "EAST", "WEST"]
        result3 = simplify_directions(test_directions3)
        assert result3 == ["EAST"]