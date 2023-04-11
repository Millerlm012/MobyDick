import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # necessary to run chromedriver headless in a docker container
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://host.docker.internal/')

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_site_online(self):
        header = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('Top 100 Frequent Words from Moby Dick', header)

    # TODO: this works locally, but fails when it's in the docker container... the docker image: selenium/standalone-chrome looks promising
    # def test_site_content(self):
    #     first_word = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'data-0'))).text
    #     self.assertEqual('#1 --- whale --- 1238', first_word)


if __name__ == '__main__':
    unittest.main()