import unittest


class TestMusicObject(unittest.TestCase):

    def test_play(self):
        pass


class TestArtist(unittest.TestCase):

    def test_init(self):
        pass

    def test_verify(self):
        pass

    def test_str(self):
        pass

    def test_play(self):
        pass

    def test_collect(self):
        pass

    def test_fill(self):
        pass


class TestAlbum(unittest.TestCase):

    def test_init(self):
        pass

    def test_verify(self):
        pass

    def test_str(self):
        pass

    def test_play(self):
        pass

    def test_collect(self):
        pass

    def test_fill(self):
        pass


class TestSong(unittest.TestCase):

    def test_init(self):
        pass

    def test_verify(self):
        pass

    def test_time_from_ms(self):
        pass

    def test_str(self):
        pass

    def test_play(self):
        pass

    def test_fill(self):
        pass


class TestLibSong(unittest.TestCase):

    def test_init(self):
        pass

    def test_time_from_s(self):
        pass

    def test_str(self):
        pass

    def test_play(self):
        pass

    def test_fill(self):
        pass


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        [
            loader.loadTestsFromTestCase(case)
            for case in
            (TestMusicObject, TestSong, TestArtist, TestAlbum, TestLibSong)
        ]
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)
