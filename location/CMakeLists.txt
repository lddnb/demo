cmake_minimum_required(VERSION 2.8.3)
project(location)

set(CMAKE_BUILD_TYPE Deubg)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

add_compile_options(-std=c++14)
add_definitions(-std=c++11)


include_directories(${PROJECT_SOURCE_DIR}/include)

#catkin
find_package(catkin REQUIRED COMPONENTS
    roscpp
    std_msgs
    pcl_ros
    tf
    eigen_conversions
)
include_directories(${catkin_INCLUDE_DIRS})



#Eigen3
#include_directories(${PROJECT_SOURCE_DIR}/third_party/eigen3)
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

#PCL
find_package(PCL 1.7 REQUIRED)
list(REMOVE_ITEM PCL_LIBRARIES "vtkproj4")
include_directories(${PCL_INCLUDE_DIRS})

#Glog
find_package(Glog REQUIRED)
include_directories(${GLOG_INCLUDE_DIR})

#GeographicLib
add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/GeographicLib)
include_directories(${PROJECT_SOURCE_DIR}/third_party/GeographicLib/include)

set(ALL_TARGET_LIBRARIES 
    ${catkin_LIBRARIES}
    ${EIGEN3_LIBS}
    ${PCL_LIBRARIES}
    #${GLOG_LIBRARIES}
    glog
    libGeographiccc
)

file(GLOB_RECURSE ALL_SRCS "*.cpp")
file(GLOB_RECURSE NODE_SRCS "src/*_node.cpp")
file(GLOB_RECURSE THIRD_PARTY_SRCS "third_party/*.cpp")
file(GLOB_RECURSE MAKE_FILE "CMakeCXXCompilerId.cpp")
list(REMOVE_ITEM ALL_SRCS ${NODE_SRCS})
list(REMOVE_ITEM ALL_SRCS ${THIRD_PARTY_SRCS})
list(REMOVE_ITEM ALL_SRCS ${MAKE_FILE})


message("ALL_SRCS = " ${ALL_SRCS})

add_executable(test_frame_node src/test_frame_node.cpp ${ALL_SRCS})
target_link_libraries(test_frame_node ${ALL_TARGET_LIBRARIES})

