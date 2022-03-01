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
        id = graphene.Int()
        number = graphene.Int()
        street = graphene.String()
        city = graphene.String()
        state = graphene.String()
    
    def mutate(self, info, id, number=None, street=None, city=None, 
               state=None):
        try:
            a = Address.objects.get(id=id)
        except Address.DoesNotExist:
            raise GraphQLError('Address does not exist.')

        if number is not None:
            a.number = number
        
        if street is not None:
            a.street = street 
        
        if city is not None:
            a.city = city 
        
        if state is not None:
            if not Address.valid_state(state):
                a.state = state
            else:
                raise GraphQLError('Invalid state chosen.') 
        
        a.save()
        return UpdateAddress(address=a)
