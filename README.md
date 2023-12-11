# SI507 Final Project
This is the Final Project of SI 507, it is a program gives users recommendations to help them find a movie according to their requirements.
Movie data source: <br>
**IMDB Top 250 Movies** (Web Scraping) <br>
**TMDB Popular 20 Movies** (Web API)

### Required Python Package
BeautifulSoup <br>
json <br>
pprint <br>
re <br>
requests <br>
webbrowser 

### Instruction for Web API
For the Web API, I have put my API key of TMDB in CachingData.py, with the URL I used for collecting the popular 20 movies in TMDB. They look like: <br>
TMDB_API_KEY = ‘…’ <br>
url = ‘…’

### Data Structure
**STEP 1: One 3-level Tree**
It is the first step of this system, knowing the preference of users for the movies they may want.
Level 1: Are you looking for a movie for family with kids?
Considering some movies may not suitable for kids under 13, the rated of movie should be the very first consideration when picking a movie. To conduct this step, I will use the attribute “rated” from the final data. Movies with rated value of G, PG, and PG-13 will go to the answer “Yes”, and others will go to the answer “No”.



