# blocks.py

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class BlockList:
    def __init__(self):
        self.blocks = []
        self.num_blocks = 0
        self.center_x, self.center_y = 0, 0

    def calc_center(self):
        sum_x, sum_y = 0, 0

        for block in self.blocks:
            sum_x = sum_x + block.x
            sum_y = sum_y + block.y

        if self.num_blocks > 0:
            self.center_x = sum_x / self.num_blocks
            self.center_y = sum_y / self.num_blocks

    def print_center(self):
        self.calc_center()
        print(
            f"Blocks: {self.num_blocks:>5}\t"
            f"Center X: {self.center_x:>6.2f}\t"
            f"Center Y: {self.center_y:>6.2f}"
        )

    def place_block(self, x, y):
        self.blocks.append(Block(x, y))
        self.num_blocks = len(self.blocks)
        self.calc_center()

    def move_blocks(self, delta_x, delta_y):
        for block in self.blocks:
            block.move(delta_x, delta_y)
        self.calc_center()
