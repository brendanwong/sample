from unittest import TestCase
from utils import validate_date, set_date, set_dates, set_year, get_week_range, get_month_range


class Test(TestCase):
    def test_validate_date(self):

        # Should return true for a valid date
        assert validate_date('2020', '05', '17')
        assert validate_date('1990', '01', 'all-days')

        # Should raise an error for invalid date
        self.assertRaises(ValueError, validate_date, '42', '42', '42')
        self.assertRaises(TypeError, validate_date, 'wrong', 'format', 'put')

    def test_set_date(self):
        # Should take in a valid date and return formatted relative url
        assert set_date('2020', '05', '17') == "top/en.wikipedia/all-access/2020/05/17"
        assert set_date('1905', '01', '01') == "top/en.wikipedia/all-access/1905/01/01"

    def test_set_dates(self):
        # Should take in a valid date and return formatted relative url
        assert set_dates('Michael_Jordan', '20200511', '20200517') == 'per-article/en.wikipedia.org/all-access/all-agents/Michael_Jordan/daily/20200511/20200517'
        # assert set_dates('')

    def test_set_year(self):
        # Should take in a valid date and return formatted relative url
        assert set_year('Michael_Jordan', '20200511', '20200517') == 'per-article/en.wikipedia.org/all-access/all-agents/Michael_Jordan/monthly/20200511/20200517'

    def test_get_week_range(self):
        # Given valid date, should return a list of tuples (year, month, day) containing the days of the week
        assert get_week_range('2020', '05', '17') == [('2020', '05', '11'), ('2020', '05', '12'), ('2020', '05', '13'),
                                                      ('2020', '05', '14'), ('2020', '05', '15'), ('2020', '05', '16'),
                                                      ('2020', '05', '17')]
        assert get_week_range('2020', '05', '11') == [('2020', '05', '11'), ('2020', '05', '12'), ('2020', '05', '13'),
                                                      ('2020', '05', '14'), ('2020', '05', '15'), ('2020', '05', '16'),
                                                      ('2020', '05', '17')]
        assert get_week_range('2020', '05', '15') == [('2020', '05', '11'), ('2020', '05', '12'), ('2020', '05', '13'),
                                                      ('2020', '05', '14'), ('2020', '05', '15'), ('2020', '05', '16'),
                                                      ('2020', '05', '17')]

    def test_get_month_range(self):
        # Given a valid month /year, should return a list of tuples (year, month, day) containing all days of the month
        assert get_month_range('2020', '05') == [('2020', '05', '01'), ('2020', '05', '02'), ('2020', '05', '03'), ('2020', '05', '04'), ('2020', '05', '05'), ('2020', '05', '06'), ('2020', '05', '07'), ('2020', '05', '08'), ('2020', '05', '09'), ('2020', '05', '10'), ('2020', '05', '11'), ('2020', '05', '12'), ('2020', '05', '13'), ('2020', '05', '14'), ('2020', '05', '15'), ('2020', '05', '16'), ('2020', '05', '17'), ('2020', '05', '18'), ('2020', '05', '19'), ('2020', '05', '20'), ('2020', '05', '21'), ('2020', '05', '22'), ('2020', '05', '23'), ('2020', '05', '24'), ('2020', '05', '25'), ('2020', '05', '26'), ('2020', '05', '27'), ('2020', '05', '28'), ('2020', '05', '29'), ('2020', '05', '30'), ('2020', '05', '31')]
