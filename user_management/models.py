from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import (
    EmailField,
    CharField,
    DateField,
    IntegerField,
    SmallIntegerField,
    BooleanField,
)


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        gender,
        food_preference,
        first_name,
        last_name,
        birth_date,
        phone,
        address_line_1,
        zip,
        city,
        state,
        password=None,
        address_line_2=None,
    ):
        user = self.model(
            email=email,
            gender=gender,
            food_preference=food_preference,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone=phone,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            zip=zip,
            city=city,
            state=state,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email,
        gender,
        food_preference,
        first_name,
        last_name,
        birth_date,
        phone,
        address_line_1,
        zip,
        city,
        state,
        password=None,
        address_line_2=None,
    ):
        user = self.create_user(
            email=email,
            password=password,
            gender=gender,
            food_preference=food_preference,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone=phone,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            zip=zip,
            city=city,
            state=state,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_DIVERSE = 2
    GENDER_OPTIONS = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_DIVERSE, "diverse"),
    )

    FOOD_OMNIVOUROUS = 0
    FOOD_VEGETARIAN = 1
    FOOD_OPTIONS = ((FOOD_OMNIVOUROUS, "omnivourous"), (FOOD_VEGETARIAN, "vegetarian"))

    email = EmailField(unique=True, verbose_name="Email address")
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    gender = SmallIntegerField(choices=GENDER_OPTIONS)
    food_preference = SmallIntegerField(choices=FOOD_OPTIONS)
    first_name = CharField(max_length=254, verbose_name="First name")
    last_name = CharField(max_length=254, verbose_name="Last name")
    birth_date = DateField()
    phone = IntegerField()
    address_line_1 = CharField(max_length=254)
    address_line_2 = CharField(max_length=254, blank=True, null=True)
    zip = CharField(max_length=254)
    city = CharField(max_length=254)
    state = CharField(max_length=254)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "gender",
        "food_preference",
        "first_name",
        "last_name",
        "birth_date",
        "phone",
        "address_line_1",
        "zip",
        "city",
        "state",
    ]

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name
