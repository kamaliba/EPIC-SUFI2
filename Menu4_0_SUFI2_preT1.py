# -*- coding: utf-8 -*-
#Boa:Dialog:Dialog1
import wx.lib.buttons , os, platform,subprocess, stat 
import random, shutil 
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from numpy import matrix
######================================
def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2,  wxID_DIALOG1BUTTON3, wxID_DIALOG1BUTTON4,  wxID_DIALOG1BUTTON5, 
 wxID_DIALOG1STATICTEXT0,
 wxID_DIALOG1TEXTCTRL0,  
 ] = [wx.NewId() for _init_ctrls in range(8)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent):
        parent.AddWindow(self.button1, 0, border=0, flag=0)
        parent.AddWindow(self.button2, 0, border=0, flag=0)
        parent.AddWindow(self.button3, 0, border=0, flag=0)  
        parent.AddWindow(self.button4, 0, border=0, flag=0)  
   
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=1, hgap=1, rows=6, vgap=0)
       
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)  
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, size=wx.Size(250, 150), style=wx.DEFAULT_DIALOG_STYLE, title=u'SUFI2.pre')
        self.SetClientSize(wx.Size(250, 120))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)            
                                                                                                                                                                                                                                                
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'EPIC Latin Hypercube Sampling', name='button1', parent=self,  size=wx.Size(250, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOG1BUTTON1)
        
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'OperationFile-EDIT (OPS2)', name='button2', parent=self,  size=wx.Size(250, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button, id=wxID_DIALOG1BUTTON2)
        
        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'CROPCOM-EDIT (OPS2)', name='button3', parent=self,  size=wx.Size(250, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button, id=wxID_DIALOG1BUTTON3)
        
        self.button4 = wx.Button(id=wxID_DIALOG1BUTTON4, label=u'PARM0810-EDIT (OPS2)', name='button4', parent=self,  size=wx.Size(250, 30), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button, id=wxID_DIALOG1BUTTON4)
                                                           
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
        parent = self.GetParent()   
