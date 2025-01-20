# setup.py

from setuptools import setup, find_packages

setup(
    name="my_package",                      # The name of your package
    version="0.1",                          # Version number
    packages=find_packages(),               # This will automatically find all packages in the directory
    install_requires=[],                    # Any dependencies your package requires
    author="Your Name",                     # Your name
    author_email="your.email@example.com",   # Your email
    description="A simple greeting package", # Short description
    classifiers=[                           # Optional: List of classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",                # Minimum Python version
)
