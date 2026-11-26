
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""


class MyOpenAddrHash:
    def __init__(self, size: int):
        assert size > 0
        # None означає відсутність елементу
        # False означає, що елемент був, але його видалили (thombstone)
        self.data = [None] * size

    def mkhash(self, key: str):
        # чи можна використати crc32? це ж не hash(), який явно заборонений
        # return zlib.crc32(key.encode('utf-8'))
        r = 0
        for c in key:
            r = (r * 31 + ord(c)) & 0xFFFFFFFF
        return r

    def add(self, key: str, value: int):
        i = start_i = self.mkhash(key) % len(self.data)
        thombstone = None
        while True:
            cell = self.data[i]
            if cell is None:
                if thombstone is not None:
                    self.data[thombstone] = value
                else:
                    self.data[i] = value
                return
            if cell is False:
                if thombstone is None:
                    thombstone = i
            elif self.data[i] == value:
                return
            i = (i+1) % len(self.data)
            if i == start_i:
                if thombstone is not None:
                    self.data[thombstone] = value
                    return
                raise Exception('No space left')

    def find(self, key: str):
        i = start_i = self.mkhash(key) % len(self.data)
        while True:
            if self.data[i] is None:
                return
            elif self.data[i] is not False:
                yield self.data[i]
            i = (i+1) % len(self.data)
            if i == start_i:
                return

    def wipe(self, key: str, value: int):
        i = start_i = self.mkhash(key) % len(self.data)
        while True:
            if self.data[i] is None:
                return
            elif self.data[i] == value:
                self.data[i] = False
                return
            i = (i+1) % len(self.data)
            if i == start_i:
                return


big_pile = []
h_ab = MyOpenAddrHash(10000)


def mkkey(author, title):
    # це буде використано для хешування, чи не так?
    # а колізіями хай сама хеш-таблиця займається
    return author + title


def init():
    """ Викликається 1 раз на початку виконання програми. """
    pass


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    if find(author, title) == False:
        big_pile.append([author, title])
        h_ab.add(mkkey(author, title), len(big_pile) - 1)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    for idx in h_ab.find(mkkey(author,title)):
        if big_pile[idx][0] == author and big_pile[idx][1] == title:
            return True
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    key = mkkey(author, title)
    for idx in h_ab.find(key):
        if big_pile[idx][0] == author and big_pile[idx][1] == title:
            big_pile[idx] = False
            h_ab.wipe(key, idx)
            return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    # для початку, повним перебором
    # python3 main.py  9,18s user 0,02s system 99% cpu 9,196 total
    result = []
    for book in big_pile:
        if book is not False and book[0] == author:
            result = result + [book[1]]
    result.sort()
    return result

