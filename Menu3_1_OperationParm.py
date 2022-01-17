#Boa:Dialog:Dialog1

import wx, os, shutil
import subprocess, stat
import numpy as np
import platform

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1,  wxID_DIALOG1STATICTEXTbar2, 
 
 wxID_DIALOG1CHECKBOX1,wxID_DIALOG1CHECKBOX2,wxID_DIALOG1CHECKBOX3,wxID_DIALOG1CHECKBOX4,wxID_DIALOG1CHECKBOX5,wxID_DIALOG1CHECKBOX7,wxID_DIALOG1CHECKBOX6,wxID_DIALOG1CHECKBOX8,wxID_DIALOG1CHECKBOX9,wxID_DIALOG1CHECKBOX10,
 wxID_DIALOG1CHECKBOX11,wxID_DIALOG1CHECKBOX12,wxID_DIALOG1CHECKBOX13,

wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2,wxID_DIALOG1STATICTEXT3,wxID_DIALOG1STATICTEXT4,wxID_DIALOG1STATICTEXT5,wxID_DIALOG1STATICTEXT6,wxID_DIALOG1STATICTEXT7,wxID_DIALOG1STATICTEXT8,
 wxID_DIALOG1STATICTEXT9,wxID_DIALOG1STATICTEXT10,

wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2, wxID_DIALOG1TEXTCTRL3, wxID_DIALOG1TEXTCTRL4, wxID_DIALOG1TEXTCTRL5, wxID_DIALOG1TEXTCTRL6, wxID_DIALOG1TEXTCTRL7, wxID_DIALOG1TEXTCTRL8,
wxID_DIALOG1TEXTCTRL9,wxID_DIALOG1TEXTCTRL10, wxID_DIALOG1TEXTCTRL11, wxID_DIALOG1TEXTCTRL12, wxID_DIALOG1TEXTCTRL13,

wxID_DIALOG1TEXTCTRL1_1,wxID_DIALOG1TEXTCTRL1_2, wxID_DIALOG1TEXTCTRL1_3, wxID_DIALOG1TEXTCTRL1_4, wxID_DIALOG1TEXTCTRL1_5, wxID_DIALOG1TEXTCTRL1_6, wxID_DIALOG1TEXTCTRL1_7, wxID_DIALOG1TEXTCTRL1_8,
wxID_DIALOG1TEXTCTRL1_9,wxID_DIALOG1TEXTCTRL1_10, wxID_DIALOG1TEXTCTRL1_11, wxID_DIALOG1TEXTCTRL1_12, wxID_DIALOG1TEXTCTRL1_13,

wxID_DIALOG1TEXTCTRL2_1,wxID_DIALOG1TEXTCTRL2_2, wxID_DIALOG1TEXTCTRL2_3, wxID_DIALOG1TEXTCTRL2_4, wxID_DIALOG1TEXTCTRL2_5, wxID_DIALOG1TEXTCTRL2_6, wxID_DIALOG1TEXTCTRL2_7, wxID_DIALOG1TEXTCTRL2_8,
wxID_DIALOG1TEXTCTRL2_9,wxID_DIALOG1TEXTCTRL2_10, wxID_DIALOG1TEXTCTRL2_11, wxID_DIALOG1TEXTCTRL2_12, wxID_DIALOG1TEXTCTRL2_13, 

wxID_DIALOG2COMBOBOX1_1,wxID_DIALOG2COMBOBOX1_2,wxID_DIALOG2COMBOBOX1_3,wxID_DIALOG2COMBOBOX1_4,wxID_DIALOG2COMBOBOX1_5,wxID_DIALOG2COMBOBOX1_6,wxID_DIALOG2COMBOBOX1_7,wxID_DIALOG2COMBOBOX1_8,
wxID_DIALOG2COMBOBOX1_9,wxID_DIALOG2COMBOBOX1_10,wxID_DIALOG2COMBOBOX1_11,wxID_DIALOG2COMBOBOX1_12,wxID_DIALOG2COMBOBOX1_13,

