import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setuptools.setup(
    name="DarkOffelsalat",
    version="0.1.1sweet1",
    author="Renaud Gaspard",
    author_email="gaspardrenaud@hotmail.com",
    description="A simple bot that sends the link of the latest video of a youtube channel in a twitch chat",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Renaud11232/dark-offelsalat",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "dark-offelsalat=darkoffelsalat.command_line:main"
        ]
    },
    install_requires=[
        "twitchio",
        "python-youtube"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)