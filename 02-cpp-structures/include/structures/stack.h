#ifndef STACK_H
#define STACK_H

#include <vector>
#include <stdexcept>

template <typename T>
class Stack {
private:
    std::vector<T> elements;

public:
    void push(T val) { elements.push_back(val); }

    void pop() {
        if (elements.empty()) throw std::underflow_error("Stos jest pusty!");
        elements.pop_back();
    }

    T top() const {
        if (elements.empty()) throw std::underflow_error("Stos jest pusty!");
        return elements.back();
    }

    bool empty() const { return elements.empty(); }
};

#endif