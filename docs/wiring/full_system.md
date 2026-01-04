# Full System Wiring

This guide covers wiring to a Raspberry Pi 4B:
* 7 linear actuators following the standard config in [basic.md](basic.md),
* 7 temperature probes, and
* a single paristaltic pump.

## Linear Actuator Pin Assignments

All 7 actuators use adjacent pin pairs with a nearby GND pin, allowing clean 2x2 terminal block connections (3 signals + 1 unused pin).

| Actuator | RPWM Pin | RPWM GPIO | LPWM Pin | LPWM GPIO | GND Pin |
|----------|----------|-----------|----------|-----------|---------|
| 1 | 7 | GPIO 4 | 8 | GPIO 14 | 6 |
| 2 | 11 | GPIO 17 | 12 | GPIO 18 | 9 |
| 3 | 15 | GPIO 22 | 16 | GPIO 23 | 14 |
| 4 | 21 | GPIO 9 | 22 | GPIO 25 | 20 |
| 5 | 23 | GPIO 11 | 24 | GPIO 8 | 25 |
| 6 | 31 | GPIO 6 | 32 | GPIO 12 | 30 |
| 7 | 35 | GPIO 19 | 36 | GPIO 16 | 34 |

## Temperature Sensors Pin Assignments

All 7 DS18B20 temperature sensors share a single 1-Wire bus. Each sensor has a unique 64-bit address and is individually addressable. Uses a 2x2 terminal block on pins 17-20.

| Signal | Pin | GPIO/Function | Notes |
|--------|-----|---------------|-------|
| Data | 19 | GPIO 10 | 1-Wire bus, 4.7K pull-up resistor to 3.3V |
| Power | 17 | 3.3V | 3.3V power |
| Ground | 20 | GND | Ground |
| Unused | 18 | GPIO 24 | - |

### Boot Configuration

GPIO 10 is not the default 1-Wire pin. Add the following to `/boot/config.txt`:

```
dtoverlay=w1-gpio,gpiopin=10
```

Reboot for changes to take effect.

### Alternative: Use Default 1-Wire Pin

To avoid boot config changes, use GPIO 4 (pin 7) for 1-Wire instead. This requires moving actuator 1 to pins 37-38:

| Actuator | RPWM Pin | RPWM GPIO | LPWM Pin | LPWM GPIO | GND Pin |
|----------|----------|-----------|----------|-----------|---------|
| 1 | 37 | GPIO 26 | 38 | GPIO 20 | 39 |

And updating the temperature sensor block to pins 5-8:

| Signal | Pin | GPIO/Function | Notes |
|--------|-----|---------------|-------|
| Data | 7 | GPIO 4 | 1-Wire bus (default), 4.7K pull-up resistor to 3.3V |
| Power | 1 | 3.3V | 3.3V power |
| Ground | 6 | GND | Ground |
| Unused | 8 | GPIO 14 | - |

## Power Requirements

Each actuator can draw several amps under load. Size your 12V PSU based on how many actuators may run simultaneously.

## Related Documentation

- [Basic Wiring Guide](basic.md) - Single actuator setup details
- [Raspberry Pi GPIO Pinout](../rpi/README.md)
