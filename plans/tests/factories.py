import factory
# from factory.faker import Faker
from faker import Faker

fake = Faker()


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'plans.Plans'
        # django_get_or_create = ('name',)

    # id = factory.Faker('id')
    name = fake.name
    amount = fake.random_int(min=10, max=100)
    is_active = True
