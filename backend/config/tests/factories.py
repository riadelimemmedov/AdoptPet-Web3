import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from abstract.constants import Genders, Status, Types
from apps.user_profile.models import Profile

# *User

User = get_user_model()


# !UserFactory
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: "normal_user{}@gmail.com".format(n))
    password = "foo12345"
    is_active = True

    @classmethod
    def create_user(cls, **kwargs):
        kwargs["is_staff"] = False
        kwargs["is_superuser"] = False
        return super().create(**kwargs)

    @classmethod
    def create_superuser(cls, **kwargs):
        if not kwargs["is_superuser"] or not kwargs["is_staff"]:
            raise ValueError("Superuser must have is_superuser=True and is_staff=True.")
        else:
            kwargs["is_staff"] = True
            kwargs["is_superuser"] = True
        return super().create(**kwargs)


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    # user = factory.SubFactory(UserFactory, profile=None)

    first_name = "Joe"
    last_name = "Doe"
    profile_key = "abc123"
    account_type = Types[1][0]
    status = Status[1][0]
    gender = Genders[1][0]
