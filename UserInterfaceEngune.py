import pygame
import time
import os

pygame.init()


class Button:
    def __init__(self, pos_x, pos_y, width, height, color, surface, color_pressed, cooldown, text, font_size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        self.color_pressed = color_pressed
        self.cooldown_timer = 1
        self.cooldown = cooldown
        self.text = text
        self.font_size = font_size
        self.unavailable = False

    def update_info(self, unavailable):
        self.unavailable = unavailable

    def work(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        do_action = False
        if (self.unavailable is not True) and (mouse_pressed[0] or mouse_pressed[2]) and mouse_pos[0] >= self.pos_x and mouse_pos[1] >= self.pos_y and mouse_pos[0] <= (self.pos_x + self.width) and mouse_pos[1] <= (self.pos_y + self.height):
            color = self.color_pressed
            if (time.time() - self.cooldown_timer) > self.cooldown:
                do_action = True
                self.cooldown_timer = time.time()
        elif self.unavailable:
            color = (128, 128, 128)
        else:
            color = self.color
        if color is not None:
            text_to_blit = pygame.font.SysFont(f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", self.font_size)  # Записываю в переменную параметры шрифта
            text_to_blit = text_to_blit.render(self.text, True, (255, 255, 255))  # Конвертирую текст из текстоваого формата в формат картинки для блицирования
            text_width = text_to_blit.get_width()  # Записываем в переменную ширину картинки(в пикселях)
            text_height = text_to_blit.get_height()  # Записываем в переменную высоту картинки(в пикселях)
            pygame.draw.rect(self.surface, color, (self.pos_x, self.pos_y, self.width, self.height))  # Рисуем кнопку
            self.surface.blit(text_to_blit, (self.pos_x + self.width / 2 - text_width / 2, self.pos_y + self.height / 2 - text_height / 2))  # Рисуем текст в центре кнопки
        return do_action


class Message:
    def __init__(self, surface, pos_x, pos_y, font, font_size):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font = font
        self.font_size = font_size
        self.cooldown_timer = 1
        self.color = (0, 0, 0)
        self.text = ""
        self.cooldown = 0
        self.is_on = True

    def update_info(self, color, text, cooldown):
        self.color = color
        self.text = text
        self.cooldown = cooldown
        self.is_on = True

    def work(self):
        if self.is_on:
            if (time.time() - self.cooldown_timer) > self.cooldown:
                self.cooldown_timer = time.time()
                self.is_on = False
            else:
                font = pygame.font.SysFont(self.font, self.font_size)  # Записываю в переменную параметры шрифта
                text_to_blit = font.render(self.text, True, self.color)  # Конвертирую текст из текстоваого формата в формат картинки для блицирования
                text_width = text_to_blit.get_width()  # Записываем в переменную ширину картинки(в пикселях)
                text_height = text_to_blit.get_height()  # Записываем в переменную высоту картинки(в пикселях)
                alpha = round(((self.cooldown - (time.time() - self.cooldown_timer)) / 4), 1) * 255  # Вычисляем значение альфа-канала
                if alpha > 255:  # Значение альфа-канала может быть больше 255, что бы программа не останавливалась добавим проверку на то больше ли значение альфа-канала чем 255
                    text_to_blit.set_alpha(0)  # Если значение альфа-канала больше 255 то мы меняем его на 0
                else:
                    text_to_blit.set_alpha(
                        int(alpha))  # Если значение альфа-канала меньше чем 255 то мы оставляем всё как есть
                self.surface.blit(text_to_blit, (self.pos_x - text_width / 2, self.pos_y - text_height / 2))  # Рисуем текст


class Label:
    def __init__(self, surface, pos_x, pos_y, font, font_size):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font = font
        self.font_size = font_size
        self.color = (0, 0, 0)
        self.text = ""

    def update_info(self, color, text):
        self.color = color
        self.text = text

    def work(self):
        font = pygame.font.SysFont(self.font, self.font_size)  # Записываю в переменную параметры шрифта
        text_to_blit = font.render(self.text, True, self.color)  # Конвертирую текст из текстоваого формата в формат картинки для блицирования
        text_width = text_to_blit.get_width()  # Записываем в переменную ширину картинки(в пикселях)
        text_height = text_to_blit.get_height()  # Записываем в переменную высоту картинки(в пикселях)
        self.surface.blit(text_to_blit, (self.pos_x - text_width / 2, self.pos_y - text_height / 2))  # Рисуем текст
