# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython I2C Device Address Scan"""
import time
import board
import busio

print("\n\n")
print("board.board_id:", board.board_id)

i2c = None
if "itsybitsy_m4_express" in board.board_id:
    i2c = board.I2C()
# elif board.board_id is 'itsybitsy_m4_express':
# i2c = busio.I2C(board.IO8, board.IO9)

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()
