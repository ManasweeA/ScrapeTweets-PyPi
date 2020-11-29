import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScrapeTweets", 
    version="1.0.0",
    author="Manaswee Adwant",
    author_email="manaswee25445@gmail.com",
    description="ScrapeTweets is a Python package that scrapes all the tweets from the Twitter API by using Hashtags. This data can be used for various purposes like Education, Research, News, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ManasweeA/ScrapeTweets-PyPi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)