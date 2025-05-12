import spacy

class Classifier():
    def __init__(self):
        self.nlp = spacy.load("Model")
    
    def predict(self, text):
        # this will return 2 things
        # first being return is a string with the predected class
        # second is a dictionary made of class_name -> confidence_score 

        self.doc = self.nlp(text)
        self.predicted_category = max(self.doc.cats, key=self.doc.cats.get)
        return self.predicted_category, self.doc.cats
    
    def predict_from_link(self):
        pass
    
    def predict_from_pdf(self):
        pass
       
