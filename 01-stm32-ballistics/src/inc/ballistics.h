#ifndef BALLISTICS_H
#define BALLISTICS_H

#include <string>
#include <vector>

struct FlightSample {
    float timestamp;
    float accel;
    float angle;
    float wind_speed;
    float wind_angle;
    float air_density;
    float projectile_mass;
};

struct Vector2D {
    float x;
    float y;
};

class BallisticsEngine {
private:
    const float g = 9.81f;
    const float drag_coef = 0.1f;

public:
    BallisticsEngine() = default;
    Vector2D predictTrajectory(const FlightSample& sample, float dt_future, float total_duration);
};

class DataLoader {
public:
    static std::vector<FlightSample> loadFromCSV(const std::string& filename);
};

#endif