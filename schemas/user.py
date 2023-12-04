#

def userEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": str(db_item["name"]),
        "email": str(db_item["email"]),
        "phone": str(db_item["phone"]),
    }

def listOfUserEntity(db_item_list) -> list:
    list_user_entity = []
    for item in db_item_list:
        list_user_entity.append(userEntity(item))
    return list_user_entity