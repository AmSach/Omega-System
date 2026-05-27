from setuptools import setup, find_packages

setup(
    name="omega-system",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "omega=core.kernel:main",
        ],
    },
    author="Aman Sachan",
    description="The Autonomous Swarm OS for Decentralized Compute.",
    python_requires=">=3.8",
)
