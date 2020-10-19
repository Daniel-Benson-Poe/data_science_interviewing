from flash_card_sets.flashcards import FlashCards

class DataEngineering(FlashCards):

    def __init__(self, questions_dict=None):
        self.questions_dict = self.answer_key()
        self.questions = self.questions_dict.keys()
        self.answers = self.questions_dict.values()

    def answer_key(self):
        question_answer_key = {
        "Test1": "Answer1",
        "Test2": "Answer2",
        "Test3": "Answer3",
        "Test4": "Answer4"
        }

        return question_answer_key
