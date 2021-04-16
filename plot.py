import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def save_graph(x_values, y_values, x_label, y_label, output_file):
    x = np.array(x_values)
    y = np.array(y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, ".-")
    plt.savefig(output_file, bbox_inches="tight")
    plt.clf()


def plot_apriltag(apriltag_s3_csv, apriltag_s2_csv, base, output):
    apriltag_s3 = pd.read_csv(apriltag_s3_csv)
    apriltag_s2 = pd.read_csv(apriltag_s2_csv)

    components = ["x", "y", "z"]
    for index, component in enumerate(components):
        apriltag_time = apriltag_s3["time"]
        apriltag_comp = apriltag_s3[component]
        plt.plot(apriltag_time, apriltag_comp, label="apriltag_s3")

        apriltag_time = apriltag_s2["time"]
        apriltag_comp = apriltag_s2[component]
        plt.plot(apriltag_time, apriltag_comp, label="apriltag_s2")

        plt.axhline(y=base[index], color='g', linestyle='-',
                    label="Ground Truth Apriltag")

        plt.xlabel("Zeit [s]")
        plt.ylabel(f"Position in {component.upper()}-Richtung [cm]")

        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.savefig(f"{output}_apriltag_{component}.png", bbox_inches="tight")

        plt.clf()


def plot_infrared(infrared_1_csv, infrared_2_csv, base, output):
    infrared_1 = pd.read_csv(infrared_1_csv)
    infrared_2 = pd.read_csv(infrared_2_csv)

    components = ["x", "y", "z"]
    for index, component in enumerate(components):
        infrared_time = infrared_1["time"]
        infrared_comp = infrared_1[component]
        plt.plot(infrared_time, infrared_comp, label="infrared_1")

        infrared_time = infrared_2["time"]
        infrared_comp = infrared_2[component]
        plt.plot(infrared_time, infrared_comp, label="infrared_2")

        plt.axhline(y=base[index], color="g",
                    linestyle='-', label="Ground Truth IR-Marker")

        plt.xlabel("Zeit [s]")
        plt.ylabel(f"Position in {component.upper()}-Richtung [cm]")

        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.savefig(f"{output}_irmarker_{component}.png", bbox_inches="tight")

        plt.clf()


if __name__ == "__main__":
    plot_apriltag(
        "./results/apriltag_test3_s3.csv",
        "./results/apriltag_test3_s2.csv",
        [2.2, -2.2, 170],
        "apriltag_test3")
    
    plot_infrared(
        "./results/infrared_test3_1.csv",
        "./results/infrared_test3_2.csv",
        [4.8, -2.2, 165],
        "irmarker_test3")
