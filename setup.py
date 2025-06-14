from setuptools import find_packages, setup

setup(
    name="ai_robot_position_scraper",
    version="0.0.4",
    author="Arun CS",
    author_email="your.email@example.com",
    description="Position scraper library for AI-Robot",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aruncs31s/ai_robot_position_scraper",
    packages=find_packages(),
    install_requires=["requests"],
)
