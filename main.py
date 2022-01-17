#!/usr/bin/env python
#Boa:App:BoaApp
import wx, os, shutil
os.chdir("E:\\PHD-SUMUP\\EPIC+SUFI2")
import modelGUIWBF
modules ={ u'modelGUIWBF': [1,'Main frame of Application', u'modelGUIWBF.py'], u'windowsRun': [0, '', u'windowsRun.py']}
class BoaApp(wx.App):
    def OnInit(self):
        self.main = modelGUIWBF.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
        
def main():
    application = BoaApp(0)
    application.MainLoop()
if __name__ == '__main__':
    main()     