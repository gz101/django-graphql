from graphene_django import DjangoObjectType
import graphene 
from graphql import GraphQLError 

from .models import Address 


class AddressType(DjangoObjectType):
    class Meta:
        model = Address 


class CreateAddress(graphene.Mutation):
    address = graphene.Field(AddressType)

    class Arguments:
        number = graphene.Int()
        street = graphene.String()
        city = graphene.String()
        state = graphene.String()
    
    def mutate(self, info, number, street, city, state):
        if not Address.valid_state(state):
            raise GraphQLError('Invalid state. Must be in Australia.')

        a = Address(
            number=number,
            street=street,
            city=city,
            state=state
        )
        a.save()
        return CreateAddress(address=a)


class UpdateAddress(graphene.Mutation):
    address = graphene.Field(AddressType)

    class Arguments:
        number = graphene.Int()
        street = graphene.String()
        city = graphene.String()
        state = graphene.String()
    
    def mutate(self, info, id, number, street, city, state):
        if not Address.valid_state(state):
            raise GraphQLError('Invalid state. Must be in Australia.')
        
        a = Address.objects.get(id=id)

        a.number = number
        a.street = street 
        a.city = city 
        a.state = state 
        a.save()
        return UpdateAddress(address=a)
