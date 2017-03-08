import unittest


class TestSongQueue(unittest.TestCase):

    def test_append(self):
        pass

    def test_extend(self):
        pass

    def test_collect(self):
        pass

    def test_play(self):
        pass

    def test_restore(self):
        pass


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromTestCase(TestSongQueue)
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)
