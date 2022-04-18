cmake_minimum_required(VERSION 3.0)

project(SoilderAndGun)

add_compile_options("-std=c++11")

set(CMAKE_BUILD_TYPE Debug)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

set( LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

add_library(Soilder_lib STATIC src/Soilder.cpp)

add_library(Gun_lib STATIC src/Gun.cpp)

target_include_directories(Soilder_lib PUBLIC ${PROJECT_SOURCE_DIR}/include)

target_include_directories(Gun_lib PUBLIC ${PROJECT_SOURCE_DIR}/include)

add_executable(SoilderAndGun main.cpp)

target_link_libraries(SoilderAndGun Soilder_lib Gun_lib)
