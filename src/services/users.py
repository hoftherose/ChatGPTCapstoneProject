from src.repositories.users import UserTable

def get_user_list():
    users = UserTable.select_all_users()
    return {"users": users}

def create_user(name: str, pswd: str):
    # UserTable.insert_user()
    return []