
#include <iostream>


int main() {
    double x;
    std::cout << "Enter a double value x" << std::endl;
    std::cin >> x;

    int count = 0;

    for (double i = x; i >= 2; i /= 2) {
        count++;
    }

    std::cout << "It takes " << count << " times for x to be less than 2." << std::endl;

    return 0;
}

