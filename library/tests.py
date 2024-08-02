from django.contrib.auth.models import Permission, Group
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from library.models import Author, Genre


class TestCaseBase(APITestCase):
    @property
    def bearer_token(self):
        user = User.objects.create(email='manager@test.com', phone='+79998888111')
        user.set_password('1234')
        user.save()
        self.user = user
        created_group = Group.objects.create(name='manager')

        # group = Group.objects.get(name='manager')
        self.user.groups.add(created_group)
        refresh = RefreshToken.for_user(self.user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class AuthorTestCase(TestCaseBase):
    def setUp(self) -> None:
        self.url = f'/api/authors/'
        self.client = APIClient()
        """Создание тестового автора"""
        self.author = Author.objects.create(last_name='test_last_name', first_name='test_first_name')

    def test_get_list_no_auth(self):
        """Тестирование получения списка авторов без авторизации."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def test_get_list_authors(self):
        """Тестирование получения списка авторов."""
        response = self.client.get(self.url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_create_author(self):
        """Тестирование создания автора."""
        data = {'last_name': 'Creating_test', 'first_name': 'Creating_test'}
        response = self.client.post(self.url, data=data, format='json', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Author.objects.filter(last_name=data['last_name']).exists())
        self.assertEqual(
            Author.objects.all().count(), 2
        )

    def test_retrieve_author(self):
        """Тестирование просмотра информации об авторе."""
        response = self.client.get(f'{self.url}{self.author.id}/', **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], self.author.last_name)

    def test_update_author(self):
        """Тестирование редактирования автора."""
        data = {'last_name': 'Updating_test', 'first_name': 'Updating_test'}
        response = self.client.patch(f'{self.url}{self.author.id}/', data=data, **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.last_name, data['last_name'])

    def test_delete_author(self):
        response = self.client.delete(f'{self.url}{self.author.id}/', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GenreTestCase(TestCaseBase):
    def setUp(self) -> None:
        self.url = f'/api/genres/'
        self.client = APIClient()
        """Создание тестового жанра"""
        self.genre = Genre.objects.create(title='test_title')

    def test_get_list_genres_no_auth(self):
        """Тестирование получения списка жанров без авторизации."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def test_get_list_genres(self):
        """Тестирование получения списка жанров."""
        response = self.client.get(self.url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_create_genre(self):
        """Тестирование создания жанра."""
        data = {'title': 'Creating_test'}
        response = self.client.post(self.url, data=data, format='json', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Genre.objects.filter(title=data['title']).exists())
        self.assertEqual(
            Genre.objects.all().count(), 2
        )

    def test_retrieve_genre(self):
        """Тестирование просмотра информации о жанре."""
        response = self.client.get(f'{self.url}{self.genre.id}/', **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.genre.title)

    def test_update_genre(self):
        """Тестирование редактирования жанра."""
        data = {'title': 'Updating_test'}
        response = self.client.patch(f'{self.url}{self.genre.id}/', data=data, **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.title, data['title'])

    def test_delete_genre(self):
        response = self.client.delete(f'{self.url}{self.genre.id}/', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
