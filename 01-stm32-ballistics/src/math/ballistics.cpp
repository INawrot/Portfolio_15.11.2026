#include "ballistics.h"
#include <fstream>
#include <sstream>
#include <cmath>
#include <iostream>

Vector2D BallisticsEngine::predictTrajectory(const FlightSample& sample, float dt_future, float total_duration) {
    float v0 = sample.accel * sample.timestamp;
    if (v0 < 0.1f) v0 = 50.0f;

    Vector2D pos = { 0.0f, 0.0f };
    Vector2D vel = { v0 * std::cos(sample.angle), v0 * std::sin(sample.angle) };
    Vector2D wind = { sample.wind_speed * std::cos(sample.wind_angle), sample.wind_speed * std::sin(sample.wind_angle) };

    float t = 0.0f;
    while (t < total_duration && pos.y >= -0.01f) {
        Vector2D v_rel = { vel.x - wind.x, vel.y - wind.y };
        float v_mag = std::sqrt(v_rel.x * v_rel.x + v_rel.y * v_rel.y);

        float f_drag = 0.5f * drag_coef * sample.air_density * v_mag * v_mag;

        float ax = 0.0f;
        float ay = -g;

        if (v_mag > 0.0f && sample.projectile_mass > 0.0f) {
            ax -= (f_drag * (v_rel.x / v_mag)) / sample.projectile_mass;
            ay -= (f_drag * (v_rel.y / v_mag)) / sample.projectile_mass;
        }

        pos.x += vel.x * dt_future;
        pos.y += vel.y * dt_future;
        vel.x += ax * dt_future;
        vel.y += ay * dt_future;
        t += dt_future;
    }
    return pos;
}

std::vector<FlightSample> DataLoader::loadFromCSV(const std::string& filename) {
    std::vector<FlightSample> samples;
    std::ifstream file(filename);
    if (!file.is_open()) return samples;

    std::string line;
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string val;
        FlightSample sample;

        std::getline(ss, val, ','); sample.timestamp = std::stof(val);
        std::getline(ss, val, ','); sample.accel = std::stof(val);
        std::getline(ss, val, ','); sample.angle = std::stof(val);
        std::getline(ss, val, ','); sample.wind_speed = std::stof(val);
        std::getline(ss, val, ','); sample.wind_angle = std::stof(val);
        std::getline(ss, val, ','); sample.air_density = std::stof(val);
        std::getline(ss, val, ','); sample.projectile_mass = std::stof(val);

        samples.push_back(sample);
    }
    return samples;
}