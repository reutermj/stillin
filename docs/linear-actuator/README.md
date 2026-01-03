# ECO-WORTHY 12V DC Linear Actuator (2" Stroke)

## Product Information

| Item | Value |
|------|-------|
| Product | ECO-WORTHY 12V DC Linear Actuator |
| Amazon ASIN | B07M9Y2JHV |
| Stroke Length | 2" (50mm) |
| Manufacturer | ECO-WORTHY |

## Specifications

| Parameter | Value |
|-----------|-------|
| Input Voltage | 12V DC |
| Max Push Load | 1500N / 330 lbs |
| Max Pull Load | 1000N / 264 lbs |
| No-load Current | 0.8A |
| Max Load Current | 3A |
| Travel Speed | 10 mm/s (0.39 in/s) |
| Duty Cycle | 25% |
| Noise Level | < 50 dB |
| Protection Class | IP54 |
| Operating Temperature | -26°C to +65°C |
| Material | Aluminum alloy |

## Wiring

| Wire Color | Connection | Action |
|------------|------------|--------|
| Red | Positive (+) | Connect to +12V |
| Black | Negative (-) | Connect to GND |

### Direction Control

| Red Wire | Black Wire | Result |
|----------|------------|--------|
| +12V | GND | Extend |
| GND | +12V | Retract |

The actuator holds its position when power is removed (built-in safety lock). It automatically stops when reaching either end of stroke (internal limit switches).

## Features

- **Aluminum Alloy Housing**: Durable construction with IP54 protection
- **Internal Limit Switches**: Auto-stops at full extension/retraction
- **Self-Locking**: Holds position when power is removed
- **Quiet Operation**: < 50 dB noise level
- **Metal Gears**: Alloy-steel shaft with metal gears for durability

## Usage with BTS7960 Motor Driver

The linear actuator can be controlled using the BTS7960 H-bridge motor driver:

| Actuator | BTS7960 |
|----------|---------|
| Red Wire | M+ |
| Black Wire | M- |

**Control Logic:**
- RPWM HIGH + LPWM LOW = Extend
- RPWM LOW + LPWM HIGH = Retract
- Both LOW = Stop (actuator holds position)

**Power Notes:**
- At 3A max load current, the BTS7960 (rated 43A) has ample capacity
- Use PWM for speed control if desired
- Monitor current via IS pins for stall detection

## References

- [Amazon Product Page](https://www.amazon.com/dp/B07M9Y2JHV)
