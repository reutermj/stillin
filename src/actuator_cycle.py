"""Basic actuator cycle test.

Extends the actuator for 1 second, then retracts for 1 second, in a loop.
Press Ctrl+C to stop.
"""

import signal
import sys
import time

from gpiozero import DigitalOutputDevice

# GPIO pins matching the wiring guide
RPWM_PIN = 17  # Extend signal
LPWM_PIN = 27  # Retract signal

CYCLE_DURATION = 1.0  # seconds


def main():
    rpwm = DigitalOutputDevice(RPWM_PIN)
    lpwm = DigitalOutputDevice(LPWM_PIN)
    # Prevent double-cleanup: gpiozero's atexit handler can race with our
    # signal handler, causing errors if we try to close already-closed devices.
    stopping = False

    def cleanup(signum, frame):
        nonlocal stopping
        if stopping:
            return
        stopping = True
        print("\nStopping...")
        rpwm.close()
        lpwm.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print("Starting actuator cycle test")
    print("Press Ctrl+C to stop")
    print()

    cycle = 0
    while True:
        cycle += 1

        print(f"Cycle {cycle}: Extending...")
        lpwm.off()
        rpwm.on()
        time.sleep(CYCLE_DURATION)

        print(f"Cycle {cycle}: Retracting...")
        rpwm.off()
        lpwm.on()
        time.sleep(CYCLE_DURATION)


if __name__ == "__main__":
    main()
