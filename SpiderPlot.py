import matplotlib.pyplot as plt
import numpy as np

# Data: Variables and their sensitivity values at a +10% shift
labels = np.array(['Labor Cost', 'Sales Price', 'Tax Rate', 'Volume', 'Utility Cost'])
stats = np.array([5, 12, 2, 15, 4]) # % impact on NPV

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]])) # Close the loop
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='blue', alpha=0.25)
ax.plot(angles, stats, color='blue', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.show()