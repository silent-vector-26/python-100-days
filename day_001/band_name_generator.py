def generate_band_name(city: str, pet_name: str) -> str:
    return f"{city} {pet_name}"


def main() -> None:
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print(f"Your band name could be {generate_band_name(city, pet_name)}")


if __name__ == "__main__":
    main()
