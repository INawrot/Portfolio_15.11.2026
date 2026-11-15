using Random 

function miller_rabin(n::Integer, k::Int=1000)
    if n < 2 return false end
    if n == 2 || n == 3 return true end
    if n % 2 == 0 return false end
    d = n - 1
    s = 0
    while d % 2 == 0
        d ÷= 2
        s += 1
    end
    for _ in 1:k
        a = rand(2:n-2)
        x = powermod(a, d, n)
        if x == 1 || x == n - 1
            continue
        end
        composite = true
        for _ in 1:s-1
            x = powermod(x, 2, n)
            if x == n - 1
                composite = false
                break
            end
        end
        if composite
            return false 
        end
    end
    return true 
end

function measure_time(n::Integer, k::Int=100)
    stats = @timed miller_rabin(n, k)
    return stats.value, stats.time
end

function save_results(start_n::Integer, m::Int, filename::String="wyniki.txt")
    open(filename, "w") do io
        println(io, "Wyniki testu dla $m liczb od $start_n:")
        println(io, "--------------------------------------------------")
        
        total_time = @elapsed begin
            for i in 0:(m - 1)
                current_n = start_n + i
                is_prime = miller_rabin(current_n)
                status = is_prime ? "Pierwsza" : "Złożona"
                println(io, "Liczba: $current_n | Wynik: $status")
            end
        end
        
        println(io, "--------------------------------------------------")
        println(io, "Całkowity czas operacji: $(round(total_time, digits=4)) sekundy")
    end
end


n_start = 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
m_count = 5000

save_results(n_start, m_count, "test_pierwszosci.txt")
wynik, czas = measure_time(123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789)