import random
import sys
import time
from flash_card_sets.data_engineering import DataEngineering
from flash_card_sets.decision_trees import DecisionTrees
from flash_card_sets.hypothesis_testing import HypothesisTesting
from flash_card_sets.linear_algebra import LinearAlgebra
from flash_card_sets.linear_models import LinearModels
from flash_card_sets.machine_learning import MachineLearning
from flash_card_sets.reviews import Reviews
from flash_card_sets.training_a_neural_network import NeuralNetworks

# Create a dictionary where the key is the question and the value is the answer
# create a run method that picks a random question from the dictionary to ask the user
# program waits for user's response
# user must input their answer
# if the answer is close enough to the correct one, the question will be placed into the "known" array
# if the answer is not close enough to the correct one, the question will be placed into the "unknown" array
# User can call method that will repeat the questions in the "unkown" array or the "known" array and
# move those questions to their respective arrays based on whether they were answered correctly or not

class FlashCards:

    def __init__(self):
        self.main_key = {}
        self.unknown_key = {}
        self.known_key = {}
        self.current_question = None
        self.current_answer = None
        self.user_answer = None
        self.run_retrieve_unknown = "unknowns"
        self.run_retrieve_known = "knowns"
        self.run_retrieve_main = "main"
        self.running = False

    def retrieve_set(self):
        print("\nWhich flashcard set would you like to use?")
        print("Type in the number corresponding to the flashcard set you want:\n")
        print("1: Hypothesis Testing\n",
              "2: Linear Algebra\n",
              "3: Linear Models\n",
              "4: Decision Trees\n",
              "5: Data Engineering\n",
              "6: Machine Learning\n",
              "7: Training a Neural Network\n",
              "8: Review\n")
        flash_set = input()

        if flash_set == "1":
            hypoth_set = HypothesisTesting()
            self.main_key = hypoth_set.questions_dict

        elif flash_set == "2":
            lin_alg_set = LinearAlgebra()
            self.main_key = lin_alg_set.questions_dict

        elif flash_set == "3":
            lin_mod_set = LinearModels()
            self.main_key = lin_mod_set.questions_dict

        elif flash_set == "4":
            dec_tree_set = DecisionTrees()
            self.main_key = dec_tree_set.questions_dict

        elif flash_set == "5":
            data_eng_set = DataEngineering()
            self.main_key = data_eng_set.questions_dict

        elif flash_set == "6":
            mach_learn_set = MachineLearning()
            self.main_key = mach_learn_set.questions_dict

        elif flash_set == "7":
            neur_net_set = NeuralNetworks()
            self.main_key = neur_net_set.questions_dict

        elif flash_set == "8":
            rev_set = Reviews()
            self.main_key = rev_set.questions_dict

    def retrieve_question(self):
        self.current_question = random.choice(list(self.main_key.keys()))

    def retrieve_answer(self):
        self.current_answer = self.main_key.pop(self.current_question)

    def place_unknown_solution(self):
        self.unknown_key[self.current_question] = self.current_answer

    def place_known_solution(self):
        self.known_key[self.current_question] = self.current_answer

    def retrieve_unknown(self):
        self.current_question = random.choice(list(self.unknown_key.keys()))
        self.current_answer = self.unknown_key.pop(self.current_question)
    
    def retrieve_known(self):
        self.current_question = random.choice(list(self.known_key.keys()))
        self.current_answer = self.known_key.pop(self.current_question)

    def gather_user_input(self):
        self.user_answer = input()

    def pull_from_requested_list(self):
        if self.user_answer == 'q':
                self.running = False
                exit()

        elif self.user_answer.lower() == self.run_retrieve_known and len(self.known_key) > 0:
            self.retrieve_known()

        elif self.user_answer.lower() == self.run_retrieve_unknown and len(self.unknown_key) > 0:
            self.retrieve_unknown()

        elif self.user_answer.lower() == self.run_retrieve_main and len(self.main_key) > 0:
            self.retrieve_question()
            self.retrieve_answer()
            
        else:
            print("I'm sorry, that wasn't a valid list. Either the list you chose is empty or you chose a list that doesn't exist.")
            print("Please try selecting again.")
            self.gather_user_input()
            self.pull_from_requested_list()

    def ask_user_question(self):
        print("The question reads: ")
        print(self.current_question)
        time.sleep(5)

    def show_solution(self):
        print("The given solution is: ")
        print(self.current_answer)

    def check_if_user_understood_solution(self):
        if self.user_answer.lower() == "yes":
            print("Congratulations, you answered correctly!")
            self.place_known_solution()
            print("The question and its solution have been placed in the 'known' list.")
        else:
            print("I'm sorry, you couldn't figure it out. We will place it in your known list to try again later.")
            self.place_unknown_solution()
            print("The question and its solution have been placed in the 'unknown' list.")

    def run(self):
        self.running = True

        print("Welcome to your flashcard program.")
        print("You will be asked a random question from a subset of questions.")
        print("You will be given 10 seconds to think of an answer before being shown the program's built-in answer.")
        print("You will then be asked if you answered correctly. Honesty will only benefit you more.")
        print("If your answer was incorrect, it will be placed in a list of unknown solutions.")
        print("If your answer was correct, it will be placed in a list of known solutions.")
        print("You will be asked which list you wish to retrieve a question from prior to starting.")

        self.retrieve_set()

        while self.running:
            print("Which list would you like to retrieve a question from?")
            print("Type 'unknowns' for the unknown list, 'knowns' for the known list, or 'main' from the main list. Type 'q' to quit the program.")
            self.gather_user_input()
            # print(random.choice(list(self.main_key.keys())))
            # print(self.user_answer)
            self.pull_from_requested_list()
            self.ask_user_question()
            self.show_solution()
            print("Were you able to guess the solution correctly? Type 'yes' for yes and 'no' for no.")
            self.gather_user_input()
            self.check_if_user_understood_solution()

        exit()

if __name__ == "__main__":
    flash_cards = FlashCards()
    flash_cards.run()