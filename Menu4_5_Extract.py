# -*- coding: utf-8 -*-
#Boa:Dialog:Dialog1
import wx.lib.buttons , os, platform,subprocess, stat 
import random, shutil 
import matplotlib.pyplot as plt
from pylab import *
import numpy  
import scipy.stats as stats
import matplotlib.patches as mpatches
#from numpy import matrix
def create(parent):
    return Dialog1(parent)
[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, wxID_DIALOG1BUTTON4,wxID_DIALOG1BUTTON5, wxID_DIALOG2CHECKBOX1,wxID_DIALOG2CHECKBOX2,wxID_DIALOG2CHECKBOX3,wxID_DIALOG2CHECKBOX4,wxID_DIALOG2CHECKBOX5,
 wxID_DIALOG1STATICTEXT1,wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4,wxID_DIALOG1STATICTEXT5,wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7,wxID_DIALOG1STATICTEXT8,
 wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2,wxID_DIALOG1TEXTCTRL3,wxID_DIALOG1TEXTCTRL4,wxID_DIALOG1TEXTCTRL5,wxID_DIALOG1TEXTCTRL6,wxID_DIALOG1TEXTCTRL7,wxID_DIALOG1TEXTCTRL8,
 
 wxID_DIALOG1STATICTEXT2_1,wxID_DIALOG1STATICTEXT2_2,wxID_DIALOG1STATICTEXT2_3,wxID_DIALOG1STATICTEXT2_4, wxID_DIALOG1TEXTCTRL2_1,wxID_DIALOG1TEXTCTRL2_2,wxID_DIALOG1TEXTCTRL2_3,wxID_DIALOG1TEXTCTRL2_4,
 wxID_DIALOG1BUTTON2_1,wxID_DIALOG1BUTTON2_2, wxID_DIALOG1BUTTON2_3, wxID_DIALOG1BUTTON2_4,wxID_FRAME1STATICBITMAP1] = [wx.NewId() for _init_ctrls in range(40)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent):
        parent.AddWindow(self.checkBox1, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox3, 0, border=0, flag=0)
        
    def _init_coll_flexGridSizer2_Items(self, parent):                            
        parent.AddWindow(self.staticText1, 0, border=0, flag=0) 
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0)       
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2, 0, border=0, flag=0)        
        parent.AddWindow(self.staticText3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4, 0, border=0, flag=0)

                
    def _init_coll_flexGridSizer3_Items(self, parent):
        # generated method, don't edit                                               
        parent.AddWindow(self.staticText2_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_3, 0, border=0, flag=0)
        parent.AddWindow(self.button2_3, 0, border=0, flag=0)  
                                                      
    def _init_coll_flexGridSizer4_Items(self, parent):
        # generated method, don't edit 
        parent.AddWindow(self.button1, 0, border=0, flag=0)          
        parent.AddWindow(self.button2, 0, border=0, flag=0)       
        parent.AddWindow(self.button3, 0, border=0, flag=0)    
        parent.AddWindow(self.button4, 0, border=0, flag=0)
        parent.AddWindow(self.button5, 0, border=0, flag=0)
        
    def _init_coll_flexGridSizer5_Items(self, parent):
        parent.AddWindow(self.staticBitmap1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText5, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl5, 0, border=0, flag=0)
                                                                                                                     
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer4, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer5, 0, border=0, flag=0)
                        
    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=4, hgap=1, rows=6, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=4, hgap=1, rows=6, vgap=0)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=4, hgap=2, rows=25, vgap=1) 
        self.flexGridSizer4 = wx.FlexGridSizer(cols=5, hgap=2, rows=25, vgap=1)  
        self.flexGridSizer5 = wx.FlexGridSizer(cols=1, hgap=20, rows=25, vgap=1)             
                                
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3) 
        self._init_coll_flexGridSizer4_Items(self.flexGridSizer4)
        self._init_coll_flexGridSizer5_Items(self.flexGridSizer5)
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,  pos=wx.Point(10, 10), size=wx.Size(800, 800), style=wx.DEFAULT_DIALOG_STYLE, title=u'SUFI2.POST')
        self.SetClientSize(wx.Size(800, 800))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)     
         
