import pickle
from icecream import ic

def read_pkl(filename) -> list[dict[str, str| float]]:
    result = []
    with open(filename, "rb") as file:
        while True:
            try:
                result.append(
                    pickle.load(file)
                )
            except EOFError:
                break
    return result


if __name__ == "__main__":
    sticks = read_pkl("sticks.pkl")
    ic(sticks)
    ic(len(sticks))