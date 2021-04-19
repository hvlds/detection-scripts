import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

def summary_generator():
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

def plot_absolute_differences():
    distances = [68, 126, 165, 204]
    apriltag_s3 = [1.105, 2.164, 3.392, 4.128]
    apriltag_s2 = [1.527, 3.436, 4.22, 8.211]
    irmarker = [3.446, 7.511, 37.829, 56.802]
    
    distances = np.array(distances)
    apriltag_s3 = np.array(apriltag_s3)
    apriltag_s2 = np.array(apriltag_s2)
    irmarker = np.array(irmarker)

    plt.plot(distances, apriltag_s3, marker = 'o', label="apriltag_s3")
    plt.plot(distances, apriltag_s2, marker = 'o', label="apriltag_s2")
    plt.plot(distances, irmarker, marker = 'o', label="irmarker")

    plt.xlabel("Ground Truth Distanz [cm]")
    plt.ylabel(f"Absolute Differenz zu der Ground Truth [cm]")

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f"absolute_differences.png", bbox_inches="tight")

def plot_std():
    distances = [68, 126, 165, 204]
    apriltag_s3 = [0.019, 0.093, 0.193, 0.319]
    apriltag_s2 = [0.028, 0.113, 0.231, 0.450]
    irmarker = [0.113, 0.993, 21.539, 4.475]
    
    distances = np.array(distances)
    apriltag_s3 = np.array(apriltag_s3)
    apriltag_s2 = np.array(apriltag_s2)
    irmarker = np.array(irmarker)

    plt.plot(distances, apriltag_s3, marker = 'o', label="apriltag_s3")
    plt.plot(distances, apriltag_s2, marker = 'o', label="apriltag_s2")
    plt.plot(distances, irmarker, marker = 'o', label="irmarker")

    plt.xlabel("Ground Truth Distanz [cm]")
    plt.ylabel(f"Standardabweichung")

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f"std_summary.png", bbox_inches="tight")

if __name__ == "__main__":
    plot_std()
