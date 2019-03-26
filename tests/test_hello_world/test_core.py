from hello_world.core import HelloWorld
import asynctest
import pytest


class HelloWorldTest(asynctest.TestCase):

    def test_canary(self):
        self.assertEqual(1, 1)

    @pytest.mark.asyncio
    async def test_world(self):
        dut = HelloWorld()
        actual = await dut.hello('hello world', 2)
        expected = ['hello world'] * 2
        self.assertEqual(actual, expected)
