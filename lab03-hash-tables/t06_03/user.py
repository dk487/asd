
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class MyHashOverflow(Exception):
    pass

class MyOpenAddrHash:
    """ Реалізація специфічної хеш-таблиці з відкритою адресацією """
    def __init__(self, size: int):
        """ Ініціалізація
        :param size: кількість елементів в хеш-таблиці """
        assert size > 0
        # None означає відсутність елементу
        # False означає, що елемент був, але його видалили (tombstone)
        self.data = [None] * size

    def mkhash(self, key: str):
        """ Генерація хеша (int) зі строки
        :param key: довільна строкова змінна """
        # чи можна використати crc32? це ж не hash(), який заборонений
        # return zlib.crc32(key.encode('utf-8'))
        r = 0
        for c in key:
            r = (r * 31 + ord(c)) & 0xFFFFFFFF
        return r

    def add(self, key: str, value):
        """ Додавання елементу в хеш-таблицю
        :param key: строка, яка виступає ключем
        :param value: довільне значення елемента """
        i = start_i = self.mkhash(key) % len(self.data)
        tombstone = None
        while True:
            if self.data[i] is None:
                if tombstone is not None:
                    self.data[tombstone] = value
                else:
                    self.data[i] = value
                return
            if self.data[i] is False:
                if tombstone is None:
                    tombstone = i
            elif self.data[i] == value:
                return
            i = (i+1) % len(self.data)
            if i == start_i:
                if tombstone is not None:
                    self.data[tombstone] = value
                    return
                raise MyHashOverflow('No space left')

    def find(self, key: str):
        """ Пошук можливих елементів по ключу
        :param key: строка, яка виступає ключем """
        i = start_i = self.mkhash(key) % len(self.data)
        while True:
            if self.data[i] is None:
                return
            if self.data[i] is not False:
                yield self.data[i]
            i = (i+1) % len(self.data)
            if i == start_i:
                return

    def wipe(self, key: str, value):
        """ Видалення елементів з точним значенням
        :param key: строка, яка виступає ключем
        :param value: значення, яке підлягає видаленню """
        i = start_i = self.mkhash(key) % len(self.data)
        while True:
            if self.data[i] is None:
                return
            if self.data[i] is not False and self.data[i] == value:
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
hash_books = None

# хеш-таблиця по авторам (які у автора є книжки)
# вміст - масив ['Aвтор', [111, 222, 333]], де 111, 222, 333 - індекси
hash_authors = None


def mkkey(author, title):
    """ Будує ключ для хешування.
    :param author: Автор книги
    :param title: Назва книги """
    return author + title

def findAuthor(author):
    """ Пошук профайлу автора.
    :param author: Автор книги
    :return: масив, якщо автор є у бібліотеці та False у іншому разі """
    for profile in hash_authors.find(author):
        if profile[0] == author:
            return profile
    return False


def init():
    """ Ініціалізація або перебудова сховища та хеш-таблиць. """
    global big_pile, hash_books, hash_authors
    new_len = max(100, len(big_pile) * 10)
    old_pile = big_pile
    big_pile = []
    hash_books = MyOpenAddrHash(new_len)
    hash_authors = MyOpenAddrHash(new_len)
    for row in old_pile:
        if row is not False:
            addBook(row[0], row[1])

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    if find(author, title):
        return

    # чи прийшов час зробити rehash? ми можемо не чекати
    # заповнення хеш-таблиці, скажімо, на 50% вже цілком достатньо
    #if 2 * len(big_pile) > len(hash_books.data):
    #    init()

    try:
        big_pile.append([author, title])
        idx = len(big_pile) - 1
        hash_books.add(mkkey(author, title), idx)

        profile = findAuthor(author)
        if profile:
            hash_authors.wipe(author, profile)
            profile[1].append(idx)
            hash_authors.add(author, profile)
        else:
            hash_authors.add(author, [author, [idx]])
    except MyHashOverflow:
        init()
        addBook(author, title)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    for idx in hash_books.find(mkkey(author,title)):
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
    for idx in hash_books.find(key):
        if big_pile[idx] == value:
            big_pile[idx] = False
            hash_books.wipe(key, idx)
            profile = findAuthor(author)
            assert profile is not False
            hash_authors.wipe(author, profile)
            profile[1].remove(idx)
            hash_authors.add(author, profile)
            return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    result = []
    profile = findAuthor(author)
    if profile:
        for idx in profile[1]:
            result.append(big_pile[idx][1])
    result.sort()
    return result
