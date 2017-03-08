import unittest


class TestView(unittest.TestCase):

    def test_setitem(self):
        pass

    def test_len(self):
        pass

    def test_replace(self):
        pass

    def test_clear(self):
        pass

    def test_is_empty(self):
        pass

    def test_copy(self):
        pass


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromTestCase(TestView)
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)
