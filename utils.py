import calendar
import logging

import requests
from constants import HEADERS, SUCCESS, TOP_FOR_DAY, YEAR_PROMPT, MONTH_PROMPT, DAY_PROMPT, VIEWS_PER_DAY, \
    WEEK_MONTH_PROMPT, INVALID_DATE_ERROR, VIEWS_PER_MONTH
import datetime


def get_date(selection):
    """
    Obtains dates depending on flow selection
    :param selection: integer corresponding to
        1) top X amount of viewed articles
        2) view count of specific article for a week/month
        3) retrieve day of the month, where an article got the most views
    :return: date
    """
    try:
        year_input = input(YEAR_PROMPT)
        month_input = input(MONTH_PROMPT)
        day_input = None
        match selection:
            case '1':
                day_input = input(DAY_PROMPT)
            case '2':
                day_input = input(WEEK_MONTH_PROMPT)
            case '3':
                # only year
                day_input = '1'

        validate_date(year_input, month_input, day_input)
        return year_input, month_input, day_input
    except Exception as e:
        raise e


def get(url, headers=HEADERS):
    """
    Executes get request with passed in url and headers
    :param url: url as string to GET
    :return: json response if
    """
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == SUCCESS:
            return response.json()
        else:
            print("Error with status code: " + str(response.status_code))
            raise Exception(response.reason)
    except Exception as exception:
        raise Exception(exception)


def validate_date(year, month, day):
    """
    Handles invalid dates, both in terms of formatting and out invalid value (i.e. 50 for month or 79 for day)
    :param year:
    :param month:
    :param day:
    :return:
    """
    if year.isdigit() and month.isdigit() and (day.isdigit() or day == 'all-days'):
        try:
            if day != 'all-days':
                # throws an exception if date is invalid
                datetime.datetime(year=int(year), month=int(month), day=int(day))
            else:
                # just need to worry about year/month in case of all-days
                datetime.datetime(year=int(year), month=int(month), day=1)
            return True
        except Exception as exception:
            logging.error(exception)
            raise ValueError

    logging.error(INVALID_DATE_ERROR)
    raise TypeError


def set_date(year, month, day):
    """
    Takes in valid date and returns formatted relative URL as a string
    :param year: string describing year
    :param month: string describing month
    :param day: string describing day
    :return: formatted relative URL
    """

    return TOP_FOR_DAY.format(year, month, day)


def set_dates(article, start_date, end_date):
    """
    Takes in article name and two validated dates and returns formatted relative URL as a string
    :param article:
    :param start_date:
    :param end_date:
    :return:
    """

    return VIEWS_PER_DAY.format(article, start_date, end_date)


def set_year(article, start_date, end_date):
    """
    Takes in article name and two validated dates and returns formatted relative URL as a string
    :param article:
    :param start_date:
    :param end_date:
    :return:
    """
    return VIEWS_PER_MONTH.format(article, start_date, end_date)


def get_week_range(year, month, day):
    """
    Given a valid date, returns a list of dates corresponding to the week, defined as Monday, Tuesday, ..., Sunday
    :param year:
    :param month:
    :param day:
    :return: Returns list of 7 dates as tuple (year, month, day)
    """
    week_number = datetime.date(int(year), int(month), int(day)).isocalendar().week

    # added adjustment due to some limitations with iso-gregorian conversion
    if datetime.date(int(year), 12, 31).isocalendar().week != 53:
        week_number += 1

    start_date = datetime.datetime.strptime(f'{year}-W{int(week_number)-1}-1', "%Y-W%W-%w").date()
    dates = [start_date + datetime.timedelta(days=d) for d in range(7)]
    formatted_dates = []
    # formatting for proper url creation
    for index, date in enumerate(dates):
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day

        formatted_dates.append((year, month, day))

    return formatted_dates


def get_month_range(year, month):
    """
    Given a month and year, returns a list of dates valid for the entire month
    :param year:
    :param month:
    :return:
    """
    num_days = calendar.monthrange(int(year), int(month))[1]
    month_range = []

    for day in range(1, num_days + 1):
        if day + 1 < 11:
            day = "0" + str(day)
        else:
            day = str(day)
        month_range.append((year, month, day))

    return month_range

