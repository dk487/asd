#include <iostream>
#include <vector>
#include <queue>

int main() {
    int n, m, k;
    if (!(std::cin >> n >> m) || n <= 0 || m < n-1)
        return 1;

    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> dist(n + 1, -1);
    std::queue<int> q;

    for (int i = 0; i < m; ++i) {
        int u, v;
        std::cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    if (!(std::cin >> k) || k <= 0)
        return 1;

    for (int i = 0; i < k; ++i) {
        int arson;
        std::cin >> arson;
        dist[arson] = 0;
        q.push(arson);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : graph[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    int max_time = -1;
    int last_vertex = -1;
    for (int v = 1; v <= n; ++v) {
        if (dist[v] > max_time) {
            max_time = dist[v];
            last_vertex = v;
        }
    }

    std::cout << max_time << '\n';
    std::cout << last_vertex << '\n';

    return 0;
}
