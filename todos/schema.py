import graphene
from graphene_django import DjangoObjectType
from .models import Todo
from graphql import GraphQLError


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(object):
    all_todos = graphene.List(TodoType)

    todo = graphene.Field(TodoType,
                          id=graphene.Int(),
                          client=graphene.String())

    def resolve_all_todos(self, info, **kwargs):
        return Todo.objects.all()

    def resolve_todo(self, info, **kwargs):
        id = kwargs.get('id')
        client = kwargs.get('client')

        if id is not None:
            return Todo.objects.get(pk=id)

        if client is not None:
            return Todo.objects.get(client=client)

        return None


class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        theme = graphene.String(required=True)
        inscription = graphene.String(required=True)
        delivery_date = graphene.String(required=True)
        client = graphene.String(required=True)
        flavors = graphene.String(required=True)
        cake_thumb = graphene.String()

    def mutate(self, info, **kwargs):
        todo = Todo(**kwargs)
        todo.save()
        return CreateTodo(todo=todo)


class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        todo_id = graphene.Int(required=True)
        theme = graphene.String()
        inscription = graphene.String()
        delivery_date = graphene.String()
        flavors = graphene.String()
        cake_thumb = graphene.String()

    def mutate(self, info, todo_id, theme, inscription, delivery_date, flavors, cake_thumb):

        todo = Todo.objects.get(id=todo_id)
        todo.theme = theme
        todo.inscription = inscription
        todo.delivery_date = delivery_date
        todo.flavors = flavors
        todo.cake_thumb = cake_thumb
        todo.save()

        return UpdateTodo(todo=todo)


class DeleteTodo(graphene.Mutation):
    todo_id = graphene.Int()

    class Arguments:
        todo_id = graphene.Int(required=True)

    def mutate(self, info, todo_id):

        todo = Todo.objects.get(id=todo_id)

        todo.delete()
        return DeleteTodo(todo=todo)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
