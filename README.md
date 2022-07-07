# Derex Learning Microfrontend

[![Github Actions](https://github.com/Abstract-Tech/derex.mfe-learning/actions/workflows/daily.yml/badge.svg?branch=master)](https://github.com/Abstract-Tech/derex.mfe-learning/actions/workflows/daily.yml)

Derex Plugin to integrate Open edX Learning Microfrontend

## Setup

- Install this package inside a derex project environment
- Add to the project derex.config.yaml

  ```yaml
  plugins:
    derex.mfe_learning: {}
  ```

## Customizations

There are some options that can be passed to the plugin configuration in your derex.config.yaml file.

- build_dir: An optional build directory which should contain a customized .env.derex file and a Caddyfile which will be included in the build context
- dockerfile_path: Path to a Dockerfile relative to the derex.config.yaml file location which will be used inplace of the default one
- aliases: Additional network aliases for the docker container. This list will also be used to populate the `CORS_ORIGIN_WHITELIST` and `LOGIN_REDIRECT_WHITELIST` LMS settings
- NODE_VERSION: The node version which will be given as a build argument
- MFE_REPOSITORY: A repository URL which will be given as a build argument
- MFE_BRANCH: A Git branch which will be checked out after cloning the Microfrontend repository

e.g.:

```yaml
plugins:
  derex.mfe-learning:
    {
      "build_dir": "mfe_learning_build",
      "dockerfile_path": "mfe_learning_build/Dockerfile",
      "aliases": [
        "learning.mydomain.com",
      ]
      "MFE_REPOSITORY": "https://github.com/edx/frontend-app-learning.git",
      "MFE_BRANCH": "open-release/lilac.master",
      "NODE_VERSION": "12-alpine",
    }
```

## Build

You can build the microfrontend image by running:

`derex build mfe-learning`

## Development

- Install [direnv](https://direnv.net/docs/installation.html)
- Allow direnv to create the virtualenv

  ```sh
  direnv allow
  ```

- Install with pip

  ```sh
  pip install -r requirements_dev.txt
  pre-commit install --install-hooks
  ```
