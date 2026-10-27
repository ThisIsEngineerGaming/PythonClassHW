from dataclasses import dataclass


@dataclass
class PileOfBricks:
    owner: str
    brick_count: int
    is_stolen_from: bool
    planned_for: str

    def announce_plans(self):
        print(
            f"{self.owner}'s pile of bricks proudly declares: "
            f"\"There are {self.brick_count} of us, and we are definitely becoming a {self.planned_for}. "
            f"Just as soon as the boss finds the time...\""
        )

    def steal_brick(self):
        if self.brick_count > 0:
            self.brick_count -= 1
            self.is_stolen_from = True
            print(
                f"Someone quietly swiped a brick from {self.owner}'s pile! "
                f"{self.brick_count} left. Nobody saw anything."
            )
        else:
            print(f"There's nothing left to steal from {self.owner}'s pile. It's purely symbolic now.")

    def collapse(self):
        print(
            f"CRASH! {self.owner}'s pile has collapsed. "
            f"{self.brick_count} bricks are now \"artistically scattered\" across the yard."
        )

    def grow_weeds(self):
        weeds = self.brick_count // 10
        print(
            f"{weeds} weed bushes have sprouted between {self.owner}'s bricks. "
            f"It's no longer a pile of bricks, it's \"landscape design\"."
        )


def main():
    pile1 = PileOfBricks("Stephen", 120, False, "summer kitchen")
    pile2 = PileOfBricks("Helen", 35, False, "gazebo")
    pile3 = PileOfBricks("Uncle Nick", 1, True, "garage")

    for pile in (pile1, pile2, pile3):
        pile.announce_plans()
        pile.steal_brick()
        pile.grow_weeds()
        pile.collapse()
        print("-" * 50)


if __name__ == "__main__":
    main()