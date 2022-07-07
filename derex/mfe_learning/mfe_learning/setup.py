"""Setup for Derex Learning Microfrontend support package."""

from setuptools import setup

setup(
    name="derex-mfe-learning",
    version="0.0.1",
    description="Support package for Derex Learning Microfrontend",
    packages=["derex_mfe_learning"],
    entry_points={
        "lms.djangoapp": [
            "derex_mfe_learning = derex_mfe_learning.app:DerexMfeLearningAppConfig"
        ],
        "cms.djangoapp": [
            "derex_mfe_learning = derex_mfe_learning.app:DerexMfeLearningAppConfig"
        ],
    },
)
