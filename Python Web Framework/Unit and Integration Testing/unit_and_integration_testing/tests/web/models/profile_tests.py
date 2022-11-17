from django.core.exceptions import ValidationError

from unit_and_integration_testing.web.models import Profile
from django.test import TestCase


class ProfileModelTests(TestCase):
    # triple A concept = Arrange, Act, Assert
    # or Setup, Do, Check result

    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        # Arrange
        profile = Profile(
        name = "Doncho",
        age = 19,
        egn='0318230467'
        )

        # Act
        profile.full_clean() # call this when test validators
        profile.save()

        # Assert
        self.assertIsNone(profile.pk)


        # if we test for wrong result

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNot(context.exception)