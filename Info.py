from Algorithm import Algorithm, AlgorithmInfo
from pyjamas.ui.HTML import HTML

class Info(Algorithm):
    def __init__(self):

        Algorithm.__init__(self)

        text="<div class='infoProse'>This is the Machine Learning Algorithms page.  "
        text+="It demonstrates ... ."
        text+="<p>This sample also demonstrates ta-ta-ta: </p></div>"
        self.initWidget(HTML(text, True))

    def onShow(self):
        pass


def init():
    return AlgorithmInfo("Info", "Introduction to Machine Learning Algorithms.", Info)
