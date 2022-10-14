from datetime import datetime
from collections import Counter, defaultdict

#-------------------------------#
#       Statistics class        #
#-------------------------------#

class Statistics:
    """
    Statistics utils
    """
    def average(values: list):
        """
        Get average value of values list
        """
        return sum(values) / len(values)

    def median(values: list):
        """
        Get median value of values list
        """
        if len(values) == 0:
            raise ValueError('provided list is empty')

        if len(values) == 1:
            return float(values[0])

        values = sorted(values)
        mid = int(len(values) / 2)
        if len(values) % 2:
            return float(values[mid])
        return (values[mid - 1] + values[mid]) / 2.0

    def variance(values: list):  # разброс оценок (дисперсия)
        """
        Calculate variance of values list
        """
        if len(values) == 0:
            raise ValueError('provided list is empty')

        if len(values) == 1:
            return 0

        values = sorted(values)
        return values[len(values) - 1] - values[0]


#-------------------------------#
#        Ratings class          #
#-------------------------------#

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    __csv_headers = ('userId','movieId','rating','timestamp')
    __csv_separator = ','
    __csv_types = (int, int, float, int)

    def __init__(self, path_to_the_file: str):
        self.filename = path_to_the_file

    def __parse_line(cls, data_line: str):
        splitted = data_line.split(cls.__csv_separator)
        return [cls.__csv_types[index](splitted[index]) 
                for index in range(len(cls.__csv_headers))]

    def get_next_data_line(self):
        """
        Read next data from file
        Yields:
            list with parsed values
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            line = file.readline()              # header line, ignore
            line = file.readline()              # first data line
            while line:
                yield self.__parse_line(line)
                line = file.readline()          # data line
    
    class Movies:
        """
        Analyzing movies data from ratings.csv
        """
        def __init__(self, ratings_cls, movies_cls: Movies):
            if not isinstance(ratings_cls, Ratings): # проверяем принадлежность экземпляра к классу
                raise ValueError('invalid Movies class object')
            if not isinstance(movies_cls, Movies): # проверяем принадлежность экземпляра к классу
                raise ValueError('invalid Movies class object')
            self.ratings = ratings_cls
            self.movies_cls = movies_cls

        def dist_by_year(self): # в каком году поставлена оценка (рейтинг)
            """
            The method returns the years distribution by ratings count,
            sorted by years ascendingly.

            Returns:
                dict: a dict where the keys are years and the values are counts of ratings
            """
            years_distribution = Counter() # количество оценок за каждый год

            for data in self.ratings.get_next_data_line():
                year = datetime.fromtimestamp(data[3]).year # извлекаем год из последнего столбца
                years_distribution[year] += 1

            return dict(sorted(years_distribution.items())) # от более ранних к более поздним


        def dist_by_rating(self): # количество оценок по каждому значению рейтинга (от 0.5 до 5.0)
            """
            The method returns the ratings distribution by counts,
            sorted by ratings ascendingly.

            Returns:
                dict: a dict where the keys are ratings and the values are counts
            """
            ratings_distribution = Counter()

            for data in self.ratings.get_next_data_line():
                ratings_distribution[data[2]] += 1

            return dict(sorted(ratings_distribution.items())) # от низких рейтингов к высоким

        def top_by_num_of_ratings(self, top_size: int): # фильмы с наибольшим количеством оценок
            """
            The method returns top-n movies by the number of ratings,
            sorted by numbers descendingly.

            Returns:
                dict: a dict where the keys are movie titles and the values are numbers
            """
            top_movies = Counter()

            for data in self.ratings.get_next_data_line():
                top_movies[self.movies_cls.get_movie_title(data[1])] += 1

            return dict(top_movies.most_common(top_size)) # наиболее часто встречающиеся элементы в порядке убывания встречаемости

        def top_by_ratings(self, n, metric=Statistics.average): # фильмы с наивысшими оценками (по средней)
            """
            The method returns top-n movies by the `average` or `median` of the ratings,
            sorted by metric descendingly.
			
            Returns:
                dict: a dict where the keys are movie titles and the values are metric values
            """
            all_movies = defaultdict(list)

            for data in self.ratings.get_next_data_line():
                all_movies[self.movies_cls.get_movie_title(data[1])].append(data[2])

            for movie in all_movies:
                all_movies[movie] = round(metric(all_movies[movie]), 2)

            return dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])

        def top_controversial(self, n):  # фильмы с наивысшим разбросом оценок
            """
            The method returns top-n movies by the variance of the ratings,
            sorted by variance descendingly.

            Returns:
                dict: a dict where the keys are movie titles and the values are the variances
            """
            all_movies = defaultdict(list)

            for data in self.ratings.get_next_data_line():
                all_movies[self.movies_cls.get_movie_title(data[1])].append(data[2])

            for movie in all_movies:
                all_movies[movie] = round(Statistics.variance(all_movies[movie]), 2)

            return dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])
        
    class Users(Movies):
        def dist_by_ratings_number(self): # распределение пользователей по количеству оценок
            """
            The method returns the distribution of users by the number of ratings made by them,
            sorted by ratings ascendingly.

            Returns:
                dict: a dict where the keys are users and the values are number of ratings
            """
            ratings_distribution = Counter()

            for data in self.ratings.get_next_data_line():
                ratings_distribution[data[0]] += 1

            return dict(sorted(ratings_distribution.items(), key=lambda item: item[1]))

        def dist_by_ratings_values(self, metric=Statistics.average): # распределение пользователей по величине оценок (по средней)
            """
            The method returns the distribution of users by `average` or `median` ratings made by them,
            sorted by ratings ascendingly.

            Returns:
                dict: a dict where the keys are users and the values are metric of ratings
            """
            all_ratings = defaultdict(list)

            for data in self.ratings.get_next_data_line():
                all_ratings[data[0]].append(data[2])

            for user in all_ratings:
                all_ratings[user] = round(metric(all_ratings[user]), 2)

            return dict(sorted(all_ratings.items(), key=lambda item: item[1]))

        def top_by_variance(self, n: int): # распределение пользователей по наивысшему разбросу оценок
            """
            The method returns top-n users with the biggest variance of their ratings,
            sorted by variance descendingly.

            Returns:
                dict: a dict where the keys are users and the values are the variances
            """
            all_ratings = defaultdict(list)

            for data in self.ratings.get_next_data_line():
                all_ratings[data[1]].append(data[2])

            for user in all_ratings:
                all_ratings[user] = round(Statistics.variance(all_ratings[user]), 2)

            return dict(sorted(all_ratings.items(), key=lambda item: item[1], reverse=True)[:n])
