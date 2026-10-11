# Phase 1 Scientific Report: PS-Q1 Biomedical Signal Classifier

## 1. Executive Summary
This report presents a controlled A/B architecture benchmark for **PS-Q1: Biomedical Signal Classifier**. Using a Variational Quantum Classifier (VQC), we evaluated how physical processor topology and connectivity constraints impact circuit compilation, routing overhead (SWAP operations), and overall execution performance under noise.

## 2. Methodology & Problem Statement
* **Selected Problem Statement:** PS-Q1 (Biomedical Signal Classifier)[cite: 1].
* **Logical Circuit:** Built using data encoding gates ($RX$) and entangling layers ($CX$) tailored for biomedical signal features.
* **Benchmark Processors:**
  * **Processor A:** Linear coupling map (`[[0,1], [1,2], [2,3], [3,4]]`).
  * **Processor B:** Extended/Ring coupling map (`[[0,1], [1,2], [2,3], [3,4], [4,0]]`).

## 3. Results & Architecture Comparison
As observed from our transpiled execution metrics and figures (`results/figures/ab_comparison.png`):
* **Circuit Depth & Gate Count:** Processor B's ring topology allowed more direct qubit interactions compared to Processor A's linear layout, significantly reducing the need for routing insertions.
* **SWAP Overhead:** Processor A incurred a higher SWAP count because non-adjacent logical operations required physical bridging across the linear chain.
* **Noise Impact:** Due to increased gate counts and SWAP operations on Processor A, the circuit experienced higher vulnerability to gate error rates.

## 4. Conclusion
Processor architecture fundamentally dictates how a logical quantum algorithm executes in practice. For hardware-constrained quantum machine learning models like PS-Q1, topologies with higher connectivity (Processor B) reduce circuit depth and improve fidelity by minimizing SWAP overhead.
