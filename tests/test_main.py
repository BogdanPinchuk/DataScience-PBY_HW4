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
