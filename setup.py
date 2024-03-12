from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="st-theme",
    version="1.1.0",
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    description="A component that returns the active theme of the Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-theme",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=["streamlit >= 1.29"],
)
