from django.test import TestCase

# from common.models import ItemDataStatus, ItemDataCollection, ItemData
# from users.models import User
#
#
# # Create your tests here.
# class CommonTests(TestCase):
#
#     def setUp(self):
#         User.objects.create_user('test_staff', '<EMAIL>', '<PASSWORD>', is_staff=True)
#         User.objects.create_user('test_admin', '<EMAIL>', '<PASSWORD>', is_superuser=True)
#         User.objects.create_user('test_user', '<EMAIL>', '<PASSWORD>')
#
#         ItemDataStatus.objects.create(
#             verbose="Тест",
#             name="test"
#         )
#
#         ItemDataCollection.objects.create(
#             verbose="Другое",
#             name="other"
#         )
#
#         ItemData.objects.create(
#             title="Тестовый объект",
#             description="# Это тестовый объект!\n Тут будет информация в markdown",
#             short_description="Это краткое описание объекта",
#
#         )
