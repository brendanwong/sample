import logging
from constants import PROMPT, TRY_AGAIN, PYTHON_ERROR
from wiki_wrapper.articles import top_articles_entry
from wiki_wrapper.view_counts import view_counts_entry


def entry():
    """
    Entry point to run the program
    :return:
    """
    choice = None
    print(PROMPT, end="")

    while choice is None:
        choice = input()
        if choice.isdigit() is False or int(choice) > 3 or int(choice) < 1:
            choice = None
        if choice is None:
            print(TRY_AGAIN, end="")

    try:
        match choice:
            # top articles
            case '1':
                result = top_articles_entry(choice)
            # get_view_counts/get_most_views
            case _:
                result = view_counts_entry(choice)

        if result:
            print(result)
    except Exception as e:
        logging.error(PYTHON_ERROR)
        logging.error(e)


entry()