wxID_DIALOG1TEXTCTRL4_1,wxID_DIALOG1TEXTCTRL4_2,wxID_DIALOG1TEXTCTRL4_3, wxID_DIALOG1TEXTCTRL4_4,wxID_DIALOG1STATICTEXT4_1,wxID_DIALOG1STATICTEXT4_2,wxID_DIALOG1STATICTEXT4_3,wxID_DIALOG1STATICTEXT4_4,] = [wx.NewId() for _init_ctrls in range(86)]

class Dialog1(wx.Dialog):
    def _init_coll_flexGridSizer1_Items(self, parent):
        parent.AddWindow(self.staticText1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddWindow(self.staticText3, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4, 0, border=0, flag=0)
        parent.AddWindow(self.staticText5, 0, border=0, flag=0)
        parent.AddWindow(self.staticText6, 0, border=0, flag=0)
        parent.AddWindow(self.staticText7, 0, border=0, flag=0)
        parent.AddWindow(self.staticText8, 0, border=0, flag=0)
        parent.AddWindow(self.staticText9, 0, border=0, flag=0)
        parent.AddWindow(self.staticText10, 0, border=0, flag=0)

    def _init_coll_flexGridSizer5_Items(self, parent):  
        parent.AddWindow(self.staticTextbar2, 0, border=0, flag=0) 

    def _init_coll_flexGridSizer2_Items(self, parent):
        # generated method, don't edit
        parent.AddWindow(self.checkBox1, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_1, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox2, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_2, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox3, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_3, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox4, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_4, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox5, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_5, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl5, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_5, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_5, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox6, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_6, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl6, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_6, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_6, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox7, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_7, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl7, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_7, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_7, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox8, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_8, 0, border=0, flag=0)        
        parent.AddWindow(self.textCtrl8, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_8, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_8, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox9, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_9, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl9, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_9, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_9, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox10, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_10, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl10, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_10, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_10, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox11, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_11, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl11, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_11, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_11, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox12, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_12, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl12, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_12, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_12, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox13, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_13, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl13, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_13, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_13, 0, border=0, flag=0)
                            
    def _init_coll_flexGridSizer3_Items(self, parent):
        # generated method, don't edit        
        parent.AddWindow(self.button1, 0, border=0, flag=0)

    def _init_coll_flexGridSizer4_Items(self, parent):
        # generated method, don't edit        
        parent.AddWindow(self.staticText4_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4_2, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4_3, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4_4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4_4, 0, border=0, flag=0)        
        parent.AddWindow(self.staticText4_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl4_1, 0, border=0, flag=0)
                        
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer4, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer5, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=25, hgap=0, rows=25, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=10, hgap=0, rows=25, vgap=0)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=10, hgap=0, rows=25, vgap=0)
        self.flexGridSizer4 = wx.FlexGridSizer(cols=6, hgap=0, rows=25, vgap=0)
        self.flexGridSizer5 = wx.FlexGridSizer(cols=4, hgap=0, rows=25, vgap=0)
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3)
        self._init_coll_flexGridSizer4_Items(self.flexGridSizer4)
        self._init_coll_flexGridSizer5_Items(self.flexGridSizer5)
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,pos=wx.Point(10, 10), size=wx.Size(810, 250),style=wx.DEFAULT_DIALOG_STYLE,title=u'Operation parameters')
        self.SetClientSize(wx.Size(810, 250))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Create Parm',name='button1', parent=self, pos=wx.Point(0, 600),size=wx.Size(400, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,id=wxID_DIALOG1BUTTON1)

        self.staticText4_1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_1,label=u'Total number of parameters', parent=self,  pos=wx.Point(340, 0), size=wx.Size(190, 20), style=wx.ALIGN_LEFT)
        self.staticText4_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText4_1.SetForegroundColour(wx.Colour(0, 0, 255))  
        self.textCtrl4_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4_1,parent=self,  size=wx.Size(50, 20))
        
        self.staticText4_2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_2,label=u'Numbers of operation parameters', parent=self,  pos=wx.Point(330, 0), size=wx.Size(190, 20), style=wx.ALIGN_LEFT)
        self.staticText4_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText4_2.SetForegroundColour(wx.Colour(0, 0, 255))  
        self.textCtrl4_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4_2,parent=self,  size=wx.Size(50, 20))        

        self.staticText4_3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_3,label=u'Numbers of crop parameters', parent=self,  pos=wx.Point(330, 0), size=wx.Size(190, 20), style=wx.ALIGN_RIGHT)
        self.staticText4_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText4_3.SetForegroundColour(wx.Colour(0, 0, 255))  
        self.textCtrl4_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4_3,parent=self,  size=wx.Size(50, 20))          
        
        self.staticText4_4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4_1,label=u'Numbers of EPIC parameters', parent=self,  pos=wx.Point(330, 0), size=wx.Size(190, 20), style=wx.ALIGN_RIGHT)
        self.staticText4_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText4_4.SetForegroundColour(wx.Colour(0, 0, 255))  
        self.textCtrl4_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4_4,parent=self,  size=wx.Size(50, 20))              

