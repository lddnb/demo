# pragma once

#include "Gun.h"
#include <memory>

class Soilder {
public:
    Soilder(std::string _soilder_name);
    void addGun(std::unique_ptr<Gun> _gun);
    void addBulletToGun(int num);
    bool fire();
private:
    std::string soilder_name;
    std::unique_ptr<Gun> gun;
};
