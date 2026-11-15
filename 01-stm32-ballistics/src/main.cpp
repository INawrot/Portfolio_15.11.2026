#include "ballistics.h"
#include <iostream>
#include <iomanip>

int main() {
    std::string filename = "flight_data.csv";
    std::vector<FlightSample> dataset = DataLoader::loadFromCSV(filename);

    if (dataset.empty()) {
        std::cerr << "Blad: Brak pliku csv lub plik jest pusty." << std::endl;
        return 1;
    }

    BallisticsEngine engine;

    std::cout << std::setw(8) << "Czas[s]"
              << std::setw(12) << "Przysp[m/s2]"
              << std::setw(10) << "Kat[rad]"
              << std::setw(12) << "Wiatr[m/s]"
              << std::setw(12) << "KatWiatru"
              << std::setw(15) << "Pred.Upadku_X"
              << std::setw(15) << "Pred.Upadku_Y" << std::endl;

    for (const auto& sample : dataset) {
        Vector2D impact = engine.predictTrajectory(sample, 0.01f, 10.0f);
        std::cout << std::fixed << std::setprecision(2)
                  << std::setw(8) << sample.timestamp
                  << std::setw(12) << sample.accel
                  << std::setw(10) << sample.angle
                  << std::setw(12) << sample.wind_speed
                  << std::setw(12) << sample.wind_angle
                  << std::setw(15) << impact.x
                  << std::setw(15) << impact.y << std::endl;
    }
    return 0;
}