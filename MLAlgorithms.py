import pyjd # this is dummy in pyjs
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Image import Image
from pyjamas.ui.Label import Label
from pyjamas.ui import HasAlignment
from pyjamas.ui.Button import Button
from pyjamas.ui.CheckBox import CheckBox
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.HTML import HTML
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.FlowPanel import FlowPanel
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.DisclosurePanel import DisclosurePanel
from pyjamas import DOM, Window
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.PasswordTextBox import PasswordTextBox
import pyjd # this is dummy in pyjs

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Hyperlink import Hyperlink
from AlgorithmList import AlgorithmList
from pyjamas import History
import kMeans
import Info
from Logger import Logger
from pyjamas import log
from MLAlgorithmService import MLAlgorithmService
from MLAlgorithmService import MLAlgorithmJSONProxy

class MLAlgorithms:
    def onHistoryChanged(self, token):
        log.writebr("onHistoryChanged: %s" % token)
        info = self.Algorithm_list.find(token)
        if info is not None:
            self.show(info, False)
        else:
            self.showInfo()

    def onModuleLoad(self):
        self.curInfo=''
        self.curAlgorithm=None
        self.description=HTML()
        self.Algorithm_list=AlgorithmList()
        self.panel=DockPanel()
        
        self.loadAlgorithms()
        self.AlgorithmContainer = DockPanel()
        self.AlgorithmContainer.setStyleName("ks-Algorithm")

        vp=VerticalPanel()
        vp.setWidth("100%")
        vp.add(self.description)
        vp.add(self.AlgorithmContainer)

        self.description.setStyleName("ks-Info")

        self.panel.add(self.Algorithm_list, DockPanel.WEST)
        self.panel.add(vp, DockPanel.CENTER)

        self.panel.setCellVerticalAlignment(self.Algorithm_list, HasAlignment.ALIGN_TOP)
        self.panel.setCellWidth(vp, "100%")

        History.addHistoryListener(self)
        RootPanel().add(self.panel)
        RootPanel().add(Logger())

        #Show the initial screen.
        initToken = History.getToken()
        if len(initToken):
            self.onHistoryChanged(initToken)
        else:
            self.showInfo()

    def show(self, info, affectHistory):
        if info == self.curInfo: return
        self.curInfo = info

        log.writebr("showing " + info.getName())
        if self.curAlgorithm is not None:
            log.writebr("removing " + str(self.curAlgorithm))
            self.curAlgorithm.onHide()
            self.AlgorithmContainer.remove(self.curAlgorithm)

        self.curAlgorithm = info.getInstance()
        self.Algorithm_list.setAlgorithmSelection(info.getName())
        self.description.setHTML(info.getDescription())

        if (affectHistory):
            History.newItem(info.getName())

        self.AlgorithmContainer.add(self.curAlgorithm, DockPanel.CENTER)
        self.AlgorithmContainer.setCellWidth(self.curAlgorithm, "100%")
        self.AlgorithmContainer.setCellHeight(self.curAlgorithm, "100%")
        self.AlgorithmContainer.setCellVerticalAlignment(self.curAlgorithm, HasAlignment.ALIGN_TOP)
        self.curAlgorithm.onShow()
        
    def loadAlgorithms(self):
        self.Algorithm_list.addAlgorithm(Info.init())
        self.Algorithm_list.addAlgorithm(kMeans.init())

    def showInfo(self):
        self.show(self.Algorithm_list.find("Info"), False)


if __name__ == '__main__':
    pyjd.setup("MLAlgorithms.html")
    app = MLAlgorithms()
    app.onModuleLoad()
    pyjd.run()
