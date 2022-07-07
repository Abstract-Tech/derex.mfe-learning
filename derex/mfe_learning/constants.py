from enum import Enum


class MfeLearningVersions(Enum):
    # Values will be passed as uppercased named arguments to the docker build
    # e.g. --build-arg MFE_VERSION_RELEASE="open-release/lilac.master"
    lilac = {
        "docker_image_prefix": "ghcr.io/abstract-tech/derex-mfe-learning-lilac",
        "MFE_REPOSITORY": "https://github.com/edx/frontend-app-learning.git",
        "MFE_BRANCH": "open-release/lilac.master",
        "NODE_VERSION": "12-alpine",
    }
