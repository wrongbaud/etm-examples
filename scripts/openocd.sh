openocd -f ../configs/rpi-swd.cfg -f ../configs/xbox.cfg -c "resume; sleep 2000; reset halt"
