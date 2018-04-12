from serialpacket import SerialPacket
import serial


class PlatformSerial:
    def __init__(self, platform_port):
        self.port = platform_port
        try:
            self.ser = serial.Serial(self.port, 115200)
        except Exception as e:
            print('[PlatformSerial| INIT ERROR: ', e, ']')
        self.read_packet = SerialPacket()
        self.write_packet = SerialPacket()

    def _read(self, packet=SerialPacket()):
        try:
            b = self.ser.read(18)
        except Exception as e:
            print('[PlatformSerial| READ ERROR', e, ']')
            return
        packet.read_bytes(b)

    def _write(self, packet=SerialPacket()):
        try:
            self.ser.write(packet.write_bytes())
        except Exception as e:
            print('[PlatformSerial| WRITE ERROR', e, ']')

    def send(self):
        self.write_packet.alive = self.read_packet.alive
        self._write(self.write_packet)

    def recv(self):
        self._read(self.read_packet)

    def set_automode(self):
        self.write_packet.aorm = SerialPacket.AORM_AUTO

    def set_manualmode(self):
        self.write_packet.aorm = SerialPacket.AORM_MANUAL

    def read(self):
        return self.read_packet.speed, self.read_packet.enc

    def write(self, gear, speed, steer, brake):
        self.write_packet.gear = gear
        self.write_packet.speed = speed
        self.write_packet.steer = steer
        self.write_packet.brake = brake

    def print_status(self):
        speed = self.read_packet.speed / 10
        steer = self.read_packet.steer / 71
        brake = (self.read_packet.brake - SerialPacket.BRAKE_NOBRAKE) / \
                (SerialPacket.BRAKE_MAXBRAKE - SerialPacket.BRAKE_NOBRAKE)
        print(self.read_packet.get_attr())
        print(str(speed) + 'kph', str(round(steer, 4)) + 'deg', str(round(brake, 4)) + 'brake')
        print()

import time
def test_move(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_FORWARD, 50, SerialPacket.STEER_STRAIGHT, SerialPacket.BRAKE_NOBRAKE)
        platform.send()

def test_back(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_BACKWARD, 60, SerialPacket.STEER_STRAIGHT, SerialPacket.BRAKE_NOBRAKE)
        platform.send()

def test_stop(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_NEUTRAL, 0, SerialPacket.STEER_STRAIGHT, 33)
        platform.send()

def test_neutral(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_NEUTRAL, 0, SerialPacket.STEER_STRAIGHT, SerialPacket.BRAKE_NOBRAKE)
        platform.send()

def test_left(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_NEUTRAL, 0, SerialPacket.STEER_MAXLEFT, SerialPacket.BRAKE_NOBRAKE)
        platform.send()

def test_right(timeout=2):
    t1 = time.time()
    while time.time() - t1 < timeout:
        platform.recv()
        platform.print_status()
        platform.write(SerialPacket.GEAR_NEUTRAL, 0, SerialPacket.STEER_MAXRIGHT, SerialPacket.BRAKE_NOBRAKE)
        platform.send()

if __name__ == '__main__':
    port = 'COM7'
    platform = PlatformSerial(port)
    while True:
        test_move()
        test_stop()
