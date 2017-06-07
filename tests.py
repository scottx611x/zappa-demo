import index
import unittest


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = index.app
        self.app.config['TESTING'] = True
        self.test_client = self.app.test_client()

    def test_index_route(self):
        response = self.test_client.get('/')
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