################################################################################################
        self.comboBox1_1 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_1, parent=self, size=wx.Size(70, 21))
        self.comboBox1_2 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_2, parent=self, size=wx.Size(70, 21))
        self.comboBox1_3 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_3, parent=self, size=wx.Size(70, 21))
        self.comboBox1_4 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_4, parent=self, size=wx.Size(70, 21))
        self.comboBox1_5 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_5, parent=self, size=wx.Size(70, 21))
        self.comboBox1_6 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_6, parent=self, size=wx.Size(70, 21))
        self.comboBox1_7 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_7, parent=self, size=wx.Size(70, 21))
        self.comboBox1_8 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_8, parent=self, size=wx.Size(70, 21))
        self.comboBox1_9 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_9, parent=self, size=wx.Size(70, 21))
        self.comboBox1_10 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_10, parent=self, size=wx.Size(70, 21))
        self.comboBox1_11 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_11, parent=self, size=wx.Size(70, 21))
        self.comboBox1_12 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_12, parent=self, size=wx.Size(70, 21))
        self.comboBox1_13 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_13, parent=self, size=wx.Size(70, 21))
################################################################################################
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,label=u'OPR-Param', parent=self,  pos=wx.Point(310, 0), size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 128, 255))        
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,label=u'Method', parent=self, pos=wx.Point(310, 0), size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,label=u'Default',  parent=self,  size=wx.Size(80, 20),pos=wx.Point(310, 0),  style=wx.ALIGN_CENTRE)
        self.staticText3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText3.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4,label=u'Minimum', parent=self,  size=wx.Size(80, 20),pos=wx.Point(310, 0),  style=wx.ALIGN_CENTRE)
        self.staticText4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText4.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5,label=u'Maximum', name='staticText5', parent=self, size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText5.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6,label=u'OPR-Param', name='staticText6', parent=self, pos=wx.Point(310, 0), size=wx.Size(80, 20),style=wx.ALIGN_CENTRE)
        self.staticText6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText6.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7, label=u'Method', name='staticTex7', parent=self, size=wx.Size(80, 20),pos=wx.Point(310, 0),  style=wx.ALIGN_CENTRE)
        self.staticText7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText7.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8,label=u'Default', name='staticText8', parent=self,  size=wx.Size(80, 20), pos=wx.Point(310, 0), style=wx.ALIGN_CENTRE)
        self.staticText8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText8.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText9 = wx.StaticText(id=wxID_DIALOG1STATICTEXT9,label=u'Minimum', name='staticText9', parent=self, size=wx.Size(80, 20),pos=wx.Point(310, 0), style=wx.ALIGN_CENTRE)
        self.staticText9.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText9.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText10 = wx.StaticText(id=wxID_DIALOG1STATICTEXT10, label=u'Maximum', name='staticText10', parent=self, size=wx.Size(80, 20),pos=wx.Point(310, 0), style=wx.ALIGN_CENTRE)
        self.staticText10.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText10.SetForegroundColour(wx.Colour(0, 128, 255))
