import unittest


class TestWriter(unittest.TestCase):

    def test_trunc(self):
        pass

    def test_replace_windows(self):
        pass

    def test_measure_fields(self):
        pass


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromTestCase(TestWriter)
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)
