from random import randint

import graphene
from graphene_django import DjangoObjectType, DjangoListField

from .models import Address, Person 


class AddressType(DjangoObjectType):
    class Meta:
        model = Address 
        fields = '__all__'


class PersonType(DjangoObjectType):
    class Meta:
        model = Person 
        fields = ('email', 'name', 'address')


class Query(graphene.ObjectType):
    people = graphene.List(PersonType)
    person_by_id = graphene.Field(PersonType, person_id=graphene.Int())
    person = graphene.Field(PersonType)

    def resolve_people(self, info, **kwargs):
        return Person.objects.all()
    
    def resolve_person_by_id(self, info, person_id):
        try:
            return Person.objects.get(pk=person_id)
        except Person.DoesNotExist:
            return None
    
    def resolve_person(self, info, **kwargs):
        random_id = randint(1, Person.objects.count())
        return Person.objects.get(pk=random_id)


schema = graphene.Schema(query=Query)
