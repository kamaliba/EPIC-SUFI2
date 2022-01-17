#Boa:Frame:Frame1
import wx, os, shutil
import Menu1_0_addFunction,Menu1_1_AddcalibrationSettings,Menu1_2_PrintSettings,Menu1_0_General_Settings
import Menu2_0_OperationSchedualT1, Menu2_1_OperationSchedualT2
import Menu3_1_OperationParm,Menu3_2_CROPCOM,Menu3_3_PARM0810
import Menu4_0_SUFI2_preT1,Menu4_1_LinuxRun_T1,Menu4_2_LinuxRun_T2,Menu4_3_windowsRun_T1,Menu4_4_windowsRun_T2,Menu4_5_Extract

def create(parent):
    return Frame1(parent)
[wxID_FRAME1, wxID_FRAME1STATUSBAR1, wxID_FRAME1PANEL1,
 wxID_FRAME1STATICTEXTbar1,  wxID_FRAME1STATICTEXTbar2, wxID_FRAME1STATICTEXTbar3,wxID_FRAME1STATICTEXTbar4,wxID_FRAME1STATICTEXTbar5,
 
 wxID_FRAME1BUTTON1,wxID_FRAME1BUTTON2,wxID_FRAME1BUTTON3,wxID_FRAME1BUTTON4,
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2,  wxID_FRAME1STATICTEXT3,  wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3,  wxID_FRAME1TEXTCTRL4,
 
 wxID_FRAME1STATICTEXT1_1, wxID_FRAME1STATICTEXT1_2, wxID_FRAME1STATICTEXT1_3, wxID_FRAME1STATICTEXT1_4,
 wxID_FRAME1TEXTCTRL1_1, wxID_FRAME1TEXTCTRL1_2,wxID_FRAME1COMBOBOX1_1, wxID_FRAME1COMBOBOX1_2,
 
 wxID_FRAME1STATICTEXT3_1,wxID_FRAME1STATICTEXT3_2,wxID_FRAME1STATICTEXT3_3,wxID_FRAME1STATICTEXT3_4,wxID_FRAME1STATICTEXT3_5,wxID_FRAME1STATICTEXT3_6, wxID_FRAME1STATICTEXT3_7, wxID_FRAME1STATICTEXT3_8, wxID_FRAME1STATICTEXT3_9,  
 wxID_FRAME1TEXTCTRL3_1,wxID_FRAME1TEXTCTRL3_2, wxID_FRAME1TEXTCTRL3_3,wxID_FRAME1TEXTCTRL3_4,wxID_FRAME1TEXTCTRL3_5,wxID_FRAME1TEXTCTRL3_6,wxID_FRAME1TEXTCTRL3_7,wxID_FRAME1TEXTCTRL3_8,wxID_FRAME1TEXTCTRL3_9,
 wxID_FRAME1STATICBITMAP1 ] = [wx.NewId() for _init_ctrls in range(47)]

[wxID_FRAME1MENU1ITEMS0, wxID_FRAME1MENU1ITEMS1,wxID_FRAME1MENU1ITEMS2] = [wx.NewId() for _init_coll_menu1_Items in range(3)]
[wxID_FRAME1MENU2ITEMS0, wxID_FRAME1MENU2ITEMS1, wxID_FRAME1MENU2ITEMS2] = [wx.NewId() for _init_coll_menu2_Items in range(3)]
[wxID_FRAME1MENU3ITEMS0, wxID_FRAME1MENU3ITEMS1, wxID_FRAME1MENU3ITEMS2, wxID_FRAME1MENU3ITEMS3, wxID_FRAME1MENU3ITEMS4] = [wx.NewId() for _init_coll_menu3_Items in range(5)]

