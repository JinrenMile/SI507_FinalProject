# SI507 Final Project
This is the Final Project of SI 507, it is a Movie Recommendation System, giving users suggestions to help them find a movie according to their requirements.
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
**STEP 1: One 3-level Tree** to know the preference of users for the movies they may want. <br>

Level 1: Are you looking for a movie for family with kids? <br>
Considering some movies may not suitable for kids under 13, the rated of movie should be the very first consideration when picking a movie. To conduct this step, I will use the attribute **“rated”** from the final data. Movies with rated value of G, PG, and PG-13 will go to the answer “yes”, and others will go to the answer “no”. <br>

Level 2: Are you looking for a movie over 2 hours? <br>
For time consideration, some users prefer long movies but others may not have enough time. To conduct this step, I will use the attribute **“runtime”** from the final data. Movies with runtime over 2 hours will go to the answer “yes”, and those with 2 hours will go to the answer “no”. <br>

Level 3: Are you looking for a movie before 2000? <br>
This question is just for some consideration of personal preference. Some users may prefer some old movies, but others may enjoy the updated ones. To conduct this step, I will use the attribute **“year”** from the final data. Movies released before 2000 will go to the answer “yes”, and those after 2000 will go to the answer “no”.

**STEP 2:** “Which movie you want more information?” <br>
After STEP 1, there will be a list of movies with assigned number, and users can type the number of the movie they are interested in for further step. They can also type “exit” to exit the system. <br>

**STEP 3:** “Do you want to see the rating of the movie?” <br>
If users type “yes”, it will show both rating and vote count of the movie they chose in STEP 2. They can also type “no” to exit the system. <br>

**STEP 4:** “Do you want to see the link for more details?” <br>
If users type “yes”, it will show the link and web of the movie they chose in STEP 2. They can also type “no” to exit the system. <br>





