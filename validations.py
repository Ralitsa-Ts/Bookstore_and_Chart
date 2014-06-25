import re
import sys
sys.path.append("model")

from library import Library
from datetime import datetime


class Validations:
    @staticmethod
    def check_title(title):
        if re.match(r'[a-zA-Z0-9\s]+', title) is not None:
            return True
        return False

    @staticmethod
    def check_name(name):
        if re.match(r'^([A-Z]*[a-z]+\s*)+?$', name) is not None:
            return True
        return False

    @staticmethod
    def check_year(year):
        if re.match(r'\d+', year) is not None:
            current_year = datetime.now().year
            return int(year) in range(1000, current_year + 1)
        return False

    @staticmethod
    def check_genre(genre):
        genres = Library.genre_list()
        if genre in genres:
            return True
        return False

    @staticmethod
    def check_rating(rating):
        if rating == '' or re.match(r'\d+', rating) is not None:
            return True
        return False

    @staticmethod
    def check_copies(copies):
        if copies == '':
            return True
        elif re.match(r'\d+', copies) is not None and int(copies) > 0:
            return True
        return False

    @staticmethod
    def check_all(title, name, year, genre, rating='', copies=''):
        check = [Validations.check_title(title), Validations.check_name(name),
                 Validations.check_year(year), Validations.check_genre(genre),
                 Validations.check_rating(rating),
                 Validations.check_copies(copies)]

        data_list = ["Title", "Author's name", "Year of publication", "Genre",
                     "Rating", "Number of copies"]

        invalid_data = []
        for check_, data in zip(check, data_list):
            if check_ is False:
                invalid_data.append(data)
        return invalid_data

