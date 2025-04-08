import click
from pathlib import Path
import subprocess
import importlib.resources as pkg_resources
import crypticorn.cli.templates as templates

def get_git_root() -> Path:
    '''Get the root directory of the git repository.'''
    try:
        return Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    except Exception:
        return Path.cwd()

def copy_template(template_name: str, target_path: Path):
    '''Copy a template file to the target path.'''
    with pkg_resources.files(templates).joinpath(template_name).open("r") as template_file:
        content = template_file.read()

    target_path.parent.mkdir(parents=True, exist_ok=True)
    with target_path.open("w") as f:
        f.write(content)

    click.secho(f"✅ Created: {target_path}", fg="green")

@click.group()
def init_group():
    """Initialize files like CI configs, linters, etc."""
    pass

@init_group.command("ruff")
def init_ruff():
    """Add .github/workflows/ruff.yml"""
    root = get_git_root()
    target = root / ".github/workflows/ruff.yml"
    copy_template("ruff.yml", target)

@init_group.command("docker")
def init_docker():
    """Add Dockerfile"""
    root = get_git_root()
    target = root / "Dockerfile"
    copy_template("Dockerfile", target)
    click.secho("Make sure to update the Dockerfile", fg="yellow")
