# blocks.py


class Block:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y

    def move(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y


class BlockList:
    def __init__(self):
        self.blocks = []
        self.num_blocks = 0
        self.center_x = 0.0
        self.center_y = 0.0

    def calc_center(self):
        sum_center_x, sum_center_y = 0.0, 0.0

        for block in self.blocks:
            sum_center_x += block.center_x
            sum_center_y += block.center_y

        if self.num_blocks > 0:
            self.center_x = sum_center_x / self.num_blocks
            self.center_y = sum_center_y / self.num_blocks

    def print_center(self):
        self.calc_center()
        print(
            f"Blocks: {self.num_blocks:>5}\t"
            f"Center X: {self.center_x:>6.2f}\t"
            f"Center Y: {self.center_y:>6.2f}"
        )

    def place_block(self, center_x, center_y):
        self.blocks.append(Block(center_x, center_y))
        self.num_blocks = len(self.blocks)
        self.calc_center()

    def move_blocks(self, delta_x, delta_y):
        for block in self.blocks:
            block.move(delta_x, delta_y)
        self.calc_center()
