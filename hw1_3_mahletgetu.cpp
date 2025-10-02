#include <iostream>

bool isPerfect(int n) {
    int sum = 1;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) sum += i;
    }
    return n > 1 && sum == n;
}

int main() {
    for (int i = 2; i <= 9999; i++) {
        if (isPerfect(i)) std::cout << i << std::endl;
    }
    return 0;
}
