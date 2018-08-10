import setuptools

setuptools.setup(
    name="authentication",
    version="0.0.1",
    author="Andre Filliettaz",
    author_email="andrentaz@gmail.com",
    description="A small authentication server",
    url="https://github.com/andrentaz/caucious-octo-enigma.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "flask",
        "flask-cors",
        "passlib",
        "pymongo",
    ]
)
