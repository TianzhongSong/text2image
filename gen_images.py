# coding=utf-8
import os
import pygame
import random

characters = '0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def genearte_images(total_number=1000, continue_gen=False, save_path='results/'):
    """
    :param total_number:  生成多少图片
    :param continue_gen:  是否接着上一次继续生成，若是则改为True
    :param save_path: 图片保存的路径
    :return: None
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    pygame.init()
    font = pygame.font.SysFont('SimHei', 31)
    f = open('char_std_5990.txt', 'r', encoding='gbk', errors='ignore')
    label_txt = f.readlines()
    f.close()
    label_index = [label.strip() for label in label_txt]
    print(label_index)
    txt_mode = 'w' if not continue_gen else 'a'

    image_counter = 1000000
    with open('labels.txt', txt_mode) as f:
        while total_number > 0:
            label_line = str(image_counter) + '.jpg'
            text_length = random.randint(3, 25)
            text = ''
            for i in range(text_length):
                ch = characters[random.randint(0, len(characters) - 1)]
                text += ch
                label_line += ' ' + str(label_index.index(ch))
            ftext = font.render(text, True, (0, 0, 0), (255, 255, 255))
            f.write(label_line + '\n')
            pygame.image.save(ftext, save_path + str(image_counter) + ".jpg")
            image_counter += 1
            total_number -= 1
        f.close()


if __name__ == '__main__':
    genearte_images(total_number=200, continue_gen=False)
