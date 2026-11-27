#include <iostream>
#include <vector>

// https://eolymp.com/problems/972
// Сортування вибором

int main() {
    int n, hh, mm, ss;
    if (!(std::cin >> n) || n <= 0 || n > 100)
        return 1;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> hh >> mm >> ss;
        arr[i] = hh*3600 + mm*60 + ss;
    }

    for (int i = 0; i < n; ++i) {
        int minpos = i;
        for (int j = i; j < n; ++j) {
            if (arr[j] < arr[minpos])
                minpos = j;
        }
        if (minpos != i)
            std::swap(arr[i], arr[minpos]);
    }

    for (int i = 0; i < n; ++i) {
        hh = arr[i] / 3600;
        mm = arr[i] % 3600 / 60;
        ss = arr[i] % 60;
        std::cout << hh << ' ' << mm << ' ' << ss << '\n';
    }

    return 0;
}
