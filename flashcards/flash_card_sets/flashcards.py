class FlashCards:
   def __init__(self, questions_dict):
       self.questions = questions_dict.keys()
       self.answers = questions_dict.values()