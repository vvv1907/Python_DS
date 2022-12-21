import pandas as pd
import requests

class NutritionFacts:

    def __init__(self, ingr, path = 'data/nutrients_norm.csv'):
        self.path = path
        self.ingr = ingr

    def nutrients_norm(self):
        self.make_nutrs_csv()
        facts = pd.read_csv('data/nutrients.csv',index_col=[0])
        daily_norm = self.daily_norm_func()
        for c in facts.columns:
            divisor = daily_norm[daily_norm.component == c]['value'].values[0]
            facts[c] = facts[c].div(divisor)
        facts.to_csv('data/nutrients_norm.csv')
        self.init_df()

    def init_df(self):
        self.df = pd.read_csv(self.path,
                 sep=',',
                 index_col='ingr')

    def daily_norm_func(self):
        di = pd.read_csv('data/daily_intakes.csv')
        di = di[['Nutrient', 'Adults and Children≥ 4 years']]
        di.columns = ['component', 'value']
        dr = pd.read_csv('data/daily_references.csv')
        dr = dr[['Food Component', 'Adults and Children ≥ 4 years']]
        dr.columns = ['component', 'value']
        dr = pd.concat([dr, di]).dropna()
        return dr

    def make_nutrs_csv(self):
        daily_norm = self.daily_norm_func()
        api = self.get_api(self.ingr)
        api[set(daily_norm.component) & set(api.columns)].to_csv('data/nutrients.csv')

    def printer(self, info):
        for ingrid, ingr_info in info.items():
            print(ingrid)
            for name, item in zip(ingr_info.index, ingr_info.values):
                if item >= 0.01:
                    print(f"{name} - {item * 100:.0f}% of Daily Value")
            print()

    stack = []
    def get_data(self, ingr):
        url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query={ingr}'
        with open('data/api_key.txt', 'r') as file:
            api_key = file.read()
        try:
            response = requests.get(url, auth=(api_key, ''))
            food = response.json()['foods'][0]['foodNutrients']
            df = pd.DataFrame(food)[['nutrientName','value']]
            df['ingr'] = ingr
            return df
        except Exception:
            self.stack.append(ingr)

    def get_api(self, arr_ingr):
        col = {'Calcium, Ca': 'Calcium', 'Choline, total': 'Choline', 'Copper, Cu': 'Copper',
            'Total lipid (fat)': 'Fat', 'Fiber, total dietary': 'Dietary Fiber',
            'Iron, Fe': 'Iron', 'Folate, DFE': 'Folate', 'Magnesium, Mg': 'Magnesium',
            'Phosphorus, P': 'Phosphorus', 'Potassium, K': 'Potassium',
            'Fatty acids, total saturated': 'Saturated fat', 'Selenium, Se': 'Selenium',
            'Sodium, Na': 'Sodium', 'Vitamin A, RAE': 'Vitamin A', 'Vitamin B-12': 'Vitamin B12',
            'Vitamin B-6': 'Vitamin B6', 'Vitamin C, total ascorbic acid': 'Vitamin C',
            'Vitamin D (D2 + D3)': 'Vitamin D', 'Vitamin E (alpha-tocopherol)': 'Vitamin E',
            'Vitamin K (phylloquinone)': 'Vitamin K', 'Zinc, Zn': 'Zinc',
            'Carbohydrate, by difference': 'Total carbohydrates'}
        df = pd.DataFrame()
        for i in arr_ingr:
            df = df.append(self.get_data(i))
        df = pd.pivot_table(df, index=['ingr'], columns=df['nutrientName'])
        df.columns = df.columns.droplevel([0])
        df.rename(col, axis='columns', inplace=True)
        return df

    def retrieve(self):
        needed_nutritions_df = self.df.loc[self.ingr]
        info = {}
        for i in range(needed_nutritions_df.shape[0]):
            ingridient = needed_nutritions_df.iloc[i].dropna()
            if ingridient.name not in info:
                info[ingridient.name] = ingridient
        return info

    def filter(self, must_nutrients, n):
        must_nutrients.sort_values(ascending=False, inplace=True)
        res = ''
        i = 0
        for name, item in zip(must_nutrients.index, must_nutrients.values):
            if i >= n:
                break
            if item >= 0.01:
                i += 1
                res += f"\n{name} - {item * 100:.0f}% of Daily Value"
        return res
