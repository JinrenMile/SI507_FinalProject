import json

class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

def movie_filter(movie, question):
    if question == "1.1 Are you looking for a movie for family with kids?":
        return movie["rated"] in ["G", "PG", "PG-13"]
    elif question == "1.2 Are you looking for a movie over 2 hours?":
        return int(movie["runtime"].split()[0][0]) >= 2
    elif question == "1.3 Are you looking for a movie before 2000?":
        return int(movie["year"]) < 2000
    return False

def build_tree(movies, questions):
    # If there is no question left, return the remaining movies
    if len(questions) == 0:
        return movies
    # Start from the first question
    question = questions[0]
    yes_movies = [movie for movie in movies if movie_filter(movie, question)]
    no_movies = [movie for movie in movies if not movie_filter(movie, question)]
    # Build a recursion
    left = build_tree(yes_movies, questions[1:])
    right = build_tree(no_movies, questions[1:])

    return Node(question, left, right)

def tree_to_dict(node):
    if isinstance(node, list):
        return {'movies': [{'number': movie['number'], 'title': movie['title'], 'year': movie['year'], 'runtime': movie['runtime'], 'rated': movie['rated'], 'rating': movie['rating'], 'vote_count': movie['vote_count'], 'link': movie['link']} for movie in node]}
    if node is None:
        return None
    return {
        'question': node.question,
        'yes_branch': tree_to_dict(node.yes),
        'no_branch': tree_to_dict(node.no)
    }

# Load movies data
with open('movie_data.json', 'r') as f:
    data = json.load(f)

questions = [
    "1.1 Are you looking for a movie for family with kids?",
    "1.2 Are you looking for a movie over 2 hours?",
    "1.3 Are you looking for a movie before 2000?"
]

root = build_tree(data, questions)
tree_dict = tree_to_dict(root)

with open('tree.json', 'w') as file:
    json.dump(tree_dict, file, indent=4)