#================related to flexGridSizer1                
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=u'Number of parameters',  parent=self,  size=wx.Size(200, 20), style=wx.ALIGN_LEFT)
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, parent=self, size=wx.Size(100, 21))
        
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=u'Objective function', parent=self,  size=wx.Size(200, 20), style=wx.ALIGN_LEFT)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, parent=self, size=wx.Size(100, 21))        
        
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=u'Threshold for objective function', parent=self,  size=wx.Size(200, 20), style=wx.ALIGN_LEFT)
        self.staticText3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3, parent=self, size=wx.Size(100, 21))   

        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=u'Number of running-average years',  parent=self,  size=wx.Size(200, 20), style=wx.ALIGN_LEFT)
        self.staticText4.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText4.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, parent=self, size=wx.Size(100, 21))  
                                                                                                                                                                                                                                               
        self.staticText2_3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_3,label=u'observed yield path', parent=self, size=wx.Size(150, 20),style=wx.ALIGN_LEFT)
        self.staticText2_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2_3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2_3.SetAutoLayout(True)
        self.textCtrl2_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_3,parent=self, size=wx.Size(510, 21))
        self.button2_3 = wx.Button(id=wxID_DIALOG1BUTTON2_3, label=u'Browse',parent=self, pos=wx.Point(0, 600), size=wx.Size(100, 20))
        self.button2_3.Bind(wx.EVT_BUTTON, self.OnButton2_3Dir, id=wxID_DIALOG1BUTTON2_3)
           
        #======================================================related to flexGridSizer 5=============================================================================                                                                                                                                                                                                                                                  
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Extract Simulated Yield', parent=self, size=wx.Size(140, 30))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOG1BUTTON1)                                                                                                                                                                                                                                                 
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Observed.txt in SUFI2.IN', parent=self,  size=wx.Size(140, 30))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button, id=wxID_DIALOG1BUTTON2)                
        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'SUFI2.POST', parent=self,  size=wx.Size(140, 30))
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button, id=wxID_DIALOG1BUTTON3)  
        self.button4 = wx.Button(id=wxID_DIALOG1BUTTON4, label=u'Plot', parent=self,  size=wx.Size(140, 30))
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button, id=wxID_DIALOG1BUTTON4) 
        self.button5 = wx.Button(id=wxID_DIALOG1BUTTON5, label=u'show Plot', parent=self,  size=wx.Size(140, 30))
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button, id=wxID_DIALOG1BUTTON5)
        
                                        
        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG2CHECKBOX1, label=u'RF', parent=self, size=wx.Size(50, 25))
        self.checkBox1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))  
        self.checkBox2 = wx.CheckBox(id=wxID_DIALOG2CHECKBOX2, label=u'IR',  parent=self, size=wx.Size(50, 25))
        self.checkBox2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))                
        self.checkBox3 = wx.CheckBox(id=wxID_DIALOG2CHECKBOX3, label=u'RF-IR',  parent=self, size=wx.Size(50, 25))
        self.checkBox3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman')) 
        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',parent=self,pos=wx.Point(50, 590), size=wx.Size(590, 590),style=0)
        
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5, label=u'regionnum',  parent=self,  size=wx.Size(100, 20), style=wx.ALIGN_LEFT)
        self.staticText5.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText5.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL5, parent=self, size=wx.Size(50, 21))  
                                                                                                        
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
        fSetup = open('OutputExtraction.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 2:
                self.textCtrl1.SetValue(txtLine.split(',')[0])
            if loopNum == 3:
                self.textCtrl2.SetValue(txtLine.split(',')[0])
            if loopNum == 4:
                self.textCtrl3.SetValue(txtLine.split(',')[0])
            if loopNum == 5:
                self.textCtrl4.SetValue(txtLine.split(',')[0]) 
            if loopNum == 6:
                self.textCtrl2_3.SetValue(txtLine.split(',')[0])                 
            if loopNum == 1:
                if txtLine.split(',')[0]=='RF':
                    self.checkBox1.SetValue(True)
                    self.checkBox2.SetValue(False)
                    self.checkBox3.SetValue(False)
                elif txtLine.split(',')[0]=='IR':
                    self.checkBox1.SetValue(False)
                    self.checkBox2.SetValue(True)
                    self.checkBox3.SetValue(False)
                elif txtLine.split(',')[0]=='RF-IR':
                    self.checkBox1.SetValue(False)
                    self.checkBox2.SetValue(False)
                    self.checkBox3.SetValue(True)                           
            loopNum=loopNum+1          
            
    def OnButton2_3Dir(self, parent):
        ### Write the par_inf.sf2 and Create the parameters sample
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            "You chose %s" % dlg.GetPath()
        self.textCtrl2_3.SetValue(dlg.GetPath())
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
        scenario=parent.textCtrl1_1.GetValue()
        fList1 = open(CurrentDir + "\\Simulation\\Input\\" + scenario +  "\\inputList.txt", "r")
        start_yr=int(parent.textCtrl3_1.GetValue())
        end_yr=start_yr+ int(parent.textCtrl3_2.GetValue())-1
        skip_yr=int(parent.textCtrl3_3.GetValue())
        start_line=11+skip_yr
        year=range(start_yr,end_yr)
        if self.checkBox1.GetValue() == True:
            Planting_system='RF'
        elif self.checkBox2.GetValue() == True:
            Planting_system='IR'
        elif self.checkBox3.GetValue() == True:
            Planting_system='RF-IR'
########################################################################################################           
        if Planting_system == "RF-IR":
                fList1 = open(CurrentDir + "\\Simulation\\Input\\" + scenario +  "\\inputList.txt", "r")        
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    s2=(lin1.split(',')[0])[0:s1]
                    fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11)
                    region=[]
                    for lin2 in fin:                                  
                        region.append(int(float((lin2.split()[10]))))
                    regionnum=max(region)
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(parent.textCtrl3_4.GetValue()) 
                    ########--------------------------------------------------Regional summing RF+IR
                    for reg in range(1, regionnum+1):
                        Fregional=open(f_SUFI2_OUT + "\\" +"Y_" +str(reg) +".txt",'w') 
                        for itr in range(1,itr_num+1):
                            Fregional.write(" " + str(itr)+ "\n")       
                            fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                            regional_YieldRF=[] 
                            TareaRF=[]         
                            for lin2 in fin:                                             
                                lon=float(lin2.split()[1])
                                lat=float(lin2.split()[2])
                                areaRF=float(lin2.split()[8])
                                areaIR=float(lin2.split()[9])
                                regionNum=int(float(lin2.split()[10]))
                                if  regionNum==reg:
                                    #-------------------------------------------------------RF
                                    TareaRF.append(areaRF)
                                    with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
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
                                    regional_YieldRF.append (Grid_Yearly_Yield)
                                    #-------------------------------------------------------IR
                                    TareaIR.append(areaIR)
                                    with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "IR" + ".ACY" ,'r') as file:
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
                                                YLD1.append(float(YLD[i]))
                                        YLD_IR.append(max(YLD1)) 
                                    Grid_Yearly_Yield=[]
                                    for i in range(0,len(YLD_RF)):
                                        Grid_Yearly_Yield.append(format(YLD_IR[i],'8.2f'))                       
                                    regional_YieldIR.append (Grid_Yearly_Yield)                                    
                          
                            for yr in range(0,len(YLD_RF)):
                                year=start_yr+yr+skip_yr
                                a=0
                                for gr in range(0,len(regional_Yield)):
                                    a=a+(float(regional_YieldRF[gr][yr])*float(TareaRF[gr]))+(float(regional_YieldIR[gr][yr])*float(TareaIR[gr]))
                                averge=a/(sum(TareaRF)+sum(TareaIR))
                                Fregional.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
                Fregional.close()
                fin.close()
                ####################################################################################################country scale 
                fList1 = open(CurrentDir + "\\Simulation\\Input\\" + scenario +  "\\inputList.txt", "r")
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(self.textCtrl1.GetValue())   
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + "Yield_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + "Y_country.txt",'w') 
                    for itr in range(1,itr_num+1):
                        #print itr
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                        Fcountry.write(str(itr)+ '\n') 
                        Country_Yield=[]        
                        for lin2 in fin:                                              
                            lon=float(lin2.split()[1])
                            lat=float(lin2.split()[2])
                            areaIR = float(lin2.split()[9])
                            areaRF = float(lin2.split()[8])                
                            ## RainFed Yield 
                            if areaIR>0 or areaRF>0:
                                f_OUTPUT.write(format(lon,'8.2f')+ ',')
                                f_OUTPUT.write(format(lat,'8.2f')+ ',')
                                with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
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
                                with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "IR" + ".ACY" ,'r') as file:
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
                    s2=(lin1.split(',')[0])[0:s1]
                    fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11)
                    region=[]
                    for lin2 in fin:                                  
                        region.append(int(float((lin2.split()[10]))))
                    regionnum=max(region)
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(parent.textCtrl3_4.GetValue()) 
                    for reg in range(1, regionnum+1):
                        Fregional=open(f_SUFI2_OUT + "\\" +"Y_" +str(reg) +".txt",'w') 
                        for itr in range(1,itr_num+1):
                            Fregional.write(" " + str(itr)+ "\n")       
                            fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                            regional_Yield=[] 
                            Tarea=[]         
                            for lin2 in fin:                                             
                                lon=float(lin2.split()[1])
                                lat=float(lin2.split()[2])
                                areaRF=float(lin2.split()[9])
                                regionNum=int(float(lin2.split()[10]))
                                if  areaRF>0 and regionNum==reg:
                                    Tarea.append(areaRF)
                                    with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "IR" + ".ACY" ,'r') as file:
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
                                    regional_Yield.append (Grid_Yearly_Yield)
                          
                            for yr in range(0,len(YLD_RF)):
                                year=start_yr+yr+skip_yr
                                a=0
                                for gr in range(0,len(regional_Yield)):
                                    a=a+(float(regional_Yield[gr][yr])*float(Tarea[gr]))
                                averge=a/sum(Tarea)
                                Fregional.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
                    Fregional.close()
                    fin.close()
                ####################################################################################################country scale 
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + "Yield_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + "Y_country.txt",'w')        
                    for itr in range(1,itr_num+1):
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
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
                                with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
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
                ###############################################################################Averaging on country level                                 
                        for yr in range(0,len(YLD_RF)):
                            year=start_yr+yr+skip_yr
                            a=0
                            for gr in range(0,len(Country_Yield)):
                                a=a+(float(Country_Yield[gr][yr])*float(Tarea[gr]))
                            averge=a/sum(Tarea)
                            Fcountry.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
