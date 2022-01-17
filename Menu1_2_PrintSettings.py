#Boa:Dialog:Dialog1

import wx, os, shutil
import subprocess, stat
import numpy as np
import platform

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2,  wxID_DIALOG1CHECKBOX1_1, 
 wxID_DIALOG1STATICTEXT2_0, wxID_DIALOG1STATICTEXT2_00, wxID_DIALOG1CHECKBOX2_1,wxID_DIALOG1CHECKBOX2_2,wxID_DIALOG1CHECKBOX2_3,wxID_DIALOG1CHECKBOX2_4,wxID_DIALOG1CHECKBOX2_5,wxID_DIALOG1CHECKBOX2_6,wxID_DIALOG1CHECKBOX2_7,
 wxID_DIALOG1CHECKBOX2_8,wxID_DIALOG1CHECKBOX2_9,
 wxID_DIALOG1STATICTEXT3_0,  wxID_DIALOG1STATICTEXT3_00, wxID_DIALOG1CHECKBOX3_1,wxID_DIALOG1CHECKBOX3_2,wxID_DIALOG1CHECKBOX3_3,wxID_DIALOG1CHECKBOX3_4,wxID_DIALOG1CHECKBOX3_5,
 wxID_DIALOG1STATICTEXT4_0,  wxID_DIALOG1STATICTEXT4_00, wxID_DIALOG1CHECKBOX4_1,wxID_DIALOG1CHECKBOX4_2,wxID_DIALOG1CHECKBOX4_3,wxID_DIALOG1CHECKBOX4_4,wxID_DIALOG1CHECKBOX4_5,wxID_DIALOG1CHECKBOX4_6,wxID_DIALOG1CHECKBOX4_7,
 wxID_DIALOG1CHECKBOX4_8,wxID_DIALOG1CHECKBOX4_9, wxID_DIALOG1CHECKBOX4_10,wxID_DIALOG1CHECKBOX4_11,
 wxID_DIALOG1STATICTEXT5_0,  wxID_DIALOG1STATICTEXT5_00, wxID_DIALOG1CHECKBOX5_1,wxID_DIALOG1CHECKBOX5_2,wxID_DIALOG1CHECKBOX5_3
 ] = [wx.NewId() for _init_ctrls in range(40)]

class Dialog1(wx.Dialog):  
    def _init_coll_flexGridSizer1_Items(self, parent): 
        parent.AddWindow(self.checkBox1_1, 0, border=0, flag=0)      
       
    def _init_coll_flexGridSizer2_Items(self, parent):
        parent.AddWindow(self.staticText2_00, 0, border=0, flag=0)  
        parent.AddWindow(self.staticText2_0, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_1, 0, border=0, flag=0) 
        parent.AddWindow(self.checkBox2_2, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_3, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_4, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_5, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_6, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_7, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_8, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox2_9, 0, border=0, flag=0)

    def _init_coll_flexGridSizer3_Items(self, parent):
        parent.AddWindow(self.staticText3_00, 0, border=0, flag=0)  
        parent.AddWindow(self.staticText3_0, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox3_1, 0, border=0, flag=0) 
        parent.AddWindow(self.checkBox3_2, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox3_3, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox3_4, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox3_5, 0, border=0, flag=0)
        
    def _init_coll_flexGridSizer4_Items(self, parent):
        parent.AddWindow(self.staticText4_00, 0, border=0, flag=0)  
        parent.AddWindow(self.staticText4_0, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_1, 0, border=0, flag=0) 
        parent.AddWindow(self.checkBox4_2, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_3, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_4, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_5, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_6, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_7, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_8, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_9, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_10, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox4_11, 0, border=0, flag=0)

    def _init_coll_flexGridSizer5_Items(self, parent):
        parent.AddWindow(self.staticText5_00, 0, border=0, flag=0)  
        parent.AddWindow(self.staticText5_0, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox5_1, 0, border=0, flag=0) 
        parent.AddWindow(self.checkBox5_2, 0, border=0, flag=0)
        parent.AddWindow(self.checkBox5_3, 0, border=0, flag=0)                             
                                                                                                      
    def _init_coll_flexGridSizer6_Items(self, parent):
        parent.AddWindow(self.button1, 0, border=0, flag=0) 
               
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer4, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer5, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer6, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=1, rows=6, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        self.flexGridSizer4 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        self.flexGridSizer5 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        self.flexGridSizer6 = wx.FlexGridSizer(cols=2, hgap=2, rows=25, vgap=1)
        
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3)
        self._init_coll_flexGridSizer4_Items(self.flexGridSizer4) 
        self._init_coll_flexGridSizer5_Items(self.flexGridSizer5)
        self._init_coll_flexGridSizer6_Items(self.flexGridSizer6)        
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,  pos=wx.Point(10, 10), size=wx.Size(530, 480), style=wx.DEFAULT_DIALOG_STYLE, title=u'Printing settings')
        self.SetClientSize(wx.Size(530, 480))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)            
