# -*- coding: utf-8 -*-
#Boa:Dialog:Dialog1

import wx.lib.buttons , os, platform,subprocess, stat 
import random, shutil 
import matplotlib.pyplot as plt
from pylab import *
import numpy  
#from numpy import matrix
def create(parent):
    return Dialog1(parent)
[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, wxID_DIALOG1BUTTON4, 

 wxID_DIALOG1STATICTEXT1,wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4,wxID_DIALOG1STATICTEXT5,wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7,wxID_DIALOG1STATICTEXT8,
 wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2,wxID_DIALOG1TEXTCTRL3,wxID_DIALOG1TEXTCTRL4,wxID_DIALOG1TEXTCTRL5,wxID_DIALOG1TEXTCTRL6,wxID_DIALOG1TEXTCTRL7,wxID_DIALOG1TEXTCTRL8,
 
 wxID_DIALOG1STATICTEXT2_1,wxID_DIALOG1STATICTEXT2_2,wxID_DIALOG1STATICTEXT2_3,wxID_DIALOG1STATICTEXT2_4, wxID_DIALOG1TEXTCTRL2_1,wxID_DIALOG1TEXTCTRL2_2,wxID_DIALOG1TEXTCTRL2_3,wxID_DIALOG1TEXTCTRL2_4,
 wxID_DIALOG1BUTTON2_1,wxID_DIALOG1BUTTON2_2, wxID_DIALOG1BUTTON2_3, wxID_DIALOG1BUTTON2_4, ] = [wx.NewId() for _init_ctrls in range(33)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent):       
        parent.AddWindow(self.staticText1, 0, border=0, flag=0) 
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0)       
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2, 0, border=0, flag=0)        
        parent.AddWindow(self.staticText3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4, 0, border=0, flag=0)
        parent.AddWindow(self.staticText5, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl5, 0, border=0, flag=0)
        parent.AddWindow(self.staticText6, 0, border=0, flag=0) 
        parent.AddWindow(self.textCtrl6, 0, border=0, flag=0)       
        parent.AddWindow(self.staticText7, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl7, 0, border=0, flag=0)        
        parent.AddWindow(self.staticText8, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl8, 0, border=0, flag=0)   
        
    def _init_coll_flexGridSizer2_Items(self, parent):
        # generated method, don't edit 
        parent.AddWindow(self.staticText2_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_1, 0, border=0, flag=0)
        parent.AddWindow(self.button2_1, 0, border=0, flag=0)  

        parent.AddWindow(self.staticText2_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_2, 0, border=0, flag=0)
        parent.AddWindow(self.button2_2, 0, border=0, flag=0)                 
                                                                        
        parent.AddWindow(self.staticText2_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_3, 0, border=0, flag=0)
        parent.AddWindow(self.button2_3, 0, border=0, flag=0)  

        parent.AddWindow(self.staticText2_4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_4, 0, border=0, flag=0)
        parent.AddWindow(self.button2_4, 0, border=0, flag=0)  
                                                      
    def _init_coll_flexGridSizer3_Items(self, parent):
        # generated method, don't edit 
        parent.AddWindow(self.button1, 0, border=0, flag=0)          
        parent.AddWindow(self.button2, 0, border=0, flag=0)       
        parent.AddWindow(self.button3, 0, border=0, flag=0)    
                                                                                                      
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)
                        
    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=4, hgap=1, rows=6, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=3, hgap=1, rows=6, vgap=0)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=3, hgap=2, rows=25, vgap=1)               
                                
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)       
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3) 
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,  pos=wx.Point(10, 10), size=wx.Size(800, 500), style=wx.DEFAULT_DIALOG_STYLE, title=u'Calibration_Settings')
        
        self.SetClientSize(wx.Size(800, 500))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)             
