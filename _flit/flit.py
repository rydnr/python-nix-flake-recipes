from domain.flake.flake import Flake
from domain.flake.recipe.base_flake_recipe import BaseFlakeRecipe

class Flit(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for flit-based projects.
    """
    def __init__(self, flake: Flake):
        """Creates a new flit flake recipe instance"""
        super().__init__(flake)

    @classmethod
    def matches(cls, flake):
        return flake.python_package.get_package_type() == "flit"
