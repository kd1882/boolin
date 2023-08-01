from flask_app.config.mysql_conn import connectToMySQL
from flask import flash


class Boolin:
    def __init__(self):
        self.db = None

    @staticmethod
    def boolean_search_generator(query, synonyms):
        terms = query.split()

        expanded_query = ""
        for term in terms:
            term_synonyms = synonyms.get(term.lower(), [])
            term_synonyms.append(term)
            synonyms_string = " OR ".join(f'"{s}"' for s in term_synonyms)
            expanded_query += f"({synonyms_string}) AND "

        expanded_query = expanded_query[:-5]

        return expanded_query
