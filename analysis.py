import pandas as pd
import os
import shutil


def print_info(csv_path, output_dir):
    data = pd.read_csv(csv_path)
    name = csv_path.split(".")[0]
    print(f"\n{name}")

    for component in ["x", "y", "z"]:
        print(f"\tComponent {component.upper()}")
        component_data = data[component]
        avg = component_data.mean()
        std = component_data.std()
        count = component_data.count()

        with open(f"{output_dir}/{name}_{component}.txt", "w+") as f:
            f.write(str(avg) + "\n")       
            f.write(str(std) + "\n")       
            f.write(str(count) + "\n")       
        

if __name__ == "__main__":
    results_dir = "./results"
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)
    else:
        shutil.rmtree(results_dir)
        os.mkdir(results_dir)

    base_dir = "./"
    for single_file in os.listdir(base_dir):
        file_extension = single_file.split(".")[-1]
        if file_extension == "csv":
            print_info(single_file, results_dir)
