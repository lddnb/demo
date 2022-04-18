#include "Soilder.h"

Soilder::Soilder(std::string _soilder_name):soilder_name(_soilder_name) {}

void Soilder::addBulletToGun(int num) {
    gun->addBullet(num);
}

bool Soilder::fire() {
    return gun->shoot();
}

void Soilder::addGun(std::unique_ptr<Gun> _gun) {
    gun = move(_gun);
}
