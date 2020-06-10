from math import sin, cos, sqrt, acos, atan2
import numpy as np


def get_angles(i, j, k, rx=0, ry=0, rz=0):
    a0 = 5
    a1 = 5
    a2 = 5
    a3 = 5
    a4 = 5
    a5 = 5

    # rx, ry and rz are in radians
    rx = np.deg2rad(rx)
    ry = np.deg2rad(ry)
    rz = np.deg2rad(rz)

    p0_6 = np.array([[i], [j], [k]])
    R_Z = np.array([[cos(rz), -1*sin(rz), 0], [sin(rz), cos(rz), 0], [0, 0, 1]])
    R_Y = np.array([[cos(ry), 0, sin(ry)], [0, 1, 0], [-1 * sin(ry), 0, cos(ry)]])
    R_X = np.array([[1, 0, 0], [0, cos(rx), -1 * sin(rx)], [0, sin(rx), cos(rx)]])
    R0_6 = np.dot(np.dot(R_X, R_Y), R_Z)

    Wo_c = p0_6 - (a5 + a4) * np.dot(R0_6, np.array([[0], [0], [1]]))
    # print(Wo_c)
    x = Wo_c[0, 0]
    y = Wo_c[1, 0]
    z = Wo_c[2, 0]
    # print(round(x), round(y), round(z))
    r = sqrt(x ** 2 + y ** 2)
    p = z - a0
    k = sqrt(r ** 2 + p ** 2)

    # radians
    t0_rad = atan2(y, x)     # radians
    t0_deg = np.rad2deg(t0_rad)  # degrees

    phi_rad = acos((a1 ** 2 + (a2 + a3) ** 2 - k ** 2) / (2 * (a2 + a3) * a1))  # radians
    phi_deg = np.rad2deg(phi_rad)  # degrees

    t2_deg = -1*(180 - phi_deg)  # degree
    t2_rad = np.deg2rad(t2_deg)  # radians

    alpha = atan2(p, r)  # radians
    beta = acos((a1 ** 2 + k ** 2 - (a2 + a3) ** 2) / (2 * a1 * k))  # radians

    t1_rad = alpha + beta  # radian
    t1_deg = np.rad2deg(t1_rad)  # degrees

    R0_1 = np.array([[cos(t0_rad), 0, sin(t0_rad)], [sin(t0_rad), 0, -1 * cos(t0_rad)], [0, 1, 0]])
    R1_2 = np.array([[cos(t1_rad), -1 * sin(t1_rad), 0], [sin(t1_rad), cos(t1_rad), 0], [0, 0, 1]])
    R2_3 = np.array([[-1 * sin(t2_rad), 0, cos(t2_rad)], [cos(t2_rad), 0, sin(t2_rad)], [0, 1, 0]])

    R0_3 = np.dot(np.dot(R0_1, R1_2), R2_3)
    R3_6 = np.dot(np.linalg.inv(R0_3), R0_6)

    t3_rad = atan2(R3_6[1, 2], R3_6[0, 2])
    t4_rad = acos(R3_6[2, 2])
    t5_rad = atan2(R3_6[2, 1], -1 * R3_6[2, 0])

    t3_deg = np.rad2deg(t3_rad)
    t4_deg = np.rad2deg(t4_rad)
    t5_deg = np.rad2deg(t5_rad)

    return [t0_deg, t1_deg, t2_deg, t3_deg, t4_deg, t5_deg]

