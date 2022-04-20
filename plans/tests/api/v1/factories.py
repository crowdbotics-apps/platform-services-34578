import factory
from faker import Faker

fake = Faker()


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'plans.Plans'
        django_get_or_create = ('name', 'amount', 'is_active',)

    # name = fake.name
    # amount = fake.random_int(min=10, max=100)
    name = "Hello world"
    amount = 10000.00
    is_active = True
