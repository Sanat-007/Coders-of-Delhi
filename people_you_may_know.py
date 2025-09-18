import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def people_you_may_know(user_id,data):
    user_friend = {}
    for user in data['users']:
        user_friend[user['id']] = set(user['friends'])

    if user_id not in user_friend:
        return []
    
    direct_friends = user_friend[user['id']]
    suggestions = {}
    for friends in direct_friends:
        # For all friends of friend
        for mutual in user_friend[friends]:
            # If mutual id is not the same user and not already a direct friend of user
            if mutual != user_id and mutual not in (direct_friends):
                # count mutual friends
                suggestions[mutual] = suggestions.get(mutual,0) + 1

    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, i in sorted_suggestions]

# LOAD DATA
data = load_data("massive_data.json")
user_id = int(input("Enter the user id :"))
recommendations = people_you_may_know(user_id,data)
print(f"People you may konw for user {user_id} : {recommendations}")