from app.calculator import Calculator


class TestCalculator:
    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(5, 3)
        assert result == 15, "Multiplication test failed"

    def test_division(self):
        calculator = Calculator()
        result = calculator.division(10, 2)
        assert result == 5, "Division test failed"

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(8, 3)
        assert result == 5, "Subtraction test failed"

    def test_adding(self):
        calculator = Calculator()
        result = calculator.adding(2, 3)
        assert result == 5, "Adding test failed"
