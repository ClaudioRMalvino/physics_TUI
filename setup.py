from setuptools import setup, find_packages

setup(
    name="physics_TUI",  # This should match your import statements
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "physics_TUI": ["appearance.tcss"],
    },
    install_requires=[
        "textual>=0.38.1",
    ],
)