import json
def clean_data(data):
    # Remove users with missing names
    data['users']= [user for user in data['users'] if user['name'].strip()]

    # Remove Duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))
    
    # Remove inactive users (no friends and no liked pages)
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    # Rmove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())

    return data

# Load, clean, and display the data
data = json.load(open('incomplete_data.json'))
data = clean_data(data)
json.dump(data, open('cleaned_data.json', 'w'), indent=4)
print("Cleaned data saved to 'cleaned_data.json'")

