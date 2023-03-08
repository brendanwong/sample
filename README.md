# Wikipedia Wrapper API

## Overall Logic
### 1. Most viewed articles per month/week/day - `articles.py`
This flow handles the scenario where the user wants to retrieve a list of the most viewed articles per amount of time.
It utilizes the endpoint: `https://wikimedia.org/api/rest_v1/metrics/pageviews/top/{project}/all-access/{YYYY}/{MM}/{DD}`
Given a date, it lets user time frame and then the date range is then generated. For each date within the range, the articles 
and their associated view counts are put into a hash table. This is later sorted and the top `TOP_ARTICLES_CUTOFF` items 
are listed for the time frame. This constant can be changed within `constants.py`

### 2. View counts/most views given an article - `view-counts.py`
This flow handles the second and third requirement of the API, when given an article, should be able to get the view count 
of that specific article for a week or a month, and retrieves the day of the month where an article gets the most views.
Utilizing similar utility functions, the time frame is and is used in conjunction with endpoint:
`https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/all-access/all-agents/{article}/daily/{YYYYMMDD}/{YYYYMMDD}`
to generate a list of view counts for a week. 
`https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/all-access/all-agents/{article}/monthly/{YYYYMMDD}/{YYYYMMDD}`
is used to generate a list of view counts for all the months given a year.

### Other notes
* much of the logic used by either flow are handle by shared utility functions in `utils.py`
* I've defined a week as starting from Monday to Sunday
  * given a date i.e. Wednesday, would return all days from the prior Monday, to the coming Sunday
* bad requests are handled throughout,
 either prompting the user to enter another input, or bubbling errors up to finally be caught in the base 
entry function
* testing for external APIs have not been included since the returns are extremely large, however in a real life scenario,
I'd mock some responses in conjunction with real ones
  

## Dependencies
* Python 3.10 or above 
* requests 2.28