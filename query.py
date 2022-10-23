from graphene import ObjectType
from data import users

class Query(ObjectType):
    @staticmethod
    def resolve_get_user(root, info, id):
        return list(filter(lambda user: user["id"]==id))[0]

    @staticmethod
    def resolve_get_users(root, info):
        return users