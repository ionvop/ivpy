import sys
import os


def main() -> None:
    data = open(sys.argv[1]).read()
    data = compile(data)
    output_path = os.path.dirname(sys.argv[1]) + "/output.py"
    open(output_path, "w").write(data)
    parameters = "\" ".join(sys.argv[2:])
    os.system(f"python \"{output_path}\" \"{parameters}")
    os.remove(output_path)


def compile(data: str, indent: int = 0) -> str:
    if indent < 0:
        indent = 0

    result = ""
    i = 0

    while i < len(data):
        char = data[i]

        if char == ".":
            i += 1
            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            result += f"{' ' * indent}print({temp})\n"
        elif char == ",":
            i += 1
            temp, i = scan(data, i, [":", ";"])
            char = data[i]
            temp = temp.strip()

            if char == ";":
                result += f"{' ' * indent}{temp} = input()\n"
                i += 1
                continue
            
            i += 1
            temp2, i = scan(data, i, [";"])
            temp2 = temp2.strip()
            result += f"{' ' * indent}{temp} = input({temp2})\n"
        elif char == "?":
            if data[i + 1] == ";":
                i += 2
                indent -= 1
                continue

            i += 1
            temp, i = scan(data, i, [":"])
            temp = temp.strip()
            result += f"{' ' * indent}if {temp}:\n"
            indent += 1
        elif char == ":":
            if data[i + 1] == "?":
                i += 2
                temp, i = scan(data, i, [":"])
                temp = temp.strip()
                result += f"{' ' * (indent - 1)}elif {temp}:\n"
                i += 1
                continue

            result += f"{' ' * (indent - 1)}else:\n"
        elif char == "[":
            result += f"{' ' * indent}while True:\n"
            indent += 1
        elif char == "]":
            indent -= 1
        elif char == "\\":
            result += f"{' ' * indent}break\n"
        elif char == "/":
            result += f"{' ' * indent}continue\n"
        elif char == ">":
            i += 1
            temp, i = scan(data, i, [")"])
            temp = temp.strip()
            result += f"{' ' * indent}def {temp}):\n"
            indent += 1
        elif char == "<":
            i += 1
            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            result += f"{' ' * indent}return {temp}\n"
            indent -= 1
        elif char == ";":
            result += f"{' ' * indent}pass\n"
        elif char == "!":
            if data[i + 1] == ":":
                i += 2
                result += f"{' ' * indent}try:\n"
                indent += 1
                continue

            if data[i + 1] == "!":
                if data[i + 2] == "!":
                    i += 3
                    temp, i = scan(data, i, [";"])
                    temp = temp.strip()
                    result += f"{' ' * indent}raise {temp}\n"
                    i += 1
                    continue

                if data[i + 2] == ":":
                    i += 3
                    result += f"{' ' * (indent - 1)}except:\n"
                    continue

                i += 2
                temp, i = scan(data, i, [":"])
                temp = temp.strip()
                result += f"{' ' * (indent - 1)}except {temp}:\n"
                i += 1
                continue

            if data[i + 1] == ";":
                i += 2
                indent -= 1
                continue

            i += 1
            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            result += f"{' ' * (indent)}exit({temp})\n"
        elif char == "/" and data[i + 1] == "/":
            i += 2
            temp, i = scan(data, i, ["\n"])
            temp = temp.strip()
            result += f"{' ' * indent}# {temp}\n"
        elif char in ["+", "-", "*", "/", "%"]:
            operator = char

            if operator == "*" and data[i + 1] == "*":
                i += 1
                operator = "**"

            i += 1
            temp, i = scan(data, i, [":", ";"])
            char = data[i]
            temp = temp.strip()

            if char == ";":
                default = 2 if operator in ["*", "/", "%", "**"] else 1

                result += f"{' ' * indent}{temp} {operator}= {default}\n"
                i += 1
                continue
            
            i += 1
            temp2, i = scan(data, i, [";"])
            temp2 = temp2.strip()
            result += f"{' ' * indent}{temp} {operator}= {temp2}\n"
        elif char == "@":
            i += 1
            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            script_dir = get_abs_script_path(temp)
            import_data = open(script_dir).read()
            import_data = compile(import_data, indent)
            result += f"{' ' * indent}{import_data}\n"
        elif char == "$":
            i += 1
            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            result += f"{' ' * indent}import {temp}\n"
        elif char in [" ", "\n", "\t"]:
            pass
        else:
            if char == "_":
                i += 1

            temp, i = scan(data, i, [";"])
            temp = temp.strip()
            result += f"{' ' * indent}{temp}\n"

        i += 1

    return result


def scan(data: str, start: int, delimiters: list[str]) -> tuple[str, int]:
    i = start
    result = ""
    is_string = False

    while i < len(data):
        char = data[i]

        if is_string and char == "\\":
            result += f"\\{data[i + 1]}"
            i += 2
            continue

        if is_string == False:
            if char == "+" and data[i + 1] == "+":
                result += "True"
                i += 2
                continue
            elif char == "-" and data[i + 1] == "-":
                result += "False"
                i += 2
                continue
            elif char == "?" and data[i + 1] == "?":
                result += "None"
                i += 2
                continue
            elif char == "&" and data[i + 1] == "&":
                result += " and "
                i += 2
                continue
            elif char == "|" and data[i + 1] == "|":
                result += " or "
                i += 2
                continue
            elif char == "!" and data[i + 1] != "=":
                result += " not "
                i += 1
                continue
            elif char == ">" and data[i + 1] == ">":
                result += " in "
                i += 2
                continue

        if char == "\"":
            is_string = not is_string

        if char in delimiters and not is_string:
            break

        result += char
        i += 1

    result = result.strip()
    return result, i


def get_abs_script_path(file_path: str = "") -> str:
    script_path = os.path.dirname(sys.argv[1])
    return os.path.join(script_path, file_path)


if __name__ == "__main__":
    main()