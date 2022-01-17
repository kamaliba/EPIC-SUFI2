#Boa:Dialog:Dialog1

import wx, os, shutil
import subprocess, stat
import numpy as np
import platform
import Menu1_0_addFunction
def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON0, wxID_DIALOG1BUTTON2, 
 wxID_DIALOG1STATICTEXT1,wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, 
 wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2,wxID_DIALOG1TEXTCTRL3,
 wxID_DIALOG1BUTTON1,wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3,
 ] = [wx.NewId() for _init_ctrls in range(12)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent):       
        parent.AddWindow(self.staticText1, 0, border=0, flag=0) 
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0) 
        parent.AddWindow(self.button1, 0, border=0, flag=0)
              
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2, 0, border=0, flag=0)   
        parent.AddWindow(self.button2, 0, border=0, flag=0)
             
        parent.AddWindow(self.staticText3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3, 0, border=0, flag=0)
        parent.AddWindow(self.button3, 0, border=0, flag=0)

                
    def _init_coll_flexGridSizer2_Items(self, parent):
        # generated method, don't edit 
        parent.AddWindow(self.button0, 0, border=0, flag=0)   
        
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=3, hgap=1, rows=6, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)       
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,  pos=wx.Point(50, 50), size=wx.Size(800, 130), style=wx.DEFAULT_DIALOG_STYLE, title=u'Physciographic data')
        self.SetClientSize(wx.Size(800, 130))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)  
#================related to flexGridSizer1                
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=u'Physiographic layer', parent=self,  size=wx.Size(120, 25), style=wx.ALIGN_LEFT)
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, parent=self, size=wx.Size(550, 25),style=0)
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Browse location', parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 25), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Dir, id=wxID_DIALOG1BUTTON1)
                
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=u'RF-harvested land', parent=self,  size=wx.Size(120, 25), style=wx.ALIGN_LEFT)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2,parent=self, size=wx.Size(550, 25),style=0, value='textCtrl2')        
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Browse file', parent=self, size=wx.Size(100, 25), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Dir, id=wxID_DIALOG1BUTTON2)
                
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=u'IR-harvested land',parent=self,  size=wx.Size(120, 25), style=wx.ALIGN_LEFT)
        self.staticText3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3, parent=self, size=wx.Size(550, 25),style=0) 
        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'Browse file', parent=self,  size=wx.Size(100, 25), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Dir, id=wxID_DIALOG1BUTTON3)          
#======================================================related to flexGridSizer2 =============================================================================                                                                                                                                                                                                                                                  
        self.button0 = wx.Button(id=wxID_DIALOG1BUTTON0, label=u'Create physiographic data', parent=self, size=wx.Size(400, 30), style=0)
        self.button0.Bind(wx.EVT_BUTTON, self.OnButton0Button, id=wxID_DIALOG1BUTTON0)
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
            if loopNum == 11:
                self.textCtrl1.SetValue(txtLine.strip(os.linesep))
            if loopNum == 12:
                self.textCtrl2.SetValue(txtLine.strip(os.linesep))
            if loopNum == 13:
                self.textCtrl3.SetValue(txtLine.strip(os.linesep))
            loopNum=loopNum+1
                
    def OnButton0Button(self, event):
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
               
        ### Location of raster data file
        cellSize = float(parent.textCtrl1_2.GetValue())
        sCrop = parent.comboBox1_2.GetValue()
        sSpatialDir = self.textCtrl1.GetValue() + pathSep        
        inputDir = parent.textCtrl2.GetValue() + "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()
        
        if os.path.isdir( "Simulation") == False:
            os.mkdir( "Simulation")
        if os.path.isdir( "Simulation\\Input") == False:
            os.mkdir( "Simulation\\Input")        
        
        if os.path.isdir(inputDir) == False:
            os.mkdir(inputDir)
        sAreaFile = "subareaAll.inf"
        fAreaFile = open(sAreaFile, readCode)
        rainfedarea_AD=self.textCtrl2.GetValue()
        Irrigatearea_AD=self.textCtrl3.GetValue()
        if parent.comboBox1_1.GetValue() == "Whole":            
            for area in fAreaFile:
                area = area.strip(os.linesep)
                if area:
                    area = area.split(';')
                    sAreaName = area[0][0:-1]
                    sAreaNumber = area[1]
                    Menu1_0_addFunction.writeInputData(parent.textCtrl1_1.GetValue(), sAreaNumber, sCrop, sSpatialDir,sAreaName,rainfedarea_AD,Irrigatearea_AD)
        else:
            for area in fAreaFile:
                area = area.strip(os.linesep)
                if area:
                    area = area.split(';')
                    sAreaName = area[0][0:-1]
                    sAreaNumber = area[1]
                    
                    if sAreaName == parent.comboBox1_1.GetValue():
                        Menu1_0_addFunction.writeInputData(parent.textCtrl1_1.GetValue(), sAreaNumber, sCrop, sSpatialDir,sAreaName,rainfedarea_AD,Irrigatearea_AD)
        fAreaFile.close()        
        ### remove the possible repeated input.txt information
        fList1 = open(inputDir + pathSep + "inputList.txt", readCode)
        listTemp = fList1.readlines()
        fList1.close()
        listData = sorted(list(set(listTemp)))
        fList2 = open(inputDir + pathSep + "inputList.txt", "wb")
        fList2.writelines(listData)
        fList2.close()  
        
      
        #dialogProgress.Destroy()
        dlg = wx.MessageDialog(self, 'All input data has been prepared!\n [Rnum, lon, lat, Dem, Slope, soil, climate, countrycode]', 'Input Write Process', \
        wx.OK | wx.ICON_INFORMATION)
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
        with open('modelGUISetup.inf','r') as file:
            data=file.readlines()   
        OTHERdata=data[0:10]         
        f = open('modelGUISetup.inf', 'w')
        for i in range(0, 10):
            f.write(OTHERdata[i])           
        f.write(self.textCtrl1.GetValue() + lineEnd)
        f.write(self.textCtrl2.GetValue() + lineEnd)
        f.write(self.textCtrl3.GetValue() + lineEnd) 
        f.write(data[13])            
        f.close()          
        
        self.Destroy()


    def OnButton3Button(self, event):
        event.Skip()

    def OnButton1Dir(self, event):
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
            print "You chose %s" % dlg.GetPath()
        self.textCtrl1.SetValue(dlg.GetPath())
        dlg.Destroy() 
        
        
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
        dlg = wx.FileDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()    
        self.textCtrl2.SetValue(dlg.GetPath())
        dlg.Destroy() 
        
    def OnButton3Dir(self, event):
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
        dlg = wx.FileDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()        
        self.textCtrl3.SetValue(dlg.GetPath())
        dlg.Destroy()                         