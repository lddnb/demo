#pragma once
#include <string>

class Gun {
public:
    Gun(std::string _gun_name):gun_name(_gun_name), bullet_num(0){} 

    void addBullet(int num);
    bool shoot();
private:
    int bullet_num;
    std::string gun_name;
};