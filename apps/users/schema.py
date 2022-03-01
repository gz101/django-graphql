from graphene_django import DjangoObjectType
import graphene 
from graphql import GraphQLError 

from .models import User 


class UserType(DjangoObjectType):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email', 'username', 'address')
