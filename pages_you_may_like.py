import json

def load_data(file_path):
    with open(file_path,'r') as file:
        return json.load(file)

def pages_you_may_like(user_id,data):
    user_pages = {}
    for user in data['users']:
        user_pages[user['id']] = set(user["liked_pages"])
    
    if user_id not in user_pages:
        return []
    
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    
    for other_users,pages in user_pages.items():
        if other_users != user_id:
            shared_pages=user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page,0) + len(shared_pages)
    
    sorted_pages = sorted(page_suggestions.items(),key=lambda x : x[1], reverse=True)
    return [page_id for page_id, _ in sorted_pages]

# Load Data
data = load_data('massive_data.json')
user_id=int(input('enter user id :'))
recommandation = pages_you_may_like(user_id,data)
print(f"pages you may like for user {user_id} : {recommandation}")