#include <iostream>
#include <vector>

// https://eolymp.com/problems/2664
// Сортування вставкою

int main() {
    int n;
    if (!(std::cin >> n) || n <= 0 || n > 100)
        return 1;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    for (int i = 1; i < n; ++i) {
        int current = arr[i];
        int j = i;
        while (j) {
            if (arr[j-1] > current)
                arr[j] = arr[j-1];
            else
                break;
            j--;
        }
        if (j != i) {
            arr[j] = current;
            for (j = 0; j < n; ++j) {
                std::cout << arr[j];
                std::cout << ((j == n-1) ? '\n' : ' ');
            }
        }
    }

    return 0;
}
