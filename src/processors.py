import json
from pathlib import Path
from qiskit.providers.fake_provider import GenericBackendV2

def load_processor(path):
    """
    Load hardware processor definition securely from a JSON file 
    with error handling and path resolution.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Processor configuration file not found at: {file_path.absolute()}")
    
    with file_path.open("r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON formatting in {file_path}: {e}")
            
    # Validate required keys
    required_keys = ["name", "num_qubits", "coupling_map", "basis_gates"]
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required configuration key '{key}' in {file_path}")
            
    return config

def get_backend_from_config(processor_config):
    """
    Instantiates a Qiskit GenericBackendV2 directly from a processor configuration dictionary.
    """
    return GenericBackendV2(
        num_qubits=processor_config["num_qubits"],
        coupling_map=processor_config["coupling_map"],
        basis_gates=processor_config["basis_gates"],
        name=processor_config.get("name", "custom_backend")
    )
