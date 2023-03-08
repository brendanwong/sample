import logging

from constants import *
from utils import get_date, get_week_range, get, set_dates, get_month_range


def get_daily_article_views(article, date_range):
    """
    This function sets the date range and gets the daily views per article
    :param date_range:
    :param article: string representing exact article title
    :return:
    """
    try:
        # formatting for URL
        start_date = date_range[0][0] + date_range[0][1] + date_range[0][2]
        end_date = date_range[1][0] + date_range[1][1] + date_range[1][2]

        relative_url = set_dates(article, start_date, end_date)
        url = BASE_URL + relative_url
        response = get(url, HEADERS)
        return response['items']
    except Exception as exception:
        raise exception


def view_counts_entry(choice):
    """
    This is the entry point and output builder for flows 2 and 3, where you can retrieve the counts of a specific
    article, and retrieve the day of the month, where an article got the most views.
    :return: string describing the result
    """
    try:
        article_input = input(ARTICLE_TITLE_PROMPT)
        year_input, month_input, day_input = get_date(choice)

        if choice == '3' or day_input == 'all-days':
            # view counts for the entire month, or choice 3 was chosen
            time = get_month_range(year_input, month_input)
        else:
            # view counts for a specific week
            time = get_week_range(year_input, month_input, day_input)

        time_range = [time[0], time[-1]]
        logging.info('Time range of: ' + str(time[0]) + ' to ' + str(time[-1]))

        article_views = get_daily_article_views(article_input, time_range)

        if choice == '2':
            total = 0
            for index, day in enumerate(time):
                logging.info(article_views[index])
                total += article_views[index]['views']
            logging.info("\nThe total views for {} to {} are: {}".format(time_range[0], time_range[1], total))
            return total
        else:
            # choice 3, get the day of month when an article given most views
            article_views = [(article['timestamp'], article['views']) for article in article_views]
            article_views = sorted(article_views, key=lambda x: x[1], reverse=True)
            logging.info("The top view counts for {} in {}-{} is: {} on day {}".format(article_input,
                        year_input, month_input, article_views[0][1], article_views[0][0][-4:-2]))
            return article_views[0][0][-4:-2]

    except Exception as exception:
        raise exception



