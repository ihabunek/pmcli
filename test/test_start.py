import unittest


class TestStart(unittest.TestCase):

    def test_validate_config(self):
        pass

    def test_validate_colour(self):
        pass

    def test_read_config(self):
        pass

    def test_hex_to_rgb(self):
        pass


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromTestCase(TestStart)
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)
