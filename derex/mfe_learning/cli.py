from pathlib import Path
from typing import Optional

import click
from derex.runner.build import build_microfrontend_image
from derex.runner.cli import ensure_project
from derex.runner.cli.build import build as derex_build_cli
from derex.runner.project import Project
from derex.runner.utils import abspath_from_egg

from derex.mfe_learning import __version__
from derex.mfe_learning.constants import MfeLearningVersions


@derex_build_cli.command("mfe-learning")
@click.pass_obj
@ensure_project
@click.argument(
    "version",
    type=click.Choice(MfeLearningVersions.__members__),
    required=False,
    callback=lambda _, __, value: value and MfeLearningVersions[value],
)
@click.option(
    "-T",
    "--target",
    type=str,
    default="final",
    help="Target to build",
)
@click.option(
    "-o",
    "--output",
    type=click.Choice(["docker", "registry"]),
    default="docker",
    help="Where to push the resulting image",
)
@click.option("-r", "--registry", type=str)
@click.option("-t", "--tag", type=str)
@click.option("--latest", "tag_latest", is_flag=True, default=False)
@click.option(
    "--only-print-image-name",
    is_flag=True,
    default=False,
    help="Only print the name which will be assigned to the image",
)
@click.option(
    "--pull",
    is_flag=True,
    default=False,
    help="Always try to pull the newer version of the image",
)
@click.option("--no-cache", is_flag=True, default=False)
@click.option("--cache-from", is_flag=True, default=False)
@click.option("--cache-to", is_flag=True, default=False)
def mfe_learning_build(
    project: Project,
    version: Optional[str],
    target: str,
    output: str,
    registry: Optional[str],
    tag: Optional[str],
    tag_latest: bool,
    only_print_image_name: bool,
    pull: bool,
    no_cache: bool,
    cache_from: bool,
    cache_to: bool,
):
    """Build microfrontend image using docker. Defaults to final image target."""
    try:
        config = project.config.get("plugins").get("derex.mfe-learning") or {}
    except AttributeError:
        config = {}

    if not version:
        version = project.openedx_version

    default_config = MfeLearningVersions[version.name]

    default_docker_image_prefix = default_config.value["docker_image_prefix"]
    tag = config.get("docker_image_tag", f"{default_docker_image_prefix}:{__version__}")
    if only_print_image_name:
        click.echo(tag)
        return 0

    default_build_dir = abspath_from_egg(
        "derex.mfe_learning", "derex/mfe_learning/docker_build/Dockerfile"
    ).parent
    build_dir = Path(config.get("build_dir") or default_build_dir)
    dockerfile_path = Path(
        config.get("dockerfile_path") or default_build_dir / "Dockerfile"
    )

    if not build_dir.exists() or not build_dir.is_dir():
        raise click.ClickException(
            f"Build dir {build_dir} does not exist or is not a directory. Aborting."
        )
    if not dockerfile_path.exists() or not dockerfile_path.is_file():
        raise click.ClickException(
            f"Dockerfile {dockerfile_path} does not exist or is not a file. Aborting."
        )

    paths_to_copy = [path for path in build_dir.iterdir()]
    build_args = {
        "NODE_VERSION": config.get(
            "NODE_VERSION", default_config.value["NODE_VERSION"]
        ),
        "MFE_REPOSITORY": config.get(
            "MFE_REPOSITORY", default_config.value["MFE_REPOSITORY"]
        ),
        "MFE_BRANCH": config.get("MFE_BRANCH", default_config.value["MFE_BRANCH"]),
    }

    build_microfrontend_image(
        project,
        target,
        paths_to_copy,
        output,
        registry,
        tag,
        tag_latest,
        pull,
        no_cache,
        cache_from,
        cache_to,
        build_args=build_args,
        dockerfile_path=dockerfile_path,
    )
