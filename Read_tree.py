import json
import webbrowser

## STEP 1: Read Tree
def load_tree_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def display_tree(node):
    # Navigate through the tree based on user input
    while 'question' in node:
        response = input(node['question'] + " (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            node = node['yes_branch']
        elif response in ['no', 'n']:
            node = node['no_branch']
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue
    if 'movies' in node:
        return node['movies']


## STEP 2: Continue asking for more information
def get_movie_info(movies):
    while True:
        user_input = input(f"\n2. Which movie do you want more information about? Enter the number or type 'exit' to exit: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting. Thank you!")
            return None

        if user_input.isdigit() and int(user_input) in [movie['number'] for movie in movies]:
            selected_movie = next(movie for movie in movies if movie['number'] == int(user_input))
            print(f"Your choice is: {selected_movie['title']}")
            return selected_movie
        else:
            print("Invalid input. Please enter a valid movie number or 'exit'.")
            continue


## STEP 3: Continue showing the rating of the movie
def show_movie_rating(selected_movie):
    while True:
        user_input = input(f"\n3. Do you want to see the rating of the movie? (yes/no): ").strip().lower()

        if user_input in ['no', 'n']:
            print("Exiting. Thank you!")
            return None

        if user_input in ['yes', 'y']:
            print(f"Rating: {selected_movie['rating']} / 10")
            print(f"Vote Count: {selected_movie['vote_count']}")
            return selected_movie
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue


## STEP 4: Continue browsing the link of the movie
def show_movie_link(selected_movie):
    while True:
        user_input = input(f"\n4. Do you want to see the link for more details? (yes/no): ").strip().lower()

        if user_input in ['no', 'n']:
            print("Exiting. Thank you!")
            return None

        if user_input in ['yes', 'y']:
            print(f"Opening the link: {selected_movie['link']}")
            webbrowser.open(selected_movie['link'])
            return selected_movie
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue


## Step 5: Run the system
def ask_to_play_again():
    while True:
        response = input(f"\nDo you want to play it again? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

while True:
    print(f"\nWelcome to the movie recommendation system!")
    tree = load_tree_from_json('tree.json')
    selected_movies = display_tree(tree)

    if selected_movies:
        for movie in selected_movies:
            print(f"{movie['number']}. {movie['title']}")

        selected_movie = get_movie_info(selected_movies)

        if selected_movie:
            selected_movie = show_movie_rating(selected_movie)
            if selected_movie:
                show_movie_link(selected_movie)
                print(f"\nHope you enjoy the movie!")

    if not ask_to_play_again():
        print(f"\nThank you for using the movie recommendation system!")
        break
