import unittest
from selenium import webdriver


class TestStudDB(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS('/home/sasha/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

    def tearDown(self):
        self.driver.quit

    def test_django_simple(self):
        self.driver.get('http://localhost:8000/')

        self.assertNotIn('Django', self.driver.title)

    def test_studdb_simple(self):
        self.driver.get('http://localhost:8000/')

        self.assertIn('StudDB', self.driver.title)


if __name__ == '__main__':
    unittest.main()
