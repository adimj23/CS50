import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        self.positive = set()
        self.negative = set()
        
        pos_words=open("positive-words.txt", "r")
        for line in pos_words:
            if not line.startswith(";") or not line.startswith(" ") :
                self.positive.add(line.rstrip("\n"))
        neg_words=open("negative-words.txt", "r")      
        for line in neg_words:
            if not line.startswith(";") or not line.startswith(" "):
                self.negative.add(line.rstrip("\n"))

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens=tokenizer.tokenize(text)
        
        plus_minus=0
        for text1 in tokens:
            if text1.lower() in self.positive:
                plus_minus=plus_minus+1
        
            elif text1.lower() in self.negative:
                plus_minus=plus_minus-1
                
                
        return plus_minus