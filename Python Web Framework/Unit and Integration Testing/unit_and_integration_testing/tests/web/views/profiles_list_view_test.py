from django.test import TestCase
from django.urls import reverse


class ProfileListViewTest(TestCase):
    def test_profiles_list_view__when_no_profiles__expect_empty_list_and_count_context(self):
        # self.client.get() makes HTTP GET request
        response = self.client.get(reverse('list profiles'))

        self.assertListEqual([], response.context['profile_list'])
        self.assertEqual(0, 'profiles_count')
