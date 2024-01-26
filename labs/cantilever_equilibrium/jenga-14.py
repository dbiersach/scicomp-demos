# jenga-14.py

from blocks import BlockList


def main():
    block_list = BlockList()

    block_list.place_block(7.5, 1.5)
    block_list.place_block(1.5, 10.5)

    while block_list.center_x < 15.0:
        block_list.print_center()
        block_list.move_blocks(3, 3)
        block_list.place_block(7.5, 1.5)
        block_list.place_block(1.5, 10.5)


main()
