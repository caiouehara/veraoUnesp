import os
import re


def fix_paths(directory):
    correct_path = "./results/exercicio"

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                content = file.read()

            updated_content = re.sub(
                r"\./listas/lista\d+/tigre/results/exercicio\d+/", correct_path, content
            )

            with open(filepath, "w") as file:
                file.write(updated_content)
            print(f"Fixed path from: {filename}")

    print("All done")


if __name__ == "__main__":
    current_directory = os.getcwd()
    fix_paths(current_directory)
