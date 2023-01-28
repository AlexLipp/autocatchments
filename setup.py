from setuptools import setup

setup(
    name="autocatchments",
    version="0.1",
    description="Tools for some analysis of drainage basins",
    url="http://github.com/AlexLipp",
    author="Alex Lipp",
    author_email="alexander.lipp@merton.ox.ac.uk",
    license="MIT",
    packages=["autocatchments"],
    install_requires=["matplotlib", "numpy", "pandas", "landlab", "gdal"],
    zip_safe=False,
)
