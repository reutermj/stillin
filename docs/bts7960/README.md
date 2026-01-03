# BTS7960 43A High Power Motor Driver Module

## Product Information

| Item | Value | Reference |
|------|-------|-----------|
| Product | AITRIP BTS7960 43A H-Bridge Motor Driver Module | - |
| Amazon ASIN | B09QKFFDQ3 | - |
| Chip | Infineon BTS7960B (dual half-bridge) | Chip Datasheet p.2 "Product Summary" |
| Driver Configuration | Dual BTS7960 H Bridge | Module Datasheet p.1 "Brief Data" |

## Specifications

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Operating Voltage | 5.5V - 27.5V | Chip Datasheet p.7 §4.1.1 |
| Input Voltage (module) | 6V - 27V DC | Module Datasheet p.1 "Brief Data" |
| Control Input Level | 3.3V - 5V | Module Datasheet p.1 "Brief Data" |
| Peak Current | 43A | Module Datasheet p.1 "Brief Data" |
| Current Limitation Level | 43A typ. | Chip Datasheet p.2 "Basic Features" |
| PWM Frequency | Up to 25 kHz | Module Datasheet p.1 "Brief Data" |
| Working Duty Cycle | 0% - 100% | Module Datasheet p.1 "Brief Data" |
| Path Resistance | typ. 16 mΩ @ 25°C | Chip Datasheet p.2 "Basic Features" |
| High Side On-Resistance | typ. 7 mΩ @ 25°C | Chip Datasheet p.9 §4.2.1 |
| Low Side On-Resistance | typ. 9 mΩ @ 25°C | Chip Datasheet p.9 §4.2.4 |
| Quiescent Current | typ. 7 µA @ 25°C | Chip Datasheet p.2 "Basic Features" |
| Supply Current (active) | typ. 2 mA, max 3 mA | Chip Datasheet p.7 §4.1.2 |
| Board Size | 50mm x 50mm x 43mm | Module Datasheet p.1 "Brief Data" |
| Weight | ~66g | Module Datasheet p.1 "Brief Data" |

## Control Input Pin Configuration

| Pin | Function | Description | Reference |
|-----|----------|-------------|-----------|
| 1 | RPWM | Forward Level or PWM signal, Active High | Module Datasheet p.3 "Control Input Pin Function" |
| 2 | LPWM | Reverse Level or PWM signal, Active High | Module Datasheet p.3 "Control Input Pin Function" |
| 3 | R_EN | Forward Drive Enable Input, Active High / Low Disable | Module Datasheet p.3 "Control Input Pin Function" |
| 4 | L_EN | Reverse Drive Enable Input, Active High / Low Disable | Module Datasheet p.3 "Control Input Pin Function" |
| 5 | R_IS | Forward Drive, Side current alarm output | Module Datasheet p.3 "Control Input Pin Function" |
| 6 | L_IS | Reverse Drive, Side current alarm output | Module Datasheet p.3 "Control Input Pin Function" |
| 7 | Vcc | +5V Power Supply for microcontroller | Module Datasheet p.3 "Control Input Pin Function" |
| 8 | Gnd | Ground Power Supply for microcontroller | Module Datasheet p.3 "Control Input Pin Function" |

## Motor Power Supply & Output Pins

| Pin | Function | Description | Reference |
|-----|----------|-------------|-----------|
| 1 | B+ | Positive Motor Power Supply, 6-27V DC | Module Datasheet p.4 "Motor Power Supply & Output Pin Assignment" |
| 2 | B- | Negative Motor Power Supply, Ground | Module Datasheet p.4 "Motor Power Supply & Output Pin Assignment" |
| 3 | M+ | Motor Output + | Module Datasheet p.4 "Motor Power Supply & Output Pin Assignment" |
| 4 | M- | Motor Output - | Module Datasheet p.4 "Motor Power Supply & Output Pin Assignment" |

## BTS7960 Chip Pin Functions

| Pin | Symbol | Function | Reference |
|-----|--------|----------|-----------|
| 1 | GND | Ground | Chip Datasheet p.5 §2.2 |
| 2 | IN | Input - Defines whether high- or lowside switch is activated | Chip Datasheet p.5 §2.2 |
| 3 | INH | Inhibit - When set to low device goes in sleep mode | Chip Datasheet p.5 §2.2 |
| 4,8 | OUT | Power output of the bridge | Chip Datasheet p.5 §2.2 |
| 5 | SR | Slew Rate - Adjustable by resistor between SR and GND | Chip Datasheet p.5 §2.2 |
| 6 | IS | Current Sense and Diagnosis | Chip Datasheet p.5 §2.2 |
| 7 | VS | Supply | Chip Datasheet p.5 §2.2 |