################################################################################################
        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1, label=u'Planting-Date', parent=self, size=wx.Size(100, 20))
        self.checkBox2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2, label=u'  PHU',  parent=self,size=wx.Size(100, 20))
        self.checkBox3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3, label=u'Planting-Density', parent=self, size=wx.Size(100, 20))
        self.checkBox4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4, label=u'  Pesticide',  parent=self, size=wx.Size(100, 20))
        self.checkBox5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5, label=u'Irrigation-APP',  parent=self,  size=wx.Size(100, 20))
        self.checkBox6 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX6, label=u'  Irrigation-Rate',parent=self, size=wx.Size(100, 20))
        self.checkBox7 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX7, label=u'FNP',parent=self, size=wx.Size(100, 20))
        self.checkBox8 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX8, label=u'  FMX',parent=self,  size=wx.Size(100, 20))
        self.checkBox9 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX9, label=u'BFT0',parent=self, size=wx.Size(100, 20))
        self.checkBox10 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX10, label=u'  P-APP',parent=self, size=wx.Size(100, 20))
        self.checkBox11 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX11, label=u'P-Rate', parent=self,  size=wx.Size(100, 20))
        self.checkBox12 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX12, label=u'  K-APP', parent=self, size=wx.Size(100, 20))
        self.checkBox13 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX13, label=u'K-Rate',parent=self, size=wx.Size(100, 20))
######################################################################        
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1,parent=self,  size=wx.Size(70, 20))
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2,parent=self,  size=wx.Size(70, 20))
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3,parent=self,  size=wx.Size(70, 20))
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4,parent=self,  size=wx.Size(70, 20))
        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL5,parent=self,  size=wx.Size(70, 20))
        self.textCtrl6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL6, parent=self, size=wx.Size(70, 20))
        self.textCtrl7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL7,parent=self,  size=wx.Size(70, 20))
        self.textCtrl8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL8,parent=self,  size=wx.Size(70, 20))
        self.textCtrl9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL9, parent=self, size=wx.Size(70, 20))
        self.textCtrl10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL10,parent=self, size=wx.Size(70, 20))
        self.textCtrl11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL11,parent=self, size=wx.Size(70, 20))
        self.textCtrl12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL12,parent=self, size=wx.Size(70, 20))
        self.textCtrl13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL13,parent=self,size=wx.Size(70, 20))

######################################################################        
        self.textCtrl1_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_1, parent=self, size=wx.Size(80, 20))
        self.textCtrl1_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_2,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_3,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_4,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_5, parent=self, size=wx.Size(80, 20))
        self.textCtrl1_6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_6,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_7, parent=self, size=wx.Size(80, 20))
        self.textCtrl1_8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_8,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_9,  parent=self, size=wx.Size(80, 20))
        self.textCtrl1_10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_10,  parent=self,size=wx.Size(80, 20))
        self.textCtrl1_11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_11, parent=self, size=wx.Size(80, 20))
        self.textCtrl1_12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_12, parent=self, size=wx.Size(80, 20))
        self.textCtrl1_13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_13, parent=self,size=wx.Size(80, 20))
 
