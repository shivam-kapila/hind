from faker import Faker
from faker.providers import BaseProvider, internet, profile
from random import sample, choice

ALLOWED_TAGS = ['culture', 'art', 'food', 'dance', 'flora and fauna', 'handloom', 'teracotta', 'jewellery', 'religion',
                'monuments', 'artifacts', 'medicine', 'games', 'lifestyle', 'festivities']
ALLOWED_TAGS_COUNT = 5

ALLOWED_CATEGORIES = ['local trivia', 'my creations', 'historical significance']


class TagsProvider(BaseProvider):
    def tags(self):
        return sample(ALLOWED_TAGS, ALLOWED_TAGS_COUNT)


class CategoryProvider(BaseProvider):
    def category(self):
        return choice(ALLOWED_CATEGORIES)


fake = Faker()
Faker.seed(12345)

fake.add_provider(internet)
fake.add_provider(profile)
fake.add_provider(TagsProvider)
fake.add_provider(CategoryProvider)
