import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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

def plot_lregression():
    base_dir = "./results"
    for single_file in os.listdir(base_dir):
        file_extension = single_file.split(".")[-1]
        if file_extension == "csv":
            data = pd.read_csv(f"{base_dir}/{single_file}")
            output = single_file.split(".")[0] + "_lregression"

            for component in ["x", "y", "z"]:
                X = data["time"].values.reshape(-1, 1)
                Y = data[component].values.reshape(-1, 1)

                linear_regressor = LinearRegression()
                linear_regressor.fit(X, Y)
                Y_pred = linear_regressor.predict(X)

                coef = linear_regressor.coef_[0][0]
                intercept = round(linear_regressor.intercept_[0], 3)

                plt.scatter(X, Y, label=f"Position in {component.upper()}-Richtung")
                plt.plot(X, Y_pred, color="red", label=f"Lineare Regression: z = {coef:.3e}t + {intercept}")
                
                plt.xlabel("Zeit [s]")
                plt.ylabel(f"Position in {component.upper()}-Richtung [cm]")

                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
                plt.savefig(f"{output}_{component}.png", bbox_inches="tight")

                plt.clf()

def plot_lregression_diff():
    csv_path = "infrared_test3.csv"
    data = pd.read_csv(f"./results/{csv_path}")
    output = csv_path.split(".")[0] + "_lregression_split"

    fig, (ax1, ax2) = plt.subplots(1, 2)

    X = data["time"].values
    Y = data["z"].values
    half_pos = int(len(Y) / 2)
    Y_1 = Y[:half_pos].reshape(-1, 1)
    Y_2 = Y[half_pos:].reshape(-1, 1)

    X_1 = X[:half_pos].reshape(-1, 1)
    X_2 = X[half_pos:].reshape(-1, 1)

    linear_regressor_1 = LinearRegression()
    linear_regressor_1.fit(X_1, Y_1)
    Y_1_pred = linear_regressor_1.predict(X_1)

    linear_regressor_2 = LinearRegression()
    linear_regressor_2.fit(X_2, Y_2)
    Y_2_pred = linear_regressor_2.predict(X_2)

    coef_1 = linear_regressor_1.coef_[0][0]
    intercept_1 = round(linear_regressor_1.intercept_[0], 3)

    coef_2 = linear_regressor_2.coef_[0][0]
    intercept_2 = round(linear_regressor_2.intercept_[0], 3)

    all_labels = [
        f"Lineare Regression: z = {coef_1:.3e}t + {intercept_1}",
        f"Position in Z-Richtung",
        f"Lineare Regression: z = {coef_2:.3e}t + {intercept_2}",
        f"Position in Z-Richtung"
    ]

    ax1.scatter(X_1, Y_1, color="orange")
    l1 = ax1.plot(X_1, Y_1_pred, color="green")
    ax1.autoscale()

    ax1.set_xlabel("Zeit [s]")
    ax1.set_ylabel(f"Position in Z-Richtung [cm]")

    ax2.scatter(X_2, Y_2)
    l2 = ax2.plot(X_2, Y_2_pred, color="red")
    ax2.autoscale()

    ax2.set_xlabel("Zeit [s]")
    ax2.set_ylabel(f"Position in Z-Richtung [cm]")

    lg = fig.legend(
        bbox_to_anchor=(1.05,1), 
        labels=all_labels, 
        loc='upper left',
        borderaxespad=0.1)
    fig.align_labels()
    plt.subplots_adjust(right=1.1)
    plt.savefig(
        f"{output}_z.png", 
        bbox_extra_artists=(lg,),
        bbox_inches="tight")

    plt.clf()

if __name__ == "__main__":
    plot_lregression_diff()