#======================================================related to flexGridSizer1  =============================================================================        
        self.checkBox1_1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1_1,  label=u'Standard Output', name='checkBox1_1', parent=self, size=wx.Size(200, 21), style=0)
        self.checkBox1_1.SetValue(False)
        self.checkBox1_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
#======================================================related to flexGridSizer2 =============================================================================          
        self.staticText2_0 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_0,label=u'          ', name='staticText2_0', parent=self,  size=wx.Size(250, 21),style=wx.ALIGN_LEFT)
        self.staticText2_0.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText2_0.SetForegroundColour(wx.Colour(0, 0, 255))        
        self.staticText2_00 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2_00,  label=u'Annual Output', name='checkBox2_00', parent=self, size=wx.Size(250, 20), style=wx.ALIGN_LEFT)
        self.staticText2_00.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        self.staticText2_00.SetForegroundColour(wx.Colour(0, 0, 255))
                        
        self.checkBox2_1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_1,  label=u'Annual cropman file (.ACM)', name='checkBox2_1', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_1.SetValue(False)
        self.checkBox2_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox2_2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_2,  label=u'Average Annual Summary (.SUM)', name='checkBox2_2', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_2.SetValue(False)
        self.checkBox2_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox2_3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_3,  label=u'Annual summary (.ANN)', name='checkBox2_3', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_3.SetValue(False)
        self.checkBox2_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
              
        self.checkBox2_4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_4,  label=u'Annual Annual Soil organic table (.ACN)', name='checkBox2_4', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_4.SetValue(False)
        self.checkBox2_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox2_5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_5,  label=u'Annual crop yield (.ACY)', name='checkBox2_5', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_5.SetValue(False)
        self.checkBox2_5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))                                                

        self.checkBox2_6 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_6,  label=u'Annual cost (.ACO)', name='checkBox2_6', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_6.SetValue(False)
        self.checkBox2_6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox2_7 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_7,  label=u'Annual biomass root weight (.ABR)', name='checkBox2_7', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_7.SetValue(False)
        self.checkBox2_7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox2_8 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_8,  label=u'Annual tree growth (.ATG)', name='checkBox2_8', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_8.SetValue(False)
        self.checkBox2_8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox2_9 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2_9,  label=u'Annual Pesticide (.APS)', name='checkBox2_8', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox2_9.SetValue(False)
        self.checkBox2_9.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
#======================================================related to flexGridSizer3 =============================================================================          
        self.staticText3_0 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3_0,label=u'          ', name='staticText3_0', parent=self,  size=wx.Size(250, 21),style=wx.ALIGN_LEFT)
        self.staticText3_0.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText3_0.SetForegroundColour(wx.Colour(0, 0, 255))        
        self.staticText3_00 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3_00,  label=u'Monthly Output', name='checkBox3_00', parent=self, size=wx.Size(250, 21), style=wx.ALIGN_LEFT)
        self.staticText3_00.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        self.staticText3_00.SetForegroundColour(wx.Colour(0, 0, 255))
                        
        self.checkBox3_1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3_1,  label=u'Monthly flipsim (.MFS)', name='checkBox3_1', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox3_1.SetValue(False)
        self.checkBox3_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox3_2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3_2,  label=u'Monthly Pesticide (.MPS)', name='checkBox3_2', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox3_2.SetValue(False)
        self.checkBox3_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox3_3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3_3,  label=u'Monthly cropman  (.MCM)', name='checkBox3_3', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox3_3.SetValue(False)
        self.checkBox3_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
              
        self.checkBox3_4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3_4,  label=u'Annual water cycle (.ABR)', name='checkBox3_4', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox3_4.SetValue(False)
        self.checkBox3_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox3_5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3_5,  label=u'Monthly Output to SWAT (.MSW)', name='checkBox3_5', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox3_5.SetValue(False)
        self.checkBox3_5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))                                                
