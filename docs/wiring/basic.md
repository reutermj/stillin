# Basic Wiring Guide: Raspberry Pi + BTS7960 + Linear Actuator

This guide covers the simplest wiring configuration to control an ECO-WORTHY 12V linear actuator using a BTS7960 motor driver and Raspberry Pi 4B.

## Components

| Component | Details |
|-----------|---------|
| Raspberry Pi 4B | Running, powered separately |
| BTS7960 Motor Driver | 43A H-Bridge module |
| Linear Actuator | ECO-WORTHY 12V DC, 2" stroke |
| 12V DC Power Supply | Minimum 3A capacity |

## Wire Colors Used

| Color | Purpose |
|-------|---------|
| Red | Power (+12V, +5V/Vcc) |
| Black | Ground |
| Yellow | RPWM signal (extend) |
| Orange | LPWM signal (retract) |
| Blue | Motor connections |

## What You'll Need

- 2x Dupont jumper wires (female-to-female): Yellow, Orange
- 2x Dupont jumper wires (female-to-female): Black (for ground)
- 2x Short jumper wires or dupont wires: Red (for enable pins)
- Hookup wire (cut to length): Red, Black, Blue

## Wiring Overview

```
     +---------------+              +-----------------+
     |   12V PSU     |              | LINEAR ACTUATOR |
     |   (external)  |              |                 |
     |  RED    BLACK |              |   Red    Black  |
     +---+-------+---+              +----+-------+----+
         |       |                       |       |                   
         |       |                       |       |                   
    +----|-------|-----------------------|-------|--------------+
    |    |       |                       |       |              |
    |    V       V                       V       V              |
    | +------+------+                 +------+------+           |
    | |  B+  |  B-  |                 |  M+  |  M-  |           |
    | +------+------+                 +------+------+           |
    | POWER TERMINALS (screw)         MOTOR TERMINALS (screw)   |
    |                                                           |
    |                        BTS7960                            |
    |                     MOTOR DRIVER                          |
    |                                                           |
    | 8-PIN CONTROL HEADER                                      |
    | +------+------+------+------+------+------+------+------+ |
    | |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   | |
    | | RPWM | LPWM | R_EN | L_EN | R_IS | L_IS | Vcc  | GND  | |
    | +------+------+------+------+------+------+------+------+ |
    |    ^      ^      ^      ^                    ^      ^     |
    |    |      |      |      |                    |      |     |
    +----|------|------|------|--------------------|------|-----+
         |      |      |      |                    |      |
         |      |      +------+--------------------+      |
         |      |            RED jumper wires             |
       YELLOW ORANGE         on board: R_EN & L_EN      BLACK
         |      |            both connect to Vcc          |
         |      |                                         |
+--------|------|-----------------------------------------|------+
|        |      |                                         |      |
|        V      V                                         V      |
| +----------+---------+------------------------------+--------+ |
| |  Pin 11  | Pin 13  |                              | Pin 14 | |
| |  GPIO 17 | GPIO 27 |             ...              |  GND   | |
| +----------+---------+------------------------------+--------+ |
|                          GPIO HEADER                           |
|                          RASPBERRY PI                          |
|                                                                |
+----------------------------------------------------------------+
```

## Connection Tables

### High-Power Connections (use hookup wire)

These carry significant current. Use appropriately rated wire.

| From | To | Wire Color | Notes |
|------|----|------------|-------|
| 12V PSU (+) | BTS7960 B+ | Red | Main motor power |
| 12V PSU (-) | BTS7960 B- | Black | Power ground |
| BTS7960 M+ | Actuator Red Wire | N/A | Motor output |
| BTS7960 M- | Actuator Black Wire | N/A | Motor output |

### Logic Connections (use dupont jumper wires)

| From | To | Wire Color | Notes |
|------|----|------------|-------|
| Pi Pin 11 (GPIO 17) | BTS7960 RPWM (pin 1) | Yellow | Extend signal |
| Pi Pin 13 (GPIO 27) | BTS7960 LPWM (pin 2) | Orange | Retract signal |
| Pi Pin 14 (GND) | BTS7960 GND (pin 8) | Black | Common ground |

### Enable Pins (on BTS7960 board only)

Tie the enable pins to Vcc so the driver is always enabled. Use short jumper wires directly on the BTS7960 8-pin header.

| From | To | Wire Color | Notes |
|------|----|------------|-------|
| BTS7960 Vcc (pin 7) | BTS7960 R_EN (pin 3) | Red | Always enabled |
| BTS7960 Vcc (pin 7) | BTS7960 L_EN (pin 4) | Red | Always enabled |

## BTS7960 8-Pin Header Reference

**Pin assignments:**
- Pin 1 (RPWM): Yellow wire from Pi GPIO 17
- Pin 2 (LPWM): Orange wire from Pi GPIO 27
- Pin 3 (R_EN): Jumper to Pin 7 (Vcc)
- Pin 4 (L_EN): Jumper to Pin 7 (Vcc)
- Pin 5 (R_IS): Not connected
- Pin 6 (L_IS): Not connected
- Pin 7 (Vcc): Source for enable jumpers
- Pin 8 (GND): Black wire from Pi GND

## Raspberry Pi 4B GPIO Pins Used

| Physical Pin | GPIO | Wire Color | Connection |
|--------------|------|------------|------------|
| 11 | GPIO 17 | Yellow | RPWM (extend) |
| 13 | GPIO 27 | Orange | LPWM (retract) |
| 14 | GND | Black | BTS7960 GND |

## Control Logic

| GPIO 17 | GPIO 27 | Result |
|---------|---------|--------|
| HIGH | LOW | Actuator extends |
| LOW | HIGH | Actuator retracts |
| LOW | LOW | Actuator stops (holds position) |
| HIGH | HIGH | Do not use (undefined) |

## Important Notes

### Common Ground
The Raspberry Pi and BTS7960 must share a common ground reference. This is why we connect Pi GND to BTS7960 GND. Without this connection, the GPIO signals won't be interpreted correctly by the motor driver.

### Actuator Safety Features
The linear actuator has internal limit switches that automatically stop it at full extension and full retraction. You don't need to worry about over-driving it.

### Power Sequencing
1. Connect all wiring with everything powered off
2. Power on the 12V supply first
3. Then power on / boot the Raspberry Pi
4. When shutting down, reverse the order

### Never Connect While Live
Always power everything off before connecting or disconnecting wires. The BTS7960 handles high currents that can damage components or cause shorts if wires are connected incorrectly while powered.

## Future Enhancements

### Current Sensing (R_IS / L_IS pins)
The R_IS and L_IS pins on the BTS7960 output a small current proportional to motor current (ratio ~8500:1). By connecting these to analog inputs (via an ADC, since the Pi lacks analog inputs), you could:

- Detect stall conditions (current spike when actuator hits limit)
- Monitor power consumption
- Implement software current limiting

This would require:
- An ADC module (e.g., ADS1115)
- Sense resistors to convert current to voltage
- Additional wiring and code

For now, the internal limit switches in the actuator provide adequate end-of-travel protection.

## Related Documentation

- [BTS7960 Motor Driver](../bts7960/README.md)
- [Linear Actuator](../linear-actuator/README.md)
