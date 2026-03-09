"""
Render the three scurvy DAGs as proper directed acyclic graphs:
non-overlapping nodes, visible directed arrows, text fully enclosed in ellipses.
"""
import daft
import matplotlib.pyplot as plt

plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

# Scurvy Prevention node: identical across all three DAGs (same size, green)
SCURVY_ASPECT = 3.8
SCURVY_SCALE = 1.2
SCURVY_FACE = "#d5f5e3"
SCURVY_EDGE = "#1e7e34"
SCURVY_PLOT = {"facecolor": SCURVY_FACE, "edgecolor": SCURVY_EDGE, "linewidth": 2.5, "alpha": 0.95}

# All nodes: aspect 3.5–4 so labels are fully enclosed in ellipse
ASPECT = 3.8
SCALE = 1.2
# Arrow visibility: slightly larger arrowheads so they are not clipped
ARROW_PARAMS = {"head_length": 0.3, "head_width": 0.12, "linewidth": 2, "edgecolor": "#333"}


def scurvy_node(pgm, name, x, y):
    """Add the shared Scurvy Prevention node."""
    pgm.add_node(
        name, "Scurvy\nPrevention", x, y,
        aspect=SCURVY_ASPECT, scale=SCURVY_SCALE,
        plot_params=dict(SCURVY_PLOT),
    )


# --- DAG 1: Lemons → Scurvy Prevention (x = 1 and 3.5, no overlap) ---
pgm = daft.PGM(dpi=180, alternate_style="outer")
pgm.add_node(
    "lemons", "Lemons", 1, 1,
    aspect=ASPECT, scale=SCALE,
    plot_params={"facecolor": "#fef9e7", "edgecolor": "#b8860b", "linewidth": 2.5, "alpha": 0.95},
)
scurvy_node(pgm, "sp1", 3.5, 1)
pgm.add_edge("lemons", "sp1", plot_params=ARROW_PARAMS)
plt.title("1747: Lemons prevent scurvy (correct but incomplete)", fontsize=11, pad=10)
pgm.render()
plt.savefig("dag1-1747.png", bbox_inches="tight", dpi=180, facecolor="white")
plt.close()

# --- DAG 2: Acid → Bacteria Death → Scurvy Prevention (x = 1, 3.5, 6) ---
pgm = daft.PGM(dpi=180, alternate_style="outer")
pgm.add_node(
    "acid", "Acid", 1, 1,
    aspect=ASPECT, scale=SCALE,
    plot_params={"facecolor": "#e8e0f0", "edgecolor": "#4a148c", "linewidth": 2.5, "alpha": 0.95},
)
pgm.add_node(
    "bd", "Bacteria\nDeath", 3.5, 1,
    aspect=ASPECT, scale=SCALE,
    plot_params={"facecolor": "#fce4ec", "edgecolor": "#c2185b", "linewidth": 2.5, "alpha": 0.95},
)
scurvy_node(pgm, "sp2", 6, 1)
pgm.add_edge("acid", "bd", plot_params=ARROW_PARAMS)
pgm.add_edge("bd", "sp2", plot_params=ARROW_PARAMS)
plt.title("Misguided belief: Acid kills bacteria (wrong)", fontsize=11, pad=10)
pgm.render()
plt.savefig("dag2-misguided.png", bbox_inches="tight", dpi=180, facecolor="white")
plt.close()

# --- DAG 3: Vitamin C → Scurvy Prevention (x = 1 and 3.5) ---
pgm = daft.PGM(dpi=180, alternate_style="outer")
pgm.add_node(
    "vc", "Vitamin C", 1, 1,
    aspect=ASPECT, scale=SCALE,
    plot_params={"facecolor": "#e0f7fa", "edgecolor": "#006064", "linewidth": 2.5, "alpha": 0.95},
)
scurvy_node(pgm, "sp3", 3.5, 1)
pgm.add_edge("vc", "sp3", plot_params=ARROW_PARAMS)
plt.title("1928: Vitamin C prevents scurvy (complete and correct)", fontsize=11, pad=10)
pgm.render()
plt.savefig("dag3-1928.png", bbox_inches="tight", dpi=180, facecolor="white")
plt.close()

print("Saved: dag1-1747.png, dag2-misguided.png, dag3-1928.png")
