from qiskit import QuantumCircuit
import numpy as np

def get_classifier_circuit(feature_vector, weights):
    """Constructs a logical quantum circuit for the PS-Q1 Biomedical Signal Classifier."""
    num_qubits = len(feature_vector)
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    for i, val in enumerate(feature_vector):
        qc.rx(val * np.pi, i)
        
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
        
    for i, w in enumerate(weights[:num_qubits]):
        qc.rz(w, i)
        
    qc.measure(range(num_qubits), range(num_qubits))
    return qc
