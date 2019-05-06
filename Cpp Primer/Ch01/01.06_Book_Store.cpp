/* Book Store */

#include <iostream>
#include"Sales_item.h"

int main() {
    Sales_item total;
    if (std::cin >> total) { 
        Sales_item trans;
        while (std::cin >> trans) {
            if (total.isbn() == trans.isbn()) {
                total = total + trans; 
            } else {
                std::cout << total << std::endl;
                total = trans;
            }
        }
        std::cout << total << std::endl;
        return 0;
    } else {
        std::cerr << "No data." << std::endl;
        return -1;
    }
}