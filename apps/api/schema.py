from graphene_django import DjangoObjectType
import graphene 

from apps.users.models import User 
from apps.addresses.models import Address 

from apps.users.schema import UserType 
from apps.addresses.schema import (
    AddressType,
    CreateAddress,
    UpdateAddress
)


class Mutation(graphene.ObjectType):
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.Int())
    addresses = graphene.List(AddressType)
    address_by_id = graphene.Field(AddressType, address_id=graphene.Int())

    def resolve_users(self, info):
        return User.objects.all()
    
    def resolve_user_by_id(self, info, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    def resolve_addresses(self, info):
        return Address.objects.all()
    
    def resolve_address_by_id(self, info, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
