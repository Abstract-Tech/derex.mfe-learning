from pathlib import Path
from typing import Dict, List, Union

import pkg_resources
from derex.runner.project import Project
from jinja2 import Template

from derex import runner  # type: ignore
from derex.mfe_learning import __version__
from derex.mfe_learning.constants import MfeLearningVersions


def generate_local_docker_compose(project: Project) -> Path:
    derex_dir = project.root / ".derex"
    if not derex_dir.is_dir():
        derex_dir.mkdir()
    local_compose_path = derex_dir / "docker-compose-mfe-learning.yml"
    template_path = Path(
        pkg_resources.resource_filename(__name__, "docker-compose-mfe-learning.yml.j2")
    )
    config = project.config.get("plugins").get("mfe-learning") or {}

    default_docker_image_prefix = MfeLearningVersions[
        project.openedx_version.name
    ].value["docker_image_prefix"]
    mfe_learning_docker_image = config.get(
        "docker_image", f"{default_docker_image_prefix}:{__version__}"
    )
    mfe_learning_aliases = config.get("aliases") or []
    tmpl = Template(template_path.read_text())
    text = tmpl.render(
        project=project,
        mfe_learning_docker_image=mfe_learning_docker_image,
        mfe_learning_aliases=mfe_learning_aliases,
    )
    local_compose_path.write_text(text)
    return local_compose_path


class MfeLearningService:
    @staticmethod
    @runner.hookimpl
    def ddc_project_options(project: Project) -> Dict[str, Union[str, List[str]]]:
        options: List[str] = []
        if "derex.mfe-learning" in project.config.get("plugins", {}):
            local_compose_path = generate_local_docker_compose(project)
            options = ["-f", str(local_compose_path)]
        return {
            "options": options,
            "name": "mfe-learning",
            "priority": "<local-project",
        }
