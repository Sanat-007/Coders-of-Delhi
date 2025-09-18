import json

# Load the JSON data from a file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Display users and their connections
def display_users(data):
    for user in data['users']:
        print(f"\n{user['name']} (ID: {user['id']})- Friends: {user['friends']} - liked Pages: {user['liked_pages']}")
        print("\nPages:")
        for page in data["pages"]:
            print(f"{page['id']} : {page['name']}")

# Load and display the data
data = load_data('massive_data.json')
display_users(data)