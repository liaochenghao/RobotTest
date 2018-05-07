import sys
from src.robot import robot


if __name__ == '__main__':
    port = 7080
    if len(sys.argv) > 1:
        port = sys.argv[1]
    robot.run(server='tornado', host='0.0.0.0', port=port)
