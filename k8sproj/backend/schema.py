import graphene
from graphene_django import DjangoObjectType
from .models import ToDo
import requests


#datatype declaration of objnect to be stored in django database. Should follow defined types in Model 
class ToDoListType(DjangoObjectType):
    class Meta:
        model=ToDo
        #needs a tuple
        fields=("text",)

# Class for inserting in the database
class CreateTodo(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)
    
    # The class attributes define the response of the mutation
    todo = graphene.Field(ToDoListType)

    # mandatory mutate method needed.
    def mutate(root, info, **kwargs):
        todo = ToDo(**kwargs)
        todo.save()

        return CreateTodo(todo)
        

# Mutation GraphQL
# mutation {
#   addTodo(text: "GQLTODO1") {
#     todo{
#       text
#     }
#   }
# }
# Performs Insert query on DB
class Mutation(graphene.ObjectType):
    add_todo = CreateTodo.Field()
    

# Query GraphQL
# {
#   allList {
#     text
#   }
# }
# Performs SELECT query on DB
counter =0

def downloadImage():	
        img=requests.get("https://picsum.photos/1200")
        print (img.content)
        with open("/tmp/kube/static/k8simage.jpg","wb") as f:
            f.write(img.content)


class Query(graphene.ObjectType):
    all_list= graphene.List(ToDoListType)  

    def resolve_all_list(root, info):
        global counter
        if (counter==0):
            downloadImage()
            counter =+ 1
        return ToDo.objects.all()

    

#runs the query and returns the result in schema
schema= graphene.Schema(query=Query,mutation=Mutation)

