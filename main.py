import pygame
import sys
import time
from pygame import Color
from japanese import Japanese

class MainWindow:

    def __init__(self):

        pygame.init()

        self.question_font = pygame.font.SysFont('Arial', 32)
        self.question_font_text = pygame.font.Font('YuGothl.ttc', 142)
        self.answer_font = pygame.font.SysFont('Arial', 24)

        self.MAIN_WINDOW_WIDTH = 850
        self.MAIN_WINDOW_HEIGHT = 640
        self.AVAILABLE_ANSWERS = 4

        self.ANSWER_SQUARE_HEIGHT = 50
        self.MAIN_SQUARE_WIDTH = self.MAIN_WINDOW_WIDTH - 20
        self.MAIN_SQUARE_HEIGHT = self.MAIN_WINDOW_HEIGHT - (self.ANSWER_SQUARE_HEIGHT
                                                             * self.AVAILABLE_ANSWERS) - 20 - (self.AVAILABLE_ANSWERS * 10)

        self.main_window = pygame.display.set_mode((self.MAIN_WINDOW_WIDTH, self.MAIN_WINDOW_HEIGHT))
        background_colour = (135, 135, 135)

        self.main_window.fill(background_colour)
        pygame.display.set_caption('Learn a new language')
        pygame.display.flip()

        self.new_question = True
        self.answered = False
        self.wrong_answers = 0
        self.correct_answers = 0
        self.selected_answers = []

        while True:

            # exit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # main functions
            if self.new_question is True:
                question, correct_answer, all_answers = self.generate_questions()
                self.new_question = False

            # draw question square
            pygame.draw.rect(self.main_window, Color('white'), (10, 10, self.MAIN_SQUARE_WIDTH, self.MAIN_SQUARE_HEIGHT))

            # write question
            self.main_window.blit(self.question_font.render('Which character is this?', True, Color('Black')), (50, 50))
            self.main_window.blit(self.question_font_text.render(question, True, Color('Black')), (300, 200))
            self.main_window.blit(self.question_font.render('C: %i | W: %i' % (self.correct_answers, self.wrong_answers),
                                                            True, Color('Black')), (500, 10))


            for answer in range(4):
                starting_height = self.MAIN_SQUARE_HEIGHT + (answer * self.ANSWER_SQUARE_HEIGHT) + (answer * 10) + 20

                if answer in self.selected_answers:
                    result = self.button(correct=correct_answer, text=all_answers[answer],
                                         top=starting_height, width=self.MAIN_SQUARE_WIDTH, height=self.ANSWER_SQUARE_HEIGHT,
                                         answered=True)

                else:
                    result = self.button(correct=correct_answer, text=all_answers[answer],
                                         top=starting_height, width=self.MAIN_SQUARE_WIDTH, height=self.ANSWER_SQUARE_HEIGHT)

                if result is True:
                    self.correct_answers += 1
                    self.selected_answers.append(answer)
                elif result is False:
                    self.wrong_answers += 1
                    self.selected_answers.append(answer)
                else:
                    pass

            # new question button
            get_new_question = pygame.draw.rect(self.main_window, Color('Yellow'), (self.MAIN_WINDOW_WIDTH - 110, 10, 100, 50))
            if get_new_question.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.new_question = True
                    self.selected_answers = []
                    time.sleep(0.3)

            self.main_window.blit(self.question_font.render('Next...', True, Color('Black')), (self.MAIN_WINDOW_WIDTH - 105, 15))
            # update event
            pygame.display.flip()

    def generate_questions(self):

        language = Japanese()
        question, correct_answer, all_answers = language.question_hiragana(4)
        return question, correct_answer, all_answers

    def button(self,correct='', text='Hello World', color='white', highlight='orange', left=10, top=10, width=100, height=100, answered=False):

        # draw rectangle for each answer
        answer = pygame.draw.rect(self.main_window, Color(color), (left, top, width, height))
        self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))

        # highlight mouseover rectangle
        if answer.collidepoint(pygame.mouse.get_pos()):
            answer = pygame.draw.rect(self.main_window, Color(highlight), (left, top, width, height))
            self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))

            if pygame.mouse.get_pressed()[0] == 1:
                if correct == text:
                    answer = pygame.draw.rect(self.main_window, Color('green'), (left, top, width, height))
                    self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))
                    time.sleep(0.2)
                    return True
                else:
                    answer = pygame.draw.rect(self.main_window, Color('red'), (left, top, width, height))
                    self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))
                    time.sleep(0.2)
                    return False

        if answered == True:
            if correct == text:
                answer = pygame.draw.rect(self.main_window, Color('green'), (left, top, width, height))
                self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))
            else:
                answer = pygame.draw.rect(self.main_window, Color('red'), (left, top, width, height))
                self.main_window.blit(self.answer_font.render(text, True, Color('Black')), (left + 50, top))

start = MainWindow()
