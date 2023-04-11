import unittest
import shutil

class TestAPIMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        shutil.copytree('./analysis/srv/files', './files')

    @classmethod
    def tearDownClass(self):
        shutil.rmtree('./files')

if __name__ == '__main__':
    unittest.main()