import main
import io
import sys

def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    numbers, total = main.main()
    sys.stdout = sys.__stdout__

    lines = captureOut.getvalue().split('\n')
    
    # Check if there are any numbers outside the range (0 < number <= 100)
    not_gt0_lt100 = [v for v in numbers if not (0 < v <= 100)]
    assert not_gt0_lt100 == [], 'Random values should be >0 and <=100'

    # Check if the total matches the sum of the numbers (including all numbers)
    assert total == sum(numbers), 'Total is not valid'

    # Check the printed output format (optional, if needed)
    assert 'The random values are' in lines[0], 'Output does not contain the correct string for random values'
    assert 'The total is' in lines[1], 'Output does not contain the correct string for total'

# Run the test
test_main_1()
