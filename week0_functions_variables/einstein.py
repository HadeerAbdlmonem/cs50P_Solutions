"""Compute energy (in joules) from mass (in kilograms) using E = mc^2."""

SPEED_OF_LIGHT_M_S = 300_000 * 1000  # ~3 x 10^8 m/s


def main():
    mass = int(input("Mass: "))
    energy = mass * SPEED_OF_LIGHT_M_S ** 2
    print(energy)


if __name__ == "__main__":
    main()
