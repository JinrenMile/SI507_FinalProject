from bs4 import BeautifulSoup
import pprint
import re
import json
import requests
pp = pprint.PrettyPrinter(indent=4)

# Step 1 IMDB
# scrape the website of IMDB top 250 movies
f = open("IMDB_top_250.html")
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')

# search by tag
all_list_items = soup.find_all('div', class_= "ipc-metadata-list-summary-item__tc")
# pp.pprint(all_list_items)
# print(all_list_items[0])

# get title of 250 movies
movie_title = []
for x in all_list_items:
    # pp.pprint(x)
    title = x.find('h3', class_="ipc-title__text")
    titletext = title.text
    # print(titletext.split('. ')[1])
    movie_title.append(titletext.split('. ')[1])

# get year, runtime, rated of 250 movies
movie_year = []
movie_runtime = []
movie_rated = []
for x in all_list_items:
    divs = x.find_all('div', class_="sc-479faa3c-7 jXgjdT cli-title-metadata")
    for div in divs:
        span_contents = [span.get_text() for span in div.find_all('span')]
        for div in divs:
            span_contents = [span.get_text() for span in div.find_all('span')]
            if len(span_contents) > 0:
                movie_year.append(span_contents[0])
            else:
                movie_year.append('N/A')
            if len(span_contents) > 1:
                movie_runtime.append(span_contents[1])
            else:
                movie_runtime.append('N/A')
            if len(span_contents) > 2:
                movie_rated.append(span_contents[2])
            else:
                movie_rated.append('N/A')

# get rating number of 250 movies
movie_raing = []
for x in all_list_items:
    divs = x.find_all('div', class_="sc-e3e7b191-0 jlKVfJ sc-479faa3c-2 eUIqbq cli-ratings-container")
    for div in divs:
        rating_span = div.select_one('span[aria-label^="IMDb rating:"]')
        if rating_span:
            rating = re.findall(r'([0-9]*\.[0-9]+|[0-9]+)', rating_span['aria-label'])[0]
            movie_raing.append(rating)
        else:
            movie_raing.append("N/A")

# get vote counts for rating
vote_counts = []
for x in all_list_items:
    count = x.find('span', class_="ipc-rating-star--voteCount")
    counttext = count.text.strip('()').strip('\xa0(')
    vote_counts.append(counttext)

# get links for more details of movies
movie_link = []
for x in all_list_items:
    links = x.find_all('a', class_="ipc-title-link-wrapper")
    for link in links:
        movie_link.append('https://m.imdb.com' + link['href'])

# cache the IMDB top 250 movies into json file
IMDB_top_250_movies = []
for i in range(250):
    movie = {
        'title': movie_title[i],
        'year': movie_year[i],
        'runtime': movie_runtime[i],
        'rated': movie_rated[i],
        'rating': float(movie_raing[i]),
        'vote_count': vote_counts[i],
        'link': movie_link[i]
    }
    IMDB_top_250_movies.append(movie)

with open('IMDB_top_250_movies.json', 'w') as json_file:
    json.dump(IMDB_top_250_movies, json_file, indent=4)


# Step 2 TMDB
# access the Web API of TMDB
TMDB_API_KEY = '2baa5e3caadaebb6ad7ede0a204e9f01'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=2baa5e3caadaebb6ad7ede0a204e9f01'

response = requests.get(url)
result = response.json()
popular_movie = result["results"]
# pp.pprint(popular_movie)

# with open('popular_movie.json', 'w') as json_file:
#     json.dump(popular_movie, json_file, indent=4)

# scrape the website for the movie links
f = open("TMDB_popular.html")
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')

all_list_items = soup.find_all('div', class_= "wrapper")
top_popular = all_list_items[:20]

# get links for more details of movies
movie_link = []
for x in top_popular:
    links = x.find_all('a')
    for link in links:
        movie_link.append('https://www.themoviedb.org' + link['href'])

with open('popular_movie.json', 'r') as f:
    top_20 = json.load(f)

# cache the TMDB popular 20 movies into json file
TMDB_popular_20_movies = []
for i in range(20):
    movie = top_20[i]
    new = {
        "title": movie["title"],
        "year": movie["release_date"].split('-')[0],
        "runtime": movie["runtime"],
        "rated": movie["rated"],
        "rating": round(movie["vote_average"], 1),
        "vote_count": movie["vote_count"],
        "link": movie_link[i]
    }
    TMDB_popular_20_movies.append(new)

with open('TMDB_popular_20_movies.json', 'w') as json_file:
    json.dump(TMDB_popular_20_movies, json_file, indent=4)


# Step 3 Combine and Cache the 2 Movie Data
movie_data = IMDB_top_250_movies + TMDB_popular_20_movies
with open('movie_data.json', 'w') as json_file:
    json.dump(movie_data, json_file, indent=4)
