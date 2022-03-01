import pytest
import os

#region Basic
@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

#endregion

#region aggrigation
# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]
#endregion

#region fixtures parametrize
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9",54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
#endregion

#region mocker
def sum(a, b):
   return a + b

def test_sum_original(mocker):
   assert sum(2, 3) == 5

def test_sum1(mocker):
   mocker.patch(__name__ + ".sum", return_value=9)
   assert sum(2, 3) == 9


def test_sum2(mocker):
   def crazy_sum(a, b):
      return b + b

   mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
   assert sum(2, 3) == 6
#endregion

#region MonkyPatch
class DummyExample():
    def test_value_based_on_current_dir(self)->int:
        current_dir=os.getcwd()

        return 1 if current_dir.endswith("MyGreatExample") else 42


@pytest.fixture()
def get_dir_for_test(monkeypatch):
    def mock_getcwd():
        return '/data/user/MyGreatExample'
    monkeypatch.setattr(os, 'getcwd', mock_getcwd)

def test_day_1(get_dir_for_test):
    example=DummyExample()
    assert (example.test_value_based_on_current_dir()==1)
#endregion