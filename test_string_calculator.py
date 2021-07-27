import string_calculator

def test_correct_params_expect_OP_NUM_NUM():
    #arrange
    cut = string_calculator.StringCalculator()
    inputVal = "+,3,4"
    expResult = ["OPERATOR", "NUMBER", "NUMBER"]

    # ACT
    result = cut.parse(inputVal)

    # Assert
    assert result == expResult