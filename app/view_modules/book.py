class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['publisher']
        self.image = 'https://images.weserv.nl/?url=' + data['image']
        self.price = '￥' + data['price'] if data['price'] else data['price']
        self.pubdate = data['pubdate']
        self.summary = data['summary']
        self.pages = data['pages'] or '未知'
        self.isbn = data['isbn13']
        self.binding = data['binding'] or '未知'

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, ex_book, keyword):
        self.total = ex_book.total
        self.books = [BookViewModel(book) for book in ex_book.books]
        self.keyword = keyword


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword

        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__book_cut_data(data)]

        return returned

    @classmethod
    def package_collections(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword

        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__book_cut_data(book) for book in data['books']]

        return returned

    @classmethod
    def __book_cut_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': ','.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
