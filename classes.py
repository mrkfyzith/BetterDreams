import pygame
import os
import numpy


class Player:
    def __init__(self):
        self.speed = 14
        self.x_offset = 0
        self.x_position = 50
        self.y_offset = 0
        self.y_position = 50

    def move(self, block_scale):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_s]:
            self.y_offset += self.speed
        if pressed_key[pygame.K_a]:
            self.x_offset -= self.speed
        if pressed_key[pygame.K_w]:
            self.y_offset -= self.speed
        if pressed_key[pygame.K_d]:
            self.x_offset += self.speed
        if self.x_offset >= block_scale:
            self.x_offset = 0
            self.x_position += 1
        if self.x_offset <= -block_scale:
            self.x_offset = 0
            self.x_position -= 1
        if self.y_offset >= block_scale:
            self.y_offset = 0
            self.y_position += 1
        if self.y_offset <= -block_scale:
            self.y_offset = 0
            self.y_position -= 1
        player_location = [self.x_position, self.y_position, self.x_offset, self.y_offset]
        return player_location

    @staticmethod
    def change_block_scale(block_scale):
        # pressed_key = pygame.key.get_pressed()
        # if pressed_key[pygame.K_EQUALS] and (150 > block_scale):
        #     block_scale += 1
        # elif pressed_key[pygame.K_MINUS] and (75 < block_scale):
        #     block_scale -= 1
        # return block_scale
        for a in pygame.event.get():
            if (a.type == pygame.MOUSEWHEEL) and (a.y == 1):
                block_scale += 5
            elif (a.type == pygame.MOUSEWHEEL) and (a.y == -1):
                block_scale -= 5
        return block_scale

    def reset_offset(self):
        self.x_offset = 0
        self.y_offset = 0


class GameEngune:
    def __init__(self):
        self.world = []
        self.texture_list = [pygame.image.load('Assets/sky.png'), pygame.image.load('Assets/grass_block.png'), pygame.image.load('Assets/stone.png'), pygame.image.load('Assets/16x16texture.png')]
        self.x_player_position = 50
        self.x_offset = 0
        self.y_player_position = 50
        self.y_offset = 0
        self.coordinates_of_visibility_horizontal = []
        self.coordinates_of_visibility_vertical = []
        self.length_list_of_visibility_horizontal = None
        self.length_list_of_visibility_vertical = None
        self.block_for_place = 1

    @staticmethod
    def open_window(width, height):
        screen = pygame.display.set_mode((width, height))  # Set window size.
        pygame.display.set_caption("NewProject")  # Set window name.
        return screen

    def read_save(self, world_size):
        os.chdir(f"{os.getcwd()}" + "\Saves")
        sorted = numpy.zeros(world_size)
        with open("World.txt", "r") as non_sorted:
            non_sorted = non_sorted.read()
        id = str()
        x = 0
        y = 0
        for i in range(len(non_sorted)):
            char = str(non_sorted[i])
            if str(char) == "0" or str(char) == "1" or str(char) == "2" or str(char) == "3" or str(char) == "4" or str(char) == "5" or str(char) == "6" or str(char) == "7" or str(char) == "8" or str(char) == "9":
                id = str(id) + str(char)
            elif str(char) == ",":
                sorted[x][y] = id
                x += 1
                id = str()
            elif str(char) == ";":
                sorted[x][y] = id
                x = 0
                y += 1
                id = str()
        self.world = sorted

    def synchronize_offset_and_player_position(self, player_location):
        self.x_player_position = player_location[0]
        self.y_player_position = player_location[1]
        self.x_offset = player_location[2]
        self.y_offset = player_location[3]

    def do_lists_of_visibility(self, width, height, block_scale):
        self.coordinates_of_visibility_horizontal = []  # В этом списке будут координаты блоков по горизонтали которые будут видны на экране
        self.coordinates_of_visibility_vertical = []  # В этом списке будут координаты блоков по вертикали которые будут видны на экране
        start_of_visibility_horizontal = self.x_player_position - (int(width / block_scale + 4)) / 2  # Кордината крайне правого блока по горизонтали который сможет увидеть игрок
        for counter in range(int(self.x_player_position + (int(width / block_scale + 4)) / 2 - start_of_visibility_horizontal)):  # Теперь мы заносим координаты блоков по горизонтали
            start_of_visibility_horizontal += 1
            self.coordinates_of_visibility_horizontal.append(int(start_of_visibility_horizontal))
        start_of_visibility_vertical = self.y_player_position - (int(height / block_scale + 4)) / 2
        for counter in range(int(self.y_player_position + (int(height / block_scale + 4)) / 2 - start_of_visibility_vertical)):
            start_of_visibility_vertical += 1
            self.coordinates_of_visibility_vertical.append(int(start_of_visibility_vertical))

    def change_world(self, width, height, block_scale):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] or mouse_pressed[2] or mouse_pressed[1]:
            mouse_pos = pygame.mouse.get_pos()
            x = -(block_scale * 2)  # Начальная позиция для рендеринга точек по горизонтали
            y = -(block_scale * 2) - self.y_offset  # Начальная позиция для рендеринга точек по вертикали
            for counter_at_vertical in range(int(height / block_scale + 4)):
                for counter_at_horizontal in range(int(width / block_scale + 4)):
                    if x < mouse_pos[0] < x + block_scale and y < mouse_pos[1] < y + block_scale and mouse_pressed[0]:
                        self.world[self.coordinates_of_visibility_horizontal[counter_at_horizontal]][self.coordinates_of_visibility_vertical[counter_at_vertical]] = self.block_for_place
                    elif x < mouse_pos[0] < x + block_scale and y < mouse_pos[1] < y + block_scale and mouse_pressed[2]:
                        self.world[self.coordinates_of_visibility_horizontal[counter_at_horizontal]][self.coordinates_of_visibility_vertical[counter_at_vertical]] = 0
                    x += block_scale
                x = -(block_scale * 2) - self.x_offset
                y += block_scale

    def change_block_for_place(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_1]:
            self.block_for_place = 1  # 1 is grass block
        elif pressed_key[pygame.K_2]:
            self.block_for_place = 2  # 2 is stone block
        elif pressed_key[pygame.K_3]:
            self.block_for_place = 3  # 2 is test 16x16 texture

    def render_capture(self, width, height, screen, block_scale):
        x = -(block_scale * 2) - self.x_offset  # Начальная позиция для рендеринга точек по горизонтали
        y = -(block_scale * 2) - self.y_offset  # Начальная позиция для рендеринга точек по вертикали
        for counter_at_vertical in range(int(height / block_scale + 4)):
            for counter_at_horizontal in range(int(width / block_scale + 4)):
                texture = pygame.transform.scale(self.texture_list[int(self.world[self.coordinates_of_visibility_horizontal[counter_at_horizontal]][self.coordinates_of_visibility_vertical[counter_at_vertical]])], (block_scale, block_scale))
                screen.blit(texture, (x, y))
                x += block_scale
            x = -(block_scale * 2) - self.x_offset
            y += block_scale
        pygame.draw.rect(screen, (0, 0, 0), (width / 2 - 25, height / 2 - 25, 50, 50))

    def save_world(self, world_size):
        with open("World.txt", "w") as save_file:
            for counter_at_vertical in range(world_size[1]):
                for counter_at_horizontal in range(world_size[0]):
                    save_file.write(str(int(self.world[counter_at_horizontal][counter_at_vertical])))
                    if counter_at_horizontal < (world_size[0] - 1):
                        save_file.write(",")
                    else:
                        save_file.write(";\n")
