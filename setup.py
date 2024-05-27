from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Python library for AxiDraw plotters to draw with Turtle graphics"

setup(
    name="turtledraw",
    version=VERSION,
    author="IAS WdKA (Boris Smeenk)",
    author_email="<b.smeenk@hr.nl>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "axicli @ https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip"
    ],
    keywords=["python", "turtle", "turtle graphics", "axidraw", "plotter", "pen plotter"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
