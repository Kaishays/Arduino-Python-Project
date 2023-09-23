
import serial
import time

# Replace '/dev/ttyACM0' with the appropriate serial port for Arduino Uno.
# Find the correct port using the Arduino IDE or by checking the Device Manager (Windows) or ls /dev (Linux).
ser = serial.Serial('dev/ttyACM0', 9600)

def set_motor_speed(pwm_value):
    # Limit the PWM value between 0 and 255
    pwm_value = max(0, min(255, pwm_value))
    
    # Send the PWM value to the Arduino over the serial port
    ser.write(str(pwm_value).encode())
    time.sleep(0.1)   

# Controls for ski winch.
if __name__ == "__main__":
    while True:
        if input("say yes to start winch") == "yes":
            set_motor_speed(255)
            time.sleep(2) # Delay to give user enough time to get put winch handle down.
            set_motor_speed(0)


