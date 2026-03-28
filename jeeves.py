"""Project-level Jeeves commands for the docs site."""

from pathlib import Path

import sh


def install_mkdocs_insiders():
    """Install the local Insiders checkout of `mkdocs-material`."""
    name = 'mkdocs-material-insiders'

    if not (Path.cwd() / name).is_dir():
        sh.gh.repo.clone(f'iolanta-tech/{name}')

    sh.pip.install('-e', name)


def serve():
    """Serve the nanopublishing site at http://localhost:6452."""
    sh.mkdocs.serve(
        '-a',
        'localhost:6452',
        _fg=True,
    )
