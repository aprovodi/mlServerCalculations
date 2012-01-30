from Algorithm import Algorithm, AlgorithmInfo
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Image import Image
from pyjamas.ui.Button import Button
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.HTML import HTML
from pyjamas import Window
import pyjamas.gmaps.Utils
from pyjamas import log
from FileOpenDlg import FileOpenDlg
from MLAlgorithmService import MLAlgorithmService
from MLAlgorithmService import MLAlgorithmJSONProxy

class kMeans(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
	self.MLAlgorithmService = MLAlgorithmService(self)
        self.image=Image(self.baseURL() + "services/kMeansPictures/lenna.png",Width="320px", Height="360px")
        self.resultImage=Image("",Width="320px", Height="360px")
        self.loadingImage = Image(self.baseURL() + "images/blanksearching.gif")
        self.calculateButton = Button("RUN", self.onButtonClick)
        self.log = Button("SHOW LOG", self.openLogFile)
        self.log.setEnabled(False)

        self.image.addLoadListener(self)
        
        topPanel = DockPanel()
        topPanel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
        topPanel.add(self.calculateButton, DockPanel.WEST)
        topPanel.add(self.loadingImage, DockPanel.CENTER)
        topPanel.add(self.log, DockPanel.EAST)
        
        panel = DockPanel()
        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
        #panel.add(HTML("<h2>Image compression</h2>", True))
        panel.add(topPanel, DockPanel.NORTH)
        panel.add(self.image, DockPanel.WEST)
        panel.add(self.resultImage, DockPanel.EAST)
        
        panel.setWidth("100%")
        self.initWidget(panel)
        self.image.setStyleName("ks-images-Image")
        self.calculateButton.setStyleName("ks-images-Button")
        
        self.loadImage("picturem.png")

    def onButtonClick(self, sender):
        Window.alert("Starting image compression...")
        self.MLAlgorithmService.callMethod("lenna.png")


    def onError(self, sender):
        pass

    def onLoad(self, sender=None):
        self.loadingImage.setUrl(self.baseURL() + "images/blanksearching.gif")

    def loadImage(self, picture):
        self.loadingImage.setUrl(self.baseURL() + "images/searching.gif")
        self.image.setUrl(self.baseURL() + "services/kMeansPictures/lenna.png")
        self.resultImage.setUrl(self.baseURL() + "services/kMeansPictures/lenna.png")
        self.resultImage.setUrl(self.baseURL() + "services/kMeansPictures/" + picture)

    def onImageClicked(self):
        Window.alert("picture!")

    def openLogFile(self, sender):
###TODO: make logging output
        fileLocation = self.baseURL() + "services/contactjson.txt"
        dlg = FileOpenDlg(fileLocation=fileLocation)
        dlg.show()

    def showStatus(self, msg):
        Window.alert(msg)

def init():
    text="This page demonstrates K-Means clustering algorithm applied to the compression of an image."
    return AlgorithmInfo("kMeans", text, kMeans)
