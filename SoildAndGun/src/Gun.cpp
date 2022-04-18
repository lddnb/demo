#include "Gun.h"
#include <iostream>

void Gun::addBullet(int num) {
    bullet_num += num;
}

bool Gun::shoot() {
    if (bullet_num <= 0) {
        std::cout << "no enough bullet" << std::endl;
        return false;
    }
    else {
        std::cout << "fire !!!" << std::endl;
        bullet_num -= 1;
        return true;
    }
}
