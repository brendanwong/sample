BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/"
TOP_FOR_DAY = "top/en.wikipedia/all-access/{}/{}/{}"
VIEWS_PER_DAY = 'per-article/en.wikipedia.org/all-access/all-agents/{}/daily/{}/{}'
VIEWS_PER_MONTH = 'per-article/en.wikipedia.org/all-access/all-agents/{}/monthly/{}/{}'
YEAR_START_TEMPLATE = '{}010100'
YEAR_END_TEMPLATE = '{}123100'
HEADERS = {'User-Agent': 'GrowTherapy'}
SUCCESS = 200
TOP_ARTICLES_CUTOFF = 10
PROMPT = """Welcome to the Wikipedia wrapper API
Select from the following functionalities:
    1) Retrieve a list of the most viewed articles (week or month)
    2) Give an article title and get the view count for a specific week or month
    3) Give an article title and get the day of the month it got the most views 
Please enter (1-3): """
TRY_AGAIN = "Enter (1-3): "
YEAR_PROMPT = 'Enter year (YYYY): '
MONTH_PROMPT = 'Enter month (MM): '
DAY_PROMPT = 'Enter day (DD) or \'all-days\' for the entire month: '
WEEK_MONTH_PROMPT = 'Enter day (DD) to specify its week or \'all-days\' for the entire month: '
WEEK_PROMPT = 'Would you like to see the top articles for the week of {}-{}-{}? (Y/N): '
ARTICLE_TITLE_PROMPT = 'Please enter the exact article title: '
WEEK_OR_MONTH_PROMPT = 'Enter \'week\' or \'month\' to specify the time frame: '
INVALID_DATE_ERROR = "Error with input, please enter valid 4 digit year, valid 2 digit month, and valid 2 digit day or \'all-days\'"
PYTHON_ERROR = 'This script has possibly failed because it uses the match syntax present from Python 3.10 and above, please install and make sure it\'s being used'