#======================================================related to flexGridSizer4 =============================================================================          
        self.staticText4_0 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_0,label=u'          ', name='staticText4_0', parent=self,  size=wx.Size(250, 21),style=wx.ALIGN_LEFT)
        self.staticText4_0.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText4_0.SetForegroundColour(wx.Colour(0, 0, 255))        
        self.staticText4_00 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_00,  label=u'Daily Output', name='checkBox4_00', parent=self, size=wx.Size(250, 20), style=wx.ALIGN_LEFT)
        self.staticText4_00.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        self.staticText4_00.SetForegroundColour(wx.Colour(0, 0, 255))
                        
        self.checkBox4_1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_1,  label=u'Daily Hydrology (.DHY)', name='checkBox4_1', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_1.SetValue(False)
        self.checkBox4_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox4_2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_2,  label=u'Daily Pesticide (.DPS)', name='checkBox4_2', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_2.SetValue(False)
        self.checkBox4_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox4_3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_3,  label=u'Daily soil temperature (.DTP)', name='checkBox4_3', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_3.SetValue(False)
        self.checkBox4_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
              
        self.checkBox4_4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_4,  label=u'Daily crop stress (.DCS)', name='checkBox3_4', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_4.SetValue(False)
        self.checkBox4_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox4_5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_5,  label=u'Daily soil organic (.DCN)', name='checkBox4_5', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_5.SetValue(False)
        self.checkBox4_5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))                                                

        self.checkBox4_6 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_6,  label=u'Daily general table (.DGN)', name='checkBox4_6', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_6.SetValue(False)
        self.checkBox4_6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox4_7 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_7,  label=u'Daily Soil table(.DSL)', name='checkBox4_7', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_7.SetValue(False)
        self.checkBox4_7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox4_8 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_8,  label=u'Daily water cycle (.DWC)', name='checkBox4_8', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_8.SetValue(False)
        self.checkBox4_8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox4_9 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_9,  label=u'Daily (.DHS)', name='checkBox4_9', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_9.SetValue(False)
        self.checkBox4_9.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox4_10 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_10,  label=u'Daily grazing file (.DGZ)', name='checkBox4_10', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_10.SetValue(False)
        self.checkBox4_10.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox4_11 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4_11,  label=u'Daily soil water (.DWT)', name='checkBox4_11', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox4_11.SetValue(False)
        self.checkBox4_11.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
#======================================================related to flexGridSizer5 =============================================================================          
        self.staticText5_0 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5_0,label=u'          ', name='staticText5_0', parent=self,  size=wx.Size(250, 21),style=wx.ALIGN_LEFT)
        self.staticText5_0.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText5_0.SetForegroundColour(wx.Colour(0, 0, 255))        
        self.staticText5_00 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5_00,  label=u'General Data', name='checkBox5_00', parent=self, size=wx.Size(250, 20), style=wx.ALIGN_LEFT)
        self.staticText5_00.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        self.staticText5_00.SetForegroundColour(wx.Colour(0, 0, 255))
                        
        self.checkBox5_1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5_1,  label=u'Ending soil table (.SOT)', name='checkBox5_1', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox5_1.SetValue(False)
        self.checkBox5_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

        self.checkBox5_2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5_2,  label=u'Summeray Operation Cost (.SCO)', name='checkBox5_2', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox5_2.SetValue(False)
        self.checkBox5_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))
        
        self.checkBox5_3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5_3,  label=u'Organic C-N summary table (.SCN)', name='checkBox5_3', parent=self, size=wx.Size(250, 20), style=0)
        self.checkBox5_3.SetValue(False)
        self.checkBox5_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,u'Times New Roman'))

