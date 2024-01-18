#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, int> mp;

    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        if (mp.find(s) == mp.end()) {
            mp[s] = i;
        }
    }
    vector<pair<string, int>> result;
    for (const auto &entry : mp) {
        result.push_back(entry);
    }

    sort(result.begin(), result.end());

    for (const auto &entry : result) {
        cout << entry.first << " " << entry.second << endl;
    }

    return 0;
}