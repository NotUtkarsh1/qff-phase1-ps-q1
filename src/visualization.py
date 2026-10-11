import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

def plot_processor_graph(processor_config, save_path=None):
    """Draw and save the processor coupling graph."""
    G = nx.Graph()
    G.add_nodes_from(range(processor_config["num_qubits"]))
    G.add_edges_from(processor_config["coupling_map"])
    
    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_size=800, node_color="lightblue", font_weight="bold")
    plt.title(f"Hardware Topology: {processor_config['name']}")
    
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
    plt.close()

def plot_comparison_chart(metrics_a, metrics_b, save_path=None):
    """Plot side-by-side architecture comparison metrics."""
    labels = ["Depth", "Total Ops", "2-Qubit Ops", "SWAPs"]
    vals_a = [metrics_a["depth"], metrics_a["total_ops"], metrics_a["two_qubit_ops_estimate"], metrics_a["swap_count"]]
    vals_b = [metrics_b["depth"], metrics_b["total_ops"], metrics_b["two_qubit_ops_estimate"], metrics_b["swap_count"]]
    
    x = range(len(labels))
    width = 0.35
    
    plt.figure(figsize=(8, 5))
    plt.bar([p - width/2 for p in x], vals_a, width, label="Processor A")
    plt.bar([p + width/2 for p in x], vals_b, width, label="Processor B")
    
    plt.xlabel("Circuit Metrics")
    plt.ylabel("Count")
    plt.title("A/B Architecture Benchmark Comparison")
    plt.xticks(x, labels)
    plt.legend()
    
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
    plt.close()
