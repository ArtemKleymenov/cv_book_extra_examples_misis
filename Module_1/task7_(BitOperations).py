import cv2
import numpy as np


if __name__ == "__main__":
    # If you're wondering why only two dimensions, well this is
    # a grayscale image, if we doing a colored image, we'd use
    # rectangle = np.zeros((300, 300, 3),np.uint8)

    # making a square
    square = np.zeros((300, 300), np.uint8)
    cv2.rectangle(square, (50, 50), (250, 250), 255, -1)
    cv2.imshow('square', square)

    ellipse = np.zeros((300, 300), np.uint8)
    cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 120, 255, -1)
    cv2.imshow('ellipse', ellipse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Shows only where they intersect
    And = cv2.bitwise_and(square, ellipse)
    cv2.imshow("AND", And)
    cv2.waitKey(0)

    # Shows where either square or ellipse is
    bitwiseOr = cv2.bitwise_or(square, ellipse)
    cv2.imshow("OR", bitwiseOr)
    cv2.waitKey(0)

    # Shows where either exist by itself
    bitwiseXor = cv2.bitwise_xor(square, ellipse)
    cv2.imshow("XOR", bitwiseXor)
    cv2.waitKey(0)

    # Shows everything that isn't part of the square
    bitwiseNot_sq = cv2.bitwise_not(square)
    cv2.imshow("NOT - square", bitwiseNot_sq)
    cv2.waitKey(0)

    bitwiseNot_el = cv2.bitwise_not(ellipse)
    cv2.imshow("NOT - ellipse", bitwiseNot_el)
    cv2.waitKey(0)
    # Notice the last operation inverts the image totally
    cv2.destroyAllWindows()
