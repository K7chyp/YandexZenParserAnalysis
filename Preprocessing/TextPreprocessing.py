from string import punctuation
from re import sub
from pymystem3 import Mystem
from SubFunctions import get_list_of_stopwords


class TextPreprocessing:
    def __init__(self, df):
        self.df = df.copy()
        self.df.columns = [
            "short_article_name",
            "article",
            "author",
            "publish_date",
            "href",
        ]
        self.apply_preprocessing_for_text()

    def delete_useless_symbols(self):
        self.df.article = self.df.article.apply(lambda x: x.replace("\n", ""))

    def make_text_columns(self):
        self.df["text"] = self.df.short_article_name + self.df.article

    def delete_punctuation_and_make_words_lower(self):
        self.df["text"] = self.df.text.apply(
            lambda x: sub(
                r"[0-9]+",  # clear all numbers
                "",
                "".join(
                    [
                        word.lower()  # Word -> word
                        for word in x
                        if word not in set(str(punctuation) + "«»—-")
                    ]  # clear punctuation
                ),
            )
        )

    def delete_stopwords(self):
        stopwords = get_list_of_stopwords()
        self.df["text"] = self.df.text.apply(
            lambda local_text: " ".join(
                [word for word in local_text.split() if word not in stopwords]
            )
        )

    def apply_lemmatization_for_text(self):
        m = Mystem()
        self.df["text"] = self.df.text.apply(lambda text: "".join(m.lemmatize(text)))
    
    def split_text_for_words(self): 
        self.df['text_spit'] = self.df.text.apply(lambda text: text.split())

    def apply_preprocessing_for_text(self): 
        self.delete_useless_symbols()
        self.make_text_columns()
        self.delete_punctuation_and_make_words_lower()
        self.delete_stopwords()
        self.apply_lemmatization_for_text()
        self.split_text_for_words()