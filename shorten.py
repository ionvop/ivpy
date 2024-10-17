import sys
import os
import time


def main() -> None:
    data = open("shorten.ivpy").read()
    data = shorten(data)
    open("shorten_output.ivpy", "w").write(data)


def shorten(data: str) -> str:
    result = ""
    i = 0
    is_string = False

    while i < len(data):
        char = data[i]

        if is_string and char == "\\":
            result += f"\\{data[i + 1]}"
            i += 2
            continue

        if char == "\"":
            is_string = not is_string

        if is_string == False:
            if char == ":":
                i += 1
                start = i
                char = data[i]

                if char == "?":
                    result += ":?"
                    i += 1
                    continue

                while True:
                    char = data[i]

                    if char in [" ", "\t", "\n"]:
                        i += 1
                        continue

                    if char == "?":
                        result += ": ?"
                        break

                    result += ":"
                    i = start - 1
                    break

                i += 1
                continue

            if char in [" ", "\t", "\n"]:
                i += 1
                continue

        result += char
        i += 1

    return result


def test() -> None:
    while True:
        data = open("shorten.ivpy").read()
        os.system("cls")
        print(shorten(data))

        while True:
            time.sleep(0.1)

            if open("shorten.ivpy").read() != data:
                break


if __name__ == "__main__":
    main()