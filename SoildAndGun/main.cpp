#include "Gun.h"
#include "Soilder.h"
#include <iostream>

void test() {
    Soilder sanduo("xusanduo");
    sanduo.addGun(std::unique_ptr<Gun>(new Gun("AK47")));
    sanduo.addBulletToGun(10);
    sanduo.fire();
}

int main() {
    std::cout << "cmake test!" << std::endl;
    test();
    return 0;
}