import sys
import importlib
from pathlib import Path

def load_module(dictionary,name):
    sys.path.insert(0,dictionary)
