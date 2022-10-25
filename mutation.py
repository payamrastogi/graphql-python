import graphene
from type import User
from data import users

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: User)

    class Arguments:
        id = graphene.String()
        name = graphene.String()
        email = graphene.String()

    @staticmethod
    def mutate(root, info, id, name, email):
        user = User(id=id, name=name, email=email)
        users.append(
            {
                "id": id,
                "name": name,
                "email": email
            }
        )
        return CreateUser(user = user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    @staticmethod
    def mutate(root, info, id, email):
        old_user = list(filter(lambda user: user["id"]==id, users))[0]
        new_user = User(id=id, name=old_user["name"], email=email)
        users.remove(old_user)
        users.append(
            {
                "id": id,
                "name": old_user["name"],
                "email": email
            }
        )
        return UpdateUser(user = new_user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    @staticmethod
    def mutate(root, info, id):
        old_user = list(filter(lambda user: user["id"]==id))[0]
        users.remove(old_user)
        return DeleteUser(user = old_user)