[wxID_FRAME1MENU4ITEMS0, wxID_FRAME1MENU4ITEMS1, wxID_FRAME1MENU4ITEMS2, wxID_FRAME1MENU4ITEMS3, wxID_FRAME1MENU4ITEMS4,wxID_FRAME1MENU4ITEMS5,wxID_FRAME1MENU4ITEMS6,wxID_FRAME1MENU4ITEMS7,wxID_FRAME1MENU4ITEMS8] = [wx.NewId() for _init_coll_menu4_Items in range(9)]
[wxID_FRAME1MENU5ITEMS0] = [wx.NewId() for _init_coll_menu5_Items in range(1)]
[wxID_FRAME1MENU6ITEMS0, wxID_FRAME1MENU6ITEMS1] = [wx.NewId() for _init_coll_menu6_Items in range(2)]
[wxID_FRAME1MENU7ITEMS0, wxID_FRAME1MENU7ITEMS1, wxID_FRAME1MENU7ITEMS2, wxID_FRAME1MENU7ITEMS3] = [wx.NewId() for _init_coll_menu7_Items in range(4)]


class Frame1(wx.Frame):    
    def _init_coll_flexGridSizer1_Items(self, parent):        
        # generated method, don't edit
        parent.AddWindow(self.staticText1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1, 0, border=0, flag=0)
        parent.AddWindow(self.button1, 0, border=0, flag=0)                  
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2, 0, border=0, flag=0)
        parent.AddWindow(self.button2, 0, border=0, flag=0)                           
        
    def _init_coll_flexGridSizer2_Items(self, parent):
        parent.AddWindow(self.staticTextbar1, 0, border=0, flag=0) 
                              
    def _init_coll_flexGridSizer3_Items(self, parent):               
        parent.AddWindow(self.staticText1_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText1_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_2, 0, border=0, flag=0)
        parent.AddWindow(self.staticText1_3, 0, border=0, flag=0)      
        parent.AddWindow(self.comboBox1_1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText1_4, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_2, 0, border=0, flag=0)
        
    def _init_coll_flexGridSizer4_Items(self, parent):
        parent.AddWindow(self.staticTextbar2, 0, border=0, flag=0) 

    def _init_coll_flexGridSizer5_Items(self, parent):
        parent.AddWindow(self.staticText3_1, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3_1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText3_2, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3_2, 0, border=0, flag=0)
        parent.AddWindow(self.staticText3_3, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3_3, 0, border=0, flag=0)
        parent.AddWindow(self.staticText3_4, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl3_4, 0, border=0, flag=0)                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    def _init_coll_boxSizer1_Items(self, parent):
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer4, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer5, 0, border=0, flag=0)        
        
    def _init_coll_menuBar1_Menus(self, parent):
        parent.Append(menu=self.menu1, title=u'General settings')
        parent.Append(menu=self.menu2, title=u'Operation settings')  
        parent.Append(menu=self.menu3, title=u'Parameterization')        
        parent.Append(menu=self.menu4, title=u'SUFI2 calibration')
        #parent.Append(menu=self.menu5, title=u'PHU')
        
    def _init_coll_menu1_Items(self, parent):
        parent.Append(help='', id=wxID_FRAME1MENU1ITEMS0, kind=wx.ITEM_NORMAL, text=u'Physiographic data')
        parent.Append(help='', id=wxID_FRAME1MENU1ITEMS1, kind=wx.ITEM_NORMAL,text=u'Calibration settings')  
        parent.Append(help='', id=wxID_FRAME1MENU1ITEMS2, kind=wx.ITEM_NORMAL,text=u'Printings settings')    
        self.Bind(wx.EVT_MENU, self.OnMenu1Items0Menu, id=wxID_FRAME1MENU1ITEMS0)
        self.Bind(wx.EVT_MENU, self.OnMenu1Items1Menu, id=wxID_FRAME1MENU1ITEMS1)
        self.Bind(wx.EVT_MENU, self.OnMenu1Items2Menu, id=wxID_FRAME1MENU1ITEMS2)

    def _init_coll_menu2_Items(self, parent):        
        parent.Append(help='', id=wxID_FRAME1MENU2ITEMS0, kind=wx.ITEM_NORMAL,text=u'OPS1')
        parent.Append(help='', id=wxID_FRAME1MENU2ITEMS1, kind=wx.ITEM_NORMAL,text=u'OPS2')
        #parent.Append(help='', id=wxID_FRAME1MENU2ITEMS2, kind=wx.ITEM_NORMAL,text=u'OPS3')
        self.Bind(wx.EVT_MENU, self.OnMenu2Items0Menu, id=wxID_FRAME1MENU2ITEMS0)
        self.Bind(wx.EVT_MENU, self.OnMenu2Items1Menu, id=wxID_FRAME1MENU2ITEMS1)
     #   self.Bind(wx.EVT_MENU, self.OnMenu2Items2Menu, id=wxID_FRAME1MENU2ITEMS2)

    def _init_coll_menu3_Items(self, parent): 
        #parent.Append(help='', id=wxID_FRAME1MENU3ITEMS0, kind=wx.ITEM_NORMAL, text=u'Parameterization.OPS1')
        parent.Append(help='', id=wxID_FRAME1MENU3ITEMS1, kind=wx.ITEM_NORMAL, text=u'Operation.OPS2')
        parent.Append(help='', id=wxID_FRAME1MENU3ITEMS2, kind=wx.ITEM_NORMAL, text=u'CROPCOM.OPS2')                       
        parent.Append(help='', id=wxID_FRAME1MENU3ITEMS3, kind=wx.ITEM_NORMAL, text=u'PARM0810.OPS2') 
        #self.Bind(wx.EVT_MENU, self.OnMenu3Items0Menu, id=wxID_FRAME1MENU3ITEMS0)
        self.Bind(wx.EVT_MENU, self.OnMenu3Items1Menu, id=wxID_FRAME1MENU3ITEMS1)
        self.Bind(wx.EVT_MENU, self.OnMenu3Items2Menu, id=wxID_FRAME1MENU3ITEMS2)
        self.Bind(wx.EVT_MENU, self.OnMenu3Items3Menu, id=wxID_FRAME1MENU3ITEMS3)                                                                                                                    
 
    def _init_coll_menu4_Items(self, parent):
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS0, kind=wx.ITEM_NORMAL,text=u'SUFI2.pre')
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS1, kind=wx.ITEM_NORMAL, text=u'SUFI2-RUN: Linux-OPS1')
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS2, kind=wx.ITEM_NORMAL,text=u'SUFI2-RUN: Linux-OPS2')
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS3, kind=wx.ITEM_NORMAL, text=u'SUFI2-RUN: Windows-OPS1')
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS4, kind=wx.ITEM_NORMAL,text=u'SUFI2-RUN: Windows-OPS2')                
        parent.Append(help='', id=wxID_FRAME1MENU4ITEMS5, kind=wx.ITEM_NORMAL, text=u'SUFI2.POST')
        self.Bind(wx.EVT_MENU, self.OnMenu4Items0Menu,id=wxID_FRAME1MENU4ITEMS0)
        self.Bind(wx.EVT_MENU, self.OnMenu4Items1Menu,id=wxID_FRAME1MENU4ITEMS1)
        self.Bind(wx.EVT_MENU, self.OnMenu4Items2Menu,id=wxID_FRAME1MENU4ITEMS2)
        self.Bind(wx.EVT_MENU, self.OnMenu4Items3Menu,id=wxID_FRAME1MENU4ITEMS3)
        self.Bind(wx.EVT_MENU, self.OnMenu4Items4Menu,id=wxID_FRAME1MENU4ITEMS4)
        self.Bind(wx.EVT_MENU, self.OnMenu4Items5Menu, id=wxID_FRAME1MENU4ITEMS5)
        
  #  def _init_coll_menu5_Items(self, parent):
    #    parent.Append(help='', id=wxID_FRAME1MENU5ITEMS0, kind=wx.ITEM_NORMAL,text=u'PHU calculation')
     #   self.Bind(wx.EVT_MENU, self.OnMenu5Items0Menu,id=wxID_FRAME1MENU5ITEMS0)
        
    def _init_coll_statusBar1_Fields(self, parent):
        parent.SetFieldsCount(1)
        parent.SetStatusText(number=0, text=u'Status')
        parent.SetStatusWidths([-1])

    def _init_utils(self):
        self.menuBar1 = wx.MenuBar()
        self.menuBar1.SetBackgroundColour(wx.Colour(255, 128, 0))
        self.menu1 = wx.Menu(title='')
        self.menu2 = wx.Menu(title='')
        self.menu3 = wx.Menu(title='')
        self.menu4 = wx.Menu(title='')
      #  self.menu5 = wx.Menu(title='')
        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menu1_Items(self.menu1)
        self._init_coll_menu2_Items(self.menu2)
        self._init_coll_menu3_Items(self.menu3)
        self._init_coll_menu4_Items(self.menu4)
     #   self._init_coll_menu5_Items(self.menu5)
                
    def _init_sizers(self):
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=3, hgap=0, rows=5, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=1, hgap=0, rows=5, vgap=2)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=4, hgap=0, rows=5, vgap=2)
        self.flexGridSizer4 = wx.FlexGridSizer(cols=1, hgap=0, rows=5, vgap=0)
        self.flexGridSizer5 = wx.FlexGridSizer(cols=4, hgap=0, rows=5, vgap=0)
        
        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3)
        self._init_coll_flexGridSizer4_Items(self.flexGridSizer4)
        self._init_coll_flexGridSizer5_Items(self.flexGridSizer5)       
        self.panel1.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,style=wx.CAPTION | wx.DEFAULT_FRAME_STYLE,title=u'EPIC+')
        self._init_utils()
        self.SetClientSize(wx.Size(560, 180))
        self.SetMenuBar(self.menuBar1)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)    

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1, name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)
        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, parent=self,pos=wx.Point(0, 0), size=wx.Size(643,824),style=wx.TAB_TRAVERSAL)    
