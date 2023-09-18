import pygame
import numpy as np
import random


class MyMap:
    coordinateForRobot = [0, 0] # (x, y)
    field = []
    fieldSize = 0
    heightOfCellInWindow = 720
    window = None
    userHeightOfCell = 0

    def __init__(self, numberOfCells, heightOfCell):
        self.heightOfCellInWindow //= numberOfCells
        self.userHeightOfCell = heightOfCell
        self.window = pygame.display.set_mode((numberOfCells * self.heightOfCellInWindow, numberOfCells * self.heightOfCellInWindow))
        self.field = np.random.randint(0, 3, size=(numberOfCells, numberOfCells))
        self.fieldSize = numberOfCells
        self.set_robot_coordinates()

    def set_robot_coordinates(self):
        while True:
            x = random.randint(0, self.fieldSize - 1)
            y = random.randint(0, self.fieldSize - 1)

            randomCoordinates = [x, y]
            if self.field[randomCoordinates[1]][randomCoordinates[0]] != 0:
                self.coordinateForRobot = randomCoordinates
                break

    def draw_field(self):
        white = (255, 255, 255)
        red = (255, 0, 0)
        black = (0, 0, 0)

        self.window.fill(white)

        pygame.draw.rect(self.window, red, (self.coordinateForRobot[0] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2 - 5,
                                            self.coordinateForRobot[1] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2 - 5,
                                            10, 10))

        for i in range(self.fieldSize):
            for j in range(self.fieldSize):
                if self.field[i][j] == 0:
                    pygame.draw.rect(self.window, black, (j * self.heightOfCellInWindow,
                                                          i * self.heightOfCellInWindow,
                                                          self.heightOfCellInWindow, self.heightOfCellInWindow))
        self.draw_lines_from_robot()
        pygame.display.update()

    def draw_lines_from_robot(self):
        red = (255, 0, 0)
        i = self.coordinateForRobot[1]
        j = self.coordinateForRobot[0]

        # up
        while i >= 0 and self.field[i][j] != 0:
            i -= 1
        pygame.draw.rect(self.window, red, (j * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                                            (i + 1) * self.heightOfCellInWindow,
                                            1, (self.coordinateForRobot[
                                                    1] - i) * self.heightOfCellInWindow - self.heightOfCellInWindow // 2))

        print(f"{{0: {j * self.userHeightOfCell + self.userHeightOfCell / 2}, {(i + 1) * self.userHeightOfCell}")
        i = self.coordinateForRobot[1]

        # right
        while j < self.fieldSize and self.field[i][j] != 0:
            j += 1
        pygame.draw.rect(self.window, red,
                         (self.coordinateForRobot[0] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                          self.coordinateForRobot[1] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                          (j - self.coordinateForRobot[0]) * self.heightOfCellInWindow - self.heightOfCellInWindow // 2,
                          1))

        print(f"90: {j * self.userHeightOfCell}, {i * self.userHeightOfCell + self.userHeightOfCell / 2}")
        j = self.coordinateForRobot[0]

        # down
        while i < self.fieldSize and self.field[i][j] != 0:
            i += 1
        pygame.draw.rect(self.window, red,
                         (self.coordinateForRobot[0] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                          self.coordinateForRobot[1] * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                          1, (i - self.coordinateForRobot[
                             1]) * self.heightOfCellInWindow - self.heightOfCellInWindow // 2))
        print(f"180: {j * self.userHeightOfCell + self.userHeightOfCell / 2}, {i * self.userHeightOfCell}")
        i = self.coordinateForRobot[1]

        # left
        while j >= 0 and self.field[i][j] != 0:
            j -= 1
        pygame.draw.rect(self.window, red, ((j + 1) * self.heightOfCellInWindow,
                                            i * self.heightOfCellInWindow + self.heightOfCellInWindow // 2,
                                            (self.coordinateForRobot[0] - j) * self.heightOfCellInWindow - self.heightOfCellInWindow // 2, 1))
        print(f"270: {(j + 1) * self.userHeightOfCell}, {i * self.userHeightOfCell + self.userHeightOfCell / 2} }}")


    def move_robot(self, deltaX, deltaY):
        if self.fieldSize > self.coordinateForRobot[0] + deltaX >= 0 and self.fieldSize > self.coordinateForRobot[1] + deltaY >= 0:
            if self.field[self.coordinateForRobot[1] + deltaY][self.coordinateForRobot[0] + deltaX] != 0:
                self.coordinateForRobot[0] += deltaX
                self.coordinateForRobot[1] += deltaY

    def run_window(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                else:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.move_robot(-1, 0)
                    if keys[pygame.K_RIGHT]:
                        self.move_robot(1, 0)
                    if keys[pygame.K_UP]:
                        self.move_robot(0, -1)
                    if keys[pygame.K_DOWN]:
                        self.move_robot(0, 1)

                    self.draw_field()