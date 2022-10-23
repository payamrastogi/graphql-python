import graphene
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User

class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class UserQuery(Query):
    user = graphene.Field(User)
    get_user = graphene.Field(User, id=graphene.String())
    get_users = graphene.List(User)

schema = graphene.Schema(query= UserQuery, mutation=UserMutation)



result = schema.execute(
    '''
    mutation {
        createUser(id:"1", name:"Alice", email:"alice@email.com"){
            user {
                id
                name
                email
            }
        }
    }
    '''
)
print(result.data)
result = schema.execute(
    '''
    mutation {
        updateUser(id:"1", email:"alice1@email.com"){
            user {
                id
                name
                email
            }
        }
    }
    '''
)
print(result.data)
result = schema.execute(
    '''
    Query {
        getUser(id:"1"){
            user {
                id
                name
                email
            }
        }
    }
    '''
)
print(result.data)