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
