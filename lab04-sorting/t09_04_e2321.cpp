#include <iostream>
#include <vector>

// https://eolymp.com/problems/2321
// Швидке сортування

void qsort(std::vector<int>& arr, int a, int b) {
    int left = a, right = b, pivot;
    if (a >= b)
        return;
    pivot = arr[a + ((b - a) >> 1)];
    while (true) {
        while (arr[left] < pivot)
            left++;
        while (pivot < arr[right])
            right--;
        if (left >= right)
            break;
        std::swap(arr[left], arr[right]);
        left++;
        right--;
    }
    qsort(arr, a, right);
    qsort(arr, right + 1, b);
}

int main() {
    int n;
    if (!(std::cin >> n) || n <= 0 || n > 1000)
        return 1;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i)
        std::cin >> arr[i];
    
    qsort(arr, 0, n-1);

    for (int i = 0; i < n; ++i)
        std::cout << arr[i] << ((i == n-1) ? '\n' : ' ');

    return 0;
}