######################################section1######################################
        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,label=u' Linux address',parent=self.panel1,  size=wx.Size(100, 20),style=wx.ALIGN_LEFT)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText1.SetAutoLayout(True)
        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1,parent=self.panel1, size=wx.Size(350, 21),style=0)
        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Browse', parent=self.panel1, pos=wx.Point(0, 600), size=wx.Size(000, 21), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Dir, id=wxID_FRAME1BUTTON1)  
                
        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,label=u' Windows address', parent=self.panel1, size=wx.Size(100, 20),style=wx.ALIGN_LEFT)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.staticText2.SetAutoLayout(True)
        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2,parent=self.panel1, size=wx.Size(350, 21),style=0)
        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Browse', name='button2', parent=self.panel1, pos=wx.Point(0, 600), size=wx.Size(100, 21), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Dir, id=wxID_FRAME1BUTTON2)                
#####################################################  Bar1##################################################### 
        self.staticTextbar1 = wx.StaticText(id=wxID_FRAME1STATICTEXTbar1,label=u'', parent=self.panel1, size=wx.Size(710, 2),style=wx.ALIGN_CENTER)
        self.staticTextbar1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticTextbar1.SetBackgroundColour(wx.Colour(128, 108, 192))
#################################################################################################################################################################                 
        self.staticText1_1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1_1,label=u' Project name', parent=self.panel1,size=wx.Size(100, 21),style=wx.ALIGN_LEFT)
        self.staticText1_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1_1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1_1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1_1,parent=self.panel1, size=wx.Size(130, 21),style=0)
        
        self.staticText1_2 = wx.StaticText(id=wxID_FRAME1STATICTEXT1_2,label=u'  Resolution', parent=self.panel1,size=wx.Size(140, 21),style=wx.ALIGN_LEFT)
        self.staticText1_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1_2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl1_2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1_2, parent=self.panel1, size=wx.Size(130, 21),style=0)

        self.staticText1_3 = wx.StaticText(id=wxID_FRAME1STATICTEXT1_3,label=u' Select area', parent=self.panel1,  size=wx.Size(100, 21),style=wx.ALIGN_LEFT)
        self.staticText1_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText1_3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.comboBox1_1 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX1_1, parent=self.panel1,  size=wx.Size(130, 21), style=0)      
                 
        self.staticText1_4 = wx.StaticText(id=wxID_FRAME1STATICTEXT1_4, label=u'  Select crop',  parent=self.panel1, size=wx.Size(140, 21),style=wx.ALIGN_LEFT)
        self.staticText1_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText1_4.SetForegroundColour(wx.Colour(0, 0, 255))
        self.comboBox1_2 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX1_2,  parent=self.panel1, size=wx.Size(130, 21), style=0)
