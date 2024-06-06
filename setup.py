from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="drago",
    version="0.1.0",
    author="DragoFtw",
    author_email="fdrago359@gmail.com",
    description="A Telegram bot for BGCL BGMI LOADER using Pyrogram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DragoServer/TelegramBot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'pyrogram',
        'aiomysql',
    ],
    entry_points={
        'console_scripts': [
            'dragot=drago.bot:main',
        ],
    },
)

