import pygame

def draw_text(text, screen, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def score_text(score):
    return f"Score: {score}"

def final_score_text(score):
    return f"Game over! Final Score: {score}"



    