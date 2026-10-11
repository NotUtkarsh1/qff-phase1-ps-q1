# Phase 1 Scientific Report: PS-Q1 Biomedical Signal Classifier

## 1. Executive Summary
This report presents a controlled A/B architecture benchmark for **PS-Q1: Biomedical Signal Classifier**. Using a Variational Quantum Classifier (VQC) with parameterized data-encoding and entangling layers, we evaluated how physical processor topology and connectivity constraints impact circuit compilation, routing overhead, and overall performance across two distinct quantum hardware architectures (**Processor A** and **Processor B**).

---

## 2. Methodology & Problem Statement
* **Selected Problem Statement:** PS-Q1 (Biomedical Signal Classifier)[cite: 1].
* **Logical Circuit Design:** 
  * Built using a 5-qubit architecture matching the biomedical feature vector length.
  * Data encoding performed via rotation gates ($RX$) combined with entangling layers ($CX$) and trainable parameter rotations ($RZ$).
* **Hardware Architectures:**
  * **Processor A (Linear Topology):** Coupling map with a linear chain (`[[0,1], [1,2], [2,3], [3,4]]`).
  * **Processor B (Ring Topology):** Coupling map with extended connectivity (`[[0,1], [1,2], [2,3], [3,4], [4,0]]`).

---

## 3. Empirical Results & Performance Metrics
Based on our transpilation execution across both hardware configurations, the resource utilization metrics are summarized below:

| Metric | Processor A (Linear) | Processor B (Ring) |
| :--- | :--- | :--- |
| **Qubits** | 5 | 5 |
| **Circuit Depth** | 10 | 24 |
| **Total Operations** | 30 | 51 |
| **2-Qubit Operations Estimate** | 4 | 4 |
| **SWAP Count** | 0 | 0 |
| **Basis Gate Breakdown** | RZ: 12, SX: 9, Measure: 5, CX: 4 | RZ: 25, SX: 17, Measure: 5, CX: 4 |

---

## 4. Architecture Analysis & Discussion
* **Circuit Depth and Compiler Optimization:** 
  Although Processor B features higher physical connectivity (the ring edge connecting qubit 4 back to qubit 0), Qiskit's stochastic compilation pipeline and basis-gate target expansions resulted in a higher gate count and circuit depth for Processor B in this specific execution run. This highlights how routing heuristics, initial virtual-to-physical layout mappings, and single-qubit basis decompositions ($SX, RZ$) heavily influence compiled output.
* **Gate Overhead:** 
  Both processors successfully routed the 5-qubit entanglement layer without requiring explicit physical `SWAP` gates (`swap_count: 0`), demonstrating that the logical circuit width fits comfortably within the physical constraints of both 5-qubit layouts.
* **Noise and Fidelity Implications:** 
  The lower overall gate count and depth observed on Processor A suggest a reduced exposure to decoherence and gate errors for this specific compilation pass, whereas Processor B's denser connectivity opens pathways for alternative layout optimization strategies under deep variational training loops.

---

## 5. Conclusion
Hardware topology and compiler mapping play a critical role in quantum machine learning deployment. While extended connectivity topologies like Processor B provide architectural flexibility for complex routing, compiler optimization choices significantly dictate the final circuit depth and gate count. Future work will extend this benchmark to evaluate classification accuracy under simulated noise models.
