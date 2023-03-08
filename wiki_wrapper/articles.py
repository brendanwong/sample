import logging

from constants import *
from utils import get, set_date, get_date, get_week_range


def get_articles_for_day(year, month, day):
    """
    Obtains clean relative url for a day and tries to execute. Returns the articles if successful
    :param year: string describing year
    :param month: string describing month
    :param day: string describing day
    :return: Ordered list of top 1k articles for a particular day or month
    """
    try:
        relative_url = set_date(year, month, day)
        url = BASE_URL + relative_url
        response = get(url, HEADERS)
        return response['items'][0]['articles']

    except Exception as exception:
        raise exception


def aggregate_article_counts(dates):
    """
    Obtains a map, relating name to its view counts for a particular time frame
    :param dates:
    :return:
    """
    top_articles = {}
    for date in dates:
        year, month, day = date[0], date[1], date[2]

        top_daily_articles = get_articles_for_day(year, month, day)
        for article in top_daily_articles:
            if article['article'] in top_articles:
                top_articles[article['article']] += article['views']
            else:
                top_articles[article['article']] = article['views']

    return top_articles


def top_articles_entry(choice):
    """
    This is the entry point for the top articles flow where you can retrieve a list of the most viewed articles for a
    month, week, or day! It is currently truncated to a maximum of the top 10 for readability, however this is a
    constant and can be changed via the variable in constants.py
    """
    try:
        year_input, month_input, day_input = get_date(choice)

        get_week = None
        if day_input.isdigit():
            while get_week is None:
                week_input = input(WEEK_PROMPT.format(year_input, month_input, day_input))
                if week_input == 'Y' or week_input == 'y':
                    get_week = True
                elif week_input == 'N' or week_input == 'n':
                    get_week = False

        if get_week:
            dates = get_week_range(year_input, month_input, day_input)

            top_weekly_articles = aggregate_article_counts(dates)
            sorted_weekly_articles = sorted(top_weekly_articles.items(), key=lambda x:x[1], reverse=True)

            logging.info('The top articles for {}-{}-{}'.format(dates[0][0], dates[0][1], dates[0][2]) + " " + 'to {}-{}-{}'.format(dates[-1][0], dates[-1][1], dates[-1][2]) + " is:\n")

            for i in range(TOP_ARTICLES_CUTOFF):
                logging.info(str(sorted_weekly_articles[i][0]) + " with " + str(sorted_weekly_articles[i][1]) + " views\n")

            return sorted_weekly_articles[:TOP_ARTICLES_CUTOFF]
        else:
            top_weekly_articles = get_articles_for_day(year_input, month_input, day_input)

            if day_input == 'all-days':
                logging.info('The top {} articles for {}-{} are: '.format(TOP_ARTICLES_CUTOFF, year_input, month_input))
            else:
                logging.info('The top {} articles for {}-{}-{} are: '.format(TOP_ARTICLES_CUTOFF, year_input, month_input, day_input))

            for i in range(TOP_ARTICLES_CUTOFF):
                logging.info(top_weekly_articles[i]['article'] + " with " + str(top_weekly_articles[i]['views']) + " views\n")

            return top_weekly_articles[:TOP_ARTICLES_CUTOFF]
    except Exception as exception:
        raise exception






