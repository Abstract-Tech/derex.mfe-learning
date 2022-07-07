from setuptools import find_namespace_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "derex.runner",
    "jinja2",
]

setup_requirements = [
    # "pytest-runner",
]

test_requirements = [
    # "pytest>=3",
]

setup(
    author="Chiruzzi Marco",
    author_email="chiruzzi.marco@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Derex Plugin to integrate Open edX Learning microfrontend",
    entry_points={
        "derex.runner": ["mfe_learning=derex.mfe_learning.config:MfeLearningService"],
        "derex.runner.cli_plugins": [
            "mfe_learning=derex.mfe_learning.cli:mfe_learning_build"
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="derex.mfe_learning",
    name="derex.mfe_learning",
    packages=find_namespace_packages(include=["derex.mfe_learning"]),
    namespace_packages=["derex"],
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Abstract-Tech/derex.mfe_learning",
    version="0.0.1",
    zip_safe=False,
    dependency_links=[
        "https://github.com/Abstract-Tech/derex.runner/tarball/v0.3.4.dev1#egg=derex.runner"
    ],
)