##################################################################  
    def OnButton1Button(self, parent):
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
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ '\\'  + "inputList.txt", readCode)
        for lin1 in fList1:             
            s11=lin1.split(',')[1]                 
            os.chdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup"  )
            proc = subprocess.Popen(["SUFI2_LH_sample.exe", 'c/'])
            proc.wait()
            proc.kill()
            
          #  src=parent.textCtrl2.GetValue()+ '\\Parameterization_SetupT1.inf'
         # des=parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11  +".Sufi2.SwatCup\\"+ 'Parameterization_SetupT1.inf'        
         #   if os.path.isfile(des) == True:
          #      os.remove(des)                                     
          #  shutil.copy(src, des)         
        fList1.close()
        os.chdir(parent.textCtrl2.GetValue())
        dlg = wx.MessageDialog(self, 'The parameters were sampled successfully', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()   

    def OnButton2Button(self, parent):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        parent = self.GetParent()                   
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ "\\"  + "inputList.txt", readCode)
        for lin1 in fList1:             
            s11=lin1.split(',')[1]
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\Parameterization_Setup.inf",'r') as file:  
                data=file.readlines() 
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\SUFI2.IN\\par_val.txt",'r') as file:
                data2=file.readlines()       
            for NRun in range(1,int(parent.textCtrl3_4.GetValue())+1): 
                ftempOPR= open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + "\\" + s11 + ".Sufi2.SwatCup\\RUN_" + str(NRun)+ "\\" + "tempOPR.DAT", "w") 
                paramNum=1
                dataLHS=data2[NRun-1].split()
                #========================Planting Date         
                if data[1].split(',')[0]=="Y":
                    ftempOPR.write("R_PDate=1+" +dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_PDate=1\n")
                #========================PHU coefficient
                if data[2].split(',')[0]=="Y":
                    ftempOPR.write("R_PHU=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_PHU=1\n")
                # ========================Planting Density     
                if data[3].split(',')[0]=="Y":
                    ftempOPR.write("R_PDensity=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_PDensity=1\n")                             
                #======================== Pesticide Rate    
                if data[4].split(',')[0]=="Y":
                    ftempOPR.write("R_PestRate=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_PestRate=1\n") 
                #======================== Irrigation Application   
                if data[5].split(',')[0]=="Y":
                    ftempOPR.write("R_IRRApp=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_IRRApp=1\n")    
                # =====================Irrigation Rate  
                if data[6].split(',')[0]=="Y":
                    ftempOPR.write("R_IRRrate=" + (1+dataLHS[paramNum]) + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_IRRrate=1\n")    
                #======================== Irrigation Rate  
                if data[7].split(',')[0]=="Y":
                    ftempOPR.write("R_FNPrate=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_FNPrate=1\n")          
                #======================== FMXRate        
                if data[8].split(',')[0]=="Y":
                    ftempOPR.write("R_FMXrate=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_FMXrate=1\n")        
                #======================== BFT0Rate        
                if data[9].split(',')[0]=="Y":
                    ftempOPR.write("R_BFT0rate=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_BFT0rate=1\n")          
                #======================== PMX   
                if data[10].split(',')[0]=="Y":
                    ftempOPR.write("R_PMX=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_PMX=1\n")   
                #======================== Prate   
                if data[11].split(',')[0]=="Y":
                    ftempOPR.write("Prate=1+" + dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("Prate=1\n")              
                #======================== KMX   
                if data[12].split(',')[0]=="Y":
                    ftempOPR.write("R_KMX=1+" +dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("R_KMX=1\n")   
                #======================== Krate   
                if data[13].split(',')[0]=="Y":
                    ftempOPR.write("Krate=1+" +dataLHS[paramNum] + "\n")
                    paramNum=paramNum+1
                else:
                    ftempOPR.write("Krate=1\n")                                     
                ftempOPR.close()                                                                
        dlg = wx.MessageDialog(self, 'The parameters were sampled in tempOPR.DAT', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy() 
                                                                                                               
    def OnButton3Button(self, parent):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        parent = self.GetParent() 
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ "\\"  + "inputList.txt", readCode)
        for lin1 in fList1:             
            s11=lin1.split(',')[1]         
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\Parameterization_Setup.inf",'r') as file:  
                data=file.readlines() 
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\SUFI2.IN\\par_val.txt",'r') as file:
                data2=file.readlines()             
                   
            for NRun in range(1,int(parent.textCtrl3_4.GetValue())+1):  
                paramNum=1+int(data[0].split(',')[1])
                dataLHS=data2[NRun-1].split()
                #======================== WA       
                if data[14].split(',')[0]=="Y":
                    if data[14].split(',')[1]=="vReplace":
                        WA=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WA=format(float(data[14].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    WA=format(float(data[14].split(',')[2]),'8.2f')
                #======================== HI       
                if data[15].split(',')[0]=="Y":
                    if data[15].split(',')[1]=="vReplace":
                        HI=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        HI=format(float(data[15].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    HI=format(float(data[15].split(',')[2]),'8.2f')
                #======================== TOPC       
                if data[16].split(',')[0]=="Y":
                    if data[16].split(',')[1]=="vReplace":
                        TOPC=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        TOPC=format(float(data[16].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    TOPC=format(float(data[16].split(',')[2]),'8.2f')
                #======================== TBSC      
                if data[17].split(',')[0]=="Y":
                    if data[17].split(',')[1]=="vReplace":
                        TBSC=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        TBSC=format(float(data[17].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    TBSC=format(float(data[17].split(',')[2]),'8.2f')             
                #======================== DMLA     
                if data[18].split(',')[0]=="Y":
                    if data[18].split(',')[1]=="vReplace":
                        DMLA=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        DMLA =format(float(data[18].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    DMLA=format(float(data[18].split(',')[2]),'8.2f')              
                #======================== DLAI     
                if data[19].split(',')[0]=="Y":
                    if data[19].split(',')[1]=="vReplace":
                        DLAI=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        DLAI=format(float(data[19].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    DLAI=format(float(data[19].split(',')[2]),'8.2f')   
                #======================== DLAP1     
                if data[20].split(',')[0]=="Y":
                    if data[20].split(',')[1]=="vReplace":
                        DLAP1=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        DLAP1=format(float(data[20].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    DLAP1=format(float(data[20].split(',')[2]),'8.2f')                
                #======================== DLAP2   
                if data[21].split(',')[0]=="Y":
                    if data[21].split(',')[1]=="vReplace":
                        DLAP2=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        DLAP2=format(float(data[21].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    DLAP2=format(float(data[21].split(',')[2]),'8.2f')   
                #======================== RLAD   
                if data[22].split(',')[0]=="Y":
                    if data[22].split(',')[1]=="vReplace":
                        RLAD=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        RLAD=format(float(data[22].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    RLAD=format(float(data[22].split(',')[2]),'8.2f')                                    
                #======================== RBMD  
                if data[23].split(',')[0]=="Y":
                    if data[23].split(',')[1]=="vReplace":
                        RBMD=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        RBMD=format(float(data[23].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    RBMD=format(float(data[23].split(',')[2]),'8.2f')              
                #======================== ALT 
                if data[24].split(',')[0]=="Y":
                    if data[24].split(',')[1]=="vReplace":
                        ALT=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        ALT=format(float(data[24].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    ALT=format(float(data[24].split(',')[2]),'8.2f') 
                #======================== GSI
                if data[25].split(',')[0]=="Y":
                    if data[25].split(',')[1]=="vReplace":
                        GSI=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        GSI=format(float(data[25].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    GSI=format(float(data[25].split(',')[2]),'8.4f')                     
                #======================== CAF
                if data[26].split(',')[0]=="Y":
                    if data[26].split(',')[1]=="vReplace":
                        CAF=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        CAF=format(float(data[26].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    CAF=format(float(data[26].split(',')[2]),'8.2f')                                       
                #======================== SDW
                if data[27].split(',')[0]=="Y":
                    if data[27].split(',')[1]=="vReplace":
                        SDW=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        SDW=format(float(data[27].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    SDW=format(float(data[27].split(',')[2]),'8.2f')   
                #======================== HMX
                if data[28].split(',')[0]=="Y":
                    if data[28].split(',')[1]=="vReplace":
                        HMX=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        HMX=format(float(data[28].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    HMX=format(float(data[28].split(',')[2]),'8.2f')                     
                #======================== RDMX
                if data[29].split(',')[0]=="Y":
                    if data[29].split(',')[1]=="vReplace":
                        RDMX=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        RDMX=format(float(data[29].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    RDMX=format(float(data[29].split(',')[2]),'8.2f')                                                                                                                                                                               
                #======================== WAC2
                if data[30].split(',')[0]=="Y":
                    if data[30].split(',')[1]=="vReplace":
                        WAC2=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WAC2=format(float(data[30].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    WAC2=format(float(data[30].split(',')[2]),'8.2f')   
                #======================== CNY
                if data[31].split(',')[0]=="Y":
                    if data[31].split(',')[1]=="vReplace":
                        CNY=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        CNY=format(float(data[31].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    CNY=format(float(data[31].split(',')[2]),'8.4f')               
                #======================== CPY
                if data[32].split(',')[0]=="Y":
                    if data[32].split(',')[1]=="vReplace":
                        CPY=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        CPY=format(float(data[32].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    CPY=format(float(data[32].split(',')[2]),'8.4f')              
                #======================== CKY
                if data[33].split(',')[0]=="Y":
                    if data[33].split(',')[1]=="vReplace":
                        CKY=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        CKY=format(float(data[33].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    CKY=format(float(data[33].split(',')[2]),'8.4f') 
                #======================== WSYF
                if data[34].split(',')[0]=="Y":
                    if data[34].split(',')[1]=="vReplace":
                        WSYF=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WSYF=format(float(data[34].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    WSYF=format(float(data[34].split(',')[2]),'8.2f')              
                #======================== PST
                if data[35].split(',')[0]=="Y":
                    if data[35].split(',')[1]=="vReplace":
                        PST=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        PST=format(float(data[35].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    PST=format(float(data[35].split(',')[2]),'8.2f') 
                #======================== CSTS
                if data[36].split(',')[0]=="Y":
                    if data[36].split(',')[1]=="vReplace":
                        CSTS=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        CSTS=format(float(data[36].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    CSTS=format(float(data[36].split(',')[2]),'8.2f')                     
                #======================== PRYG
                if data[37].split(',')[0]=="Y":
                    if data[37].split(',')[1]=="vReplace":
                        PRYG=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        PRYG=format(float(data[37].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    PRYG=format(float(data[37].split(',')[2]),'8.2f')                                 
                #======================== PRYF
                if data[38].split(',')[0]=="Y":
                    if data[38].split(',')[1]=="vReplace":
                        PRYF=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        PRYF=format(float(data[38].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    PRYF=format(float(data[38].split(',')[2]),'8.2f')                                 
                #======================== WCY
                if data[39].split(',')[0]=="Y":
                    if data[39].split(',')[1]=="vReplace":
                        WCY=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WCY=format(float(data[39].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    WCY=format(float(data[39].split(',')[2]),'8.2f')                                                                                             
                #======================== BN1
                if data[40].split(',')[0]=="Y":
                    if data[40].split(',')[1]=="vReplace":
                        BN1=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BN1=format(float(data[40].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BN1=format(float(data[40].split(',')[2]),'8.4f') 
                #======================== BN2                                                               
                if data[41].split(',')[0]=="Y":
                    if data[41].split(',')[1]=="vReplace":
                        BN2=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BN2=format(float(data[41].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BN2=format(float(data[41].split(',')[2]),'8.4f')                                                                          
                #======================== BN3                                                              
                if data[42].split(',')[0]=="Y":
                    if data[42].split(',')[1]=="vReplace":
                        BN3=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BN3=format(float(data[42].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BN3=format(float(data[42].split(',')[2]),'8.4f')                                                                                          
                #======================== BP1                                                               
                if data[43].split(',')[0]=="Y":
                    if data[43].split(',')[1]=="vReplace":
                        BP1=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BP1=format(float(data[43].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BP1=format(float(data[43].split(',')[2]),'8.4f')                                                                                                                    
                #======================== BP2                                                               
                if data[44].split(',')[0]=="Y":
                    if data[44].split(',')[1]=="vReplace":
                        BP2=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BP2=format(float(data[44].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BP2=format(float(data[44].split(',')[2]),'8.4f')                   
                #======================== BP3                                                              
                if data[45].split(',')[0]=="Y":
                    if data[45].split(',')[1]=="vReplace":
                        BP3=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BP3=format(float(data[45].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BP3=format(float(data[45].split(',')[2]),'8.4f')                   
                #======================== BK1                                                               
                if data[46].split(',')[0]=="Y":
                    if data[46].split(',')[1]=="vReplace":
                        BK1=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BK1=format(float(data[46].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BK1=format(float(data[46].split(',')[2]),'8.4f')                   
                #======================== BK2                                                               
                if data[47].split(',')[0]=="Y":
                    if data[47].split(',')[1]=="vReplace":
                        BK2=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BK2=format(float(data[47].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BK2=format(float(data[47].split(',')[2]),'8.4f')                   
                #======================== BK3                                                               
                if data[48].split(',')[0]=="Y":
                    if data[48].split(',')[1]=="vReplace":
                        BK3=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        BK3=format(float(data[48].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    BK3=format(float(data[48].split(',')[2]),'8.4f')                   
                #======================== BW1                                                               
                if data[49].split(',')[0]=="Y":
                    if data[49].split(',')[1]=="vReplace":
                        BW1=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        BW1=format(float(data[49].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    BW1=format(float(data[49].split(',')[2]),'8.3f')                   
                #======================== BW2                                                               
                if data[50].split(',')[0]=="Y":
                    if data[50].split(',')[1]=="vReplace":
                        BW2=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        BW2=format(float(data[50].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    BW2=format(float(data[50].split(',')[2]),'8.3f')               
                #======================== BW3                                                               
                if data[51].split(',')[0]=="Y":
                    if data[51].split(',')[1]=="vReplace":
                        BW3=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        BW3=format(float(data[51].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    BW3=format(float(data[51].split(',')[2]),'8.3f')               
                #======================== IDC                                                               
                if data[52].split(',')[0]=="Y":
                    if data[52].split(',')[1]=="vReplace":
                        IDC=format(float(dataLHS[paramNum]),'7.0f')
                    else:
                        IDC=format(float(data[52].split(',')[2])*(1+float(dataLHS[paramNum])),'7.0f')
                    paramNum=paramNum+1
                else:
                    IDC=format(float(data[52].split(',')[2]),'7.0f')  
                IDC=IDC+'.'             
                #======================== FRST1                                                              
                if data[53].split(',')[0]=="Y":
                    if data[53].split(',')[1]=="vReplace":
                        FRST1 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        FRST1 =format(float(data[53].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    FRST1 =format(float(data[53].split(',')[2]),'8.2f')                
                #======================== FRST2                                                              
                if data[54].split(',')[0]=="Y":
                    if data[54].split(',')[1]=="vReplace":
                        FRST2 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        FRST2 =format(float(data[54].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    FRST2 =format(float(data[54].split(',')[2]),'8.2f')               
                #======================== WAVP                                                              
                if data[55].split(',')[0]=="Y":
                    if data[55].split(',')[1]=="vReplace":
                        WAVP =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WAVP =format(float(data[55].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    WAVP =format(float(data[55].split(',')[2]),'8.2f')               
                #======================== VPTH                                                            
                if data[56].split(',')[0]=="Y":
                    if data[56].split(',')[1]=="vReplace":
                        VPTH =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        VPTH =format(float(data[56].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    VPTH =format(float(data[56].split(',')[2]),'8.2f')                       
                #======================== VPD2                                                           
                if data[57].split(',')[0]=="Y":
                    if data[57].split(',')[1]=="vReplace":
                        VPD2 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        VPD2 =format(float(data[57].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    VPD2=format(float(data[57].split(',')[2]),'8.2f')                  
                #======================== RWPC1                                                           
                if data[58].split(',')[0]=="Y":
                    if data[58].split(',')[1]=="vReplace":
                        RWPC1 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        RWPC1 =float(data[58].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    RWPC1=format(float(data[58].split(',')[2]),'8.2f')               
                #======================== RWPC2                                                           
                if data[59].split(',')[0]=="Y":
                    if data[59].split(',')[1]=="vReplace":
                        RWPC2 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        RWPC2 =float(data[59].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    RWPC2=format(float(data[59].split(',')[2]),'8.2f')                      
                #======================== GMHU                                                           
                if data[60].split(',')[0]=="Y":
                    if data[60].split(',')[1]=="vReplace":
                        GMHU =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        GMHU =float(data[60].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    GMHU=format(float(data[60].split(',')[2]),'8.2f')              
                #======================== PPLP1                                                           
                if data[61].split(',')[0]=="Y":
                    if data[61].split(',')[1]=="vReplace":
                        PPLP1 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        PPLP1 =float(data[61].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    PPLP1=format(float(data[61].split(',')[2]),'8.2f')               
                #======================== PPLP2                                                           
                if data[62].split(',')[0]=="Y":
                    if data[62].split(',')[1]=="vReplace":
                        PPLP2 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        PPLP2 =float(data[62].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    PPLP2=format(float(data[62].split(',')[2]),'8.2f')                
                #======================== STX1                                                           
                if data[63].split(',')[0]=="Y":
                    if data[63].split(',')[1]=="vReplace":
                        STX1 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        STX1 =float(data[63].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    STX1=format(float(data[63].split(',')[2]),'8.2f') 
                #======================== STX2                                                           
                if data[64].split(',')[0]=="Y":
                    if data[64].split(',')[1]=="vReplace":
                        STX2 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        STX2 =float(data[64].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    STX2=format(float(data[64].split(',')[2]),'8.2f')              
                #======================== BLG1                                                           
                if data[65].split(',')[0]=="Y":
                    if data[65].split(',')[1]=="vReplace":
                        BLG1 =format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        BLG1 =float(data[65].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    BLG1=format(float(data[65].split(',')[2]),'8.2f')                            
                #======================== BLG2                                                           
                if data[66].split(',')[0]=="Y":
                    if data[66].split(',')[1]=="vReplace":
                        BLG2=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        BLG2=float(data[66].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    BLG2=format(float(data[66].split(',')[2]),'8.2f')                                           
                #======================== WUB                                                           
                if data[67].split(',')[0]=="Y":
                    if data[67].split(',')[1]=="vReplace":
                        WUB=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        WUB=float(data[67].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    WUB=format(float(data[67].split(',')[2]),'8.2f')                                                      
                #======================== FTO                                                           
                if data[68].split(',')[0]=="Y":
                    if data[68].split(',')[1]=="vReplace":
                        FTO=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        FTO=float(data[68].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    FTO=format(float(data[68].split(',')[2]),'8.2f')
                #======================== FLT                                                           
                if data[69].split(',')[0]=="Y":
                    if data[69].split(',')[1]=="vReplace":
                        FLT=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        FLT=float(data[69].split(',')[2])*(1+float(dataLHS[paramNum]))
                    paramNum=paramNum+1
                else:
                    FLT=format(float(data[69].split(',')[2]),'8.2f')                
                
                txtline=str(WA)+str(HI)+str(TOPC)+str(TBSC)+str(DMLA)+str(DLAI)+str(DLAP1)+str(DLAP2)+str(RLAD)+str(RBMD)+str(ALT)+str(GSI)+str(CAF)+str(SDW)+str(HMX)+str(RDMX)+str(WAC2)+str(CNY)+str(CPY)+\
                str(CKY)+str(WSYF)+str(PST)+str(CSTS)+str(PRYG)+str(PRYF)+str(WCY)+str(BN1)+str(BN2)+str(BN3)+str(BP1)+str(BP2)+str(BP3)+str(BK1)+str(BK2)+str(BK3)+str(BW1)+str(BW2)+str(BW3)+str(IDC)+\
                str(FRST1)+str(FRST2)+str(WAVP)+str(VPTH)+str(VPD2)+str(RWPC1)+str(RWPC2)+str(GMHU)+str(PPLP1)+str(PPLP2)+str(STX1)+str(STX2)+str(BLG1)+str(BLG2)+str(WUB)+str(FTO)+str(FLT)  
                                                                                              
                addres=parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + "\\" + s11 + ".Sufi2.SwatCup\\RUN_" + str(NRun)
                ftempcrop= open(addres + "\\" + "tempCROPCOM.DAT", "w")                
                fcrop= open(addres + "\\" + "CROPCOM.DAT", readCode)
                loop=1
                if parent.comboBox1_2.GetValue() =='Maize':
                    cropcomline=4
                    croplintxt='    2 CORN' + txtline  +'      6.CORN\n'
                elif parent.comboBox1_2.GetValue()=='Rice':
                    cropcomline=20
                    croplintxt='   18 RICE' + txtline  +'    150.RICE\n'
                elif parent.comboBox1_2.GetValue()=='W-Wheat':
                    cropcomline=12
                    croplintxt='   10 WWHT' + txtline  +'    150.WINTER WHEAT\n'
                elif parent.comboBox1_2.GetValue()=='Soybean':
                    cropcomline=3                               
                    croplintxt='    1 SOYB' + txtline  +'     15.SOYBEANS\n'                
                elif parent.comboBox1_2.GetValue()=='Barley':
                    cropcomline=14
                    croplintxt='   14 BARL' + txtline  +'    150.BARLEY\n' 
                elif parent.comboBox1_2.GetValue()=='Sorghum':
                    cropcomline=32
                    croplintxt='   30 SGHY' + txtline  +'     10.SORGHUM HAY\n'         
                elif parent.comboBox1_2.GetValue()=='Millet':
                    cropcomline=81
                    croplintxt='   79 PMIL' + txtline  +'     10.PEARL MILLET\n' 
                    
                for txlin in fcrop:
                    if loop==cropcomline:
                        txlin=croplintxt
                    loop=loop+1
                    ftempcrop.write(txlin)
                ftempcrop.close()
                fcrop.close()
                os.remove(addres + "\\" + "CROPCOM.DAT")
                os.rename(addres + "\\" + "tempCROPCOM.DAT",addres + "\\" + "CROPCOM.DAT")
        dlg = wx.MessageDialog(self, 'The parameters were Edited in CROPCOM.DAT', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy() 

    def OnButton5Button(self, parent):
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

        dlg = wx.MessageDialog(self, 'The parameters were sampled in CROPCOM.DAT', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy() 


    def OnButton4Button(self, parent):
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
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue()+ "\\"  + "inputList.txt", readCode)
        for lin1 in fList1:             
            s11=lin1.split(',')[1]         
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\Parameterization_Setup.inf",'r') as file:  
                data=file.readlines() 
            with open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s11 + ".Sufi2.SwatCup\\SUFI2.IN\\par_val.txt",'r') as file:
                data2=file.readlines()             
                   
            for NRun in range(1,int(parent.textCtrl3_4.GetValue())+1):  
                paramNum=1+int(data[0].split(',')[1])+int(data[0].split(',')[2])
                dataLHS=data2[NRun-1].split()
                #======================== Param01       
                if data[70].split(',')[0]=="Y":
                    if data[70].split(',')[1]=="vReplace":
                        Param01=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param01=format(float(data[70].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param01=format(float(data[70].split(',')[2]),'8.1f')  
                #======================== Param02       
                if data[71].split(',')[0]=="Y":
                    if data[71].split(',')[1]=="vReplace":
                        Param02=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param02=format(float(data[71].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param02=format(float(data[71].split(',')[2]),'8.1f') 
                #======================== Param03       
                if data[72].split(',')[0]=="Y":
                    if data[72].split(',')[1]=="vReplace":
                        Param03=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param03=format(float(data[72].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param03=format(float(data[72].split(',')[2]),'8.2f')         
                #======================== Param04       
                if data[73].split(',')[0]=="Y":
                    if data[72].split(',')[73]=="vReplace":
                        Param04=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param04=format(float(data[73].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param04=format(float(data[73].split(',')[2]),'8.1f')                  
                #======================== Param05       
                if data[74].split(',')[0]=="Y":
                    if data[74].split(',')[1]=="vReplace":
                        Param05=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param05=format(float(data[74].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param05=format(float(data[74].split(',')[2]),'8.1f')         
                #======================== Param06       
                if data[75].split(',')[0]=="Y":
                    if data[75].split(',')[1]=="vReplace":
                        Param06=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param06=format(float(data[75].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param06=format(float(data[75].split(',')[2]),'8.1f')    
                #======================== Param07       
                if data[76].split(',')[0]=="Y":
                    if data[76].split(',')[1]=="vReplace":
                        Param07=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param07=format(float(data[76].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param07=format(float(data[76].split(',')[2]),'8.1f')                        
                #======================== Param08       
                if data[77].split(',')[0]=="Y":
                    if data[77].split(',')[1]=="vReplace":
                        Param08=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param08=format(float(data[77].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param08=format(float(data[77].split(',')[2]),'8.1f')                             
                #======================== Param09      
                if data[78].split(',')[0]=="Y":
                    if data[78].split(',')[1]=="vReplace":
                        Param09=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param09=format(float(data[78].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param09=format(float(data[78].split(',')[2]),'8.1f')    
                #======================== Param10       
                if data[79].split(',')[0]=="Y":
                    if data[79].split(',')[1]=="vReplace":
                        Param10=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param10=format(float(data[79].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param10=format(float(data[79].split(',')[2]),'8.1f')                        
                #======================== Param11       
                if data[80].split(',')[0]=="Y":
                    if data[80].split(',')[1]=="vReplace":
                        Param11=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param11=format(float(data[80].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param11=format(float(data[80].split(',')[2]),'8.1f')                                                                                            
                #======================== Param12      
                if data[81].split(',')[0]=="Y":
                    if data[81].split(',')[1]=="vReplace":
                        Param12=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param12=format(float(data[81].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param12=format(float(data[81].split(',')[2]),'8.1f')          
                #======================== Param13       
                if data[82].split(',')[0]=="Y":
                    if data[82].split(',')[1]=="vReplace":
                        Param13=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param13=format(float(data[82].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param13=format(float(data[82].split(',')[2]),'8.1f')          
                #======================== Param14       
                if data[83].split(',')[0]=="Y":
                    if data[83].split(',')[1]=="vReplace":
                        Param14=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param14=format(float(data[83].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param14=format(float(data[83].split(',')[2]),'8.1f')          
                #======================== Param15       
                if data[84].split(',')[0]=="Y":
                    if data[84].split(',')[1]=="vReplace":
                        Param15=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param15=format(float(data[84].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param15=format(float(data[84].split(',')[2]),'8.1f')          
                #======================== Param16       
                if data[85].split(',')[0]=="Y":
                    if data[85].split(',')[1]=="vReplace":
                        Param16=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param16=format(float(data[85].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param16=format(float(data[85].split(',')[2]),'8.2f')          
                #======================== Param17       
                if data[86].split(',')[0]=="Y":
                    if data[86].split(',')[1]=="vReplace":
                        Param17=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        Param17=format(float(data[86].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    Param17=format(float(data[86].split(',')[2]),'8.3f')          
                #======================== Param18       
                if data[87].split(',')[0]=="Y":
                    if data[87].split(',')[1]=="vReplace":
                        Param18=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param18=format(float(data[87].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param18=format(float(data[87].split(',')[2]),'8.1f')          
                #======================== Param19       
                if data[88].split(',')[0]=="Y":
                    if data[88].split(',')[1]=="vReplace":
                        Param19=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param19=format(float(data[88].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param19=format(float(data[88].split(',')[2]),'8.1f')          
                #======================== Param20       
                if data[89].split(',')[0]=="Y":
                    if data[89].split(',')[1]=="vReplace":
                        Param20=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param20=format(float(data[89].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param20=format(float(data[89].split(',')[2]),'8.1f')          
                #======================== Param21       
                if data[90].split(',')[0]=="Y":
                    if data[90].split(',')[1]=="vReplace":
                        Param21=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param21=format(float(data[90].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param21=format(float(data[90].split(',')[2]),'8.1f')          
                #======================== Param22       
                if data[91].split(',')[0]=="Y":
                    if data[91].split(',')[1]=="vReplace":
                        Param22=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        Param22=format(float(data[91].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    Param22=format(float(data[91].split(',')[2]),'8.4f')          
                #======================== Param23       
                if data[92].split(',')[0]=="Y":
                    if data[92].split(',')[1]=="vReplace":
                        Param23=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param23=format(float(data[92].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param23=format(float(data[92].split(',')[2]),'8.1f')          
                #======================== Param24       
                if data[93].split(',')[0]=="Y":
                    if data[93].split(',')[1]=="vReplace":
                        Param24=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param24=format(float(data[93].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param24=format(float(data[93].split(',')[2]),'8.1f')          
                #======================== Param25       
                if data[94].split(',')[0]=="Y":
                    if data[94].split(',')[1]=="vReplace":
                        Param25=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param25=format(float(data[94].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param25=format(float(data[94].split(',')[2]),'8.2f')          
                #======================== Param26       
                if data[95].split(',')[0]=="Y":
                    if data[95].split(',')[1]=="vReplace":
                        Param26=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param26=format(float(data[95].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param26=format(float(data[95].split(',')[2]),'8.2f')          
                #======================== Param27       
                if data[96].split(',')[0]=="Y":
                    if data[96].split(',')[1]=="vReplace":
                        Param27=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param27=format(float(data[96].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param27=format(float(data[96].split(',')[2]),'8.1f')          
                #======================== Param06       
                if data[97].split(',')[0]=="Y":
                    if data[97].split(',')[1]=="vReplace":
                        Param28=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param28=format(float(data[97].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param28=format(float(data[97].split(',')[2]),'8.2f')          
                #======================== Param29       
                if data[98].split(',')[0]=="Y":
                    if data[98].split(',')[1]=="vReplace":
                        Param29=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param29=format(float(data[98].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param29=format(float(data[98].split(',')[2]),'8.2f')          
                #======================== Param30       
                if data[99].split(',')[0]=="Y":
                    if data[99].split(',')[1]=="vReplace":
                        Param30=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param30=format(float(data[99].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param30=format(float(data[99].split(',')[2]),'8.1f')          
                #======================== Param31      
                if data[100].split(',')[0]=="Y":
                    if data[100].split(',')[1]=="vReplace":
                        Param31=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param31=format(float(data[100].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param31=format(float(data[100].split(',')[2]),'8.2f')          
                #======================== Param32       
                if data[101].split(',')[0]=="Y":
                    if data[101].split(',')[1]=="vReplace":
                        Param32=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        Param32=format(float(data[101].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    Param32=format(float(data[101].split(',')[2]),'8.3f')          
                #======================== Param33       
                if data[102].split(',')[0]=="Y":
                    if data[102].split(',')[1]=="vReplace":
                        Param33=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param33=format(float(data[102].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param33=format(float(data[102].split(',')[2]),'8.2f')          
                #======================== Param34       
                if data[103].split(',')[0]=="Y":
                    if data[103].split(',')[1]=="vReplace":
                        Param34=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param34=format(float(data[103].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param34=format(float(data[103].split(',')[2]),'8.2f')          
                #======================== Param35      
                if data[104].split(',')[0]=="Y":
                    if data[104].split(',')[1]=="vReplace":
                        Param35=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param35=format(float(data[104].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param35=format(float(data[104].split(',')[2]),'8.2f')          
                #======================== Param36       
                if data[105].split(',')[0]=="Y":
                    if data[105].split(',')[1]=="vReplace":
                        Param36=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param36=format(float(data[105].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param36=format(float(data[105].split(',')[2]),'8.2f')          
                #======================== Param37       
                if data[106].split(',')[0]=="Y":
                    if data[106].split(',')[1]=="vReplace":
                        Param37=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param37=format(float(data[106].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param37=format(float(data[106].split(',')[2]),'8.2f')          
                #======================== Param38       
                if data[107].split(',')[0]=="Y":
                    if data[107].split(',')[1]=="vReplace":
                        Param38=format(float(dataLHS[paramNum]),'8.4f')
                    else:
                        Param38=format(float(data[107].split(',')[2])*(1+float(dataLHS[paramNum])),'8.4f')
                    paramNum=paramNum+1
                else:
                    Param38=format(float(data[107].split(',')[2]),'8.4f')          
                #======================== Param39       
                if data[108].split(',')[0]=="Y":
                    if data[108].split(',')[1]=="vReplace":
                        Param39=format(float(dataLHS[paramNum]),'8.1f')
                    else:
                        Param39=format(float(data[108].split(',')[2])*(1+float(dataLHS[paramNum])),'8.1f')
                    paramNum=paramNum+1
                else:
                    Param39=format(float(data[108].split(',')[2]),'8.1f')          
                #======================== Param40       
                if data[109].split(',')[0]=="Y":
                    if data[109].split(',')[1]=="vReplace":
                        Param40=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param40=format(float(data[109].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param40=format(float(data[109].split(',')[2]),'8.2f')          
                #======================== Param41       
                if data[110].split(',')[0]=="Y":
                    if data[110].split(',')[1]=="vReplace":
                        Param41=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param41=format(float(data[110].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param41=format(float(data[110].split(',')[2]),'8.2f')          
                #======================== Param06       
                if data[111].split(',')[0]=="Y":
                    if data[111].split(',')[1]=="vReplace":
                        Param42=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param42=format(float(data[111].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param42=format(float(data[111].split(',')[2]),'8.2f')          
                #======================== Param43       
                if data[112].split(',')[0]=="Y":
                    if data[112].split(',')[1]=="vReplace":
                        Param43=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param43=format(float(data[112].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param43=format(float(data[112].split(',')[2]),'8.2f')          
                #======================== Param44       
                if data[113].split(',')[0]=="Y":
                    if data[113].split(',')[1]=="vReplace":
                        Param44=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param44=format(float(data[113].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param44=format(float(data[113].split(',')[2]),'8.2f')          
                #======================== Param45      
                if data[114].split(',')[0]=="Y":
                    if data[114].split(',')[1]=="vReplace":
                        Param45=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param45=format(float(data[114].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param45=format(float(data[114].split(',')[2]),'8.2f')          
                #======================== Param46       
                if data[115].split(',')[0]=="Y":
                    if data[115].split(',')[1]=="vReplace":
                        Param46=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param46=format(float(data[115].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param46=format(float(data[115].split(',')[2]),'8.2f')          
                #======================== Param47      
                if data[116].split(',')[0]=="Y":
                    if data[116].split(',')[1]=="vReplace":
                        Param47=format(float(dataLHS[paramNum]),'8.6f')
                    else:
                        Param47=format(float(data[116].split(',')[2])*(1+float(dataLHS[paramNum])),'8.6f')
                    paramNum=paramNum+1
                else:
                    Param47=format(float(data[116].split(',')[2]),'8.6f')          
                #======================== Param48      
                if data[117].split(',')[0]=="Y":
                    if data[117].split(',')[1]=="vReplace":
                        Param48=format(float(dataLHS[paramNum]),'8.6f')
                    else:
                        Param48=format(float(data[117].split(',')[2])*(1+float(dataLHS[paramNum])),'8.6f')
                    paramNum=paramNum+1
                else:
                    Param48=format(float(data[117].split(',')[2]),'8.6f')          
                #======================== Param49       
                if data[118].split(',')[0]=="Y":
                    if data[118].split(',')[1]=="vReplace":
                        Param49=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param49=format(float(data[118].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param49=format(float(data[118].split(',')[2]),'8.2f')          
                #======================== Param50       
                if data[119].split(',')[0]=="Y":
                    if data[119].split(',')[1]=="vReplace":
                        Param50=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param50=format(float(data[119].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param50=format(float(data[119].split(',')[2]),'8.2f')          
                #======================== Param51       
                if data[120].split(',')[0]=="Y":
                    if data[120].split(',')[1]=="vReplace":
                        Param51=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param51=format(float(data[120].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param51=format(float(data[120].split(',')[2]),'8.2f')          
                #======================== Param52       
                if data[121].split(',')[0]=="Y":
                    if data[121].split(',')[1]=="vReplace":
                        Param52=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param52=format(float(data[121].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param52=format(float(data[121].split(',')[2]),'8.2f')               
                #======================== Param53       
                if data[122].split(',')[0]=="Y":
                    if data[122].split(',')[1]=="vReplace":
                        Param53=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param53=format(float(data[122].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param53=format(float(data[122].split(',')[2]),'8.2f')               
                #======================== Param54       
                if data[123].split(',')[0]=="Y":
                    if data[123].split(',')[1]=="vReplace":
                        Param54=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param54=format(float(data[123].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param54=format(float(data[123].split(',')[2]),'8.2f')               
                #======================== Param55       
                if data[124].split(',')[0]=="Y":
                    if data[124].split(',')[1]=="vReplace":
                        Param55=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param55=format(float(data[124].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param55=format(float(data[124].split(',')[2]),'8.2f')               
                #======================== Param56       
                if data[125].split(',')[0]=="Y":
                    if data[125].split(',')[1]=="vReplace":
                        Param56=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param56=format(float(data[125].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param56=format(float(data[125].split(',')[2]),'8.2f')               
                #======================== Param57       
                if data[126].split(',')[0]=="Y":
                    if data[126].split(',')[1]=="vReplace":
                        Param57=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param57=format(float(data[126].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param57=format(float(data[126].split(',')[2]),'8.2f')               
                #======================== Param58       
                if data[127].split(',')[0]=="Y":
                    if data[127].split(',')[1]=="vReplace":
                        Param58=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param58=format(float(data[127].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param58=format(float(data[127].split(',')[2]),'8.2f')               
                #======================== Param59       
                if data[128].split(',')[0]=="Y":
                    if data[128].split(',')[1]=="vReplace":
                        Param59=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param59=format(float(data[128].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param59=format(float(data[128].split(',')[2]),'8.2f')               
                #======================== Param60      
                if data[129].split(',')[0]=="Y":
                    if data[129].split(',')[1]=="vReplace":
                        Param60=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param60=format(float(data[129].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param60=format(float(data[129].split(',')[2]),'8.2f')               
                #======================== Param61       
                if data[130].split(',')[0]=="Y":
                    if data[130].split(',')[1]=="vReplace":
                        Param61=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param61=format(float(data[130].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param61=format(float(data[130].split(',')[2]),'8.2f')               
                #======================== Param62       
                if data[131].split(',')[0]=="Y":
                    if data[131].split(',')[1]=="vReplace":
                        Param62=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param62=format(float(data[131].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param62=format(float(data[131].split(',')[2]),'8.2f')               
                #======================== Param63       
                if data[132].split(',')[0]=="Y":
                    if data[132].split(',')[1]=="vReplace":
                        Param63=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param63=format(float(data[132].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param63=format(float(data[132].split(',')[2]),'8.2f')              
                #======================== Param64       
                if data[133].split(',')[0]=="Y":
                    if data[133].split(',')[1]=="vReplace":
                        Param64=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param64=format(float(data[133].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param64=format(float(data[133].split(',')[2]),'8.2f')              
                #======================== Param65       
                if data[134].split(',')[0]=="Y":
                    if data[134].split(',')[1]=="vReplace":
                        Param65=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param65=format(float(data[134].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param65=format(float(data[134].split(',')[2]),'8.2f')              
                #======================== Param66       
                if data[135].split(',')[0]=="Y":
                    if data[135].split(',')[1]=="vReplace":
                        Param66=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param66=format(float(data[135].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param66=format(float(data[135].split(',')[2]),'8.2f')              
                #======================== Param67       
                if data[136].split(',')[0]=="Y":
                    if data[136].split(',')[1]=="vReplace":
                        Param67=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param67=format(float(data[136].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param67=format(float(data[136].split(',')[2]),'8.2f')              
                #======================== Param68      
                if data[137].split(',')[0]=="Y":
                    if data[137].split(',')[1]=="vReplace":
                        Param68=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param68=format(float(data[137].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param68=format(float(data[137].split(',')[2]),'8.2f')              
                #======================== Param69       
                if data[138].split(',')[0]=="Y":
                    if data[138].split(',')[1]=="vReplace":
                        Param69=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param69=format(float(data[138].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param69=format(float(data[138].split(',')[2]),'8.2f')              
                #======================== Param70      
                if data[139].split(',')[0]=="Y":
                    if data[139].split(',')[1]=="vReplace":
                        Param70=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param70=format(float(data[139].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param70=format(float(data[139].split(',')[2]),'8.2f')              
                #======================== Param71      
                if data[140].split(',')[0]=="Y":
                    if data[140].split(',')[1]=="vReplace":
                        Param71=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param71=format(float(data[140].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param71=format(float(data[140].split(',')[2]),'8.2f')              
                #======================== Param72      
                if data[141].split(',')[0]=="Y":
                    if data[141].split(',')[1]=="vReplace":
                        Param72=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param72=format(float(data[141].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param72=format(float(data[141].split(',')[2]),'8.2f')              
                #======================== Param73      
                if data[142].split(',')[0]=="Y":
                    if data[142].split(',')[1]=="vReplace":
                        Param73=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param73=format(float(data[142].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param73=format(float(data[142].split(',')[2]),'8.2f')              
                #======================== Param74      
                if data[143].split(',')[0]=="Y":
                    if data[143].split(',')[1]=="vReplace":
                        Param74=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param74=format(float(data[143].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param74=format(float(data[143].split(',')[2]),'8.2f')              
                #======================== Param75     
                if data[144].split(',')[0]=="Y":
                    if data[144].split(',')[1]=="vReplace":
                        Param75=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param75=format(float(data[144].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param75=format(float(data[144].split(',')[2]),'8.2f')              
                #======================== Param76     
                if data[145].split(',')[0]=="Y":
                    if data[145].split(',')[1]=="vReplace":
                        Param76=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param76=format(float(data[145].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param76=format(float(data[145].split(',')[2]),'8.2f')              
                #======================== Param77      
                if data[146].split(',')[0]=="Y":
                    if data[146].split(',')[1]=="vReplace":
                        Param77=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param77=format(float(data[146].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param77=format(float(data[146].split(',')[2]),'8.2f')              
                #======================== Param78      
                if data[147].split(',')[0]=="Y":
                    if data[147].split(',')[1]=="vReplace":
                        Param78=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param78=format(float(data[147].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param78=format(float(data[147].split(',')[2]),'8.2f')              
                #======================== Param79      
                if data[148].split(',')[0]=="Y":
                    if data[148].split(',')[1]=="vReplace":
                        Param79=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param79=format(float(data[148].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param79=format(float(data[148].split(',')[2]),'8.2f')              
                #======================== Param80      
                if data[149].split(',')[0]=="Y":
                    if data[149].split(',')[1]=="vReplace":
                        Param80=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param80=format(float(data[149].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param80=format(float(data[149].split(',')[2]),'8.2f')              
                #======================== Param81      
                if data[150].split(',')[0]=="Y":
                    if data[150].split(',')[1]=="vReplace":
                        Param81=format(float(dataLHS[paramNum]),'8.3f')
                    else:
                        Param81=format(float(data[150].split(',')[2])*(1+float(dataLHS[paramNum])),'8.3f')
                    paramNum=paramNum+1
                else:
                    Param81=format(float(data[150].split(',')[2]),'8.3f')          
                #======================== Param82      
                if data[151].split(',')[0]=="Y":
                    if data[151].split(',')[1]=="vReplace":
                        Param82=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param82=format(float(data[151].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param82=format(float(data[151].split(',')[2]),'8.2f')          
                #======================== Param83      
                if data[152].split(',')[0]=="Y":
                    if data[152].split(',')[1]=="vReplace":
                        Param83=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param83=format(float(data[152].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param83=format(float(data[152].split(',')[2]),'8.2f')          
                #======================== Param84      
                if data[153].split(',')[0]=="Y":
                    if data[153].split(',')[1]=="vReplace":
                        Param84=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param84=format(float(data[153].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param84=format(float(data[153].split(',')[2]),'8.2f')          
                #======================== Param85      
                if data[154].split(',')[0]=="Y":
                    if data[154].split(',')[1]=="vReplace":
                        Param85=format(float(dataLHS[paramNum]),'8.2f')
                    else:
                        Param85=format(float(data[154].split(',')[2])*(1+float(dataLHS[paramNum])),'8.2f')
                    paramNum=paramNum+1
                else:
                    Param85=format(float(data[154].split(',')[2]),'8.2f') 
                txtlin1=Param01+Param02+Param03+Param04+Param05+Param06+Param07+Param08+Param09+Param10
                txtlin2=Param11+Param12+Param13+Param14+Param15+Param16+Param17+Param18+Param19+Param20 
                txtlin3=Param21+Param22+Param23+Param24+Param25+Param26+Param27+Param28+Param29+Param30 
                txtlin4=Param31+Param32+Param33+Param34+Param35+Param36+Param37+Param38+Param39+Param40 
                txtlin5=Param41+Param42+Param43+Param44+Param45+Param46+Param47+Param48+Param49+Param50 
                txtlin6=Param51+Param52+Param53+Param54+Param55+Param56+Param57+Param58+Param59+Param60 
                txtlin7=Param61+Param62+Param63+Param64+Param65+Param66+Param67+Param68+Param69+Param70 
                txtlin8=Param71+Param72+Param73+Param74+Param75+Param76+Param77+Param78+Param79+Param80
                txtlin9=Param81+Param82+Param83+Param84+Param85       
                                                                                              
                addres=parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + "\\" + s11 + ".Sufi2.SwatCup\\RUN_" + str(NRun)
                ftempcrop= open(addres + "\\" + "tempParam0810.DAT", "w")                
                fcrop= open(addres + "\\" + "PARM0810.DAT", readCode)
                loop=1
                for txlin in fcrop:
                    if loop==31:
                        txlin=txtlin1 + '\n'
                    if loop==32:
                        txlin=txtlin2+ '\n'
                    if loop==33:
                        txlin=txtlin3 + '\n'                   
                    if loop==34:
                        txlin=txtlin4+ '\n'                    
                    if loop==35:
                        txlin=txtlin5+ '\n'                    
                    if loop==36:
                        txlin=txtlin6+ '\n'
                    if loop==37:
                        txlin=txtlin7 + '\n'                                           
                    if loop==38:
                        txlin=txtlin8 + '\n'                   
                    if loop==39:
                        txlin=txtlin9  + '\n'                  
                    loop=loop+1
                    ftempcrop.write(txlin)
                ftempcrop.close()
                fcrop.close()
                os.remove(addres + "\\" + "PARM0810.DAT")
                os.rename(addres + "\\" + "tempParam0810.DAT",addres + "\\" + "PARM0810.DAT")        

        dlg = wx.MessageDialog(self, 'The parameters were sampled in CROPCOM.DAT', 'Simulation process', wx.OK | wx.ICON_INFORMATION)
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
###############################################################################