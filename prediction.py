import pandas as pd
import pickle


class Predictions:

    def __init__(self, age, internships, cgpa, stream, historyofbacklogs):
        self.age = age
        self.internships = internships
        self.cgpa = cgpa
        self.stream = stream
        self.historyofbacklogs = historyofbacklogs

    def predict(self):
        pkl_in = open("student_placement_prediction.pkl", 'rb')
        reg = pickle.load(pkl_in)
        categ = ['Student will not be placed', 'Student will be placed']
        custom_data = [[self.age, self.stream, self.internships, self.cgpa, self.historyofbacklogs]]
        prediction = reg.predict(pd.DataFrame(custom_data))
        predictions_custom = prediction[0]
        result = categ[int(predictions_custom)]
        return result
