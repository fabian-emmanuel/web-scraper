from locators.quote_locators import QuoteLocators

class QuoteParser:
    """
    Class to find out the data of a quote div
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.content} \n -> by {self.author} \n\n'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select_one(locator)]