import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__), '..', 'src')))  # noqa

import test_client
import test_music_objects
import test_songqueue
import test_start
import test_view
import test_writer

tests = {
    "client.py": test_client,
    "music_objects.py": test_music_objects,
    "songqueue.py": test_songqueue,
    "start.py": test_start,
    "view.py": test_view,
    "writer.py": test_writer,
}

for test in tests:
    print('Testing %s...' % test)
    tests[test].run()
    print()