#####################################################  Bar1##################################################### 
        self.staticTextbar2 = wx.StaticText(id=wxID_FRAME1STATICTEXTbar2,label=u'',  parent=self.panel1, size=wx.Size(720, 2),style=wx.ALIGN_CENTER)
        self.staticTextbar2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticTextbar2.SetBackgroundColour(wx.Colour(128, 128, 192))                                                                                                                                                                                                                                             
###################################################   flexgridsizer10           ################################################# 
        self.staticText3_1 = wx.StaticText(id=wxID_FRAME1STATICTEXT3_1,label=u' Start year', parent=self.panel1,  size=wx.Size(100, 20),style=wx.ALIGN_LEFT)
        self.staticText3_1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))  
        self.staticText3_1.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3_1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3_1,parent=self.panel1, size=wx.Size(130, 21),style=0) 
                                         
        self.staticText3_2 = wx.StaticText(id=wxID_FRAME1STATICTEXT3_2,label=u'  Number of years', parent=self.panel1,  size=wx.Size(140, 20),style=wx.ALIGN_LEFT)
        self.staticText3_2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman')) 
        self.staticText3_2.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3_2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3_2,parent=self.panel1, size=wx.Size(130, 21),style=0)                                                                                   

        self.staticText3_3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3_3,label=u' Warm-up years', parent=self.panel1,  size=wx.Size(100, 20),style=wx.ALIGN_LEFT)
        self.staticText3_3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman')) 
        self.staticText3_3.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3_3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3_3,parent=self.panel1, size=wx.Size(130, 21),style=0)      

        self.staticText3_4 = wx.StaticText(id=wxID_FRAME1STATICTEXT3_4,label=u'  Numbers of runs',  parent=self.panel1,  size=wx.Size(140, 20),style=wx.ALIGN_LEFT)
        self.staticText3_4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman')) 
        self.staticText3_4.SetForegroundColour(wx.Colour(0, 0, 255))
        self.textCtrl3_4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3_4,parent=self.panel1, size=wx.Size(130, 21),style=0)                
       
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
        area=[]
        crop=[]        
        fArea = open('areaSelect.inf', readCode)        
        while True:
            temp1 = fArea.readline()
            if temp1:
                if temp1 == "\n":
                    continue
                else:
                    temp2 = temp1.strip(os.linesep).split(';')[0][0:-1]
                    area.append(temp2)
            else:
                break
        fArea.close()
        self.comboBox1_1.SetItems(area)
        fCrop = open('cropSelect.inf', readCode)        
        while True:
            temp3 = fCrop.readline()
            if temp3:
                if temp3 == "\n":
                    continue
                else:
                    temp4 = temp3.strip(os.linesep)
                    crop.append(temp4)
            else:
                break
        fCrop.close()        
        
        self.comboBox1_2.SetItems(crop)  
                            
        fSetup = open('modelGUISetup.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 1:
                self.textCtrl1.SetValue(txtLine.strip(os.linesep))
            if loopNum == 2:
                self.textCtrl2.SetValue(txtLine.strip(os.linesep))
            if loopNum == 3:
                self.textCtrl1_1.SetValue(txtLine.strip(os.linesep))                
            if loopNum == 4:
                self.textCtrl1_2.SetValue(txtLine.strip(os.linesep))
            if loopNum == 5:                
                self.comboBox1_1.SetValue(txtLine.strip(os.linesep))
            if loopNum == 6:                
                self.comboBox1_2.SetValue(txtLine.strip(os.linesep))           
            if loopNum == 7:         
                self.textCtrl3_1.SetValue(txtLine.strip(os.linesep))
            if loopNum == 8:
                self.textCtrl3_2.SetValue(txtLine.strip(os.linesep))
            if loopNum == 9:
                self.textCtrl3_3.SetValue(txtLine.strip(os.linesep)) 
            if loopNum == 10:
                self.textCtrl3_4.SetValue(txtLine.strip(os.linesep))                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            loopNum += 1
        fSetup.close()
        
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
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            print "You chose %s" % dlg.GetPath()
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
        dlg = wx.DirDialog(self, "Choose a directory:")
        if dlg.ShowModal() == wx.ID_OK:
            print "You chose %s" % dlg.GetPath()
        self.textCtrl3.SetValue(dlg.GetPath())
        dlg.Destroy()         
        
    def OnButton4Dir(self, event):
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
        self.textCtrl4.SetValue(dlg.GetPath())
        dlg.Destroy() 
        
    def OnButton5Dir(self, event):
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
        self.textCtrl5.SetValue(dlg.GetPath())
        dlg.Destroy()                 
    def OnButton6Dir(self, event):
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
        self.textCtrl6.SetValue(dlg.GetPath())
        dlg.Destroy()                                 
    def OnButton7Dir(self, event):
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
        self.textCtrl7.SetValue(dlg.GetPath())
        dlg.Destroy()         
    
    def OnFrame1Close(self, event):        
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
        OTHERdata=data[10:14] 

        f = open('modelGUISetup.inf', 'w')        
        f.write(self.textCtrl1.GetValue() + lineEnd)
        f.write(self.textCtrl2.GetValue() + lineEnd)      
        f.write(self.textCtrl1_1.GetValue() + lineEnd)
        f.write(self.textCtrl1_2.GetValue() + lineEnd)
        f.write(self.comboBox1_1.GetValue() + lineEnd)
        f.write(self.comboBox1_2.GetValue() + lineEnd)
        f.write(self.textCtrl3_1.GetValue()+ lineEnd)
        f.write(self.textCtrl3_2.GetValue()+ lineEnd)  
        f.write(self.textCtrl3_3.GetValue()+ lineEnd)
        f.write(self.textCtrl3_4.GetValue()+ lineEnd)    
        for i in range(0, 4):
            f.write(OTHERdata[i])            
        f.close()
        self.Destroy()
#===================================================Menu1 functions       

    def OnMenu1Items0Menu(self, event):              
        dlg = Menu1_0_General_Settings.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
    
    def OnMenu1Items1Menu(self, event):              
        dlg = Menu1_1_AddcalibrationSettings.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnMenu1Items2Menu(self, event):              
        dlg = Menu1_2_PrintSettings.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
#===================================================Menu2 functions  
    def OnMenu2Items0Menu(self, event): 
        dlg = Menu2_0_OperationSchedualT1.Dialog2(self)                
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
            
    def OnMenu2Items1Menu(self, event):    
          dlg = Menu2_1_OperationSchedualT2.Dialog2(self) 
          try:
              dlg.ShowModal()
          finally:
              dlg.Destroy()
#===================================================Menu2 functions  
    def OnMenu3Items1Menu(self, event):
        ### Spatial map                
        dlg = Menu3_1_OperationParm.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnMenu3Items2Menu(self, event):
        ### Scatter map        
        dlg = Menu3_2_CROPCOM.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnMenu3Items3Menu(self, event):
        ### Scatter map        
        dlg = Menu3_3_PARM0810.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
#===================================================Menu4 functions                         
    def OnMenu4Items0Menu(self, event):
        ### Trade volume analysis        
        dlg = Menu4_0_SUFI2_preT1.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
    def OnMenu4Items1Menu(self, event):
        ### Trade volume analysis        
        dlg =Menu4_1_LinuxRun_T1.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
    def OnMenu4Items2Menu(self, event):
        ### Trade volume analysis        
        dlg =Menu4_2_LinuxRun_T2.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
                      
    def OnMenu4Items3Menu(self, event):
       ### IO-based analysis   
        dlg =Menu4_3_windowsRun_T1.Dialog1(self)     
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
            
    def OnMenu4Items4Menu(self, event):
        ### Trade volume analysis        
        dlg =Menu4_4_windowsRun_T2.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()            

    def OnMenu4Items5Menu(self, event):
        ### IO-based analysis        
        dlg =Menu4_5_Extract.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()


