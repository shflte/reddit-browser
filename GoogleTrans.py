from googletrans import Translator

def translate(text, theSrc, theDest): 
    result = Translator().translate(text, src=theSrc, dest=theDest).text
    return result
