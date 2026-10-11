def circuit_metrics(qc):
    """Extract circuit depth, qubit count, gate counts, and SWAP overhead."""
    ops = qc.count_ops()
    two_q_names = {"cx", "cz", "ecr", "swap", "rxx", "ryy", "rzz"}
    return {
        "depth": qc.depth(),
        "num_qubits": qc.num_qubits,
        "total_ops": sum(ops.values()),
        "two_qubit_ops_estimate": sum(
            n for g, n in ops.items() if g.lower() in two_q_names
        ),
        "swap_count": ops.get("swap", 0),
        "operations": dict(ops)
    }
