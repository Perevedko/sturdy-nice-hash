# coding: utf-8

SECONDS_PER_DAY = 60 * 60 * 24
# SUPER_MAGIC_CONSTANT = 2 ** 32

def profitability(
    hashrate,
    difficulty,
    reward_per_block
):

    return (reward_per_block * hashrate * SECONDS_PER_DAY) / (difficulty * SUPER_MAGIC_CONSTANT)
