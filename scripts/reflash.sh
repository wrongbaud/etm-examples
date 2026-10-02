#!/bin/bash
openocd -f ../configs/rpi-swd.cfg -f ../configs/xbox.cfg -c "reset halt; stm32f2x unlock 0; reset halt; stm32f2x mass_erase 0; flash write_bank 0 ../firmware/048-121.bin; reset"