######################################################################        
        self.textCtrl2_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_1,parent=self, size=wx.Size(80, 20))
        self.textCtrl2_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_2, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_3, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_4, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_5, parent=self, size=wx.Size(80, 20))
        self.textCtrl2_6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_6, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_7, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_8, parent=self, size=wx.Size(80, 20))
        self.textCtrl2_9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_9, parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_10,parent=self, size=wx.Size(80, 20))
        self.textCtrl2_11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_11,parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_12,parent=self,  size=wx.Size(80, 20))
        self.textCtrl2_13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_13,parent=self, size=wx.Size(80, 20))
        
        #========================================================related to flexGridSizer12=============================================== 
        self.staticTextbar2 = wx.StaticText(id=wxID_DIALOG1STATICTEXTbar2, label=u'    ',name='staticTextbar3',parent=self, size=wx.Size(1300, 2),style=wx.ALIGN_CENTER)
        self.staticTextbar2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticTextbar2.SetBackgroundColour(wx.Colour(18, 18, 192))          
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

        TOP = ['rRelative', 'vReplace']
        self.comboBox1_1.SetItems(TOP)  
        self.comboBox1_2.SetItems(TOP)  
        self.comboBox1_3.SetItems(TOP)  
        self.comboBox1_4.SetItems(TOP)  
        self.comboBox1_5.SetItems(TOP)  
        self.comboBox1_6.SetItems(TOP)  
        self.comboBox1_7.SetItems(TOP)  
        self.comboBox1_8.SetItems(TOP)  
        self.comboBox1_9.SetItems(TOP)  
        self.comboBox1_10.SetItems(TOP)  
        self.comboBox1_11.SetItems(TOP)  
        self.comboBox1_12.SetItems(TOP)  
        self.comboBox1_13.SetItems(TOP)  
        
        fSetup = open('Parameterization_Setup.inf', readCode)

        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 1:
                self.textCtrl4_1.SetValue(txtLine.split(',')[0])
                self.textCtrl4_2.SetValue(txtLine.split(',')[1])
                self.textCtrl4_3.SetValue(txtLine.split(',')[2])        
                self.textCtrl4_4.SetValue(txtLine.split(',')[3])     
            
            if loopNum == 2:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox1.SetValue(True)
                else:
                    self.checkBox1.SetValue(False)
                self.comboBox1_1.SetValue(txtLine.split(',')[1])
                self.textCtrl1.SetValue(txtLine.split(',')[2])
                self.textCtrl1_1.SetValue(txtLine.split(',')[3])
                self.textCtrl2_1.SetValue(txtLine.split(',')[4])
            if loopNum == 3:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox2.SetValue(True)
                else:
                    self.checkBox2.SetValue(False)                
                self.comboBox1_2.SetValue(txtLine.split(',')[1])
                self.textCtrl2.SetValue(txtLine.split(',')[2])
                self.textCtrl1_2.SetValue(txtLine.split(',')[3])
                
                self.textCtrl2_2.SetValue(txtLine.split(',')[4])
            if loopNum == 4:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox3.SetValue(True)
                else:
                    self.checkBox3.SetValue(False)                
                self.comboBox1_3.SetValue(txtLine.split(',')[1])
                self.textCtrl3.SetValue(txtLine.split(',')[2])
                self.textCtrl1_3.SetValue(txtLine.split(',')[3])
                self.textCtrl2_3.SetValue(txtLine.split(',')[4])
            if loopNum == 5:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox4.SetValue(True)
                else:
                    self.checkBox4.SetValue(False)                
                self.comboBox1_4.SetValue(txtLine.split(',')[1])
                self.textCtrl4.SetValue(txtLine.split(',')[2])
                self.textCtrl1_4.SetValue(txtLine.split(',')[3])
                self.textCtrl2_4.SetValue(txtLine.split(',')[4])
            if loopNum == 6:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox5.SetValue(True)
                else:
                    self.checkBox5.SetValue(False)                
                self.comboBox1_5.SetValue(txtLine.split(',')[1])
                self.textCtrl5.SetValue(txtLine.split(',')[2])
                self.textCtrl1_5.SetValue(txtLine.split(',')[3])
                self.textCtrl2_5.SetValue(txtLine.split(',')[4])            
            if loopNum == 7:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox6.SetValue(True)
                else:
                    self.checkBox6.SetValue(False)                
                self.comboBox1_6.SetValue(txtLine.split(',')[1])
                self.textCtrl6.SetValue(txtLine.split(',')[2])
                self.textCtrl1_6.SetValue(txtLine.split(',')[3])
                self.textCtrl2_6.SetValue(txtLine.split(',')[4])                
            if loopNum == 8:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox7.SetValue(True)
                else:
                    self.checkBox7.SetValue(False)                
                self.comboBox1_7.SetValue(txtLine.split(',')[1])
                self.textCtrl7.SetValue(txtLine.split(',')[2])
                self.textCtrl1_7.SetValue(txtLine.split(',')[3])
                self.textCtrl2_7.SetValue(txtLine.split(',')[4])                                                    
            if loopNum == 9:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox8.SetValue(True)
                else:
                    self.checkBox8.SetValue(False)                
                self.comboBox1_8.SetValue(txtLine.split(',')[1])
                self.textCtrl8.SetValue(txtLine.split(',')[2])
                self.textCtrl1_8.SetValue(txtLine.split(',')[3])
                self.textCtrl2_8.SetValue(txtLine.split(',')[4])            
            if loopNum == 10:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox9.SetValue(True)
                else:
                    self.checkBox9.SetValue(False)                
                self.comboBox1_9.SetValue(txtLine.split(',')[1])
                self.textCtrl9.SetValue(txtLine.split(',')[2])
                self.textCtrl1_9.SetValue(txtLine.split(',')[3])
                self.textCtrl2_9.SetValue(txtLine.split(',')[4])            
            if loopNum == 11:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox10.SetValue(True)
                else:
                    self.checkBox10.SetValue(False)                
                self.comboBox1_10.SetValue(txtLine.split(',')[1])
                self.textCtrl10.SetValue(txtLine.split(',')[2])
                self.textCtrl1_10.SetValue(txtLine.split(',')[3])
                self.textCtrl2_10.SetValue(txtLine.split(',')[4])            
            if loopNum == 12:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox11.SetValue(True)
                else:
                    self.checkBox11.SetValue(False)                
                self.comboBox1_11.SetValue(txtLine.split(',')[1])
                self.textCtrl11.SetValue(txtLine.split(',')[2])
                self.textCtrl1_11.SetValue(txtLine.split(',')[3])
                self.textCtrl2_11.SetValue(txtLine.split(',')[4])                        
            if loopNum == 13:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox12.SetValue(True)
                else:
                    self.checkBox12.SetValue(False)                
                self.comboBox1_12.SetValue(txtLine.split(',')[1])
                self.textCtrl12.SetValue(txtLine.split(',')[2])
                self.textCtrl1_12.SetValue(txtLine.split(',')[3])
                self.textCtrl2_12.SetValue(txtLine.split(',')[4])            
            if loopNum == 14:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox13.SetValue(True)
                else:
                    self.checkBox13.SetValue(False)                
                self.comboBox1_13.SetValue(txtLine.split(',')[1])
                self.textCtrl13.SetValue(txtLine.split(',')[2])
                self.textCtrl1_13.SetValue(txtLine.split(',')[3])
                self.textCtrl2_13.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                              
            loopNum += 1
        fSetup.close()
    
    def OnDialog1Close(self, event):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep 
        with open('Parameterization_Setup.inf','r') as file:
            data=file.readlines()       
        OTHERdata=data[14:155]
        f = open('Parameterization_Setup.inf', 'w')  
        f.write(self.textCtrl4_1.GetValue() +',')
        f.write(self.textCtrl4_2.GetValue() +',')
        f.write(self.textCtrl4_3.GetValue() +',')
        f.write(self.textCtrl4_4.GetValue() +',\n')
        if self.checkBox1.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')
        f.write(self.comboBox1_1.GetValue()+',')
        f.write(self.textCtrl1.GetValue() +',')
        f.write(self.textCtrl1_1.GetValue()+',')
        f.write(self.textCtrl2_1.GetValue()+',\n')
        
        if self.checkBox2.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')       
        f.write(self.comboBox1_2.GetValue()+',')
        f.write(self.textCtrl2.GetValue() +',')
        f.write(self.textCtrl1_2.GetValue()+',')
        f.write(self.textCtrl2_2.GetValue()+',\n')

        if self.checkBox3.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')     
        f.write(self.comboBox1_3.GetValue()+',')
        f.write(self.textCtrl3.GetValue() +',')
        f.write(self.textCtrl1_3.GetValue()+',')
        f.write(self.textCtrl2_3.GetValue()+',\n')        
        
        if self.checkBox4.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')      
        f.write(self.comboBox1_4.GetValue()+',')
        f.write(self.textCtrl4.GetValue() +',')
        f.write(self.textCtrl1_4.GetValue()+',')
        f.write(self.textCtrl2_4.GetValue()+',\n')
        
        if self.checkBox5.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')      
        f.write(self.comboBox1_5.GetValue()+',')
        f.write(self.textCtrl5.GetValue() +',')
        f.write(self.textCtrl1_5.GetValue()+',')
        f.write(self.textCtrl2_5.GetValue()+',\n')                
                        
        if self.checkBox6.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_6.GetValue()+',')
        f.write(self.textCtrl6.GetValue() +',')
        f.write(self.textCtrl1_6.GetValue()+',')
        f.write(self.textCtrl2_6.GetValue()+',\n')                                        
        
        if self.checkBox7.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_7.GetValue()+',')
        f.write(self.textCtrl7.GetValue() +',')
        f.write(self.textCtrl1_7.GetValue()+',')
        f.write(self.textCtrl2_7.GetValue()+',\n')              
        
        if self.checkBox8.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')      
        f.write(self.comboBox1_8.GetValue()+',')
        f.write(self.textCtrl8.GetValue() +',')
        f.write(self.textCtrl1_8.GetValue()+',')
        f.write(self.textCtrl2_8.GetValue()+',\n')        
        
        if self.checkBox9.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')      
        f.write(self.comboBox1_9.GetValue()+',')
        f.write(self.textCtrl9.GetValue() +',')
        f.write(self.textCtrl1_9.GetValue()+',')
        f.write(self.textCtrl2_9.GetValue()+',\n')        
        
        if self.checkBox10.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')       
        f.write(self.comboBox1_10.GetValue()+',')
        f.write(self.textCtrl10.GetValue() +',')
        f.write(self.textCtrl1_10.GetValue()+',')
        f.write(self.textCtrl2_10.GetValue()+',\n')
        
        if self.checkBox11.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')       
        f.write(self.comboBox1_11.GetValue()+',')
        f.write(self.textCtrl11.GetValue() +',')
        f.write(self.textCtrl1_11.GetValue()+',')
        f.write(self.textCtrl2_11.GetValue()+',\n')                

        if self.checkBox12.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')       
        f.write(self.comboBox1_12.GetValue()+',')
        f.write(self.textCtrl12.GetValue() +',')
        f.write(self.textCtrl1_12.GetValue()+',')
        f.write(self.textCtrl2_12.GetValue()+',\n')                                
                                                                
        if self.checkBox13.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')       
        f.write(self.comboBox1_13.GetValue()+',')
        f.write(self.textCtrl13.GetValue() +',')
        f.write(self.textCtrl1_13.GetValue()+',')
        f.write(self.textCtrl2_13.GetValue()+',\n') 
                                                                                                                                                                                                                                                                                                           
        for i in range(0, 141):
            f.write(OTHERdata[i])        
        f.close()
        self.Destroy()

    def OnButton1Button(self, event):
        ### Write the par_inf.sf2 and Create the parameters sample
        ### Setting for different OS
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep        
        ### Inherit attributes from parent class        
        parent = self.GetParent()
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\inputList.txt", readCode)       
        for lin1 in fList1: 
            s1=lin1.split(',')[1]
            if os.path.isdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 + ".Sufi2.SwatCup\\" + '\\SUFI2.IN') == True:
                 shutil.rmtree(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 + ".Sufi2.SwatCup\\" + '\\SUFI2.IN') 
            os.mkdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 + ".Sufi2.SwatCup\\" +'\\SUFI2.IN') 
             
            if os.path.isdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 + ".Sufi2.SwatCup\\" + '\\Echo') == False:
                os.mkdir(parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 + ".Sufi2.SwatCup\\"+ '\\Echo')
                
            src=parent.textCtrl2.GetValue()+ "\\Database\\sufi2EXE"
            dst=parent.textCtrl2.GetValue()+ "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks=False, ignore=None)
                else:
                    shutil.copy2(s, d)   
                                  
            fSufi2Parm = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+'\\SUFI2.IN\\' + 'par_inf.txt', 'wb')            
            fSufi2Parm.write(self.textCtrl4_1.GetValue() + ' : Number of Parameters' + lineEnd)
            fSufi2Parm.write(parent.textCtrl3_4.GetValue() + ' : number of simulations' + lineEnd)
            fSufi2Parm.write('' + lineEnd)
            fSufi2Parm.write('' + lineEnd)
            
            fPar_Name = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+ '\\Par_Name.OUT', 'wb')
            counter=1
            if self.checkBox1.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_1.GetValue()[0] + '_Planting_date     ' + self.textCtrl1_1.GetValue() + '       ' + self.textCtrl2_1.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Planting_date\n" )
                counter=counter+1
            
            if self.checkBox2.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_2.GetValue()[0] + '_PHU     ' + self.textCtrl1_2.GetValue() + '       ' + self.textCtrl2_2.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PHU\n" )
                counter=counter+1            
                                
            if self.checkBox3.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_3.GetValue()[0] + '_Planting_density     ' + self.textCtrl1_3.GetValue() + '       ' + self.textCtrl2_3.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Planting_density \n" )
                counter=counter+1            
                           
            if self.checkBox4.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_4.GetValue()[0] + '_Pesticide    ' + self.textCtrl1_4.GetValue() + '       ' + self.textCtrl2_4.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Pesticide\n" )
                counter=counter+1            
                            
            if self.checkBox5.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_5.GetValue()[0]  + '_Irrigation_App     ' + self.textCtrl1_5.GetValue() + '       ' + self.textCtrl2_5.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Irrigation_App\n" )
                counter=counter+1            
                            
            if self.checkBox6.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_6.GetValue()[0]  + '_Irrigation_Rate     ' + self.textCtrl1_6.GetValue() + '       ' + self.textCtrl2_6.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Irrigation_Rate\n" )
                counter=counter+1            
                            
            if self.checkBox7.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_7.GetValue()[0]  + '_FNP     ' + self.textCtrl1_7.GetValue() + '       ' + self.textCtrl2_7.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FNP\n" )
                counter=counter+1            
                            
            if self.checkBox8.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_8.GetValue()[0]  + '_FMX     ' + self.textCtrl1_8.GetValue() + '       ' + self.textCtrl2_8.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FMX\n" )
                counter=counter+1            
                            
            if self.checkBox9.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_9.GetValue()[0]  + '_BFT0     ' + self.textCtrl1_9.GetValue() + '       ' + self.textCtrl2_9.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BFT0\n" )
                counter=counter+1             
                            
            if self.checkBox10.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_10.GetValue()[0]  + '_PAPP    ' + self.textCtrl1_10.GetValue() + '       ' + self.textCtrl2_10.GetValue() + lineEnd)        
                fPar_Name.write(str(counter) + " :PAPP\n" )
                counter=counter+1             
                            
            if self.checkBox11.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_11.GetValue()[0]  + '_PRate     ' + self.textCtrl1_11.GetValue() + '       ' + self.textCtrl2_11.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PRate \n" )
                counter=counter+1             
                            
            if self.checkBox12.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_12.GetValue()[0]  + '_KAPP     ' + self.textCtrl1_12.GetValue() + '       ' + self.textCtrl2_12.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :KAPP\n" )
                counter=counter+1             
                            
            if self.checkBox13.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_13.GetValue()[0] + '_KRate     ' + self.textCtrl1_13.GetValue() + '       ' + self.textCtrl2_13.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :KRate\n" )
                counter=counter+1                                         
            fSufi2Parm.close()
            fPar_Name.close()


        dlg = wx.MessageDialog(self, 'SUFI2 sampleing parameters have been created!', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()



    def OnButton3Button(self, event):
        event.Skip()

    def OnButton4Button(self, event):
        event.Skip()