#======================================================related to flexGridSizer2 =============================================================================                                                                                                                                                                                                                                                  
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Edit PRINT0810.DAT', name='button1', parent=self,  size=wx.Size(200, 30), style=0)
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
        parent = self.GetParent()
        fSetup = open(parent.textCtrl2.GetValue() + '/PRINTSetup.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 1:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox1_1.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox1_1.SetValue(False)
            if loopNum == 2:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_1.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_1.SetValue(False)
            if loopNum == 3:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_2.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_2.SetValue(False)
            if loopNum == 4:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_1.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_1.SetValue(False)
            if loopNum == 5:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_2.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_2.SetValue(False)
            if loopNum == 6:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_1.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_1.SetValue(False)
            if loopNum == 7:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_2.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_2.SetValue(False)
            if loopNum == 8:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_3.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_3.SetValue(False)               
            if loopNum == 9:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox5_1.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox5_1.SetValue(False)         
            if loopNum == 10:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_3.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_3.SetValue(False)
            if loopNum == 11:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_3.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_3.SetValue(False)
            if loopNum == 12:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_4.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_4.SetValue(False)
            if loopNum == 13:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox5_2.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox5_2.SetValue(False) 
            if loopNum == 14:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_4.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_4.SetValue(False)
            if loopNum == 15:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_5.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_5.SetValue(False)                                              
            if loopNum == 16:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox5_3.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox5_3.SetValue(False)
            if loopNum == 17:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_6.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_6.SetValue(False)
            if loopNum == 18:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_11.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_11.SetValue(False)                                              
            if loopNum == 19:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_5.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_5.SetValue(False)
            if loopNum == 20:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_6.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_6.SetValue(False)
            if loopNum == 21:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_7.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_7.SetValue(False)                                              
            if loopNum == 22:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_5.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_5.SetValue(False)
            if loopNum == 23:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_4.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_4.SetValue(False)
            if loopNum == 24:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_8.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_8.SetValue(False)
            if loopNum == 25:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox3_5.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox3_5.SetValue(False)
            if loopNum == 26:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox2_9.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox2_9.SetValue(False)
            if loopNum == 27:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_8.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_8.SetValue(False)
            if loopNum == 28:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_9.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_9.SetValue(False)
            if loopNum == 29:
                if txtLine.strip(os.linesep) == '   1':
                    self.checkBox4_10.SetValue(True)
                if txtLine.strip(os.linesep) == '   0':
                    self.checkBox4_10.SetValue(False) 
            loopNum += 1
        fSetup.close()        
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
        fSetup = open(parent.textCtrl2.GetValue() + '/PRINTSetup.inf', 'w')
##################################################################        
        if self.checkBox1_1.GetValue() == True:
            txt1='   1'
        else:
            txt1='   0'        
        fSetup.write(txt1 +lineEnd)
        if self.checkBox2_1.GetValue() == True: 
            txt2='   1'
        else:
            txt2='   0'
        fSetup.write(txt2 +lineEnd)
        if self.checkBox2_2.GetValue() == True: 
            txt3='   1'
        else:
            txt3='   0'                        
        fSetup.write(txt3 +lineEnd)
        if self.checkBox4_1.GetValue() == True: 
            txt4='   1'
        else:
            txt4='   0'        
        fSetup.write(txt4 +lineEnd)
        if self.checkBox4_2.GetValue() == True: 
            txt5='   1'
        else:
            txt5='   0'         
        fSetup.write(txt5 +lineEnd)
        if self.checkBox3_1.GetValue() == True: 
            txt6='   1'
        else:
            txt6='   0'         
        fSetup.write(txt6 +lineEnd)
        if self.checkBox3_2.GetValue() == True: 
            txt7='   1'
        else:
            txt7='   0'      
        fSetup.write(txt7 +lineEnd)
        if self.checkBox2_3.GetValue() == True: 
            txt8='   1'
        else:
            txt8='   0'               
        fSetup.write(txt8 +lineEnd)
        if self.checkBox5_1.GetValue() == True: 
            txt9='   1'
        else:
            txt9='   0'                           
        fSetup.write(txt9 +lineEnd)
        if self.checkBox4_3.GetValue() == True: 
            txt10='   1'
        else:
            txt10='   0'               
        fSetup.write(txt10 +lineEnd)
        if self.checkBox3_3.GetValue() == True: 
            txt11='   1'
        else:
            txt11='   0'
        fSetup.write(txt11 +lineEnd)      
        if self.checkBox4_4.GetValue() == True: 
            txt12='   1'
        else:
            txt12='   0'            
        fSetup.write(txt12 +lineEnd)
        if self.checkBox5_2.GetValue() == True: 
            txt13='   1'
        else:
            txt13='   0'
        fSetup.write(txt13 +lineEnd)
        if self.checkBox2_4.GetValue() == True: 
            txt14='   1'
        else:
            txt14='   0'      
        fSetup.write(txt14 +lineEnd)       
        if self.checkBox4_5.GetValue() == True: 
            txt15='   1'
        else:
            txt15='   0'      
        fSetup.write(txt15 +lineEnd)
        if self.checkBox5_3.GetValue() == True: 
            txt16='   1'
        else:
            txt16='   0'      
        fSetup.write(txt16 +lineEnd)
        if self.checkBox4_6.GetValue() == True: 
            txt17='   1'
        else:
            txt17='   0'      
        fSetup.write(txt17 +lineEnd)
        if self.checkBox4_11.GetValue() == True: 
            txt18='   1'
        else:
            txt18='   0'
        fSetup.write(txt18 +lineEnd)  
        if self.checkBox2_5.GetValue() == True: 
            txt19='   1'
        else:
            txt19='   0'                  
        fSetup.write(txt19 +lineEnd)                              
        if self.checkBox2_6.GetValue() == True: 
            txt20='   1'
        else:
            txt20='   0'    
        fSetup.write(txt20 +lineEnd)    
        if self.checkBox4_7.GetValue() == True: 
            txt21='   1'
        else:
            txt21='   0'
        fSetup.write(txt21 +lineEnd)               
        if self.checkBox3_5.GetValue() == True: 
            txt22='   1'
        else:
            txt22='   0'
        fSetup.write(txt22 +lineEnd)  
        if self.checkBox3_4.GetValue() == True: 
            txt23='   1'
        else:
            txt23='   0'  
        fSetup.write(txt23 +lineEnd)
        if self.checkBox2_8.GetValue() == True: 
            txt24='   1'
        else:
            txt24='   0'                          
        fSetup.write(txt24 +lineEnd)
        if self.checkBox3_5.GetValue() == True: 
            txt25='   1'
        else:
            txt25='   0'  
        fSetup.write(txt25 +lineEnd)
        if self.checkBox2_9.GetValue() == True: 
            txt26='   1'
        else:
            txt26='   0'                                                                                                                                                              
        fSetup.write(txt26 +lineEnd)
        if self.checkBox4_9.GetValue() == True: 
            txt27='   1'
        else:
            txt27='   0'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        fSetup.write(txt27 +lineEnd)
        if self.checkBox4_9.GetValue() == True: 
            txt28='   1'
        else:
            txt28='   0'  
        fSetup.write(txt28 +lineEnd)                
        if self.checkBox4_10.GetValue() == True: 
            txt29='   1'
        else:
            txt29='   0'      
        fSetup.write(txt29 +lineEnd)
        fSetup.close()        
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\inputList.txt", readCode) 
        itrNUm= int(parent.textCtrl3_4.GetValue())
        for lin1 in fList1: 
            s1=lin1.split(',')[1]
            for i in range(1,itrNUm+1):
               fprnt1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\PRNT0810.DAT", readCode)
               ftmpprnt = open(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\TMPPRNT0810.DAT", 'w')
               loop=1
               for txtLine in fprnt1:
                   if loop== 15:
                       txtLine=txt1+txt2+txt3+txt4+txt5+txt6+txt7+txt8+txt9+txt10+txt11+txt12+txt13+txt14+txt15+txt16+txt17+txt18+txt19+txt20
                   if loop==16:
                       txt30=txtLine[36:61]
                       txtLine=txt21+txt22+txt23+txt24+txt25+txt26+txt27+txt28+txt29
                   ftmpprnt.write(txtLine.strip(os.linesep) + lineEnd)
                   loop=loop+1
               ftmpprnt.close()
               fprnt1.close()
               if os.path.isfile(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\PRNT0810.DAT"):
                   os.remove(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\PRNT0810.DAT")
               os.rename(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\TMPPRNT0810.DAT", parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue() + "\\" + s1 + ".Sufi2.SwatCup\\RUN_" + str(i) + "\\PRNT0810.DAT")
        dlg = wx.MessageDialog(self, 'Printing file was edited', 'Message', wx.OK | wx.ICON_INFORMATION)
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

