from setuptools import setup

setup(
    name='mpu9x50',
    version='0.0.1',
    description='MPU9X50 IMUs',
    author='Peter Somers',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=['imu']
)