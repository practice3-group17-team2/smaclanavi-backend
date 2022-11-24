# manage.py test administer_data.tests.test_savedata
from django.test import TestCase

import re
from administer_data.scraping import sb_savedata

# manage.py test administer_data.tests.test_savedata.TestSbSaveData
class TestSbSaveData(TestCase):

    def test_save_data(self):
        sb_savedata.save_data()

    # manage.py test administer_data.tests.test_savedata.TestSbSaveData.test_fix_data
    def test_fix_data(self):
        sb_savedata.fix_data()
    
    def reg(self):
        text = "横浜市鶴見区（2）"
        print(re.split(r'.+?市.+?区|.+?[市区町村]', text))
