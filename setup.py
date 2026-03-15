from setuptools import setup, find_packages

setup(
    name="textartisan",
    version="1.0.0",
    description="Professional ASCII art and text banner generation library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="M3",
    author_email="arabemossab@gmail.com",
    url="https://github.com/Mr-Mossab/textartisan",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'textartisan=textartisan:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Artistic Software",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
    ],
    python_requires='>=3.6',
    keywords="ascii art banner text graphics font color gradient animation terminal cli",
    project_urls={
        "Documentation": "https://github.com/Mr-Mossab/textartisan/wiki",
        "Source": "https://github.com/Mr-Mossab/textartisan",
        "Tracker": "https://github.com/Mr-Mossab/textartisan/issues",
    },
)