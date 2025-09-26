import unittest
import shutil
from os import remove, mkdir, path
from guachi.config import DictMatch, OptionConfigurationError
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class MockDict(dict):
	pass

# (테스트용 config 파일 생성 함수 등은 생략, 실제 테스트 코드만 반영)

class TestConfigOptions(unittest.TestCase):
	def setUp(self):
		self.mapped_options = {
			'guachi.db.host': 'db_host',
			'guachi.db.port': 'db_port',
			'guachi.web.host': 'web_host',
			'guachi.web.port': 'web_port',
		}
		self.mapped_defaults = {
			'db_host': 'localhost',
			'db_port': 27017,
			'web_host': 'localhost',
			'web_port': '8080',
		}

	def tearDown(self):
		pass

	def test_options_config_none_empty_defaults(self):
		opts = DictMatch()
		actual = opts.options()
		expected = {}
		self.assertEqual(actual, expected)

	def test_options_config_invalid_empty_defaults(self):
		opts = DictMatch(config='/path/to/invalid/file')
		actual = opts.options()
		expected = {}
		self.assertEqual(actual, expected)

	def test_options_config_dict_empty_defaults(self):
		opts = DictMatch(config={})
		actual = opts.options()
		expected = {}
		self.assertEqual(actual, expected)

	def test_options_from_dict(self):
		opt = DictMatch(config={}, mapped_defaults=self.mapped_defaults)
		actual = opt.options()
		expected = self.mapped_defaults
		self.assertEqual(actual, expected)

	def test_options_dict_like_object(self):
		mock_dict = MockDict()
		opt = DictMatch(config=mock_dict, mapped_defaults=self.mapped_defaults)
		actual = opt.options()
		expected = self.mapped_defaults
		self.assertEqual(actual, expected)
