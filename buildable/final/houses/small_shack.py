from buildable.house import House
from class_types.buildind_types import BuildingTypes


class SmallShack(House):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, BuildingTypes.SMALL_SHACK, tax=5, desirability=-5, max_citizen=9, prosperity=15,
                         fire_risk=0, destruction_risk=0)

    def is_upgradable(self) -> bool:
        #TODO : Add temple and get if map have any temple
        return False

    def conditions_fulfilled(self) -> bool:
        return self.get_current_tile().get_water_access()

    def upgrade(self):
        from buildable.final.houses.large_shack import LargeShack
        super().upgrade_to(LargeShack)

    def downgrade(self):
        from buildable.final.houses.large_tent import LargeTent
        super().upgrade_to(LargeTent)