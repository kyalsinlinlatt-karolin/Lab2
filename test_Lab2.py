import Lab2

def test_find_min_max():
    expected_result = [1, 6]
    test_list = [1, 6, 5, 4, 3, 2]
    result = Lab2.find_min_max(test_list)
    assert (result == expected_result)

def test_avg():
    expected_result = 3.54083333
    test_list = [1,6,4.245,3,5,2]
    result = Lab2.calc_average(test_list)
    assert(round(result,4) == round(expected_result,4))

def test_median():
    expected_result = 3.5
    test_list = [1, 2, 3, 4, 5, 6]
    result = Lab2.calc_median_temperature(test_list)
    assert(result == expected_result)