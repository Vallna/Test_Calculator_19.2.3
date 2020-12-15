import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,3,4) == 12

    #def test_multiplay_calculation_failed(self):
        #assert self.calc.multiply(self,2,2) == 5

    def test_division_calculation_correctly(self):
        assert self.calc.division(self,6,3) == 2

    def test_subtraction_calculat_correctly(self):
        assert self.calc.subtraction(self,6,3) == 3

    def test_adding_calcul_correctly(self):
        assert self.calc.adding(self,3,4) == 7