###########################################################################################################                                 
        elif Planting_system == "RF":           
                for lin1 in fList1:
                    lin11=lin1.split(',')[0]
                    s1=len(lin1.split(',')[0])-10
                    s11=lin1.split(',')[1]
                    s2=(lin1.split(',')[0])[0:s1]
                    fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11)
                    region=[]
                    for lin2 in fin:                                  
                        region.append(int(float((lin2.split()[10]))))

                    regionnum=max(region)
                    f_SUFI2_OUT=parent.textCtrl2.GetValue()+"\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\SUFI2.OUT"
                    if os.path.isdir(f_SUFI2_OUT) == True:
                        shutil.rmtree(f_SUFI2_OUT)
                    os.mkdir(f_SUFI2_OUT)
                    itr_num=int(parent.textCtrl3_4.GetValue()) 
                    for reg in range(1, regionnum+1):
                        Fregional=open(f_SUFI2_OUT + "\\" +"Y_" +str(reg) +".txt",'w') 
                        for itr in range(1,itr_num+1):
                            Fregional.write(" " + str(itr)+ "\n")       
                            fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
                            regional_Yield=[] 
                            Tarea=[]         
                            for lin2 in fin:                                             
                                lon=float(lin2.split()[1])
                                lat=float(lin2.split()[2])
                                areaRF=float(lin2.split()[8])
                                regionNum=int(float(lin2.split()[10]))
                                if  areaRF>0 and regionNum==reg:
                                    Tarea.append(areaRF)
                                    with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
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
                                    regional_Yield.append (Grid_Yearly_Yield)
                          
                            for yr in range(0,len(YLD_RF)):
                                year=start_yr+yr+skip_yr
                                a=0
                                for gr in range(0,len(regional_Yield)):
                                    a=a+(float(regional_Yield[gr][yr])*float(Tarea[gr]))
                                averge=a/sum(Tarea)
                                Fregional.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
                    Fregional.close()
                    fin.close()
                ####################################################################################################country scale 
                    f_OUTPUT=open(f_SUFI2_OUT + "\\" + "Yield_Grid.txt",'w')
                    Fcountry=open(f_SUFI2_OUT + "\\" + "Y_country.txt",'w')        
                    for itr in range(1,itr_num+1):
                        f_OUTPUT.write(" " + str(itr)+ "\n")          
                        fin=open(CurrentDir + "\\Simulation\\Input\\" + scenario + "\\" +lin11[0:s1]+ "_Input.txt")
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
                                with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"  + parent.textCtrl1_1.GetValue() + "\\" + s11+ ".Sufi2.SwatCup\\RUN_" + str(itr)+ "\\" + lin2.split()[0] + "RF" + ".ACY" ,'r') as file:
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
                ###############################################################################Averaging on country level                                 
                        for yr in range(0,len(YLD_RF)):
                            year=start_yr+yr+skip_yr
                            a=0
                            for gr in range(0,len(Country_Yield)):
                                a=a+(float(Country_Yield[gr][yr])*float(Tarea[gr]))
                            averge=a/sum(Tarea)
                            Fcountry.write(str(year)+ "  " + format(averge,'8.2f')+ '\n')
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
        
        if self.checkBox1.GetValue() == True:
            Planting_system='RF'
        elif self.checkBox2.GetValue() == True:
            Planting_system='IR'
        elif self.checkBox3.GetValue() == True:
            Planting_system='RF-IR' 
        fList1 = open(parent.textCtrl2.GetValue() + "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()  +  "\\inputList.txt", "r")
        start_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_3.GetValue())
        end_yr=int(parent.textCtrl3_1.GetValue())+ int(parent.textCtrl3_2.GetValue())-1
        number_point= end_yr-start_yr+1    
           
        for lin1 in fList1:
            #------------------------------------------------------------------------------------------------------------------------------------------------   
            s1=len(lin1.split(',')[0])
            s2=(lin1.split(',')[0])[0:s1-10]  
            lin11=lin1.split(',')[0]
            if Planting_system=='RF':
                with open(self.textCtrl2_3.GetValue() +"\\Yield_RF_"+ s2 + ".txt", "r") as file:
                    data=file.readlines() 
            if Planting_system=='IR':
                with open(self.textCtrl2_3.GetValue() +"\\yield_IR_"+ s2 + ".txt", "r") as file:
                    data=file.readlines()    
            if Planting_system=='RF-IR':
                with open(self.textCtrl2_3.GetValue() +"\\yield_T_"+ s2 + ".txt", "r") as file:
                    data=file.readlines()  
            #------------------------------------------------------------------------------------------------------------------------------------------------        
            YLD=[]
            fin=open(parent.textCtrl2.GetValue() + "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\" +lin11)        
            region=[]
            for lin2 in fin:                                  
                region.append(int(float((lin2.split()[10]))))
            regionnum=max(region)  
            if    regionnum==1:
                regionnum=0                                                       
            #------------------------------------------------Country level observed level------------------------------
            fvar=open(parent.textCtrl2.GetValue()  + "\\Simulation\\CalibrationRuns\\" +  parent.textCtrl1_1.GetValue()  + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "var_file_name.txt","w")
            fobs2=open(parent.textCtrl2.GetValue()  + "\\Simulation\\CalibrationRuns\\" +  parent.textCtrl1_1.GetValue()   + "\\" + lin1.split(',')[1] + ".Sufi2.SwatCup\\" + "SUFI2.IN\\" + "observed.txt","w")
            fobs2.write(str(regionnum+1)+"  : number of observed variables\n")
            fobs2.write(self.textCtrl2.GetValue() + "   : Objective function time_step, 1=mult,2=sum,3=r2,4=chi2,5=NS,6=br2,7=Ssqr\n")
            fobs2.write(self.textCtrl3.GetValue() + "   : max or min value of objective function threshold where program stops\n")
            fobs2.write( " \n")
            fobs2.write( " \n")
            fobs2.write("Y_country  : this is the name of variable to be included in the objective function\n")
            fvar.write( "Y_country.txt\n")
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
            #---------------------------------------------------------------------------------------------------------------------- 
            yr=[]
            YLD=[]
            for i in range(0,len(data)):
                yr.append(data[i].split()[0])
                YLD.append(data[i].split()[1]) 
            end_yr= int(parent.textCtrl3_1.GetValue())+int(parent.textCtrl3_2.GetValue())
            for y in range(start_yr,end_yr):
                for i, j in enumerate(yr):
                    if j == str(y):
                        A=0
                        for z1 in range(0,int(self.textCtrl4.GetValue())):
                            A=A+float(YLD[i-z1])                                    
                        fobs2.write(str(yr[i])+ "   1   " + str(float(A)/int(self.textCtrl4.GetValue())) + "\n") 
            fobs2.write( " \n")
            fobs2.write( " \n")
            #####################################################################################################################################################
            #----------------------------------------------------------------------------------------------------------------------------------------------------
            ##############################################################################adding regional data###################################################                                                
            if regionnum>0:
                for reg in range(1, regionnum+1):
                    YLD=[]
                    yr=[] 
                    for v in range(0,len(data)):
                        YLD.append(data[v].split()[reg+1])
                        yr.append(data[v].split()[0])         
                    fobs2.write("Y_"+ str(reg) + "  : this is the name of variable to be included in the objective function\n")
                    fvar.write("Y_"+ str(reg) + ".txt\n")
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
                                fobs2.write(str(y)+ "   1   " + YLD[i] + "\n")   
                    fobs2.write( " \n")
                fobs2.write( " \n")            
                fobs2.close()                                  
                fvar.close()
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
        
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ '\\'  + "inputList.txt", readCode)
        for lin1 in fList1:             
            s11=lin1.split(',')[1]  
            os.chdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup"  )
            proc = subprocess.Popen(["SUFI2_Post.bat", 'c/'])
            proc.wait()
            proc.kill()
        fList1.close()
        os.chdir(parent.textCtrl2.GetValue())

        dlg = wx.MessageDialog(self, 'SUFI2.POST were successfully executed', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()   
                     
    def OnButton4Button(self, event):       
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        parent = self.GetParent()
        scenario=parent.textCtrl1_1.GetValue()
        
        if self.checkBox1.GetValue() == True:
            Planting_system='RF'
        elif self.checkBox2.GetValue() == True:
            Planting_system='IR'
        elif self.checkBox3.GetValue() == True:
            Planting_system='RF-IR'        
        
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ '\\'  + "inputList.txt", "r")
        
        for lin1 in fList1: 
            lin11=lin1.split(',')[0]
            s1=len(lin1.split(',')[0])-10
            s11=lin1.split(',')[1]
            s2=(lin1.split(',')[0])[0:s1]
            
            if Planting_system=='RF':
                with open(self.textCtrl2_3.GetValue() +"\\Yield_RF_"+ s2 + ".txt", "r") as file:
                    data=file.readlines() 
            if Planting_system=='IR':
                with open(self.textCtrl2_3.GetValue() +"\\yield_IR_"+ s2 + ".txt", "r") as file:
                    data=file.readlines()    
            if Planting_system=='RF-IR':
                with open(self.textCtrl2_3.GetValue() +"\\yield_T_"+ s2 + ".txt", "r") as file:
                    data=file.readlines()           
            #------------------------------------------------------------------------------------------------------------------------------------------------        
            YLD=[]
            fin=open(parent.textCtrl2.GetValue() + "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\" +lin11)        
            region=[]
            for lin2 in fin:                                  
                region.append(int(float((lin2.split()[10]))))
            regionnum=max(region)  
            if    regionnum==1:
                regionnum=0  
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"+ parent.textCtrl1_1.GetValue()+ "\\" + s11 + ".Sufi2.SwatCup\\" + "SUFI2.OUT"+"\\95ppu.txt", 'r') as inF:
                data95ppu=inF.readlines()
            startline=int(float(len(data95ppu))/(regionnum+1))
            start=[]
            end=[]
            for i in range(0,len(data95ppu),startline):
                start.append(i+2)
                end.append(i+startline-7)
    
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"+ parent.textCtrl1_1.GetValue()+ "\\" + s11 + ".Sufi2.SwatCup\\" + "SUFI2.OUT"+"\\best_sim.txt", 'r') as inF:
                dataBestSim=inF.readlines()
            startline2=int(float(len(dataBestSim))/(regionnum+1))
            start1=[]
            end1=[]
            for i in range(0,len(dataBestSim),startline2):
                start1.append(i+3)
                end1.append(i+startline2-1)    
            yr=range(int(parent.textCtrl3_1.GetValue())+int(parent.textCtrl3_3.GetValue()),int(parent.textCtrl3_1.GetValue())+int(parent.textCtrl3_2.GetValue()))
            for i in range(0, regionnum+1):
                L95PPU=[]
                U95PPU=[]
                observed=[]
                simulated=[]
                for j in range(start[i],end[i]):
                    observed.append(float(data95ppu[j].split()[0]))
                    L95PPU.append(float(data95ppu[j].split()[1]))
                    U95PPU.append(float(data95ppu[j].split()[2]))    
                for k in range(start1[i],end1[i]):
                    simulated.append(float(dataBestSim[k].split()[1]))

                f1 = plt.figure()
                plt.fill_between(yr,L95PPU,U95PPU,color='green',alpha=.8)
                plt.scatter(yr,observed,color='red',alpha=.8)
                plt.plot(yr,simulated,lw=2)
                plt.ylabel(lin1.split(',')[1]+ str(i)+ " (t/ha)")
                locs,labels = xticks()
                xticks(locs, map(lambda x: "%.0f" % x, locs*1e0)) 
                plt.xlim(yr[0], yr[len(yr)-1])               
                green_patch = mpatches.Patch(color='green',alpha=.8,label='95PPU')
                blue_patch = mpatches.Patch(color='blue', label='Best simulation')
                plt.legend(handles=[green_patch,blue_patch])        
                plt.savefig(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"+ parent.textCtrl1_1.GetValue()+ "\\" + s11 + ".Sufi2.SwatCup\\" + "SUFI2.OUT"+pathSep+lin1.split(',')[1]+str(i)+".jpg", bbox_inches='tight')               
        dlg = wx.MessageDialog(self, 'SUFI2.POST were successfully executed', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy() 
    def OnButton5Button(self, event):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        parent = self.GetParent()
        
        def scale_bitmap(bitmap, width, height):
            image = wx.ImageFromBitmap(bitmap)
            image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
            result = wx.BitmapFromImage(image)
            return result
            
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ '\\'  + "inputList.txt", "r")
        for lin1 in fList1: 
            s11=lin1.split(',')[1]        
            bmp = wx.Bitmap(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\"+ parent.textCtrl1_1.GetValue()+ "\\" + s11 + ".Sufi2.SwatCup\\" + "SUFI2.OUT\\"+lin1.split(',')[1]+ self.textCtrl5.GetValue()+".jpg", wx.BITMAP_TYPE_JPEG)
            bmp = scale_bitmap(bmp, 580, 580)
            self.staticBitmap1.SetBitmap(bmp)
                                                                                                                                
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