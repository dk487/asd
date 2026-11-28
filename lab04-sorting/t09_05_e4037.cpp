#include <iostream>
#include <vector>
#include <cstdint>

// https://eolymp.com/problems/4037
// Сортування злиттям

void merge(std::vector<std::uint64_t>& arr, int left, int mid, int right) {
    std::vector<std::uint64_t> temp;
    int i = left;
    int j = mid + 1;
    while (i <= mid && j <= right) {
        if ((arr[i] >> 32) <= (arr[j] >> 32)) {
            temp.push_back(arr[i]);
            i++;
        } else {
            temp.push_back(arr[j]);
            j++;
        }
    }
    while (i <= mid) {
        temp.push_back(arr[i]);
        i++;
    }
    while (j <= right) {
        temp.push_back(arr[j]);
        j++;
    }
    for (unsigned int k = 0; k < temp.size(); k++) {
        arr[left + k] = temp[k];
    }
}

void mergeSort(std::vector<std::uint64_t>& arr, int left, int right) {
    if (left >= right)
        return;
    int mid = left + ((right - left) >> 1);
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

int main() {
    int n;
    std::uint32_t pri, sec;
    if (!(std::cin >> n) || n <= 0 || n > 100000)
        return 1;

    std::vector<std::uint64_t> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> pri >> sec;
        arr[i] = (std::uint64_t(pri) << 32) + sec;
    }
    
    mergeSort(arr, 0, n-1);

    for (int i = 0; i < n; ++i) {
        pri = arr[i] >> 32;
        sec = arr[i] & 0xffffffff;
        std::cout << pri << ' ' << sec << '\n';
    }

    return 0;
}
