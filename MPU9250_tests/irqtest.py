# Test program for IRQ based access to MPU9250
# Note there will be small differences between the lines because
# of drift or movement occurring between the readings
from mpu9250 import MPU9250

imu = MPU9250(bus=1, device_addr=0x68)

for count in range(10):
    scale = 6.6666                      # Correction factors involve floating point
    mag = list(map(lambda x, y : x*y/scale, imu.mag.ixyz, imu.mag_correction))
    print("Interrupt:", [x/16384 for x in imu.accel.ixyz], [x/131 for x in imu.gyro.ixyz], mag)
    print("Normal:   ", imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
    print()
