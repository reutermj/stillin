"""Basic actuator cycle test.

Extends the actuator for 1 second, then retracts for 1 second, in a loop.
Press Ctrl+C to stop.
"""

import time

from src.linear_actuator import LinearActuator

# GPIO pins matching the wiring guide
RPWM_PIN = 17  # Extend signal
LPWM_PIN = 27  # Retract signal

CYCLE_DURATION = 1.0  # seconds


def main():
    print("Starting actuator cycle test")
    print("Press Ctrl+C to stop")
    print()

    try:
        with LinearActuator(rpwm_pin=RPWM_PIN, lpwm_pin=LPWM_PIN) as actuator:
            cycle = 0
            while True:
                cycle += 1

                print(f"Cycle {cycle}: Extending...")
                actuator.extend()
                time.sleep(CYCLE_DURATION)

                print(f"Cycle {cycle}: Retracting...")
                actuator.retract()
                time.sleep(CYCLE_DURATION)
    except KeyboardInterrupt:
        print("\nStopping...")


if __name__ == "__main__":
    main()
