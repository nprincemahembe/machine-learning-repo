import platform
import sys

print("=== Environment Information ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Operating system: {platform.platform()}")

try:
import numpy
import pandas
import sklearn
import scipy
import matplotlib
import seaborn

print("\n=== Library Versions ===")
print(f"NumPy: {numpy.__version__}")
print(f"Pandas: {pandas.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Seaborn: {seaborn.__version__}")

except ImportError as error:
print(f"\nA library is not installed: {error}")
print("Install the pinned requirements before running this script.")