class IslandValidator:

    def __init__(self, island):

        self.island = island

        self.errors = []

    def validate(self):

        self.errors.clear()

        self.check_island()

        self.check_convergence()

        return self.errors

    # -------------------------------------

    def check_island(self):

        if self.island.island_no <= 0:

            self.errors.append({

                "type": "island",

                "message": "Invalid Island Number."

            })

    # -------------------------------------

    def check_convergence(self):

        if self.island.converged not in [0, 1]:

            self.errors.append({

                "type": "convergence",

                "message": "Convergence must be 0 or 1."

            })