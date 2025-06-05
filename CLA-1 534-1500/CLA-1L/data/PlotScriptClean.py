import numpy as np
import matplotlib.pyplot as plt

# === EDIT THESE ===
data_file = 'rgs.npy'        # Path to data file (e.g., rgs.npy)
x_label = 'Time (ns)'        # X-axis label
y_label = 'Radius of Gyration (nm)'  # Y-axis label
plot_title = 'Radius of Gyration vs Time: CLA-1L Repetitive Region 534-1500'    # Plot title
save_fig = False             # Set True to save instead of show
output_file = 'plot.png'     # Output image file name
dt = 10e-15 * 7000           # Time per frame in seconds (adjust wfreq here)
# ===================

# Generate time array based on data length and dt
data = np.load(data_file)
time = np.arange(len(data)) * dt * 1e9  # convert to ns

# Set up plot
plt.figure(figsize=(8, 5))
plt.plot(time, data, color='black', linewidth=1.5)
plt.xlabel(x_label, fontsize=12)
plt.ylabel(y_label, fontsize=12)
plt.title(plot_title, fontsize=14)
plt.grid(True, which='both', linestyle='--', alpha=0.4)
plt.tight_layout()

if save_fig:
    plt.savefig(output_file, dpi=300)
else:
    plt.show()
