
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
            if self.data[i] is None:
                if thombstone is not None:
                    self.data[thombstone] = value
                else:
                    self.data[i] = value
                return
            if self.data[i] is False:
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
            elif self.data[i] is not False and self.data[i] == value:
                self.data[i] = False
                return
            i = (i+1) % len(self.data)
            if i == start_i:
                return


# сховище елементів вигляду ['Автор', 'Книга'] або False
# елементи тільки додаються в кінець, непотрібні заміняються на False
big_pile = []

# хеш-таблиця по авторам та назвам книжок
# вміст - індекс книги в big_pile
h_ab = None

# хеш-таблиця по авторам (які у автора є книжки)
# вміст - масив ['Aвтор', [111, 222, 333]], де 111, 222, 333 - індекси
h_a = None


def mkkey(author, title):
    # це буде використано для хешування, чи не так?
    # а колізіями хай сама хеш-таблиця займається
    return author + title


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global big_pile, h_ab, h_a
    new_len = max(100, len(big_pile) * 10)
    old_pile = big_pile
    big_pile = []
    h_ab = MyOpenAddrHash(new_len)
    h_a = MyOpenAddrHash(new_len)
    for row in old_pile:
        if row is not False:
            addBook(row[0], row[1])


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    if find(author, title) == True:
        return

    # чи прийшов час зробити rehash?
    # заповнення хеш-таблиці на 50% вже цілком достатньо
    if 2 * len(big_pile) > len(h_ab.data):
        init()

    big_pile.append([author, title])
    idx = len(big_pile) - 1
    h_ab.add(mkkey(author, title), idx)

    for author_books in h_a.find(author):
        if author_books[0] == author:
            h_a.wipe(author, author_books)
            author_books[1].append(idx)
            h_a.add(author, author_books)
            return

    # це перша книга цього автора?
    h_a.add(author, [author, [idx]])


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
    value = [author, title]
    for idx in h_ab.find(key):
        if big_pile[idx] == value:
            big_pile[idx] = False
            h_ab.wipe(key, idx)
            for author_books in h_a.find(author):
                if author_books[0] == author:
                    h_a.wipe(author, author_books)
                    author_books[1].remove(idx)
                    h_a.add(author, author_books)
                    return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    # python3 main.py  2,29s user 0,01s system 99% cpu 2,299 total
    result = []
    for author_books in h_a.find(author):
        if author_books[0] == author:
            for idx in author_books[1]:
                result.append(big_pile[idx][1])
    result.sort()
    return result

