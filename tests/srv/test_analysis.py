import unittest
import shutil
import json
from analysis.srv.analyze_moby_dick import load_file, clean_line, count_top_100_frequent_words

class TestAnalysisMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        shutil.copytree('./analysis/srv/files', './files')

    @classmethod
    def tearDownClass(self):
        shutil.rmtree('./files')

    def test_load_file(self):
        self.assertEqual(type(load_file('mobydick.txt')), type([]))

    def test_clean_line(self):
        # punc that will be spaces -> —-
        # punc that will be replaced with "" -> !@#$%^&*()=+_`~[]\|;:'",./<>?“”’s
        self.assertEqual(clean_line("""!@#$%^&*()=+_`~[]\|;:'",./<>?“”’sthis—is-good"""), 'this is good')

    def test_count_top_100_frequent_words(self):
        count_top_100_frequent_words()

        with open('./files/top_100.txt') as f:
            top_100 = json.loads(f.read())

        answer = json.loads('''[["whale", 1238], ["ship", 518], ["ahab", 517], ["sea", 455], ["ye", 427], ["head", 347], ["boat", 337], ["time", 334], ["captain", 329], ["chapter", 308], ["white", 281], ["whales", 271], ["thou", 268], ["stubb", 258], ["queequeg", 253], ["little", 249], ["round", 247], ["sperm", 245], ["hand", 215], ["own", 205], ["look", 202], ["deck", 199], ["starbuck", 199], ["water", 190], ["day", 179], ["pequod", 178], ["world", 176], ["life", 175], ["fish", 171], ["sir", 171], ["seen", 165], ["line", 160], ["eyes", 156], ["cried", 156], ["oh", 154], ["night", 152], ["god", 152], ["sort", 152], ["nor", 151], ["aye", 151], ["boats", 144], ["air", 143], ["crew", 141], ["half", 136], ["tell", 135], ["whaling", 133], ["thee", 131], ["mast", 130], ["hands", 130], ["soon", 129], ["feet", 127], ["till", 122], ["don\u2019t", 119], ["called", 116], ["towards", 115], ["found", 115], ["poor", 114], ["thy", 113], ["times", 112], ["body", 110], ["heard", 110], ["flask", 109], ["stand", 107], ["moment", 105], ["sight", 105], ["voyage", 103], ["sail", 102], ["sun", 102], ["strange", 98], ["hold", 98], ["nantucket", 97], ["leviathan", 96], ["dead", 92], ["black", 92], ["heart", 91], ["leg", 90], ["oil", 90], ["death", 90], ["stood", 90], ["arm", 89], ["am", 89], ["indeed", 89], ["true", 88], ["iron", 88], ["eye", 88], ["cabin", 87], ["heads", 87], ["sometimes", 87], ["matter", 87], ["seas", 86], ["jonah", 85], ["ships", 85], ["moby", 84], ["hard", 84], ["wild", 84], ["dick", 83], ["soul", 83], ["tail", 82], ["standing", 82], ["ocean", 81]]''')
        self.assertEqual(100, len(top_100))
        self.assertEqual(answer, top_100)

if __name__ == '__main__':
    unittest.main()