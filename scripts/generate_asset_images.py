import matplotlib.pyplot as plt
from pathlib import Path

# Create output directory
output_dir = Path("assets/qff_phase1_latex_images")
output_dir.mkdir(parents=True, exist_ok=True)

equations = {
    "eq_qubit_state.png": r"$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$",
    "eq_bell_state.png": r"$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$",
    "eq_graph.png": r"$G = (V, E)$ where $V = \text{qubits}$, $E = \text{coupling map}$",
    "eq_bell_fidelity.png": r"$F(\rho, \sigma) = \left( \operatorname{tr} \sqrt{\sqrt{\rho}\sigma\sqrt{\rho}} \right)^2$",
    "eq_zz_expectation.png": r"$\langle Z_i Z_j \rangle = \langle \psi | Z_i \otimes Z_j | \psi \rangle$",
    "eq_standard_error.png": r"$\text{SE} = \frac{\sigma}{\sqrt{N}}$"
}

for filename, latex_str in equations.items():
    fig, ax = plt.subplots(figsize=(6, 1.2))
    ax.axis('off')
    ax.text(0.5, 0.5, latex_str, fontsize=20, ha='center', va='center')
    
    file_path = output_dir / filename
    plt.savefig(file_path, bbox_inches='tight', dpi=300)
    plt.close()

print("All asset equation images generated successfully inside assets/qff_phase1_latex_images/!")
