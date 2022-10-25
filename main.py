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


### Create User###
result = schema.execute(
    '''
    mutation {
        createUser(id:"3", name:"Cate", email:"cate@email.com"){
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
### Update User###
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
print(result.errors)
#####Get user by id ####
result = schema.execute(
    '''
    query {
        getUser(id:"1"){
            id
            name
            email
        }
    }
    '''
)
print(result.data)
#print(result.errors)
#### Get all users######
result = schema.execute(
    '''
    query {
        getUsers {
            id
            name
            email
        }
    }
    '''
)
print(result.data)