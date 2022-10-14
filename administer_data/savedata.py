from . import scraping
from models import TestSaveData

test_word = "スマホ教室" #任意の言葉、なんでもいい
link_ls, title_ls = scraping.search_google(test_word)

for i in range(len(link_ls)):
    TestSaveData.objects.create(title=title_ls[i], url=link_ls[i])
