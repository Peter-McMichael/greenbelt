import matplotlib.pyplot as plt
import math

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
                

prime_list = []


def generate_primes(limit):
    for i in range (0, limit):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
        


def plot_graph(primes):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")

    max_prime = max(primes)

    max_radius = int(math.sqrt(max_prime)) + 1

    for prime in primes:
        angle = prime * (math.pi / 180)

        radius = math.sqrt(prime)

        x=radius*math.cos(angle)
        y=radius * math.sin(angle)

        ax.plot(x, y, "m*")
    
    ax.set_facecolor("black")
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    plt.title("Prime Numbers in a Spiral Pattern")
    plt.grid(True)
    plt.show()


limit = int(input("Limit: "))
generate_primes(limit)
plot_graph(prime_list)
# plot_graph(primes)


