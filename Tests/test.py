import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
         with pytest.raises(ZeroDivisionError):
             self.calc.division(1, 0)

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_substraction_success(self):
        assert self.calc.substraction(self, 1, 1) == 0

    def teardown(self):
        print("Выполнение метода Teardown")

