#include <iostream>

// https://eolymp.com/problems/7452

class Node
{
public:
    int data;
    Node *next;
    Node() : next(NULL) {};
    Node(int data, Node *next = NULL) : data(data), next(next) {};
    // В умові сказано:
    // Ви можете створювати (використовувати) за необхідності додаткові методи
    void Print(void);           
    void PrintReverse(void);
};

class List 
{
public:
    Node *head, *tail;
    List() : head(NULL), tail(NULL) {};
    void addToTail(int val); // Додати число val в кінець Зв'язного Списку
    void Print(void); // Вивести елементи Зв'язного Списку
    void PrintReverse(void); // Вивести елементи Зв'язного Списку в зворотному порядку
};

void List::addToTail(int val)
{
    Node *oldTail = this->tail;
    Node *newTail = new Node(val, NULL);
    this->tail = newTail;
    if (oldTail) {
        oldTail->next = newTail;
    } else {
        this->head = newTail;
    }
}

void List::Print()
{
    if (this->head) {
        this->head->Print();
    }
    std::cout << '\n';
}

void List::PrintReverse()
{
    if (this->head) {
        this->head->PrintReverse();
    }
    std::cout << '\n';
}

void Node::Print()
{
    std::cout << this->data;
    if (this->next) {
        std::cout << ' ';
        this->next->Print();
    }
}

void Node::PrintReverse()
{
    if (this->next) {
        this->next->PrintReverse();
        std::cout << ' ';
    }
    std::cout << this->data;
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

    l.Print();
    l.PrintReverse();

    return 0;
}
