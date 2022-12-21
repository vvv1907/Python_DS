import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

class SimilarRecipes:
    def __init__(self, list_of_ingredients):
        df = pd.read_csv('data/epi_r_short.csv')
        self.ingredients = list_of_ingredients
        df_filter = df
        for ing in list_of_ingredients:
            df_filter = df_filter[df_filter[ing] == 1]
        if df_filter.shape == 0:
            self.filter = None
        else:
            self.filter = df_filter

    def find_all(self):
        if self.filter is None:
            return None
        return self.filter

    def get_recipe(self, recipe):
        url_epic = 'https://www.epicurious.com/search/' + recipe.replace(' ', '%20')
        resp = requests.get(url_epic, time.sleep(3))
        if resp.status_code != 200:
            return None
        data = resp.text
        soup = BeautifulSoup(data, 'lxml')
        for a in soup.find_all('a', href=True):
            if '/recipes/food/views/' in a['href']:
                return 'https://www.epicurious.com' + str(a['href'])

    def top_similar(self, n):
        filter = self.filter
        filter['extra_num'] = filter.iloc[:,3:].sum(axis=1, ) - len(self.ingredients)
        topn = filter.sort_values(by='rating', ascending=False).iloc[:n+1,:]
        if topn.shape[0] == 0:
            print("Our database have no recipes with these ingridients.")

        URL = []
        text_with_recipes = ''
        for i in range (topn.shape[0]):
            title = topn.iloc[i].title
            rating = topn.iloc[i].rating
            URL = SimilarRecipes.get_recipe(self, title)
            if (URL):
                text_with_recipes += f'-  {title}, rating: {rating}, URL: {URL}\n'
        return text_with_recipes
