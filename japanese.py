import numpy as np
from random import shuffle

class Japanese:
    def question_hiragana(self, number_answers):

        hiragana = [
					# a
					('あ', 'a'),
                    ('か', 'ka'),
                    ('が', 'ga'),
					('さ', 'sa'),
					('ざ', 'za'),
					('た', 'ta'),
					('だ', 'da'),
					('な', 'na'),
					('は', 'ha'),
					('ば', 'ba'),
					('ぱ', 'pa'),
					('ま', 'ma'),
					('や', 'ya'),
					('ら', 'ra'),
					('わ', 'wa'),
					('ん', 'n'),
					# i
					('い', 'i'),
                    ('き', 'ki'),
                    ('ぎ', 'gi'),
					('し', 'shi'),
					('じ', 'gi'),
					('ち', 'tchi'),
					('ぢ', 'gi'),
					('に', 'ni'),
					('ひ', 'hi'),
					('び', 'bi'),
					('ぴ', 'pi'),
					('み', 'mi'),
					('り', 'ri'),
					('ゐ', 'wi (no longer used)'),
					# u
					('う', 'u'),
                    ('く', 'ku'),
                    ('ぐ', 'gu'),
					('す', 'su'),
					('ず', 'zu'),
					('つ', 'tsu'),
					('づ', 'dzu'),
					('ぬ', 'nu'),
					('ふ', 'fu'),
					('ぶ', 'bu'),
					('ぷ', 'pu'),
					('む', 'mu'),
					('ゆ', 'yu'),
					('る', 'ru'),
					# e
					('え', 'e'),
                    ('け', 'ke'),
                    ('げ', 'ge'),
					('せ', 'se'),
					('ぜ', 'ze'),
					('て', 'te'),
					('で', 'de'),
					('ね', 'ne'),
					('へ', 'he'),
					('べ', 'be'),
					('ぺ', 'pe'),
					('め', 'me'),
					('れ', 're'),
					('ゑ', 'we (no longer used)'),
					# o
					('お', 'o'),
                    ('こ', 'ko'),
                    ('ご', 'go'),
					('そ', 'so'),
					('ぞ', 'zo'),
					('と', 'to'),
					('ど', 'do'),
					('の', 'no'),
					('ほ', 'ho'),
					('ぼ', 'bo'),
					('ぽ', 'po'),
					('も', 'mo'),
					('よ', 'yo'),
					('ろ', 'ro'),
					('を', 'wo'),
        ]

        random_question = np.random.randint(len(hiragana))
        question = hiragana[random_question][0]
        correct_answer = hiragana[random_question][1]

        answers = [correct_answer]

        # wrong answers generator
        for number_answer in range(number_answers - 1):
            random_question = np.random.randint(len(hiragana))
            answers.append(hiragana[random_question][1])

        shuffle(answers)

        return question, correct_answer, answers

    def question_katakana(self, number_answers):

        katakana = [('ka', 'ta'),
                    ('ka', 'na')]

        random_question = np.random.randint(len(katakana))
        question = katakana[random_question][0]
        correct_answer = katakana[random_question][1]

        answers = [correct_answer]

        # wrong answers generator
        for number_answer in range(number_answers - 1):
            random_question = np.random.randint(len(katakana))
            answers.append(katakana[random_question][1])

        shuffle(answers)

        return question, correct_answer, answers
