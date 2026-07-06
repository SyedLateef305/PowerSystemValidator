from models.island import Island


class IslandParser:

    def __init__(self, section):
        self.section = section

    def parse(self):

        rows = []

        for row in self.section:

            if row.startswith("%"):
                continue

            rows.append(row.split())

        island = Island(

            island_no=int(rows[0][0]),
            converged=int(rows[0][1])

        )

        return island