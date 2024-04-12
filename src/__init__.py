# src/__init__.py
try:
    # Try to get the version of the installed package
    from importlib.metadata import version
    __version__ = version("pylaptoppred")
except ImportError:
    # Fallback to a default version if not installed
    __version__ = "0.0.0-dev"
