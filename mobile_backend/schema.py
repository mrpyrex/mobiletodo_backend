import graphene
import graphql_jwt
import todos.schema


class Query(todos.schema.Query, graphene.ObjectType):
    pass


class Mutation(todos.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
