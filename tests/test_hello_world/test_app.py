from hello_world.app import create_app
import asynctest
import pytest


class HelloWorldAppTest(asynctest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_canary(self):
        self.assertEqual(1, 1)

    @pytest.mark.asyncio
    async def test_hello(self):
        response = await self.client.post('/api/hello', json=dict(message='hello world', count=5))
        self.assertEqual(response.status_code, 200)
        actual = await response.get_json()
        expected = ['hello world'] * 5
        self.assertEqual(actual, expected)