## Protection Features

| Feature | Description | Reference |
|---------|-------------|-----------|
| Overvoltage Lock Out | Shuts lowside off and turns highside on if VS exceeds VOV(OFF) (27.6-30V) | Chip Datasheet p.13 §4.3.1 |
| Undervoltage Shut Down | Device shuts off if VS drops below VUV(OFF) (4.0-5.4V) | Chip Datasheet p.13 §4.3.2 |
| Overtemperature Protection | Integrated temperature sensor, shuts down both output stages, latched until reset | Chip Datasheet p.13 §4.3.3 |
| Thermal Shutdown Temperature | typ. 175°C (min 152°C, max 200°C) | Chip Datasheet p.16 §4.3.10 |
| Thermal Hysteresis | typ. 7K | Chip Datasheet p.16 §4.3.12 |
| Current Limitation | Switched mode current limitation at 43A typ. | Chip Datasheet p.13-14 §4.3.4 |
| Short Circuit Protection | Protected against output short to GND, VS, and load short | Chip Datasheet p.15 §4.3.5 |

## Control Logic Truth Table

| INH | IN | High Side | Low Side | IS Output | Mode | Reference |
|-----|-----|-----------|----------|-----------|------|-----------|
| 0 | X | OFF | OFF | 0 | Stand-by mode | Chip Datasheet p.19 §4.4.5 |
| 1 | 0 | OFF | ON | 0 | LSS active | Chip Datasheet p.19 §4.4.5 |
| 1 | 1 | ON | OFF | CS | HSS active | Chip Datasheet p.19 §4.4.5 |

## Input Characteristics

| Parameter | Min | Typ | Max | Unit | Reference |
|-----------|-----|-----|-----|------|-----------|
| High level voltage (INH, IN) | - | 1.75/1.6 | 2.15/2 | V | Chip Datasheet p.20 §4.4.1 |
| Low level voltage (INH, IN) | 1.1 | 1.4 | - | V | Chip Datasheet p.20 §4.4.2 |
| Input voltage hysteresis | - | 350/200 | - | mV | Chip Datasheet p.20 §4.4.3 |
| Input current (high) | - | 30 | 150 | µA | Chip Datasheet p.20 §4.4.4 |

## Current Sense

| Parameter | Min | Typ | Max | Unit | Reference |
|-----------|-----|-----|-----|------|-----------|
| Current sense ratio (kILIS = IL/IIS) | 6 | 8.5 | 11 | x10³ | Chip Datasheet p.20 §4.4.6 |
| Max sense current (fault condition) | 4 | 4.5 | 7 | mA | Chip Datasheet p.20 §4.4.7 |

## Maximum Ratings

| Parameter | Min | Max | Unit | Reference |
|-----------|-----|-----|------|-----------|
| Supply voltage | -0.3 | 45 | V | Chip Datasheet p.6 §3.0.1 |
| Logic Input Voltage | -0.3 | 5.3 | V | Chip Datasheet p.6 §3.0.2 |
| HS/LS continuous drain current | -40 | 40 | A | Chip Datasheet p.6 §3.0.3 |
| HS/LS pulsed drain current | -60 | 60 | A | Chip Datasheet p.6 §3.0.4-5 |
| Junction temperature | -40 | 150 | °C | Chip Datasheet p.6 §3.0.9 |
| Storage temperature | -55 | 150 | °C | Chip Datasheet p.6 §3.0.10 |

## Thermal Characteristics

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Thermal Resistance Junction-Case (Low Side) | 1.8 | K/W | Chip Datasheet p.21 §5.0.1 |
| Thermal Resistance Junction-Case (High Side) | 0.9 | K/W | Chip Datasheet p.21 §5.0.2 |
| Thermal Resistance Junction-Case (both) | 1.0 | K/W | Chip Datasheet p.21 §5.0.3 |
| Thermal Resistance Junction-Ambient | 35 | K/W | Chip Datasheet p.21 §5.0.4 |

## Documentation Files

- `BTS7960_Motor_Driver_Module.pdf` - Module datasheet from Handsontec (7 pages)
- `BTS7960_Chip_Datasheet.pdf` - Infineon BTS7960 chip datasheet (28 pages)

## References

- [Amazon Product Page](https://www.amazon.com/AITRIP-BTS7960-Driver-Arduino-Current/dp/B09QKFFDQ3)
- [Instructables Tutorial](https://www.instructables.com/Motor-Driver-BTS7960-43A/)
- [Electropeak Arduino Guide](https://electropeak.com/learn/interfacing-bts7960-43a-high-power-motor-driver-module-with-arduino/)
- [Raspberry Pi Forums Discussion](https://forums.raspberrypi.com/viewtopic.php?t=176168)
