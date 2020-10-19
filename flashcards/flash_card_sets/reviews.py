from flash_card_sets.flashcards import FlashCards

class Reviews(FlashCards):

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

{
    "What is the difference between supervised and unsupervised machine learning?" : "supervised machine learning requires labeled data for training, unsupervised machine learning does not",
    "What is 'bias' in the 'bias, variance tradeoff?" : "error caused by an oversimplified model",
    "What is 'variance' in the 'bias, variance tradeoff?" : "error caused by an overfitted model. model complexity that crosses over the bias/variance equilibrium",
    "What are some low bias machine learning algorithms?" : "decision trees, k-nn, svm",
    "what are some high bias machine learning algorithms?" : "linear regression, logistic regression",
    "What is the bias, variance tradoff?" : "while increasing the bias variance is decreased, while decreasing the variance bias is decreased. the goal is to find the lowest equilibrium.",
    "Explain the bias, variance tradeoff in k-nearest neighbors algorithm." : "low bias, high variance. can be changed by increasing k which will increase number of neighbors contributing to prediction which will increase the bias.",
    "Explain the bias, variance tradeoff in the support vector machine algorithm." : "low bias, high variance. can be changed by increasing C parameter that influences number of violations of margin allowed in the training data, which increases bias",
    "What is exploding gradients?" : "the accumulation of large error gradients leading to large increases in the weights during training of neural networks",
    "What affect does exploding gradients have?" : "neural network model becomes unstable and unable to learn from the training data",
    "What is a gradient?" : "calculated direction and magnitude in training of a neural network used to update network weights in the right direction and value",
    "What is a confusion matrix?" : "table containing 4 outputs including true positives, false positives, true negatives, and false negatives based on binary classification",
    "What are some measures that can be derived from a confusion matrix?" : "error-rate (FP+FN)/(P+N), accuracy (TP+TN)/(P+N), specificity(TN/N), sensitivity(TP/P), precision(TP)/(TP+FP), and recall",
    "What is a dataset used for performance evaluation? What should it include?" : "test dataset, should include correct labels and predicted labels",
    "Explain how a ROC curve works." : "graphically represents difference between true positive rates and false positive rates often used for determining tradeoff between sensitivity and false positive rate",
    "What is selection bias?" : "the sample obtained for analysis does not represent the intended population",
    "Explain SVM machine learning algorithm in detail." : "support vector machine is a supervised machine learning algorithm used for both regression and classification. given an n-feature training dataset it plots it in n-dimensional space with each coordinate value representing the value of a feature. seperates out different classes through hyper planes based on kernel function.",
    "What are the 4 types of kernels in SVM?" : "linear kernel, polynomial kernel, radial basis kernel, sigmoid kernel",
    "Explain decision tree algorithm in detail." : "Supervised machine learning model used for regression and classification and can handle both categorical and numerical data. breaks down data into smaller and smaller subsets while at the same time building an associated decision tree. this results in a decision true containing leaf nodes and decision nodes.",
    "What is entropy in decision tree algorithms?" : "used to check homogeneity of a sample. Decision trees are built top-down and involve partitioning data into homogenous subsets.",
    "What is information gain in decision tree algorithms?" : "based on decrease in entropy after dataset is split on an attribute. The main goal of a decision tree is to find attributes that return the highest information gain.",
    "What is pruning in decision trees?" : "removing subnodes ",
    "What is ensemble learning?" : "combining diverse set of individual models together to improvise on the stability and predictive power of the model. Two of the more popular ensemble models are bagging and boosting.",
    "What is the ensemble learning method 'bagging'?" : "implements similar models on small populations then takes the mean of all the predictions. helps reduce variance error",
    "What is the ensemble learning method 'boosting'?" : "adjusts the weight of an observation iteratively based on the last classification. incorrect classification increases the weight, and vice versa. helps decrease bias error. prone to overfitting.",
    "What is random forest?" : "ensemble learning method used for regression and classification tasks. made up of a group of decision trees, where each tree gives a classification and the forest choses which classification has the most 'votes' or in the case of regression it takes the average of the outputs",
    "What cross-validation technique would you use on a time series dataset?" : "techniques like forward chaining should be used to deal with the inherent chronological order. This allows you to build a model based on past data then look at forward facing data.",
    "What is logistic regression?" : "predicts the binary outcome from linear combination of predictor variables. Examples: predicting which political leader will win an election.",
    "What is normal distribution?" : "a bell shaped curve on a graph, formed based on the idea that the data is distributed in a way that lacks bias to the left and right of the dense middle.",
    "What is a box cox transformation?" : "transforms non normal dependant variables into normal shape, allowing you to run a broader number of tests - many statistical tests require normality in the data.",
    "How do you define the number of clusters in a K-Means clustering algorithm?" : "'K' defines the number of clusters. Sum of squares is generally used to explain homogeneity within a cluster. Using this you can create an elbow curve that plots the SS achieved compared to the number of clusters. You can determine the best suited number of clusters based on what number of clusters the decrement of SS starts to significantly slow down.",
    "What is deep learning?" : "Machine learning method inspired by the function and structure of the brain. An extention of neural networks. Considers a very large number of hidden layers for better understanding of input output relationships.",
    "What are recurrent neural networks(RNNs)?" : "Type of artificial neural network designed to recognize pattern from a sequence of data. Like feedforward nets, channels information through node-based mathematical operations, but instead of feeding the information straight through, RNNs cycle the information through loops: RNNs have two sources of input, the present and recent past, the combination of which determines how to deal with new data. Generated error bacckpropagate and are used to adjust the weights",
    "What is machine learning?" : "Field of computer science that gives computers the ability to learn without being explicitly programmed.",
    "What are the categories of machine learning?" : "supervised machine learning, unsupervised machine learning, reinforcement learning",
    "What is reinforcement learning?" : "learning what to do and how to map situations to actions. maximize the numerical reward signal. learner must discover which action will yield the maximum reward.",
    "What is regularization?" : "Process of adding a tuning partameter to a model to induce smoothness to prevent overfitting.",
    "What is TF/IDF vectorization?" : "term frequency-inverse document frequency. numerical statistic indeded to reflect importance of a word to a document in a collection or corpus. often used as weighting factor in information retrieval and text mining. increases proportionally to the number of times a word appears in the document, but offset by frequency of the word in the corpus to help adjust for the fact that some words appear more frequently in general.",
    "What are Recommender Systems?" : "information filtering systems meant to predict preferences or ratings a user would give a product. Widely used in movies, news, research articles, products, social tags, etc.",
    "What is the difference between Regression and classification ML techniques?" : "Both are supervised machine learning algorithms. Classification problems label data using discrete values ('A', 'B' etc) while regression problems label data using continuous values (1.23, 1.333, etc)",
    "What is p-value?" : "helps determine the strength of your results in a hypothesis test. Low p-value (<= 0.05) indicates strength against the null hypothesis allowing us to reject it. High p-value (>= 0.05) indicates strength for null hypothesis allowing us to accept the null hypothesis.",
    "What is 'naive' in naive bayes?" : "Bayes theorem describes the probability of an event based on prior knowledge of the conditions that might be related to the event. It is 'naive' because it makes assumptions that may or may not turn out to be correct.",
}