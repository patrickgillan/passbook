from setuptools import setup

version = __import__("passbook").__version__

setup(
    name="Passbook",
    version=version,
    author="Patrick Gillan",
    author_email="patrickrgillan@gmail.com",
    packages=["passbook", "passbook.test"],
    url="http://github.com/patrickgillan/passbook/",
    license=open("LICENSE.txt").read(),
    description="Passbook file generator",
    long_description=open("README.md").read(),
    download_url="http://pypi.python.org/packages/source/P/Passbook/Passbook-%s.tar.gz"
    % version,
    install_requires=[
        "cryptography==45.0.4",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