#================related to flexGridSizer1                
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=u'Number of iterations',  parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, parent=self, size=wx.Size(100, 21))
        
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=u'Number of parameters', parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, parent=self, size=wx.Size(100, 21))        
        
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=u'Name of iteration', parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3, parent=self, size=wx.Size(100, 21))   

        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=u'crop',  parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText4.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText4.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, parent=self, size=wx.Size(100, 21))  
        
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5, label=u'resolution',  parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText5.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText5.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL5, parent=self, size=wx.Size(100, 21))    
                     
        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6, label=u'Objective function',  parent=self,  size=wx.Size(150, 20), style=wx.ALIGN_LEFT)
        self.staticText6.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText6.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL6, parent=self, size=wx.Size(100, 21))
        
        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7, label=u'Threshold for objective function', parent=self,  size=wx.Size(250, 20), style=wx.ALIGN_LEFT)
        self.staticText7.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText7.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL7, parent=self, size=wx.Size(100, 21))        

        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8, label=u'Number of running-average years', parent=self,  size=wx.Size(250, 20), style=wx.ALIGN_LEFT)
        self.staticText8.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText8.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL8, parent=self, size=wx.Size(100, 21))       
#======================================================related to flexGridSizer2 =============================================================================                                                                                                                                                                                                                                                  
        self.staticText2_1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_1,label=u'Rainfed Area', parent=self, size=wx.Size(150, 20),style=wx.ALIGN_LEFT)
        self.staticText2_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2_1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2_1.SetAutoLayout(True)
        self.textCtrl2_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_1,parent=self, size=wx.Size(510, 21))
        self.button2_1 = wx.Button(id=wxID_DIALOG1BUTTON2_1, label=u'Browse',parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 20))
        self.button2_1.Bind(wx.EVT_BUTTON, self.OnButton2_1Dir, id=wxID_DIALOG1BUTTON2_1)

        self.staticText2_2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_2,label=u'Irrigated Area', parent=self, size=wx.Size(150, 20),style=wx.ALIGN_LEFT)
        self.staticText2_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2_2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2_2.SetAutoLayout(True)
        self.textCtrl2_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_2,parent=self, size=wx.Size(510, 21))
        self.button2_2 = wx.Button(id=wxID_DIALOG1BUTTON2_2, label=u'Browse',parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 20))
        self.button2_2.Bind(wx.EVT_BUTTON, self.OnButton2_2Dir, id=wxID_DIALOG1BUTTON2_2)
                                                                                                                                                                                                                                               
        self.staticText2_3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_3,label=u'observed yield location', parent=self, size=wx.Size(150, 20),style=wx.ALIGN_LEFT)
        self.staticText2_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2_3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2_3.SetAutoLayout(True)
        self.textCtrl2_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_3,parent=self, size=wx.Size(510, 21))
        self.button2_3 = wx.Button(id=wxID_DIALOG1BUTTON2_3, label=u'Browse',parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 20))
        self.button2_3.Bind(wx.EVT_BUTTON, self.OnButton2_3Dir, id=wxID_DIALOG1BUTTON2_3)
        
        self.staticText2_4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_4,label=u'observed yield location', parent=self, size=wx.Size(150, 20),style=wx.ALIGN_LEFT)
        self.staticText2_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2_4.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2_4.SetAutoLayout(True)
        self.textCtrl2_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_4,parent=self, size=wx.Size(510, 21))
        self.button2_4 = wx.Button(id=wxID_DIALOG1BUTTON2_4, label=u'Browse',parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 20))
        self.button2_4.Bind(wx.EVT_BUTTON, self.OnButton2_4Dir, id=wxID_DIALOG1BUTTON2_4)        
        #======================================================related to flexGridSizer 5=============================================================================                                                                                                                                                                                                                                                  
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Extract Simulated Yield', parent=self, size=wx.Size(200, 30))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOG1BUTTON1)                                                                                                                                                                                                                                                 
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Creat observed.txt in SUFI2.IN', parent=self,  size=wx.Size(200, 30))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button, id=wxID_DIALOG1BUTTON2)                
        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'Extract RAIN FED', parent=self,  size=wx.Size(200, 30))
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button, id=wxID_DIALOG1BUTTON3)  
                
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
        self.textCtrl1.SetValue( parent.textCtrl3_4.GetValue())
        self.textCtrl2.SetValue( parent.textCtrl3_5.GetValue())
        self.textCtrl3.SetValue( parent.textCtrl1_1.GetValue())
        self.textCtrl4.SetValue( parent.comboBox1_2.GetValue())
        self.textCtrl5.SetValue( parent.textCtrl1_2.GetValue())
        fSetup = open('OutputExtraction.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 1:
                self.textCtrl6.SetValue(txtLine.split(',')[0])
            if loopNum == 2:
                self.textCtrl7.SetValue(txtLine.split(',')[0])
            if loopNum == 3:
                self.textCtrl2_1.SetValue(txtLine.split(',')[0])
            if loopNum == 4:
                self.textCtrl2_2.SetValue(txtLine.split(',')[0])
            if loopNum == 5:
                self.textCtrl2_3.SetValue(txtLine.split(',')[0]) 
            if loopNum == 6:
                self.textCtrl2_4.SetValue(txtLine.split(',')[0])             
            loopNum=loopNum+1          
                   
    def OnButton2_2Dir(self, parent):
        ### Write the par_inf.sf2 and Create the parameters sample
        dlg = wx.FileDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()
        self.textCtrl2_2.SetValue(dlg.GetPath())
        dlg.Destroy()  

    def OnButton2_1Dir(self, parent):
        ### Write the par_inf.sf2 and Create the parameters sample
        dlg = wx.FileDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()
        self.textCtrl2_1.SetValue(dlg.GetPath())
        dlg.Destroy()  

    def OnButton2_3Dir(self, parent):
        ### Write the par_inf.sf2 and Create the parameters sample
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()
        self.textCtrl2_3.SetValue(dlg.GetPath())
        dlg.Destroy()  

    def OnButton2_4Dir(self, parent):
        ### Write the par_inf.sf2 and Create the parameters sample
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()
        self.textCtrl2_4.SetValue(dlg.GetPath())
        dlg.Destroy() 

    def OnButton1Button(self, event):       
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        parent = self.GetParent()
        ######================================
        cropName=self.textCtrl4.GetValue
        CurrentDir=parent.textCtrl2.GetValue()
        resolution=float(parent.textCtrl1_2.GetValue())
        
        irAreaFile = self.textCtrl2_1.GetValue()
        rfAreaFile = self.textCtrl2_2.GetValue()
        
        irAreaData = np.genfromtxt(irAreaFile, skip_header=6)
        rfAreaData = np.genfromtxt(rfAreaFile, skip_header=6)
        irAreaData[irAreaData<0]=0
        rfAreaData[rfAreaData<0]=0
        fIR = open(irAreaFile, readCode)
        nColIR = int(fIR.readline().strip(os.linesep).split()[1])
        nRowIR = int(fIR.readline().strip(os.linesep).split()[1])
        xCorIR = int(fIR.readline().strip(os.linesep).split()[1])
        yCorIR = int(fIR.readline().strip(os.linesep).split()[1])
        yUpCorIR = yCorIR + resolution*nRowIR
        fIR.close()
        fRF = open(rfAreaFile, readCode)
        nColRF = int(fRF.readline().strip(os.linesep).split()[1])
        nRowRF = int(fRF.readline().strip(os.linesep).split()[1])
        xCorRF = int(fRF.readline().strip(os.linesep).split()[1])
        yCorRF = int(fRF.readline().strip(os.linesep).split()[1])
        yUpCorRF = yCorRF + resolution*nRowRF
        fRF.close()
        ##=================================================================================================================================
        scenario=parent.textCtrl1_1.GetValue()
        fList1 = open(CurrentDir + "\\input\\" + scenario +  "\\inputList.txt", "r")
        start_yr=int(parent.textCtrl3_1.GetValue())
        end_yr=start_yr+ int(parent.textCtrl3_2.GetValue())-1
        skip_yr=int(parent.textCtrl3_3.GetValue())
        start_line=11+skip_yr
        year=range(start_yr,end_yr)
########################################################################################################
        fopt=open(parent.textCtrl2.GetValue() + "\\" + 'OperationSchedual_T2.inf','r')
        loop_Num=1
        for optlin in fopt:
            if loop_Num==16:
                Planting_system=optlin.split(',')[0]
                Opt_num=optlin.split(',')[1]
            loop_Num=loop_Num+1
        fopt.close()             
        if Planting_system == "RF-IR":        
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    print s11
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(self.textCtrl1.GetValue())   
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + s11 +"_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + s11 +"_country.txt",'w') 
                    for itr in range(1,itr_num+1):
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                        Fcountry.write(str(itr)+ '\n') 
                        Country_Yield=[]        
                        for lin2 in fin:                                              
                            lon=float(lin2.split()[1])
                            lat=float(lin2.split()[2])
                            
                            areaRF=float(lin2.split()[8])
                            indexLatIR = int(((yUpCorIR-lat)/resolution)-0.5)
                            indexLatRF = int(((yUpCorRF-lat)/resolution)-0.5)
                            indexLonIR = int(((lon-xCorIR)/resolution)-0.5)
                            indexLonRF = int(((lon-xCorRF)/resolution)-0.5)
                            areaIR = irAreaData[indexLatIR, indexLonIR]
                            areaRF = rfAreaData[indexLatRF, indexLonRF]                 
                            ## RainFed Yield 
                            if areaIR>0 or areaRF>0:
                                f_OUTPUT.write(format(lon,'8.2f')+ ',')
                                f_OUTPUT.write(format(lat,'8.2f')+ ',')
                                ## Rainfed Yield 
                                with open(parent.textCtrl2.GetValue()+ "\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
                                    data=file.readlines() 
                                yr=[]
                                YLD=[]
                                for i in range(11,len(data)):
                                    yr.append(data[i].split()[0])
                                    YLD.append(data[i].split()[3])
                                YLD_RF=[]
                                for y in range(start_yr+skip_yr,end_yr+1):
                                    YLD1=[]
                                    for i, j in enumerate(yr):
                                        if j == str(y):
                                            A=0
                                            for z1 in range(0,int(self.textCtrl8.GetValue())):
                                                A=A+float(YLD[i-z1])                                    
                                            YLD1.append(float(A)/int(self.textCtrl8.GetValue()))
                                    YLD_RF.append(max(YLD1)) 
                                ## Irrigation Yield 
                                with open(parent.textCtrl2.GetValue()+ "\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "IR" + ".ACY" ,'r') as file:
                                    data=file.readlines() 
                                yr=[]
                                YLD=[]
                                for i in range(11,len(data)):
                                    yr.append(data[i].split()[0])
                                    YLD.append(data[i].split()[3])
                                YLD_IR=[]
                                for y in range(start_yr+skip_yr,end_yr+1):
                                    YLD1=[]
                                    for i, j in enumerate(yr):
                                        if j == str(y):
                                            A=0
                                            for z1 in range(0,int(self.textCtrl8.GetValue())):
                                                A=A+float(YLD[i-z1])                                    
                                            YLD1.append(float(A)/int(self.textCtrl8.GetValue()))
                                    YLD_IR.append(max(YLD1))
                                areaTOT = areaRF + areaIR 
                                Grid_Yearly_Yield=[]
                                for i in range(0,len(YLD_IR)):
                                    A1=areaRF*YLD_RF[i]+areaIR*YLD_IR[i]
                                    A2=A1/areaTOT
                                    Grid_Yearly_Yield.append(format(A2,'8.2f'))
                                    f_OUTPUT.write(format(A2,'5.2f')+ ',')
                                f_OUTPUT.write( '\n')                           
                                Country_Yield.append (Grid_Yearly_Yield)                                 
                        for yr in range(0,len(YLD_IR)):
                            year=start_yr+yr+skip_yr
                            a=0
                            for gr in range(0,len(Country_Yield)):
                                a=a+float(Country_Yield[gr][yr])
                            averge=a/len(Country_Yield)
                            Fcountry.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
########################################################################################################### 
        elif Planting_system == "IR":
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(self.textCtrl1.GetValue())   
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + s11 +"_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + s11 +"_country.txt",'w')        
                    fin=open(CurrentDir + "\\input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                
                    for itr in range(1,itr_num+1):
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                        Fcountry.write(str(itr)+ '\n') 
                        Country_Yield=[]          
                        for lin2 in fin:                                              
                            lon=float(lin2.split()[1])
                            lat=float(lin2.split()[2])
                            areaIR=float(lin2.split()[8])          
                            if  areaIR>0:
                                f_OUTPUT.write(format(lon,'8.2f')+ ',')
                                f_OUTPUT.write(format(lat,'8.2f')+ ',')
                                with open(parent.textCtrl2.GetValue()+ "\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "IR" + ".ACY" ,'r') as file:
                                    data=file.readlines() 
                                yr=[]
                                YLD=[]
                                for i in range(11,len(data)):
                                    yr.append(data[i].split()[0])
                                    YLD.append(data[i].split()[3])

                                YLD_RF=[]
                                for y in range(start_yr+skip_yr,end_yr+1):
                                    YLD1=[]
                                    for i, j in enumerate(yr):
                                        if j == str(y):
                                            YLD1.append(float(YLD[i]))
                                    YLD_RF.append(max(YLD1)) 
                                areaTOT = areaIR 
                                Grid_Yearly_Yield=[]
                                for i in range(0,len(YLD_RF)):
                                    A1=areaIR*YLD_RF[i]
                                    A2=A1/areaTOT
                                    Grid_Yearly_Yield.append(format(A2,'8.2f'))
                                    f_OUTPUT.write(format(A2,'5.2f')+ ',')
                                f_OUTPUT.write( '\n')                           
                                Country_Yield.append (Grid_Yearly_Yield)  
                #####Averaging on country level                                 
                        for yr in range(0,len(YLD_RF)):
                            year=start_yr+yr+skip_yr
                            a=0
                            for gr in range(0,len(Country_Yield)):
                                a=a+float(Country_Yield[gr][yr])
                            averge=a/len(Country_Yield)
                            Fcountry.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
###########################################################################################################                                 
        elif Planting_system == "RF": 
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(self.textCtrl1.GetValue())   
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + s11 +"_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + s11 +"_country.txt",'w')        
                    for itr in range(1,itr_num+1):
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                        Fcountry.write(str(itr)+ '\n') 
                        Country_Yield=[] 
                        Tarea=[]         
                        for lin2 in fin:                                              
                            lon=float(lin2.split()[1])
                            lat=float(lin2.split()[2])
                            areaRF=float(lin2.split()[8])   
                            if  areaRF>0:
                                Tarea.append(areaRF)
                                f_OUTPUT.write(format(lon,'8.2f')+ ',')
                                f_OUTPUT.write(format(lat,'8.2f')+ ',')
                                with open(parent.textCtrl2.GetValue()+ "\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
                                    data=file.readlines() 
                                yr=[]
                                YLD=[]
                                for i in range(11,len(data)):
                                    yr.append(data[i].split()[0])
                                    YLD.append(data[i].split()[3])
                                YLD_RF=[]
                                for y in range(start_yr+skip_yr,end_yr+1):
                                    YLD1=[]
                                    for i, j in enumerate(yr):
                                        if j == str(y):
                                            YLD1.append(float(YLD[i]))
                                    YLD_RF.append(max(YLD1)) 
                                Grid_Yearly_Yield=[]
                                for i in range(0,len(YLD_RF)):
                                    Grid_Yearly_Yield.append(format(YLD_RF[i],'8.2f'))
                                    f_OUTPUT.write(format(YLD_RF[i],'5.2f')+ ',')
                                f_OUTPUT.write( '\n')                           
                                Country_Yield.append (Grid_Yearly_Yield)  
####################################################################################################Averaging on country level 
                        for yr in range(0+int(self.textCtrl8.GetValue())-1,len(YLD_RF)):
                            year=start_yr+yr+skip_yr
                            average=0
                            for run in range(0,int(self.textCtrl8.GetValue())):
                                a=0
                                for gr in range(0,len(Country_Yield)):
                                    a=a+(float(Country_Yield[gr][yr-run])*float(Tarea[gr]))
                                average=average+a/sum(Tarea)
                            averget=average/int(self.textCtrl8.GetValue())
                            Fcountry.write(str(year)+ "  " + format(averget,'8.2f')+ '\n')
        Fcountry.close()             
        f_OUTPUT.close()
        fin.close()
        fList1.close()  
######################################################################################################################################                                                        
        dlg = wx.MessageDialog(self, 'Outputs were extracted', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnButton2Button(self, event):       
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        parent = self.GetParent()
        fList1 = open(parent.textCtrl2.GetValue() + "\\input\\" + self.textCtrl3.GetValue() +  "\\inputList.txt", "r")
        start_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_3.GetValue())
        end_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_2.GetValue())-1
        number_point= end_yr-start_yr+1    
        for lin1 in fList1:
            fvar=open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "var_file_name.txt","w")
            fobs2=open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "observed.txt","w")
            fobs2.write("1  : number of observed variables\n")
            fobs2.write(self.textCtrl6.GetValue() + "   : Objective function time_step, 1=mult,2=sum,3=r2,4=chi2,5=NS,6=br2,7=Ssqr\n")
            fobs2.write(self.textCtrl7.GetValue() + "   : max or min value of objective function threshold where program stops\n")
            fobs2.write( " \n")
            fobs2.write( " \n")
            fobs2.write(lin1.split(',')[1] + "_country  : this is the name of variable to be included in the objective function\n")
            fvar.write(lin1.split(',')[1] + "_country.txt\n")
            fobs2.write("1     : weight of this variable in the objective function\n")
            fobs2.write("-1    : a signal can be divided into small and large values. This is the value of separation. This is not considered if -1\n")
            fobs2.write("-1    : a signal can be divided into small and large values. This is the value of separation. This is not considered if -1\n")
            fobs2.write("1     : if separation of signal is considered, this is weight of the smaller values in the objective function\n")
            fobs2.write("1     : if separation of signal is considered, this is weight of the larger values in the objective function\n")
            fobs2.write("0.05   : max or min value of objective function threshold where program stops\n")
            fobs2.write(str(number_point-int(self.textCtrl8.GetValue())+1) +"   : number of data points for this variable as it follows below. First column is a sequential number from 1 with missing values missing\n")
            fobs2.write("     : as shown, second column is variable name and date, third column is variable value. Same format is repeated for all other variables\n")  
            fobs2.write( " \n")
            fobs2.write( " \n")  
            s1=len(lin1.split(',')[0])
            s2=(lin1.split(',')[0])[0:s1-10]
            with open(self.textCtrl2_3.GetValue() +"\\yield_"+self.textCtrl4.GetValue()+ "_"+ s2 + ".txt", "r") as file:
                data=file.readlines() 
            yr=[]
            YLD=[]
            for i in range(0,len(data)):
                yr.append(data[i].split()[0])
                YLD.append(data[i].split()[1]) 
            end_yr= int(parent.textCtrl3_1.GetValue())+int(parent.textCtrl3_2.GetValue())
            for y in range(start_yr+int(self.textCtrl8.GetValue())-1,end_yr):
                for i, j in enumerate(yr):
                    if j == str(y):
                        A=0
                        for z1 in range(0,int(self.textCtrl8.GetValue())):
                            A=A+float(YLD[i-z1])                                    
                        fobs2.write(str(yr[i])+ "   1   " + str(float(A)/int(self.textCtrl8.GetValue())) + "\n")
                         
            fobs2.write( " \n")
            fobs2.write( " \n")

##############################################################################adding Grid-based data
            YLD=[]
            with open(self.textCtrl2_4.GetValue() +"\\yield_"+self.textCtrl4.GetValue()+ "_"+ s2 + ".txt", "r") as file:
                data=file.readlines() 
            yr=data[0].split()[2:len(data[0])]
            for v in range(1,len(data)):
                YLD=[]
                YLD=data[v].split()[2:len(data[v])]
                number_point=0
                for i in range(0,len(YLD)):
                    if float(YLD[i])!=-1:
                        number_point=number_point+1
                if number_point>0:
                    fobs2.write("Grid_"+ str(v) +": this is the name of variable to be included in the objective function\n")
                    fvar.write("Grid_"+ str(v) + ".txt\n")
                    fobs2.write("1     : weight of this variable in the objective function\n")
                    fobs2.write("-1    : a signal can be divided into small and large values. This is the value of separation. This is not considered if -1\n")
                    fobs2.write("-1    : a signal can be divided into small and large values. This is the value of separation. This is not considered if -1\n")
                    fobs2.write("1     : if separation of signal is considered, this is weight of the smaller values in the objective function\n")
                    fobs2.write("1     : if separation of signal is considered, this is weight of the larger values in the objective function\n")
                    fobs2.write("0.05   : max or min value of objective function threshold where program stops\n")
                    fobs2.write(str(number_point)+"   : number of data points for this variable as it follows below. First column is a sequential number from 1 with missing values missing\n")
                    fobs2.write("     : as shown, second column is variable name and date, third column is variable value. Same format is repeated for all other variables\n")  
                    fobs2.write( " \n")
                    fobs2.write( " \n")              
                for y in range(start_yr,end_yr):
                    for i, j in enumerate(yr):
                        if j == str(y):
                            if float(YLD[i])!= -1:
                                fobs2.write(str(y)+ "   1   " + YLD[i] + "\n")   
                if number_point>0:
                    fobs2.write( " \n")
            fobs2.write( " \n")            
            fobs2.close()                                  
            fvar.close()
###############################################################
            with open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "observed.txt", "r") as file:
                data=file.readlines() 
            with open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "var_file_name.txt", "r") as file:
                datavar=file.readlines()
            indv=len( datavar)
            fobs2=open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "observed.txt","w")
            fobs2.write(str(indv)+"  : number of observed variables\n")
            for i in range(1, len(data)):
                fobs2.write(data[i])

        dlg = wx.MessageDialog(self, 'observed.txt were build-up', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()        
    
    def OnButton3Button(self, event):       
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        parent = self.GetParent()
        fList1 = open(parent.textCtrl2.GetValue() + "\\Input\\" + self.textCtrl3.GetValue() +  "\\inputList.txt", "r")
        start_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_3.GetValue())
        end_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_2.GetValue())-1
        for lin1 in fList1:
            lin11=lin1.split(',')[0]
            s1=len(lin1.split(',')[0])
            s2=(lin1.split(',')[0])[0:s1-10]
            s11=lin1.split(',')[1]
            YLDD=[]
            with open(self.textCtrl2_4.GetValue() +"\\yield_"+self.textCtrl4.GetValue()+ "_"+ s2 + ".txt", "r") as file:
                data=file.readlines()               
            yr=data[0].split()[2:len(data[0])]
            year=[]
            for t1 in range(0,len(yr)):
                year.append(float(yr[t1]))
            maxyear=max(year)
            minyear=min(year)
            for v in range(1,len(data)):
                YLDD=[]
                YLDD=data[v].split()[2:len(data[v])]
                number_point=0
                for i in range(0,len(YLDD)):
                    if float(YLDD[i])!=-1:
                        number_point=number_point+1
                if number_point>0:
                    fsim=open(parent.textCtrl2.GetValue()  + "\\CalibrationRuns\\" + self.textCtrl3.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.OUT\\" + "Grid_"+ str(v)+ ".txt","w") 
                    for itr in range(1,int(self.textCtrl1.GetValue())+1):   
                        fsim.write(str(itr)+ '\n')                             
                        with open(parent.textCtrl2.GetValue()+ "\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + str(v) + "RF" + ".ACY" ,'r') as file:
                            dataf=file.readlines() 
                        YLD=[]
                        YR=[]
                        for i in range(11,len(dataf)):
                            YLD.append(dataf[i].split()[3]) 
                            YR.append(dataf[i].split()[0])                    
                        for y in range(int(minyear),int(maxyear)+1):
                            YLD1=[]
                            for j1, j in enumerate(YR):
                                if j == str(y):
                                    YLD1.append(float(YLD[j1]))
                            if len(YLD1)>0:
                                YLDf=max(YLD1)
                                if float(YLD[j1])!= -1:
                                    fsim.write(str(y)+  "    " + str(YLDf) + "\n")               
                fsim.close()                                  
        dlg = wx.MessageDialog(self, 'observed.txt were build-up', 'Message', wx.OK | wx.ICON_INFORMATION)
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