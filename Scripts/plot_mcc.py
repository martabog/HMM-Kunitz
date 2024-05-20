import matplotlib.pyplot as plt
import pickle
import sys


def plot_mcc_vs_evalue(mcc, evalue_range):
    '''Plots MCC values against different e-value thresholds.'''
    
    plt.plot(evalue_range, mcc, marker='o')
    plt.xscale('log')
    plt.xlabel("E-value Threshold (log scale)")
    plt.ylabel("MCC")
    plt.title("MCC vs. E-value Threshold")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv)>1:
        evalue_range = []
        for i in range(1,16):
            eval = 10**(-i)
            evalue_range.append(eval)

        with open(sys.argv[1], "rb") as f:
            mcc_score = pickle.load(f)
        
        plot_mcc_vs_evalue(mcc_score, evalue_range)
    else:
        print("Not enough command-line arguments.")




