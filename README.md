# Portfolio Inżynierii Oprogramowania

Repozytorium zawiera zaawansowane projekty inżynierskie demonstrujące moje umiejętności w zakresie systemów embedded, niskopoziomowej optymalizacji kodu, algorytmiki oraz integracji systemów z bazami danych.

---

## Przegląd Projektów

### 1. Wydajnościowa Symulacja Balistyczna (C++ / STM32)
* **Lokalizacja:** `/01-stm32-ballistics`
* **Opis:** Implementacja algorytmu symulacji balistycznej w czasie rzeczywistym, zoptymalizowana pod kątem mikrokontrolerów z rodziny STM32 (rdzenie ARM Cortex-M). Program przetwarza serie danych pomiarowych (20 rekordów) i generuje precyzyjne tabele wyników.
* **Wykorzystane technologie:** C++, programowanie niskopoziomowe (Bare-metal / HAL), optymalizacja zmiennoprzecinkowa (FPU), CMake/Make.
* **Czego mnie to nauczyło:** Efektywnego zarządzania ograniczonymi zasobami sprzętowymi (RAM/Flash), profilowania kodu pod kątem wydajności mikroprocesorów oraz debugowania sprzętowego.

### 2. Modułowa Biblioteka Struktur Danych (C++17)
* **Lokalizacja:** `/02-cpp-structures`
* **Opis:** Implementacja od zera podstawowych struktur danych (`Stack`, `Queue`, `LinkedList`, `BinaryTree`, `MaxHeap`) jako nowoczesnej biblioteki typu *Header-Only*.
* **Wykorzystane technologie:** C++17, szablony (Templates), CMake (zarządzanie modułami przez powiązania `INTERFACE`), dynamiczna alokacja pamięci.
* **Czego mnie to nauczyło:** Głębokiego zrozumienia paradygmatu RAII, unikania wycieków pamięci bez użycia gotowych kontenerów biblioteki standardowej oraz modularnej konfiguracji CMake.

### 3. Integracja Relacyjnych Baz Danych (Python)
* **Lokalizacja:** `/03-python-sql`
* **Opis:** System automatyzacji zadań i operacji na danych strukturyzowanych wykorzystujący relacyjną bazę danych i zapytania SQL.
* **Wykorzystane technologie:** Python 3, SQL, SQLite/PostgreSQL, operacje CRUD.
* **Czego mnie to nauczyło:** Projektowania schematów bazodanowych, optymalizacji zapytań (indeksy, transakcje) oraz bezpiecznego łączenia logiki aplikacji z warstwą persystencji danych.

### 4. Test Probabilistyczny Millera-Rabina (Julia)
* **Lokalizacja:** `/04-julia-algorithms`
* **Opis:** Wysoko wydajna implementacja algorytmu Millera-Rabina do testowania pierwszości bardzo dużych liczb, wykorzystywanego w nowoczesnej kryptografii.
* **Wykorzystane technologie:** Julia, typy bezznakowe wysokiej precyzji, optymalizacja numeryczna.
* **Czego mnie to nauczyło:** Matematycznego podejścia do optymalizacji algorytmów, unikania alokacji wewnątrz pętli krytycznych oraz programowania w środowisku obliczeń naukowych o wysokiej wydajności.

---

## Jak uruchomić projekty?

Każdy podfolder zawiera dedykowaną instrukcję uruchomienia i wymagania systemowe:
* **STM32:** Projekt skonfigurowany pod toolchain `arm-none-eabi-gcc`. Możliwość uruchomienia w środowisku STM32CubeIDE lub CLion (z wykorzystaniem OpenOCD).
* **C++:** Wymagany kompilator zgodny z C++17 oraz CMake (wersja min. 3.15). Uruchomienie poprzez profil `structures_test`.
* **Python:** Wymagane zainstalowanie zależności: `pip install -r requirements.txt`.
* **Julia:** Wymagane środowisko Julia. Uruchomienie poleceniem `julia src/main.jl`.
