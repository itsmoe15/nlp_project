import spacy
from pypdf  import PdfReader
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
    
    def predict_from_pdf(self, pdf_path):
        #this will return the same as predict
        #note: it takes the path of the pdf NOT the pdf itself :/
        #save the pdf to disk then call the method on its location

        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        # print(text)
        return self.predict(text)

