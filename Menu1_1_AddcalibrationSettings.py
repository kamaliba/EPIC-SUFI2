#Boa:Dialog:Dialog1
import wx, os, shutil
import subprocess, stat
import numpy as np
import platform

def create(parent):
    return Dialog1(parent)
[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, 
 wxID_DIALOG1STATICTEXT1,wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, 
 wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2,wxID_DIALOG1TEXTCTRL3,wxID_DIALOG1TEXTCTRL4] = [wx.NewId() for _init_ctrls in range(11)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent):       
        parent.AddWindow(self.staticText1, 0, border=0, flag=0) 
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0)            

                        
    def _init_coll_flexGridSizer2_Items(self, parent):
        # generated method, don't edit 
        parent.AddWindow(self.staticText4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4, 0, border=0, flag=0) 
        parent.AddWindow(self.button2, 0, border=0, flag=0) 
        parent.AddWindow(self.button1, 0, border=0, flag=0)   
        
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=10, rows=10, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=3, hgap=10, rows=10, vgap=0)
        
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)       
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,pos=wx.Point(120, 120),size=wx.Size(650, 80), style=wx.DEFAULT_DIALOG_STYLE, title=u'Calibration settings')
        self.SetClientSize(wx.Size(650, 80))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)   
#================related to flexGridSizer1                
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=u'Number of runs', parent=self,  size=wx.Size(100, 25), style=wx.ALIGN_LEFT)
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, parent=self, size=wx.Size(100, 25),style=0)
#======================================================related to flexGridSizer2 =============================================================================       
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=u'EPIC basefiles',  parent=self,  size=wx.Size(100, 25), style=wx.ALIGN_LEFT)
        self.staticText4.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, parent=self, size=wx.Size(450, 25),style=0) 
        self.staticText4.SetForegroundColour(wx.Colour(0, 0, 255))  
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Browse folder', parent=self, size=wx.Size(80, 25), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Dir, id=wxID_DIALOG1BUTTON2)        
                                                                                                                                                                                                                                           
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Create run files', parent=self,  size=wx.Size(100, 30), style=wx.ALIGN_LEFT)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOG1BUTTON1)
        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        fSetup = open('modelGUISetup.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 14:
                self.textCtrl4.SetValue(txtLine.strip(os.linesep))
            loopNum=loopNum+1  
        self.textCtrl1.SetValue(parent.textCtrl3_4.GetValue())

    def OnButton2Dir(self, event):
        ### Write the par_inf.sf2 and Create the parameters sample
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        parent = self.GetParent()    
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()    
        self.textCtrl4.SetValue(dlg.GetPath())
        dlg.Destroy() 

    def OnButton1Button(self, event):
        ### Write the par_inf.sf2 and Create the parameters sample
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        parent = self.GetParent()    
        if os.path.isdir(parent.textCtrl2.GetValue()+pathSep +"\\Simulation\\CalibrationRuns") == False:
            os.mkdir(parent.textCtrl2.GetValue()+pathSep +"\\Simulation\\CalibrationRuns")
            
        if os.path.isdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()) == True:
            shutil.rmtree(parent.textCtrl2.GetValue() +  "\\Simulation\\CalibrationRuns\\" +  parent.textCtrl1_1.GetValue())
        os.mkdir(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue())
        
        fList1 = open(parent.textCtrl2.GetValue()+  "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\inputList.txt", readCode)                
        for lin1 in fList1: 
            s1=lin1.split(',')[1]
            os.mkdir(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" +  parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\")
            loop=1
            while loop< (int(self.textCtrl1.GetValue())+1):
                e="RUN_" + str(loop)
                os.mkdir(parent.textCtrl2.GetValue() +  "\\Simulation\\CalibrationRuns\\" +  parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\" + e)
                src=self.textCtrl4.GetValue() 
                dst=parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" +   parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\" + e
                for item in os.listdir(src):
                    s = os.path.join(src, item)
                    d = os.path.join(dst, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, symlinks=False, ignore=None)
                    else:
                        shutil.copy2(s, d)
                loop+=1                       
        fList1.close()
        dlg = wx.MessageDialog(self, 'Run folders were created', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnDialog1Close(self, event):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        self.Destroy()

    def OnButton3Button(self, event):
        event.Skip()

