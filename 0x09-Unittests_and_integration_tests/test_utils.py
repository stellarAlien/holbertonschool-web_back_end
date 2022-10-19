#!/usr/bin/env python3
"""
writing tests here
"""

import logging
import unittest
from unittest.mock import patch, Mock, MagicMock
from utils import access_nested_map, get_json, memoize
import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''test case for reading mapping functions'''

    @parameterized.expand(
        [
            ({"a": 1}, ("a"), 1),
            ({"a": {"b": 2}}, ("a"), '{"b": 2}'),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        '''test  utils nested map'''
        v = self.assertEqual(access_nested_map(nested_map, path), expected)
        return v

    @parameterized.expand([
        ({}, ("a"), 'a')
        ({"a": 1}, ("a", "b"), 'b')
    ]
    )
    def test_access_nested_map_exception(self, nested_map, path, key):
        '''check for  key error'''
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError()".format(key), repr(error.exception))

    class TestGetJson(unittest.TestCase):
        '''test for requests module'''
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
        )
        @patch('utils.requests.get')
        def test_get_json(self, mock_get, test_url, test_payload):
            '''test get method'''

            mock_get.json.return_value = MagicMock(response=test_payload)
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''tests for memoize'''

    def test_memoize(self):
        '''test basic memoize function'''
        class TestClass():
            '''test class inside emoize test class'''
            def a_method(self):
                '''a method'''
                return 42

            @memoize
            def a_property(self):
                '''a property'''
                return self.a_method()

            def test_a_property():
                '''test a property'''
                with patch.object(TestClass, 'a_method') as m:
                    test_class = TestClass()
                    test_class.a_method()
                    test_class.a_method()
                    m.assert_called_once()
