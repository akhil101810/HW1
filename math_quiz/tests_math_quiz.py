import unittest
from math_quiz import rand_int, rand_optr, do_operation


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_optr(self):
        # test if the operator is +,-,*
        operators=['+','-','*']
        for _ in range(1000): #Test for large number
            r_optr = rand_optr()
            self.assertIn(r_optr,operators)

    def test_do_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 2, '*', '4 * 2', 8)

            ]
            #check if expected answer is same as from code
            for num1, num2, optr, expected_problem, expected_answer in test_cases:
                problem, answer = do_operation(num1, num2, optr)
                self.assertEqual(problem,expected_problem)
                self.assertEqual(answer,expected_answer)

if __name__ == "__main__":
    unittest.main()
