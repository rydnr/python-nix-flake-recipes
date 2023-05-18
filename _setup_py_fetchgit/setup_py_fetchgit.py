from domain.flake.flake import Flake
from domain.flake.recipe.base_flake_recipe import BaseFlakeRecipe

class SetuppyFetchgit(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for setup.py-based projects, using fetchgit
    """
    def __init__(self, flake: Flake):
        """Creates a new setup.py+fetchgit flake recipe instance"""
        super().__init__(flake)

    def usesGitrepoSha256(self):
        return True

    @classmethod
    def type_matches(cls, flake) -> bool:
        return not flake.python_package.git_repo.in_github() and flake.python_package.get_type() == "setup.py" and not flake.python_package.package_in_pypi() and not flake.python_package.git_repo.is_monorepo()
