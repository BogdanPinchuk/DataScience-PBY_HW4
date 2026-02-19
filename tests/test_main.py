import unittest
import io

from unittest import TestCase
from contextlib import redirect_stdout
from apps.main import *

if __name__ == '__main__':
    unittest.main()


class TestFormReportData(TestCase):
    def test_form_report_data(self):
        key = 'Attribute'
        value = 'Result'
        general_data = (0, 0, list())

        (actual_max_len_lf, actual_max_len_rt, actual_data_list) = form_report_data(key, value, general_data)
        expected_max_len_lf = 9
        expected_max_len_rt = 6
        expected_data_list = [(key, value)]

        self.assertEqual(expected_max_len_lf, actual_max_len_lf)
        self.assertEqual(expected_max_len_rt, actual_max_len_rt)
        self.assertEqual(expected_data_list, actual_data_list)


class TestPrintReportStr(TestCase):
    def test_print_report_string(self):
        general_data = (10, 10)
        row_data = ('Attribute', 'Result')

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_report_string(row_data, general_data)

        actual = buffer.getvalue().strip()
        expected = 'Attribute  | Result'
        self.assertEqual(expected, actual)


class TestPrintLineSplitter(TestCase):
    def test_print_line_splitter(self):
        general_data = (10, 10)

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_line_splitter(general_data)

        actual = buffer.getvalue().strip()
        expected = '-' * sum(general_data, 5)
        self.assertEqual(expected, actual)


class TestCalcCosSimilarity(TestCase):
    def test_calc_cosine_similarity(self):
        v1 = np.array([2, 1, 0, 2])
        v2 = np.array([1, 0, 1, 2])
        tolerance = 4

        actual_cos_alpha, actual_alpha_deg = calc_cosine_similarity(v1, v2)
        expected_cos_alpha = 0.8165
        expected_alpha_deg = 35.2644
        self.assertAlmostEqual(expected_cos_alpha, actual_cos_alpha, places=tolerance)
        self.assertAlmostEqual(expected_alpha_deg, actual_alpha_deg, places=tolerance)

    def test_calc_cosine_similarity_v2_len_0(self):
        v1 = np.array([2, 1, 0, 2])
        v2 = np.array([])

        # wait the exception
        with self.assertRaises(ValueError) as context:
            calc_cosine_similarity(v1, v2)

        expected = 'At least one vector has zero dimension!'
        self.assertEqual(expected, str(context.exception))

    def test_calc_cosine_similarity_v1_len_0(self):
        v1 = np.array([])
        v2 = np.array([1, 0, 1, 2])

        # wait the exception
        with self.assertRaises(ValueError) as context:
            calc_cosine_similarity(v1, v2)

        expected = 'At least one vector has zero dimension!'
        self.assertEqual(expected, str(context.exception))

    def test_calc_cosine_similarity_vs_len_0(self):
        v1 = np.array([])
        v2 = np.array([])

        # wait the exception
        with self.assertRaises(ValueError) as context:
            calc_cosine_similarity(v1, v2)

        expected = 'At least one vector has zero dimension!'
        self.assertEqual(expected, str(context.exception))

    def test_calc_cosine_similarity_vs_dif_lens(self):
        v1 = np.array([2, 1, 0])
        v2 = np.array([1, 0, 1, 2])

        # wait the exception
        with self.assertRaises(ValueError) as context:
            calc_cosine_similarity(v1, v2)

        expected = 'Vectors have different dimensions!'
        self.assertEqual(expected, str(context.exception))


class TestCompareValues(TestCase):
    def test_compare_values_lt(self):
        value1 = 1
        value2 = 2
        actual = compare_values(value1, value2)
        expected = '<'
        self.assertEqual(expected, actual)

    def test_compare_values_gt(self):
        value1 = 2
        value2 = 1
        actual = compare_values(value1, value2)
        expected = '>'
        self.assertEqual(expected, actual)

    def test_compare_values_eq(self):
        value1 = 1
        value2 = 1
        actual = compare_values(value1, value2)
        expected = '=='
        self.assertEqual(expected, actual)
