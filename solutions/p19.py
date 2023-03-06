import math

def minDistance(target):
    return target - 3 + 0.0427/2

def maxDistance(target):
    return target + 3 - 0.0427/2

def total_time(angle, distance):
    return (math.sqrt(
        2 * distance * math.sin(angle) / (9.8 * math.cos(angle))
    ))

def speed(distance, angle):
    return distance / (math.cos(angle) * total_time(angle, distance))


target = int(input())
angle = int(input()) * math.pi / 180
print("The maximum speed is: {:.2f} m/s.".format(speed(maxDistance(target), angle)))
print("The minimum speed is: {:.2f} m/s.".format(speed(minDistance(target), angle)))