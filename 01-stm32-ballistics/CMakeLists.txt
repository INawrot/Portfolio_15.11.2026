cmake_minimum_required(VERSION 3.15)
project(BallisticsSimulation CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(src/inc)

add_executable(${PROJECT_NAME}
        src/main.cpp
        src/math/ballistics.cpp
)