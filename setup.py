import pathlib
from setuptools import setup, find_packages


if __name__ == '__main__':

    # The directory containing this file
    HERE = pathlib.Path(__file__).parent
    
    # The text of the README file
    README = (HERE / "README.md").read_text()

    setup(
        name="python-aux",
        version="0.3.0",
        description="Python Utilities ft. pandas, matplotlib and more",
        long_description=README,
        long_description_content_type="text/markdown",
        url="https://github.com/kanodiaayush/python-utilities",
        author="kanodiaayush, kasince2k",
        author_email="kanodiaayush@gmail.com, kasince2k@gmail.com",
        packages=find_packages(exclude=["examples", "docs"]),
        install_requires=["numpy", "pandas", "matplotlib"],
    )
