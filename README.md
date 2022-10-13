# Raspberry-Pi-Pico-and-7-Segment-display
Interface a common cathode Seven segment display to Raspberry Pi Pico.
Here we are going to interface a Seven segment LED display woth Raspberry Pi Pico. Seven segment dispaly are of two types, here we are using a common cathode(LT543) type seven segment display.
# Connections of common cathode Seven segment with Raspberry Pi Pico
Connect the common cathode pin of the segment LED to GND pin of Raspberry Pi Pico.
Connect the rest segment pins to the Raspberry Pi Pico, in series with 100 ohm current limiting resistors with given wiring scheme.
a------> GPIO0
b------> GPIO1
c------> GPIO2
d------> GPIO3
e------> GPIO4
f------> GPIO5
g------> GPIO6
# Connections of common anode Seven segment with Raspberry Pi Pico
Connect the common anode pin of the segment LED to VBUS pin of Raspberry Pi Pico.
Connect the rest segment pins to the Raspberry Pi Pico, in series with 100 ohm current limiting resistors with given wiring scheme.
a------> GPIO0
b------> GPIO1
c------> GPIO2
d------> GPIO3
e------> GPIO4
f------> GPIO5
g------> GPIO6
