from pyjamas.ui.Composite import Composite
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Hyperlink import Hyperlink
from Logger import Logger

class AlgorithmList(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.vp_list=VerticalPanel()
        self.Algorithms=[]
        self.selectedAlgorithm=-1
        
        self.initWidget(self.vp_list)
        self.setStyleName("ks-List")

    def addAlgorithm(self, info):
        name = info.getName()
        link = Hyperlink(name, False, TargetHistoryToken=name)
        link.setStyleName("ks-AlgorithmItem")
        self.vp_list.add(link)
        self.Algorithms.append(info)

    def find(self, AlgorithmName):
        for info in self.Algorithms:
            if info.getName()==AlgorithmName:
                return info
        return None

    def setAlgorithmSelection(self, name):
        if self.selectedAlgorithm <> -1:
            self.vp_list.getWidget(self.selectedAlgorithm).removeStyleName("ks-AlgorithmItem-selected")

        for i in range(len(self.Algorithms)):
            info = self.Algorithms[i]
            if (info.getName()==name):
                self.selectedAlgorithm = i
                widget=self.vp_list.getWidget(self.selectedAlgorithm)
                widget.addStyleName("ks-AlgorithmItem-selected")
                return


