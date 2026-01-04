"""Linear actuator control via BTS7960 motor driver.

This module provides a LinearActuator class for controlling 12V DC linear
actuators through a BTS7960 H-bridge motor driver connected to Raspberry Pi
GPIO pins.
"""

from gpiozero import DigitalOutputDevice

# Architecture
# =================================================================================================
#
# How do we wire up the actuator?
# -------------------------------------------------------------------------------------------------
# Single actuator setup: docs/wiring/basic.md
# 
# How do we control the direction of the actuator?
# -------------------------------------------------------------------------------------------------
# BTS7960 H-bridge is controlled via two GPIO pins (RPWM, LPWM).
#
# Command   | RPWM | LPWM
# ----------|------|------
# extend    | HIGH | LOW
# retract   | LOW  | HIGH
# hold      | LOW  | LOW
# undefined | HIGH | HIGH
#
# Why DigitalOutputDevice?
# -------------------------------------------------------------------------------------------------
# Variable speed via PWM is not needed; we only care about extend/retract.
# Uses gpiozero DigitalOutputDevice for simple on/off control.


class LinearActuator:
    """Controls a linear actuator via BTS7960 motor driver.

    Use as a context manager to ensure GPIO resources are released:

        with LinearActuator(rpwm_pin=17, lpwm_pin=27) as actuator:
            actuator.extend()

    Multiple actuators:

        with (
            LinearActuator(rpwm_pin=17, lpwm_pin=27) as actuator1,
            LinearActuator(rpwm_pin=22, lpwm_pin=23) as actuator2,
        ):
            actuator1.extend()
            actuator2.retract()

    Args:
        rpwm_pin: GPIO pin number for the extend signal.
        lpwm_pin: GPIO pin number for the retract signal.
    """

    def __init__(self, rpwm_pin: int, lpwm_pin: int):
        self._rpwm = DigitalOutputDevice(rpwm_pin)
        self._lpwm = DigitalOutputDevice(lpwm_pin)

    def extend(self) -> None:
        """Start extending the actuator."""
        self._lpwm.off()
        self._rpwm.on()

    def retract(self) -> None:
        """Start retracting the actuator."""
        self._rpwm.off()
        self._lpwm.on()

    def stop(self) -> None:
        """Stop the actuator (holds current position)."""
        self._rpwm.off()
        self._lpwm.off()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._rpwm.close()
        self._lpwm.close()
        return False
