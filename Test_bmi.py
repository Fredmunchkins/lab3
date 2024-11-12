from Lab2.bmi import calculate_bmi

def test_underweight():
    # Test for BMI value that should be classified as "Under Weight"
    assert calculate_bmi(1.8, 50)

def test_normal_weight():
    # Test for BMI value that should be classified as "Normal Weight"
    assert calculate_bmi(1.75, 70) 

def test_overweight():
    # Test for BMI value that should be classified as "Over Weight"
    assert calculate_bmi(1.6, 80) 