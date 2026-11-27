#include <iostream>

// https://eolymp.com/problems/7468

/**
 * NOTE: здається, в описі задачі є проблема з форматуванням
 *
 * NOTE: в умові лабораторної роботи вказано наступне:
 * 
 * >  Вказівка 1. У завданнях 15.5 та 15.7 має бути реалізований
 * >  та використаний один з різновидів зв'язного списку
 * >  (однозв'язний, двозв`язний, кільцевий або з поточним
 * >  елементом), навіть, якщо це суперечить вимогам задачі
 * >  на порталі Eolymp.
 * 
 * Це можна зрозуміти таким чином, що 15.5 та 15.7 мають
 * використовувати різні типи списків; хоча це не стверджується
 * явним чином, але мені здається що буде безпечніше зробити
 * два різних типи списку (15.5 - однозв'язний, 15.7 - двозв'язний).
 */


class Node
{
public:
    int data;
    Node *prev;
    Node *next;
    Node() : prev(NULL), next(NULL) {};
    Node(int data, Node *prev = NULL, Node *next = NULL) : data(data), prev(prev), next(next) {};
};

class List 
{
public:
    Node *head, *tail;
    List() : head(NULL), tail(NULL) {};
    void addToTail(int val); // Додати число val в кінець зв'язного Списку
    void ReorderList(void); // Перевпорядкувати список, як описано вище 
    void Print(void); // Вивести елементи зв'язного Списку
};

void List::addToTail(int val)
{
    Node *oldTail = this->tail;
    Node *newTail = new Node(val, oldTail, NULL);
    this->tail = newTail;
    if (oldTail) {
        oldTail->next = newTail;
    } else {
        this->head = newTail;
    }
}

void List::ReorderList()
{
    Node *first = this->head;
    Node *second;
    Node *moving = this->tail;

    if (!first) {
        return;
    }

    second = first->next;

    while (first && second && (moving != second)) {
        second = first->next;

        // відрізали останній елемент від хвоста
        this->tail = moving->prev;
        this->tail->next = NULL;

        // вставили відрізаний між first та second
        moving->prev = first;
        moving->next = second;
        first->next = moving;
        second->prev = moving;

        first = second;
        second = first->next;
        moving = this->tail;
    }
}

void List::Print()
{
    Node *current = this->head;
    while (current) {
        std::cout << current->data;
        current = current->next;
        if (current) {
            std::cout << ' ';
        }
    }
    std::cout << '\n';
}

int main() {
    int value, n = 0;
    List l;

    if (!(std::cin >> n) || n <= 0) {
        return 1;
    }

    while (n--) {
        std::cin >> value;
        l.addToTail(value);
    }

    l.ReorderList();
    l.Print();

    return 0;
}
