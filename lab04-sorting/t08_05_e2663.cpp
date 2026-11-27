#include <iostream>
#include <vector>

int main() {
    int n, count = 0, sorted;
    if (!(std::cin >> n) || n <= 0)
        return 1;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    do {
        sorted = 1;
        for (int i = 1; i < n; ++i) {
            if (arr[i-1] > arr[i]) {
                std::swap(arr[i-1], arr[i]);
                sorted = 0;
                count++;
            }
        }
    } while (!sorted);

    std::cout << count << '\n';
    return 0;
}
