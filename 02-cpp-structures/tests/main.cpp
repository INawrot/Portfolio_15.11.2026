#include <structures/linked_list.h>
#include <structures/stack.h>
#include <structures/queue.h>
#include <structures/binary_tree.h>
#include <structures/max_heap.h>
#include <iostream>

int main() {
    std::cout << "=== URUCHOMIENIE OSOBNEJ APLIKACJI TESTOWEJ ===\n";

    Stack<int> s;
    s.push(42);
    std::cout << "Dziala! Top: " << s.top() << "\n";

    return 0;
}