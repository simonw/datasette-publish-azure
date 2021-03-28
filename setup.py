from setuptools import setup
import os

VERSION = "0.1a0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-publish-azure",
    description="Publish Datasette instances to Azure Functions",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-publish-azure",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-publish-azure/issues",
        "CI": "https://github.com/simonw/datasette-publish-azure/actions",
        "Changelog": "https://github.com/simonw/datasette-publish-azure/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_publish_azure"],
    entry_points={"datasette": ["publish_azure = datasette_publish_azure"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-publish-azure[test]"],
    package_data={"datasette_publish_azure": ["static/*", "templates/*"]},
    python_requires=">=3.6",
)
