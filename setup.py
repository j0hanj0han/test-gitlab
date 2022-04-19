
import setuptools

# Test the code :)
EXTRAS = {
    'test': ['pytest==6.2.5', "pytest-cov==3.0.0", "flake8==4.0.1"]
}

setuptools.setup(
    name="mypypipackage",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    extras_require=EXTRAS,
)
