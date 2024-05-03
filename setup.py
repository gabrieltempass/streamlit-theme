from pathlib import Path

import setuptools


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="st-theme",
    version="1.2.2",
    description="A component that returns the active theme of the Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-theme",
    project_urls={
        "Source Code": "https://github.com/gabrieltempass/streamlit-theme",
        "Bug Tracker": "https://github.com/gabrieltempass/streamlit-theme/issues",
        "Release notes": "https://github.com/gabrieltempass/streamlit-theme/releases",
        "Documentation": "https://github.com/gabrieltempass/streamlit-theme",
        "Community": "https://discuss.streamlit.io/t/new-component-st-theme-it-returns-the-active-theme-of-the-streamlit-app/64424",
    },
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    license="MIT License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ],
    packages=[
        "streamlit_theme",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "st-theme = streamlit_theme:print_version",
        ],
    },
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.33",
    ],
)
