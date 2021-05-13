from string import punctuation
from re import sub


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
        self.delete_useless_symbols()
        self.make_text_columns()
        self.text_preprocessing()

    def delete_useless_symbols(self):
        self.df.article = self.df.article.apply(lambda x: x.replace("\n", ""))

    def make_text_columns(self):
        self.df["text"] = self.df.short_article_name + self.df.article

    def text_preprocessing(self):
        self.df["text"] = self.df.text.apply(
            lambda x: sub(
                r"[0-9]+",
                "",
                "".join(
                    [
                        word.lower()
                        for word in x
                        if word not in set(str(punctuation) + "«»—-")
                    ]
                ),
            )
        )
