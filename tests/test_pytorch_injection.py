from pathlib import Path
from fickling.pytorch import PyTorchModelWrapper

w = PyTorchModelWrapper("pytorch_model.pt")
w.inject_payload(
    "print(123)",
    Path("pytorch_injected.pt")
)

print("Injected model created:", Path("pytorch_injected.pt").exists())
