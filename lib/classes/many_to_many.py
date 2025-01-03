class Article:
    all = []

    def __init__(self, author, magazine=None, title=None):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters long")
        
        self._title = title
        self._author = author
        self._magazine = magazine
    
        # self.magazine.add_article(self)
        self.author.add_article(self)

        # Adding the article to the list of all articles
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise Exception("Title must be between 5 and 50 characters long")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = value

    @classmethod
    def get_all_articles(cls):
        return cls.all


class Author:
    def __init__(self, name, magazine=None, title="None"):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must not be empty")

        self._name = name
        self._articles = []
        self._magazine=magazine
        self._title=title

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def add_article(self,magazine,title):
        """
        Creates and adds an article to the author's list of articles.
        """
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("Title must be between 5 and 50 characters")

        # Create the article
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters")
        
        if not isinstance(category, str):
            raise Exception("Category must be a string")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        self._category = value

    def add_article(self, article):
       self._articles.append(article)
        # return article

    def articles(self):
        return self._articles
