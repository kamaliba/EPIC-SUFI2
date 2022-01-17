#Boa:Dialog:Dialog1

import wx, os, shutil
import subprocess, stat
import numpy as np
import platform

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, 
 
 wxID_DIALOG1CHECKBOX1,wxID_DIALOG1CHECKBOX2,wxID_DIALOG1CHECKBOX3,wxID_DIALOG1CHECKBOX4,wxID_DIALOG1CHECKBOX5,wxID_DIALOG1CHECKBOX7,wxID_DIALOG1CHECKBOX6,wxID_DIALOG1CHECKBOX8,wxID_DIALOG1CHECKBOX9,wxID_DIALOG1CHECKBOX10,
 wxID_DIALOG1CHECKBOX11,wxID_DIALOG1CHECKBOX12,wxID_DIALOG1CHECKBOX13,wxID_DIALOG1CHECKBOX14,wxID_DIALOG1CHECKBOX15,wxID_DIALOG1CHECKBOX16,wxID_DIALOG1CHECKBOX17,wxID_DIALOG1CHECKBOX18,wxID_DIALOG1CHECKBOX19,wxID_DIALOG1CHECKBOX20,
 wxID_DIALOG1CHECKBOX21,wxID_DIALOG1CHECKBOX22,wxID_DIALOG1CHECKBOX23,wxID_DIALOG1CHECKBOX24,wxID_DIALOG1CHECKBOX25,wxID_DIALOG1CHECKBOX26,wxID_DIALOG1CHECKBOX27,wxID_DIALOG1CHECKBOX28,wxID_DIALOG1CHECKBOX29,wxID_DIALOG1CHECKBOX30, 
 wxID_DIALOG1CHECKBOX31,wxID_DIALOG1CHECKBOX32,wxID_DIALOG1CHECKBOX33,wxID_DIALOG1CHECKBOX34,wxID_DIALOG1CHECKBOX35,wxID_DIALOG1CHECKBOX36,wxID_DIALOG1CHECKBOX37,wxID_DIALOG1CHECKBOX38,wxID_DIALOG1CHECKBOX39,wxID_DIALOG1CHECKBOX40, 
 wxID_DIALOG1CHECKBOX41,wxID_DIALOG1CHECKBOX42,wxID_DIALOG1CHECKBOX43,wxID_DIALOG1CHECKBOX44, wxID_DIALOG1CHECKBOX45,wxID_DIALOG1CHECKBOX46,wxID_DIALOG1CHECKBOX47,wxID_DIALOG1CHECKBOX48,wxID_DIALOG1CHECKBOX49,wxID_DIALOG1CHECKBOX50,
 wxID_DIALOG1CHECKBOX51,wxID_DIALOG1CHECKBOX52,wxID_DIALOG1CHECKBOX53,wxID_DIALOG1CHECKBOX54,wxID_DIALOG1CHECKBOX55,wxID_DIALOG1CHECKBOX56,

wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2,wxID_DIALOG1STATICTEXT3,wxID_DIALOG1STATICTEXT4,wxID_DIALOG1STATICTEXT5,wxID_DIALOG1STATICTEXT6,wxID_DIALOG1STATICTEXT7,wxID_DIALOG1STATICTEXT8,wxID_DIALOG1STATICTEXT9,
 wxID_DIALOG1STATICTEXT9,wxID_DIALOG1STATICTEXT10,

 wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2, wxID_DIALOG1TEXTCTRL3, wxID_DIALOG1TEXTCTRL4, wxID_DIALOG1TEXTCTRL5, wxID_DIALOG1TEXTCTRL6, wxID_DIALOG1TEXTCTRL7, wxID_DIALOG1TEXTCTRL8,
wxID_DIALOG1TEXTCTRL9,wxID_DIALOG1TEXTCTRL10, wxID_DIALOG1TEXTCTRL11, wxID_DIALOG1TEXTCTRL12, wxID_DIALOG1TEXTCTRL13, wxID_DIALOG1TEXTCTRL14, wxID_DIALOG1TEXTCTRL15, wxID_DIALOG1TEXTCTRL16,
wxID_DIALOG1TEXTCTRL17,wxID_DIALOG1TEXTCTRL18, wxID_DIALOG1TEXTCTRL19, wxID_DIALOG1TEXTCTRL20, wxID_DIALOG1TEXTCTRL21, wxID_DIALOG1TEXTCTRL22, wxID_DIALOG1TEXTCTRL23, wxID_DIALOG1TEXTCTRL24,
wxID_DIALOG1TEXTCTRL25,wxID_DIALOG1TEXTCTRL26, wxID_DIALOG1TEXTCTRL27, wxID_DIALOG1TEXTCTRL28, wxID_DIALOG1TEXTCTRL29, wxID_DIALOG1TEXTCTRL30, wxID_DIALOG1TEXTCTRL31, wxID_DIALOG1TEXTCTRL32,
wxID_DIALOG1TEXTCTRL33,wxID_DIALOG1TEXTCTRL34, wxID_DIALOG1TEXTCTRL35, wxID_DIALOG1TEXTCTRL36, wxID_DIALOG1TEXTCTRL37, wxID_DIALOG1TEXTCTRL38, wxID_DIALOG1TEXTCTRL39, wxID_DIALOG1TEXTCTRL40,
wxID_DIALOG1TEXTCTRL41,wxID_DIALOG1TEXTCTRL42, wxID_DIALOG1TEXTCTRL43, wxID_DIALOG1TEXTCTRL44, wxID_DIALOG1TEXTCTRL45, wxID_DIALOG1TEXTCTRL46, wxID_DIALOG1TEXTCTRL47, wxID_DIALOG1TEXTCTRL48,
wxID_DIALOG1TEXTCTRL49,wxID_DIALOG1TEXTCTRL50, wxID_DIALOG1TEXTCTRL51, wxID_DIALOG1TEXTCTRL52, wxID_DIALOG1TEXTCTRL53, wxID_DIALOG1TEXTCTRL54, wxID_DIALOG1TEXTCTRL55,wxID_DIALOG1TEXTCTRL56,
                                
 wxID_DIALOG1TEXTCTRL1_1,wxID_DIALOG1TEXTCTRL1_2, wxID_DIALOG1TEXTCTRL1_3, wxID_DIALOG1TEXTCTRL1_4, wxID_DIALOG1TEXTCTRL1_5, wxID_DIALOG1TEXTCTRL1_6, wxID_DIALOG1TEXTCTRL1_7, wxID_DIALOG1TEXTCTRL1_8,
wxID_DIALOG1TEXTCTRL1_9,wxID_DIALOG1TEXTCTRL1_10, wxID_DIALOG1TEXTCTRL1_11, wxID_DIALOG1TEXTCTRL1_12, wxID_DIALOG1TEXTCTRL1_13, wxID_DIALOG1TEXTCTRL1_14, wxID_DIALOG1TEXTCTRL1_15, wxID_DIALOG1TEXTCTRL1_16,
wxID_DIALOG1TEXTCTRL1_17,wxID_DIALOG1TEXTCTRL1_18, wxID_DIALOG1TEXTCTRL1_19, wxID_DIALOG1TEXTCTRL1_20, wxID_DIALOG1TEXTCTRL1_21, wxID_DIALOG1TEXTCTRL1_22, wxID_DIALOG1TEXTCTRL1_23, wxID_DIALOG1TEXTCTRL1_24,
wxID_DIALOG1TEXTCTRL1_25,wxID_DIALOG1TEXTCTRL1_26, wxID_DIALOG1TEXTCTRL1_27, wxID_DIALOG1TEXTCTRL1_28, wxID_DIALOG1TEXTCTRL1_29, wxID_DIALOG1TEXTCTRL1_30, wxID_DIALOG1TEXTCTRL1_31, wxID_DIALOG1TEXTCTRL1_32,
wxID_DIALOG1TEXTCTRL1_33,wxID_DIALOG1TEXTCTRL1_34, wxID_DIALOG1TEXTCTRL1_35, wxID_DIALOG1TEXTCTRL1_36, wxID_DIALOG1TEXTCTRL1_37, wxID_DIALOG1TEXTCTRL1_38, wxID_DIALOG1TEXTCTRL1_39, wxID_DIALOG1TEXTCTRL1_40,
wxID_DIALOG1TEXTCTRL1_41,wxID_DIALOG1TEXTCTRL1_42, wxID_DIALOG1TEXTCTRL1_43, wxID_DIALOG1TEXTCTRL1_44, wxID_DIALOG1TEXTCTRL1_45, wxID_DIALOG1TEXTCTRL1_46, wxID_DIALOG1TEXTCTRL1_47, wxID_DIALOG1TEXTCTRL1_48,
wxID_DIALOG1TEXTCTRL1_49,wxID_DIALOG1TEXTCTRL1_50, wxID_DIALOG1TEXTCTRL1_51, wxID_DIALOG1TEXTCTRL1_52, wxID_DIALOG1TEXTCTRL1_53, wxID_DIALOG1TEXTCTRL1_54, wxID_DIALOG1TEXTCTRL1_55,wxID_DIALOG1TEXTCTRL1_56,

wxID_DIALOG1TEXTCTRL2_1,wxID_DIALOG1TEXTCTRL2_2, wxID_DIALOG1TEXTCTRL2_3, wxID_DIALOG1TEXTCTRL2_4, wxID_DIALOG1TEXTCTRL2_5, wxID_DIALOG1TEXTCTRL2_6, wxID_DIALOG1TEXTCTRL2_7, wxID_DIALOG1TEXTCTRL2_8,
wxID_DIALOG1TEXTCTRL2_9,wxID_DIALOG1TEXTCTRL2_10, wxID_DIALOG1TEXTCTRL2_11, wxID_DIALOG1TEXTCTRL2_12, wxID_DIALOG1TEXTCTRL2_13, wxID_DIALOG1TEXTCTRL2_14, wxID_DIALOG1TEXTCTRL2_15, wxID_DIALOG1TEXTCTRL2_16,
wxID_DIALOG1TEXTCTRL2_17,wxID_DIALOG1TEXTCTRL2_18, wxID_DIALOG1TEXTCTRL2_19, wxID_DIALOG1TEXTCTRL2_20, wxID_DIALOG1TEXTCTRL2_21, wxID_DIALOG1TEXTCTRL2_22, wxID_DIALOG1TEXTCTRL2_23, wxID_DIALOG1TEXTCTRL2_24,
wxID_DIALOG1TEXTCTRL2_25,wxID_DIALOG1TEXTCTRL2_26, wxID_DIALOG1TEXTCTRL2_27, wxID_DIALOG1TEXTCTRL2_28, wxID_DIALOG1TEXTCTRL2_29, wxID_DIALOG1TEXTCTRL2_30, wxID_DIALOG1TEXTCTRL2_31, wxID_DIALOG1TEXTCTRL2_32,
wxID_DIALOG1TEXTCTRL2_33,wxID_DIALOG1TEXTCTRL2_34, wxID_DIALOG1TEXTCTRL2_35, wxID_DIALOG1TEXTCTRL2_36, wxID_DIALOG1TEXTCTRL2_37, wxID_DIALOG1TEXTCTRL2_38, wxID_DIALOG1TEXTCTRL2_39, wxID_DIALOG1TEXTCTRL2_40,
wxID_DIALOG1TEXTCTRL2_41,wxID_DIALOG1TEXTCTRL2_42, wxID_DIALOG1TEXTCTRL2_43, wxID_DIALOG1TEXTCTRL2_44, wxID_DIALOG1TEXTCTRL2_45, wxID_DIALOG1TEXTCTRL2_46, wxID_DIALOG1TEXTCTRL2_47, wxID_DIALOG1TEXTCTRL2_48,
wxID_DIALOG1TEXTCTRL2_49,wxID_DIALOG1TEXTCTRL2_50, wxID_DIALOG1TEXTCTRL2_51, wxID_DIALOG1TEXTCTRL2_52, wxID_DIALOG1TEXTCTRL2_53, wxID_DIALOG1TEXTCTRL2_54, wxID_DIALOG1TEXTCTRL2_55,wxID_DIALOG1TEXTCTRL2_56,

wxID_DIALOG2COMBOBOX1_1,wxID_DIALOG2COMBOBOX1_2,wxID_DIALOG2COMBOBOX1_3,wxID_DIALOG2COMBOBOX1_4,wxID_DIALOG2COMBOBOX1_5,wxID_DIALOG2COMBOBOX1_6,wxID_DIALOG2COMBOBOX1_7,wxID_DIALOG2COMBOBOX1_8,
wxID_DIALOG2COMBOBOX1_9,wxID_DIALOG2COMBOBOX1_10,wxID_DIALOG2COMBOBOX1_11,wxID_DIALOG2COMBOBOX1_12,wxID_DIALOG2COMBOBOX1_13,wxID_DIALOG2COMBOBOX1_14,wxID_DIALOG2COMBOBOX1_15,wxID_DIALOG2COMBOBOX1_16,
wxID_DIALOG2COMBOBOX1_17,wxID_DIALOG2COMBOBOX1_18,wxID_DIALOG2COMBOBOX1_19,wxID_DIALOG2COMBOBOX1_20,wxID_DIALOG2COMBOBOX1_21,wxID_DIALOG2COMBOBOX1_22,wxID_DIALOG2COMBOBOX1_23,wxID_DIALOG2COMBOBOX1_24,
wxID_DIALOG2COMBOBOX1_25,wxID_DIALOG2COMBOBOX1_26,wxID_DIALOG2COMBOBOX1_27,wxID_DIALOG2COMBOBOX1_28,wxID_DIALOG2COMBOBOX1_29,wxID_DIALOG2COMBOBOX1_30,wxID_DIALOG2COMBOBOX1_31,wxID_DIALOG2COMBOBOX1_32,
wxID_DIALOG2COMBOBOX1_33,wxID_DIALOG2COMBOBOX1_34,wxID_DIALOG2COMBOBOX1_35,wxID_DIALOG2COMBOBOX1_36,wxID_DIALOG2COMBOBOX1_37,wxID_DIALOG2COMBOBOX1_38,wxID_DIALOG2COMBOBOX1_39,wxID_DIALOG2COMBOBOX1_40,
wxID_DIALOG2COMBOBOX1_41,wxID_DIALOG2COMBOBOX1_42,wxID_DIALOG2COMBOBOX1_43,wxID_DIALOG2COMBOBOX1_44,wxID_DIALOG2COMBOBOX1_45,wxID_DIALOG2COMBOBOX1_46,wxID_DIALOG2COMBOBOX1_47,wxID_DIALOG2COMBOBOX1_48,
wxID_DIALOG2COMBOBOX1_49,wxID_DIALOG2COMBOBOX1_50,wxID_DIALOG2COMBOBOX1_51,wxID_DIALOG2COMBOBOX1_52,wxID_DIALOG2COMBOBOX1_53,wxID_DIALOG2COMBOBOX1_54,wxID_DIALOG2COMBOBOX1_55,wxID_DIALOG2COMBOBOX1_56,


] = [wx.NewId() for _init_ctrls in range(293)]

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
        
        parent.AddWindow(self.checkBox14, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_14, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl14, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_14, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_14, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox15, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_15, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl15, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_15, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_15, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox16, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_16, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl16, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_16, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_16, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox17, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_17, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl17, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_17, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_17, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox18, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_18, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl18, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_18, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_18, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox19, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_19, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl19, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_19, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_19, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox20, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_20, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl20, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_20, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_20, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox21, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_21, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl21, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_21, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_21, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox22, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_22, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl22, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_22, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_22, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox23, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_23, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl23, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_23, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_23, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox24, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_24, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl24, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_24, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_24, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox25, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_25, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl25, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_25, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_25, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox26, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_26, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl26, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_26, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_26, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox27, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_27, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl27, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_27, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_27, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox28, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_28, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl28, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_28, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_28, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox29, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_29, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl29, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_29, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_29, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox30, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_30, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl30, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_30, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_30, 0, border=0, flag=0)        

        parent.AddWindow(self.checkBox31, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_31, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl31, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_31, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_31, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox32, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_32, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl32, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_32, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_32, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox33, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_33, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl33, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_33, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_33, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox34, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_34, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl34, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_34, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_34, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox35, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_35, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl35, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_35, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_35, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox36, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_36, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl36, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_36, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_36, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox37, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_37, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl37, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_37, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_37, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox38, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_38, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl38, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_38, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_38, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox39, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_39, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl39, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_39, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_39, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox40, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_40, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl40, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_40, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_40, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox41, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_41, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl41, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_41, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_41, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox42, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_42, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl42, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_42, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_42, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox43, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_43, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl43, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_43, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_43, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox44, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_44, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl44, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_44, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_44, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox45, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_45, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl45, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_45, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_45, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox46, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_46, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl46, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_46, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_46, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox47, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_47, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl47, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_47, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_47, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox48, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_48, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl48, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_48, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_48, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox49, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_49, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl49, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_49, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_49, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox50, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_50, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl50, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_50, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_50, 0, border=0, flag=0)
                
        parent.AddWindow(self.checkBox51, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_51, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl51, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_51, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_51, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox52, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_52, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl52, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_52, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_52, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox53, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_53, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl53, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_53, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_53, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox54, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_54, 0, border=0, flag=0)       
        parent.AddWindow(self.textCtrl54, 0, border=0, flag=0)   
        parent.AddWindow(self.textCtrl1_54, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_54, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox55, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_55, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl55, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_55, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_55, 0, border=0, flag=0)

        parent.AddWindow(self.checkBox56, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_56, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl56, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_56, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_56, 0, border=0, flag=0)        
                        
    def _init_coll_flexGridSizer3_Items(self, parent):
        # generated method, don't edit        
        parent.AddWindow(self.button1, 0, border=0, flag=0)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.flexGridSizer1, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer2, 0, border=0, flag=0)
        parent.AddSizer(self.flexGridSizer3, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.flexGridSizer1 = wx.FlexGridSizer(cols=25, hgap=0, rows=50, vgap=0)
        self.flexGridSizer2 = wx.FlexGridSizer(cols=10, hgap=0, rows=50, vgap=0)
        self.flexGridSizer3 = wx.FlexGridSizer(cols=10, hgap=0, rows=50, vgap=0)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer2_Items(self.flexGridSizer2)
        self._init_coll_flexGridSizer3_Items(self.flexGridSizer3)
        self.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,pos=wx.Point(376, 237), size=wx.Size(852, 771),style=wx.DEFAULT_DIALOG_STYLE,title=u'Crop parameters')
        self.SetClientSize(wx.Size(856, 643))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Create Parm',name='button1', parent=self, pos=wx.Point(0, 600),size=wx.Size(400, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,id=wxID_DIALOG1BUTTON1)

        self.comboBox1_1 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_1, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_2 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_2, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_3 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_3, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_4 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_4, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_5 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_5, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_6 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_6, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_7 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_7, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_8 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_8, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_9 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_9, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_10 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_10, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_11 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_11, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_12 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_12, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_13 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_13, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_14 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_14, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_15 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_15, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_16 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_16, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_17 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_17, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_18 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_18, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_19 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_19, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_20 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_20, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_21 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_21, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_22 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_22, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_23 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_23, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_24= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_24, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_25 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_25, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_26= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_26, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_27= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_27, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_28 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_28, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_29 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_29, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_30= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_30, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_31 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_31, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_32 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_32, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_33= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_33, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_34= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_34, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_35= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_35, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_36= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_36, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_37= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_37, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_38= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_38, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_39= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_39, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_40= wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_40, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_41 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_41, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_42 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_42, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_43 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_43, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_44 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_44, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_45 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_45, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_46 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_46, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_47 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_47, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_48 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_48, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_49 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_49, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_50 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_50, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_51 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_51, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_52 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_52, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_53 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_53, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_54 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_54, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_55 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_55, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_56 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_56, parent=self, size=wx.Size(90, 21), style=0)

################################################################################################
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,label=u'CROP Param', name='staticText1', parent=self,  pos=wx.Point(310, 0), size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,  False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 128, 255))        
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,label=u'Method', name='staticText2', parent=self, pos=wx.Point(310, 0), size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText2.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,label=u'Default', name='staticText3', parent=self,  size=wx.Size(80, 20),pos=wx.Point(310, 0),  style=wx.ALIGN_CENTRE)
        self.staticText3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText3.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4,label=u'Minimum', name='staticText4', parent=self,  size=wx.Size(80, 20),pos=wx.Point(310, 0),  style=wx.ALIGN_CENTRE)
        self.staticText4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Times New Roman'))
        self.staticText4.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5,label=u'Maximum', name='staticText5', parent=self, size=wx.Size(80, 20), style=wx.ALIGN_CENTRE)
        self.staticText5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,False, u'Times New Roman'))
        self.staticText5.SetForegroundColour(wx.Colour(0, 128, 255))
        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6,label=u'CROP Param', name='staticText6', parent=self, pos=wx.Point(310, 0), size=wx.Size(80, 20),style=wx.ALIGN_CENTRE)
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
        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1, label=u'WA', name='checkBox1', parent=self, size=wx.Size(80, 20), style=wx.ALIGN_LEFT)
        self.checkBox2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2, label=u'HI', name='checkBox2', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3, label=u'TOPC', name='checkBox3', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4, label=u'TBSC', name='checkBox4', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5, label=u'DMLA',    name='checkBox5', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox6 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX6, label=u'DLAI', name='checkBox6', parent=self, size=wx.Size(80, 20), style=wx.CAPTION)
        self.checkBox7 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX7, label=u'DLAP1', name='checkBox7', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox8 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX8, label=u'DLAP2', name='checkBox8', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox9 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX9, label=u'RLAD',name='checkBox9', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox10 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX10, label=u'RBMD', name='checkBox10', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox11 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX11, label=u'ALT',name='checkBox11', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox12 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX12, label=u'GSI', name='checkBox12', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox13 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX13, label=u'CAF', name='checkBox13', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox14 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX14, label=u'SDW', name='checkBox14', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox15 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX15, label=u'HMX', name='checkBox15', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox16 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX16, label=u'RDMX', name='checkBox16', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox17 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX17, label=u'WAC2',name='checkBox17', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox18 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX18, label=u'CNY',  name='checkBox18', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox19 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX19, label=u'CPY',name='checkBox19', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox20 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX20, label=u'CKY',name='checkBox20', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox21 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX21, label=u'WSYF', name='checkBox21', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox22 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX22, label=u'PST',name='checkBox22', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox23 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX23, label=u'CSTS',name='checkBox23', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox24 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX24, label=u'PRYG', name='checkBox24', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox25 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX25, label=u'PRYF', name='checkBox25', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox26 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX26, label=u'WCY',name='checkBox26', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox27 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX27, label=u'BN1',name='checkBox27', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox28 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX28, label=u'BN2', name='checkBox28', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox29 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX29, label=u'BN3', name='checkBox29', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox30 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX30, label=u'BP1',  name='checkBox30', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox31 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX31, label=u'BP2',  name='checkBox31', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox32 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX32, label=u'BP3', name='checkBox32', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox33 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX33, label=u'BK1',name='checkBox33', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox34 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX34, label=u'BK2',name='checkBox34', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox35 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX35, label=u'BK3',name='checkBox35', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox36 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX36, label=u'BW1',name='checkBox36', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox37 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX37, label=u'BW2',name='checkBox37', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox38 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX38, label=u'BW3',name='checkBox38', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox39 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX39, label=u'IDC',name='checkBox39', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox40 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX40, label=u'FRST1',name='checkBox40', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox41 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX41, label=u'FRST2',name='checkBox41', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox42 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX42, label=u'WAVP',name='checkBox42', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox43 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX43, label=u'VPTH',name='checkBox43', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox44 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX44, label=u'VPD2',name='checkBox44', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox45 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX45, label=u'RWPC1',name='checkBox45', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox46 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX46, label=u'RWPC2',name='checkBox46', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox47 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX47, label=u'GMHU',name='checkBox47', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox48 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX48, label=u'PPLP1', name='checkBox48', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox49 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX49, label=u'PPLP2',name='checkBox49', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox50 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX50, label=u'STX1',name='checkBox50', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox51 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX51, label=u'STX2', name='checkBox51', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox52 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX52, label=u'BLG1', name='checkBox52', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox53 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX53, label=u'BLG2',name='checkBox53', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox54 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX54, label=u'WUB', name='checkBox54', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox55 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX55, label=u'FTO', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox56 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX56, label=u'FLT', name='checkBox56', parent=self, size=wx.Size(80, 20), style=0)
######################################################################        
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1')
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, name='textCtrl2', parent=self, pos=wx.Point(310, 20), size=wx.Size(80, 20), style=0, value='textCtrl2')
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3, name='textCtrl3', parent=self, pos=wx.Point(570, 20), size=wx.Size(80, 20), style=0, value='textCtrl3')
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, name='textCtrl4', parent=self, pos=wx.Point(830, 20), size=wx.Size(80, 20), style=0, value='textCtrl4')
        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL5, name='textCtrl5', parent=self, pos=wx.Point(1090, 20), size=wx.Size(80, 20), style=0, value='textCtrl5')
        self.textCtrl6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL6, name='textCtrl6', parent=self, pos=wx.Point(50, 40), size=wx.Size(80, 20), style=0, value='textCtrl6')
        self.textCtrl7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL7, name='textCtrl7', parent=self, pos=wx.Point(310, 40), size=wx.Size(80, 20), style=0, value='textCtrl7')
        self.textCtrl8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL8, name='textCtrl8', parent=self, pos=wx.Point(570, 40), size=wx.Size(80, 20), style=0, value='textCtrl8')
        self.textCtrl9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL9, name='textCtrl9', parent=self, pos=wx.Point(830, 40), size=wx.Size(80, 20), style=0, value='textCtrl9')
        self.textCtrl10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL10, name='textCtrl10', parent=self, pos=wx.Point(1090, 40), size=wx.Size(80, 20), style=0, value='textCtrl10')
        self.textCtrl11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL11, name='textCtrl11', parent=self, pos=wx.Point(50, 60), size=wx.Size(80, 20), style=0, value='textCtrl11')
        self.textCtrl12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL12, name='textCtrl12', parent=self, pos=wx.Point(310, 60), size=wx.Size(80, 20), style=0, value='textCtrl12')
        self.textCtrl13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL13,name='textCtrl13', parent=self, pos=wx.Point(570, 60),size=wx.Size(80, 20), style=0, value='textCtrl13')
        self.textCtrl14 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL14,name='textCtrl14', parent=self, pos=wx.Point(830, 60), size=wx.Size(80, 20), style=0, value='textCtrl14')
        self.textCtrl15 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL15, name='textCtrl15', parent=self, pos=wx.Point(1090, 60), size=wx.Size(80, 20), style=0, value='textCtrl15')
        self.textCtrl16 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL16, name='textCtrl16', parent=self, pos=wx.Point(50, 80), size=wx.Size(80, 20), style=0, value='textCtrl16')
        self.textCtrl17 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL17, name='textCtrl17', parent=self, pos=wx.Point(310, 80), size=wx.Size(80, 20), style=0, value='textCtrl17')
        self.textCtrl18 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL18, name='textCtrl18', parent=self, pos=wx.Point(570, 80), size=wx.Size(80, 20), style=0, value='textCtrl18')
        self.textCtrl19 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL19, name='textCtrl19', parent=self, pos=wx.Point(830, 80), size=wx.Size(80, 20), style=0, value='textCtrl19')
        self.textCtrl20 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL20,name='textCtrl20', parent=self, pos=wx.Point(1090, 80), size=wx.Size(80, 20), style=0, value='textCtrl20')
        self.textCtrl21 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL21,name='textCtrl21', parent=self, pos=wx.Point(50, 100), size=wx.Size(80, 20), style=0, value='textCtrl21')
        self.textCtrl22 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL22, name='textCtrl22', parent=self, pos=wx.Point(310, 100),size=wx.Size(80, 20), style=0, value='textCtrl22')
        self.textCtrl23 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL23, name='textCtrl23', parent=self, pos=wx.Point(570, 100), size=wx.Size(80, 20), style=0, value='textCtrl23')
        self.textCtrl24 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL24, name='textCtrl24', parent=self, pos=wx.Point(830, 100),size=wx.Size(80, 20), style=0, value='textCtrl24')
        self.textCtrl25 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL25, name='textCtrl25', parent=self, pos=wx.Point(1090, 100),size=wx.Size(80, 20), style=0, value='textCtrl25')
        self.textCtrl26 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL26, name='textCtrl26', parent=self, pos=wx.Point(50, 120), size=wx.Size(80, 20), style=0, value='textCtrl26')
        self.textCtrl27 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL27, name='textCtrl27', parent=self, pos=wx.Point(310, 120), size=wx.Size(80, 20), style=0, value='textCtrl27')
        self.textCtrl28 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL28, name='textCtrl28', parent=self, pos=wx.Point(570, 120), size=wx.Size(80, 20), style=0, value='textCtrl28')
        self.textCtrl29 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL29, name='textCtrl29', parent=self, pos=wx.Point(830, 120), size=wx.Size(80, 20), style=0, value='textCtrl29')
        self.textCtrl30 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL30, name='textCtrl30', parent=self, pos=wx.Point(1090, 120), size=wx.Size(80, 20), style=0, value='textCtrl30')
        self.textCtrl31 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL31, name='textCtrl31', parent=self, pos=wx.Point(50, 140),size=wx.Size(80, 20), style=0, value='textCtrl31')
        self.textCtrl32 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL32,  name='textCtrl32', parent=self, pos=wx.Point(310, 140), size=wx.Size(80, 20), style=0, value='textCtrl32')
        self.textCtrl33 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL33, name='textCtrl33', parent=self, pos=wx.Point(570, 140), size=wx.Size(80, 20), style=0, value='textCtrl33')
        self.textCtrl34 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL34,name='textCtrl34', parent=self, pos=wx.Point(830, 140),size=wx.Size(80, 20), style=0, value='textCtrl34')
        self.textCtrl35 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL35, name='textCtrl35', parent=self, pos=wx.Point(1090, 140), size=wx.Size(80, 20), style=0, value='textCtrl35')
        self.textCtrl36 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL36, name='textCtrl36', parent=self, pos=wx.Point(50, 160),size=wx.Size(80, 20), style=0, value='textCtrl36')
        self.textCtrl37 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL37,  name='textCtrl37', parent=self, pos=wx.Point(310, 160), size=wx.Size(80, 20), style=0, value='textCtrl37')
        self.textCtrl38 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL38,name='textCtrl38', parent=self, pos=wx.Point(570, 160),  size=wx.Size(80, 20), style=0, value='textCtrl38')
        self.textCtrl39 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL39, name='textCtrl39', parent=self, pos=wx.Point(830, 160), size=wx.Size(80, 20), style=0, value='textCtrl39')
        self.textCtrl40 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL40, name='textCtrl40', parent=self, pos=wx.Point(1090, 160),size=wx.Size(80, 20), style=0, value='textCtrl40')
        self.textCtrl41 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL41, name='textCtrl41', parent=self, pos=wx.Point(50, 180), size=wx.Size(80, 20), style=0, value='textCtrl41')
        self.textCtrl42 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL42,name='textCtrl42', parent=self, pos=wx.Point(310, 180), size=wx.Size(80, 20), style=0, value='textCtrl42')
        self.textCtrl43 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL43, name='textCtrl43', parent=self, pos=wx.Point(570, 180), size=wx.Size(80, 20), style=0, value='textCtrl43')
        self.textCtrl44 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL44,name='textCtrl44', parent=self, pos=wx.Point(830, 180),size=wx.Size(80, 20), style=0, value='textCtrl44')
        self.textCtrl45 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL45, name='textCtrl45', parent=self, pos=wx.Point(1090, 180),size=wx.Size(80, 20), style=0, value='textCtrl45')
        self.textCtrl46 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL46,name='textCtrl46', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl46')
        self.textCtrl47 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL47,name='textCtrl47', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl47')
        self.textCtrl48 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL48,name='textCtrl48', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl48')
        self.textCtrl49 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL49, name='textCtrl49', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl49')
        self.textCtrl50 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL50, name='textCtrl50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl50')
        self.textCtrl51 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL51, name='textCtrl51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl51')
        self.textCtrl52 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL52, name='textCtrl52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl52')
        self.textCtrl53 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL53, name='textCtrl53', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl53')
        self.textCtrl54 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL54,  name='textCtrl54', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl54')
        self.textCtrl55 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL55, name='textCtrl55', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl55')
        self.textCtrl56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL56, name='textCtrl56', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl56')
######################################################################        
        self.textCtrl1_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_1, name='textCtrl1_1', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_1')
        self.textCtrl1_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_2, name='textCtrl2', parent=self,  pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_2')
        self.textCtrl1_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_3, name='textCt1_rl3', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_3')
        self.textCtrl1_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_4, name='textCtrl1_4', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_4')
        self.textCtrl1_5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_5, name='textCtrl1_5', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_5')
        self.textCtrl1_6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_6, name='textCtrl1_6', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_6')
        self.textCtrl1_7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_7, name='textCtrl1_7', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_7')
        self.textCtrl1_8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_8, name='textCtrl1_8', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_8')
        self.textCtrl1_9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_9, name='textCtrl1_9', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_9')
        self.textCtrl1_10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_10, name='textCtrl1_10', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_10')
        self.textCtrl1_11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_11, name='textCtrl1_11', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_11')
        self.textCtrl1_12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_12, name='textCtrl1_12', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_12')
        self.textCtrl1_13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_13,name='textCtrl1_13', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_13')
        self.textCtrl1_14 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_14,name='textCtrl1_14', parent=self,  pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_14')
        self.textCtrl1_15 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_15, name='textCtrl1_15', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_15')
        self.textCtrl1_16 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_16, name='textCtrl1_16', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_16')
        self.textCtrl1_17 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_17, name='textCtrl1_17', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_17')
        self.textCtrl1_18 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_18, name='textCtrl1_18', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_18')
        self.textCtrl1_19 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_19, name='textCtrl1_19', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_19')
        self.textCtrl1_20 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_20,name='textCtrl1_20', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_20')
        self.textCtrl1_21 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_21,name='textCtrl1_21', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_21')
        self.textCtrl1_22 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_22, name='textCtrl1_22', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_22')
        self.textCtrl1_23 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_23, name='textCtrl1_23', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_23')
        self.textCtrl1_24 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_24, name='textCtrl1_24', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_24')
        self.textCtrl1_25 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_25, name='textCtrl1_25', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_25')
        self.textCtrl1_26 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_26, name='textCtrl1_26', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_26')
        self.textCtrl1_27 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_27, name='textCtrl1_27', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_27')
        self.textCtrl1_28 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_28, name='textCtrl1_28', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_28')
        self.textCtrl1_29 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_29, name='textCtrl1_29', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_29')
        self.textCtrl1_30 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_30, name='textCtrl1_30', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_30')
        self.textCtrl1_31 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_31, name='textCtrl1_31', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_31')
        self.textCtrl1_32 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_32,  name='textCtrl1_32', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_32')
        self.textCtrl1_33 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_33, name='textCtrl1_33', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_33')
        self.textCtrl1_34 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_34,name='textCtrl1_34', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_34')
        self.textCtrl1_35 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_35, name='textCtrl1_35', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_35')
        self.textCtrl1_36 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_36, name='textCtrl1_36', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_36')
        self.textCtrl1_37 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_37,  name='textCtrl1_37', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_37')
        self.textCtrl1_38 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_38,name='textCtrl1_38', parent=self, pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_38')
        self.textCtrl1_39 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_39, name='textCtrl1_39', parent=self,pos=wx.Point(310, 440),  size=wx.Size(80, 20), style=0, value='textCtrl1_39')
        self.textCtrl1_40 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_40, name='textCtrl1_40', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_40')
        self.textCtrl1_41 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_41, name='textCtrl1_41', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_41')
        self.textCtrl1_42 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_42,name='textCtrl1_42', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_42')
        self.textCtrl1_43 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_43, name='textCtrl1_43', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_43')
        self.textCtrl1_44 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_44,name='textCtrl1_44', parent=self,pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_44')
        self.textCtrl1_45 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_45, name='textCtrl1_45', parent=self,pos=wx.Point(310, 440), size=wx.Size(80, 20), style=0, value='textCtrl1_45')
        self.textCtrl1_46 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_46,name='textCtrl1_46', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_46')
        self.textCtrl1_47 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_47,name='textCtrl1_47', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_47')
        self.textCtrl1_48 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_48,name='textCtrl1_48', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_48')
        self.textCtrl1_49 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_49, name='textCtrl1_49', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_49')
        self.textCtrl1_50 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_50, name='textCtrl1_50', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_50')
        self.textCtrl1_51 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_51, name='textCtrl1_51', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_51')
        self.textCtrl1_52 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_52, name='textCtrl1_52', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_52')
        self.textCtrl1_53 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_53, name='textCtrl1_53', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_53')
        self.textCtrl1_54 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_54,  name='textCtrl1_54', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_54')
        self.textCtrl1_55 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_55, name='textCtrl1_55', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_55')
        self.textCtrl1_56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_56, name='textCtrl1_56', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_56')

######################################################################        
        self.textCtrl2_1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_1, name='textCtrl2_1', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_1')
        self.textCtrl2_2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_2, name='textCtrl2_2', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_2')
        self.textCtrl2_3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_3, name='textCt2_rl3', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_3')
        self.textCtrl2_4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_4, name='textCtrl2_4', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_4')
        self.textCtrl2_5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_5, name='textCtrl2_5', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_5')
        self.textCtrl2_6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_6, name='textCtrl2_6', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_6')
        self.textCtrl2_7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_7, name='textCtrl2_7', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_7')
        self.textCtrl2_8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_8, name='textCtrl2_8', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_8')
        self.textCtrl2_9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_9, name='textCtrl2_9', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_9')
        self.textCtrl2_10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_10, name='textCtrl2_10', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_10')
        self.textCtrl2_11 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_11, name='textCtrl2_11', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_11')
        self.textCtrl2_12 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_12, name='textCtrl2_12', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_12')
        self.textCtrl2_13 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_13,name='textCtrl2_13', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_13')
        self.textCtrl2_14 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_14,name='textCtrl2_14', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_14')
        self.textCtrl2_15 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_15, name='textCtrl2_15', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_15')
        self.textCtrl2_16 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_16, name='textCtrl2_16', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_16')
        self.textCtrl2_17 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_17, name='textCtrl2_17', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_17')
        self.textCtrl2_18 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_18, name='textCtrl2_18', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl2_18')
        self.textCtrl2_19 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_19, name='textCtrl2_19', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_19')
        self.textCtrl2_20 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_20,name='textCtrl2_20', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_20')
        self.textCtrl2_21 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_21,name='textCtrl2_21', parent=self,size=wx.Size(80, 20), style=0, value='textCtrl2_21')
        self.textCtrl2_22 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_22, name='textCtrl2_22', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl2_22')
        self.textCtrl2_23 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_23, name='textCtrl2_23', parent=self, pos=wx.Point(570, 100), size=wx.Size(80, 20), style=0, value='textCtrl2_23')
        self.textCtrl2_24 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_24, name='textCtrl2_24', parent=self, pos=wx.Point(830, 100),size=wx.Size(80, 20), style=0, value='textCtrl2_24')
        self.textCtrl2_25 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_25, name='textCtrl2_25', parent=self, pos=wx.Point(1090, 100),size=wx.Size(80, 20), style=0, value='textCtrl2_25')
        self.textCtrl2_26 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_26, name='textCtrl2_26', parent=self, pos=wx.Point(50, 120), size=wx.Size(80, 20), style=0, value='textCtrl2_26')
        self.textCtrl2_27 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_27, name='textCtrl2_27', parent=self, pos=wx.Point(310, 120), size=wx.Size(80, 20), style=0, value='textCtrl2_27')
        self.textCtrl2_28 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_28, name='textCtrl2_28', parent=self, pos=wx.Point(570, 120), size=wx.Size(80, 20), style=0, value='textCtrl2_28')
        self.textCtrl2_29 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_29, name='textCtrl2_29', parent=self, pos=wx.Point(830, 120), size=wx.Size(80, 20), style=0, value='textCtrl2_29')
        self.textCtrl2_30 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_30, name='textCtrl2_30', parent=self, pos=wx.Point(1090, 120), size=wx.Size(80, 20), style=0, value='textCtrl2_30')
        self.textCtrl2_31 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_31, name='textCtrl2_31', parent=self, pos=wx.Point(50, 140),size=wx.Size(80, 20), style=0, value='textCtrl2_31')
        self.textCtrl2_32 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_32,  name='textCtrl2_32', parent=self, pos=wx.Point(310, 140), size=wx.Size(80, 20), style=0, value='textCtrl2_32')
        self.textCtrl2_33 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_33, name='textCtrl2_33', parent=self, pos=wx.Point(570, 140), size=wx.Size(80, 20), style=0, value='textCtrl2_33')
        self.textCtrl2_34 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_34,name='textCtrl2_34', parent=self, pos=wx.Point(830, 140),size=wx.Size(80, 20), style=0, value='textCtrl2_34')
        self.textCtrl2_35 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_35, name='textCtrl2_35', parent=self, pos=wx.Point(1090, 140), size=wx.Size(80, 20), style=0, value='textCtrl2_35')
        self.textCtrl2_36 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_36, name='textCtrl2_36', parent=self, pos=wx.Point(50, 160),size=wx.Size(80, 20), style=0, value='textCtrl2_36')
        self.textCtrl2_37 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_37,  name='textCtrl2_37', parent=self, pos=wx.Point(310, 160), size=wx.Size(80, 20), style=0, value='textCtrl2_37')
        self.textCtrl2_38 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_38,name='textCtrl2_38', parent=self, pos=wx.Point(570, 160),  size=wx.Size(80, 20), style=0, value='textCtrl2_38')
        self.textCtrl2_39 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_39, name='textCtrl2_39', parent=self, pos=wx.Point(830, 160), size=wx.Size(80, 20), style=0, value='textCtrl2_39')
        self.textCtrl2_40 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_40, name='textCtrl2_40', parent=self, pos=wx.Point(1090, 160),size=wx.Size(80, 20), style=0, value='textCtrl2_40')
        self.textCtrl2_41 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_41, name='textCtrl2_41', parent=self, pos=wx.Point(50, 180), size=wx.Size(80, 20), style=0, value='textCtrl2_41')
        self.textCtrl2_42 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_42,name='textCtrl2_42', parent=self, pos=wx.Point(310, 180), size=wx.Size(80, 20), style=0, value='textCtrl2_42')
        self.textCtrl2_43 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_43, name='textCtrl2_43', parent=self, pos=wx.Point(570, 180), size=wx.Size(80, 20), style=0, value='textCtrl2_43')
        self.textCtrl2_44 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_44,name='textCtrl2_44', parent=self, pos=wx.Point(830, 180),size=wx.Size(80, 20), style=0, value='textCtrl2_44')
        self.textCtrl2_45 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_45, name='textCtrl2_45', parent=self, pos=wx.Point(1090, 180),size=wx.Size(80, 20), style=0, value='textCtrl2_45')
        self.textCtrl2_46 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_46,name='textCtrl2_46', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl2_46')
        self.textCtrl2_47 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_47,name='textCtrl2_47', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_47')
        self.textCtrl2_48 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_48,name='textCtrl2_48', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_48')
        self.textCtrl2_49 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_49, name='textCtrl2_49', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_49')
        self.textCtrl2_50 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_50, name='textCtrl2_50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_50')
        self.textCtrl2_51 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_51, name='textCtrl2_51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl2_51')
        self.textCtrl2_52 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_52, name='textCtrl2_52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_52')
        self.textCtrl2_53 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_53, name='textCtrl2_53', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_53')
        self.textCtrl2_54 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_54,  name='textCtrl2_54', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl2_54')
        self.textCtrl2_55 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_55, name='textCtrl2_55', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl2_55')
        self.textCtrl2_56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_56, name='textCtrl2_56', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl2_56')
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
        self.comboBox1_14.SetItems(TOP)  
        self.comboBox1_15.SetItems(TOP)  
        self.comboBox1_16.SetItems(TOP)  
        self.comboBox1_17.SetItems(TOP)  
        self.comboBox1_18.SetItems(TOP)  
        self.comboBox1_19.SetItems(TOP)  
        self.comboBox1_20.SetItems(TOP)  
        self.comboBox1_21.SetItems(TOP)  
        self.comboBox1_22.SetItems(TOP)  
        self.comboBox1_23.SetItems(TOP)  
        self.comboBox1_24.SetItems(TOP)  
        self.comboBox1_25.SetItems(TOP)  
        self.comboBox1_26.SetItems(TOP)  
        self.comboBox1_27.SetItems(TOP)  
        self.comboBox1_28.SetItems(TOP)  
        self.comboBox1_29.SetItems(TOP)  
        self.comboBox1_30.SetItems(TOP)  
        self.comboBox1_31.SetItems(TOP)  
        self.comboBox1_32.SetItems(TOP)  
        self.comboBox1_33.SetItems(TOP)  
        self.comboBox1_34.SetItems(TOP)  
        self.comboBox1_35.SetItems(TOP)  
        self.comboBox1_36.SetItems(TOP)  
        self.comboBox1_37.SetItems(TOP)  
        self.comboBox1_38.SetItems(TOP)  
        self.comboBox1_39.SetItems(TOP)  
        self.comboBox1_40.SetItems(TOP)  
        self.comboBox1_41.SetItems(TOP)  
        self.comboBox1_42.SetItems(TOP)  
        self.comboBox1_43.SetItems(TOP)  
        self.comboBox1_44.SetItems(TOP)  
        self.comboBox1_45.SetItems(TOP)  
        self.comboBox1_46.SetItems(TOP)  
        self.comboBox1_47.SetItems(TOP)  
        self.comboBox1_48.SetItems(TOP)  
        self.comboBox1_49.SetItems(TOP)  
        self.comboBox1_50.SetItems(TOP)  
        self.comboBox1_51.SetItems(TOP)  
        self.comboBox1_52.SetItems(TOP)  
        self.comboBox1_53.SetItems(TOP)  
        self.comboBox1_54.SetItems(TOP)  
        self.comboBox1_55.SetItems(TOP)
        self.comboBox1_56.SetItems(TOP)  
        with open('modelGUISetup.inf','r') as file:
            ADD=file.readlines() 
        fSetup = open('Parameterization_Setup.inf', readCode)
        with open(ADD[13].strip(os.linesep) +'\\CROPCOM.DAT','r') as file:
            data=file.readlines()        
        if parent.comboBox1_2.GetValue()=='Maize':
            Default=data[3].split() 
        elif parent.comboBox1_2.GetValue()=='Rice':
            Default=data[19].split()       
        elif parent.comboBox1_2.GetValue()=='W-Wheat':
            Default=data[11].split() 
        elif parent.comboBox1_2.GetValue()=='S-Wheat':
            Default=data[12].split() 
        elif parent.comboBox1_2.GetValue()=='Soybean':
            Default=data[2].split()                         
        elif parent.comboBox1_2.GetValue()=='Barley':
            Default=data[15].split()  
        elif parent.comboBox1_2.GetValue()=='Sorghum':
            Default=data[4].split()                             
        elif parent.comboBox1_2.GetValue()=='Sorghum':
            Default=data[120].split()
        elif parent.comboBox1_2.GetValue()=='Cassava':
            Default=data[115].split()
                                                                                                              
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 15:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox1.SetValue(True)
                else:
                    self.checkBox1.SetValue(False)
                self.comboBox1_1.SetValue(txtLine.split(',')[1])
                self.textCtrl1.SetValue(Default[2])
                self.textCtrl1_1.SetValue(txtLine.split(',')[3])
                self.textCtrl2_1.SetValue(txtLine.split(',')[4])
            if loopNum == 16:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox2.SetValue(True)
                else:
                    self.checkBox2.SetValue(False)
                self.comboBox1_2.SetValue(txtLine.split(',')[1])
                self.textCtrl2.SetValue(Default[3])
                self.textCtrl1_2.SetValue(txtLine.split(',')[3])
                self.textCtrl2_2.SetValue(txtLine.split(',')[4])
            if loopNum == 17:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox3.SetValue(True)
                else:
                    self.checkBox3.SetValue(False)
                self.comboBox1_3.SetValue(txtLine.split(',')[1])
                self.textCtrl3.SetValue(Default[4])
                self.textCtrl1_3.SetValue(txtLine.split(',')[3])
                self.textCtrl2_3.SetValue(txtLine.split(',')[4])
            if loopNum == 18:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox4.SetValue(True)
                else:
                    self.checkBox4.SetValue(False)
                self.comboBox1_4.SetValue(txtLine.split(',')[1])
                self.textCtrl4.SetValue(Default[5])
                self.textCtrl1_4.SetValue(txtLine.split(',')[3])
                self.textCtrl2_4.SetValue(txtLine.split(',')[4])            
            if loopNum == 19:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox5.SetValue(True)
                else:
                    self.checkBox5.SetValue(False)
                self.comboBox1_5.SetValue(txtLine.split(',')[1])
                self.textCtrl5.SetValue(Default[6])
                self.textCtrl1_5.SetValue(txtLine.split(',')[3])
                self.textCtrl2_5.SetValue(txtLine.split(',')[4])            
            if loopNum == 20:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox6.SetValue(True)
                else:
                    self.checkBox6.SetValue(False)
                self.comboBox1_6.SetValue(txtLine.split(',')[1])
                self.textCtrl6.SetValue(Default[7])
                self.textCtrl1_6.SetValue(txtLine.split(',')[3])
                self.textCtrl2_6.SetValue(txtLine.split(',')[4])
            if loopNum == 21:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox7.SetValue(True)
                else:
                    self.checkBox7.SetValue(False)
                self.comboBox1_7.SetValue(txtLine.split(',')[1])
                self.textCtrl7.SetValue(Default[8])
                self.textCtrl1_7.SetValue(txtLine.split(',')[3])
                self.textCtrl2_7.SetValue(txtLine.split(',')[4])                                        
            if loopNum == 22:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox8.SetValue(True)
                else:
                    self.checkBox8.SetValue(False)
                self.comboBox1_8.SetValue(txtLine.split(',')[1])
                self.textCtrl8.SetValue(Default[9])
                self.textCtrl1_8.SetValue(txtLine.split(',')[3])
                self.textCtrl2_8.SetValue(txtLine.split(',')[4])            
            if loopNum == 23:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox9.SetValue(True)
                else:
                    self.checkBox9.SetValue(False)
                self.comboBox1_9.SetValue(txtLine.split(',')[1])
                self.textCtrl9.SetValue(Default[10])
                self.textCtrl1_9.SetValue(txtLine.split(',')[3])
                self.textCtrl2_9.SetValue(txtLine.split(',')[4])            
            if loopNum == 24:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox10.SetValue(True)
                else:
                    self.checkBox10.SetValue(False)
                self.comboBox1_10.SetValue(txtLine.split(',')[1])
                self.textCtrl10.SetValue(Default[11])
                self.textCtrl1_10.SetValue(txtLine.split(',')[3])
                self.textCtrl2_10.SetValue(txtLine.split(',')[4])            
            if loopNum == 24:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox11.SetValue(True)
                else:
                    self.checkBox11.SetValue(False)
                self.comboBox1_11.SetValue(txtLine.split(',')[1])
                self.textCtrl11.SetValue(Default[12])
                self.textCtrl1_11.SetValue(txtLine.split(',')[3])
                self.textCtrl2_11.SetValue(txtLine.split(',')[4])            
            if loopNum == 26:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox12.SetValue(True)
                else:
                    self.checkBox12.SetValue(False)
                self.comboBox1_12.SetValue(txtLine.split(',')[1])
                self.textCtrl12.SetValue(Default[13])
                self.textCtrl1_12.SetValue(txtLine.split(',')[3])
                self.textCtrl2_12.SetValue(txtLine.split(',')[4])            
            if loopNum == 27:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox13.SetValue(True)
                else:
                    self.checkBox13.SetValue(False)
                self.comboBox1_13.SetValue(txtLine.split(',')[1])
                self.textCtrl13.SetValue(Default[14])
                self.textCtrl1_13.SetValue(txtLine.split(',')[3])
                self.textCtrl2_13.SetValue(txtLine.split(',')[4])            
            if loopNum == 28:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox14.SetValue(True)
                else:
                    self.checkBox14.SetValue(False)
                self.comboBox1_14.SetValue(txtLine.split(',')[1])
                self.textCtrl14.SetValue(Default[15])
                self.textCtrl1_14.SetValue(txtLine.split(',')[3])
                self.textCtrl2_14.SetValue(txtLine.split(',')[4])                
            if loopNum == 29:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox15.SetValue(True)
                else:
                    self.checkBox15.SetValue(False)
                self.comboBox1_15.SetValue(txtLine.split(',')[1])
                self.textCtrl15.SetValue(Default[16])
                self.textCtrl1_15.SetValue(txtLine.split(',')[3])
                self.textCtrl2_15.SetValue(txtLine.split(',')[4])    
                
            if loopNum == 30:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox16.SetValue(True)
                else:
                    self.checkBox16.SetValue(False)
                self.comboBox1_16.SetValue(txtLine.split(',')[1])
                self.textCtrl16.SetValue(Default[17])
                self.textCtrl1_16.SetValue(txtLine.split(',')[3])
                self.textCtrl2_16.SetValue(txtLine.split(',')[4])    
                
            if loopNum == 31:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox17.SetValue(True)
                else:
                    self.checkBox17.SetValue(False)
                self.comboBox1_17.SetValue(txtLine.split(',')[1])
                self.textCtrl17.SetValue(Default[18])
                self.textCtrl1_17.SetValue(txtLine.split(',')[3])
                self.textCtrl2_17.SetValue(txtLine.split(',')[4]) 
                
            if loopNum == 32:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox18.SetValue(True)
                else:
                    self.checkBox18.SetValue(False)
                self.comboBox1_18.SetValue(txtLine.split(',')[1])
                self.textCtrl18.SetValue(Default[19])
                self.textCtrl1_18.SetValue(txtLine.split(',')[3])
                self.textCtrl2_18.SetValue(txtLine.split(',')[4])                                                                               
                                                                                                                                      
            if loopNum == 33:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox19.SetValue(True)
                else:
                    self.checkBox19.SetValue(False)
                self.comboBox1_19.SetValue(txtLine.split(',')[1])
                self.textCtrl19.SetValue(Default[20])
                self.textCtrl1_19.SetValue(txtLine.split(',')[3])
                self.textCtrl2_19.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                     

            if loopNum == 34:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox20.SetValue(True)
                else:
                    self.checkBox20.SetValue(False)
                self.comboBox1_20.SetValue(txtLine.split(',')[1])
                self.textCtrl20.SetValue(Default[21])
                self.textCtrl1_20.SetValue(txtLine.split(',')[3])
                self.textCtrl2_20.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            if loopNum == 35:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox21.SetValue(True)
                else:
                    self.checkBox21.SetValue(False)
                self.comboBox1_21.SetValue(txtLine.split(',')[1])
                self.textCtrl21.SetValue(Default[22])
                self.textCtrl1_21.SetValue(txtLine.split(',')[3])
                self.textCtrl2_21.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            if loopNum == 36:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox22.SetValue(True)
                else:
                    self.checkBox22.SetValue(False)
                self.comboBox1_22.SetValue(txtLine.split(',')[1])
                self.textCtrl22.SetValue(Default[23])
                self.textCtrl1_22.SetValue(txtLine.split(',')[3])
                self.textCtrl2_22.SetValue(txtLine.split(',')[4])                                                                                                                                            
            
            if loopNum == 37:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox23.SetValue(True)
                else:
                    self.checkBox23.SetValue(False)
                self.comboBox1_23.SetValue(txtLine.split(',')[1])
                self.textCtrl23.SetValue(Default[24])
                self.textCtrl1_23.SetValue(txtLine.split(',')[3])
                self.textCtrl2_23.SetValue(txtLine.split(',')[4])                
            
            if loopNum == 38:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox24.SetValue(True)
                else:
                    self.checkBox24.SetValue(False)
                self.comboBox1_24.SetValue(txtLine.split(',')[1])
                self.textCtrl24.SetValue(Default[25])
                self.textCtrl1_24.SetValue(txtLine.split(',')[3])
                self.textCtrl2_24.SetValue(txtLine.split(',')[4])                
            if loopNum == 39:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox25.SetValue(True)
                else:
                    self.checkBox25.SetValue(False)
                self.comboBox1_25.SetValue(txtLine.split(',')[1])
                self.textCtrl25.SetValue(Default[26])
                self.textCtrl1_25.SetValue(txtLine.split(',')[3])
                self.textCtrl2_25.SetValue(txtLine.split(',')[4])                
            if loopNum == 40:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox26.SetValue(True)
                else:
                    self.checkBox26.SetValue(False)
                self.comboBox1_26.SetValue(txtLine.split(',')[1])
                self.textCtrl26.SetValue(Default[27])
                self.textCtrl1_26.SetValue(txtLine.split(',')[3])
                self.textCtrl2_26.SetValue(txtLine.split(',')[4])                
            if loopNum == 41:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox27.SetValue(True)
                else:
                    self.checkBox27.SetValue(False)
                self.comboBox1_27.SetValue(txtLine.split(',')[1])
                self.textCtrl27.SetValue(Default[28])
                self.textCtrl1_27.SetValue(txtLine.split(',')[3])
                self.textCtrl2_27.SetValue(txtLine.split(',')[4])                
            if loopNum == 42:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox28.SetValue(True)
                else:
                    self.checkBox28.SetValue(False)
                self.comboBox1_28.SetValue(txtLine.split(',')[1])
                self.textCtrl28.SetValue(Default[29])
                self.textCtrl1_28.SetValue(txtLine.split(',')[3])
                self.textCtrl2_28.SetValue(txtLine.split(',')[4])                
            if loopNum == 43:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox29.SetValue(True)
                else:
                    self.checkBox29.SetValue(False)
                self.comboBox1_29.SetValue(txtLine.split(',')[1])
                self.textCtrl29.SetValue(Default[30])
                self.textCtrl1_29.SetValue(txtLine.split(',')[3])
                self.textCtrl2_29.SetValue(txtLine.split(',')[4])   
            if loopNum == 44:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox30.SetValue(True)
                else:
                    self.checkBox30.SetValue(False)
                self.comboBox1_30.SetValue(txtLine.split(',')[1])
                self.textCtrl30.SetValue(Default[31])
                self.textCtrl1_30.SetValue(txtLine.split(',')[3])
                self.textCtrl2_30.SetValue(txtLine.split(',')[4])                                                    
            if loopNum == 45:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox31.SetValue(True)
                else:
                    self.checkBox31.SetValue(False)
                self.comboBox1_31.SetValue(txtLine.split(',')[1])
                self.textCtrl31.SetValue(Default[32])
                self.textCtrl1_31.SetValue(txtLine.split(',')[3])
                self.textCtrl2_31.SetValue(txtLine.split(',')[4])                                                                                                         
            if loopNum ==46:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox32.SetValue(True)
                else:
                    self.checkBox32.SetValue(False)
                self.comboBox1_32.SetValue(txtLine.split(',')[1])
                self.textCtrl32.SetValue(Default[33])
                self.textCtrl1_32.SetValue(txtLine.split(',')[3])
                self.textCtrl2_32.SetValue(txtLine.split(',')[4])                                                                                                                                                         
            if loopNum == 47:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox33.SetValue(True)
                else:
                    self.checkBox33.SetValue(False)
                self.comboBox1_33.SetValue(txtLine.split(',')[1])
                self.textCtrl33.SetValue(Default[34])
                self.textCtrl1_33.SetValue(txtLine.split(',')[3])
                self.textCtrl2_33.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                          
            if loopNum == 48:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox34.SetValue(True)
                else:
                    self.checkBox34.SetValue(False)
                self.comboBox1_34.SetValue(txtLine.split(',')[1])
                self.textCtrl34.SetValue(Default[35])
                self.textCtrl1_34.SetValue(txtLine.split(',')[3])
                self.textCtrl2_34.SetValue(txtLine.split(',')[4])                
            if loopNum == 49:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox35.SetValue(True)
                else:
                    self.checkBox35.SetValue(False)
                self.comboBox1_35.SetValue(txtLine.split(',')[1])
                self.textCtrl35.SetValue(Default[36])
                self.textCtrl1_35.SetValue(txtLine.split(',')[3])
                self.textCtrl2_35.SetValue(txtLine.split(',')[4])                
            if loopNum == 50:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox36.SetValue(True)
                else:
                    self.checkBox36.SetValue(False)
                self.comboBox1_36.SetValue(txtLine.split(',')[1])
                self.textCtrl36.SetValue(Default[37])
                self.textCtrl1_36.SetValue(txtLine.split(',')[3])
                self.textCtrl2_36.SetValue(txtLine.split(',')[4])                
            if loopNum == 51:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox37.SetValue(True)
                else:
                    self.checkBox37.SetValue(False)
                self.comboBox1_37.SetValue(txtLine.split(',')[1])
                self.textCtrl37.SetValue(Default[38])
                self.textCtrl1_37.SetValue(txtLine.split(',')[3])
                self.textCtrl2_37.SetValue(txtLine.split(',')[4])                
            if loopNum == 52:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox38.SetValue(True)
                else:
                    self.checkBox38.SetValue(False)
                self.comboBox1_38.SetValue(txtLine.split(',')[1])
                self.textCtrl38.SetValue(Default[39])
                self.textCtrl1_38.SetValue(txtLine.split(',')[3])
                self.textCtrl2_38.SetValue(txtLine.split(',')[4])                
            if loopNum == 53:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox39.SetValue(True)
                else:
                    self.checkBox39.SetValue(False)
                self.comboBox1_39.SetValue(txtLine.split(',')[1])
                self.textCtrl39.SetValue(Default[40])
                self.textCtrl1_39.SetValue(txtLine.split(',')[3])
                self.textCtrl2_39.SetValue(txtLine.split(',')[4])                
            if loopNum == 54:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox40.SetValue(True)
                else:
                    self.checkBox40.SetValue(False)
                self.comboBox1_40.SetValue(txtLine.split(',')[1])
                self.textCtrl40.SetValue(Default[41])
                self.textCtrl1_40.SetValue(txtLine.split(',')[3])
                self.textCtrl2_40.SetValue(txtLine.split(',')[4])    
            if loopNum == 55:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox41.SetValue(True)
                else:
                    self.checkBox41.SetValue(False)
                self.comboBox1_41.SetValue(txtLine.split(',')[1])
                self.textCtrl41.SetValue(Default[42])
                self.textCtrl1_41.SetValue(txtLine.split(',')[3])
                self.textCtrl2_41.SetValue(txtLine.split(',')[4])                                            
            if loopNum == 56:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox42.SetValue(True)
                else:
                    self.checkBox42.SetValue(False)
                self.comboBox1_42.SetValue(txtLine.split(',')[1])
                self.textCtrl42.SetValue(Default[43])
                self.textCtrl1_42.SetValue(txtLine.split(',')[3])
                self.textCtrl2_42.SetValue(txtLine.split(',')[4])                
            if loopNum == 57:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox43.SetValue(True)
                else:
                    self.checkBox43.SetValue(False)
                self.comboBox1_43.SetValue(txtLine.split(',')[1])
                self.textCtrl43.SetValue(Default[44])
                self.textCtrl1_43.SetValue(txtLine.split(',')[3])
                self.textCtrl2_43.SetValue(txtLine.split(',')[4])                
            if loopNum == 58:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox44.SetValue(True)
                else:
                    self.checkBox44.SetValue(False)
                self.comboBox1_44.SetValue(txtLine.split(',')[1])
                self.textCtrl44.SetValue(Default[45])
                self.textCtrl1_44.SetValue(txtLine.split(',')[3])
                self.textCtrl2_44.SetValue(txtLine.split(',')[4])                
            if loopNum == 59:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox45.SetValue(True)
                else:
                    self.checkBox45.SetValue(False)
                self.comboBox1_45.SetValue(txtLine.split(',')[1])
                self.textCtrl45.SetValue(Default[46])
                self.textCtrl1_45.SetValue(txtLine.split(',')[3])
                self.textCtrl2_45.SetValue(txtLine.split(',')[4])                      
            if loopNum == 60:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox46.SetValue(True)
                else:
                    self.checkBox46.SetValue(False)
                self.comboBox1_46.SetValue(txtLine.split(',')[1])
                self.textCtrl46.SetValue(Default[47])
                self.textCtrl1_46.SetValue(txtLine.split(',')[3])
                self.textCtrl2_46.SetValue(txtLine.split(',')[4])                                                                   
            if loopNum == 61:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox47.SetValue(True)
                else:
                    self.checkBox47.SetValue(False)
                self.comboBox1_47.SetValue(txtLine.split(',')[1])
                self.textCtrl47.SetValue(Default[48])
                self.textCtrl1_47.SetValue(txtLine.split(',')[3])
                self.textCtrl2_47.SetValue(txtLine.split(',')[4])                                                                                                                           
            if loopNum == 62:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox48.SetValue(True)
                else:
                    self.checkBox48.SetValue(False)
                self.comboBox1_48.SetValue(txtLine.split(',')[1])
                self.textCtrl48.SetValue(Default[49])
                self.textCtrl1_48.SetValue(txtLine.split(',')[3])
                self.textCtrl2_48.SetValue(txtLine.split(',')[4])                                                                                                            
            if loopNum == 63:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox49.SetValue(True)
                else:
                    self.checkBox49.SetValue(False)
                self.comboBox1_49.SetValue(txtLine.split(',')[1])
                self.textCtrl49.SetValue(Default[50])
                self.textCtrl1_49.SetValue(txtLine.split(',')[3])
                self.textCtrl2_49.SetValue(txtLine.split(',')[4])                
            if loopNum == 64:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox50.SetValue(True)
                else:
                    self.checkBox50.SetValue(False)
                self.comboBox1_50.SetValue(txtLine.split(',')[1])
                self.textCtrl50.SetValue(Default[51])
                self.textCtrl1_50.SetValue(txtLine.split(',')[3])
                self.textCtrl2_50.SetValue(txtLine.split(',')[4])    
            if loopNum == 65:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox51.SetValue(True)
                else:
                    self.checkBox51.SetValue(False)
                self.comboBox1_51.SetValue(txtLine.split(',')[1])
                self.textCtrl51.SetValue(Default[52])
                self.textCtrl1_51.SetValue(txtLine.split(',')[3])
                self.textCtrl2_51.SetValue(txtLine.split(',')[4])                                               
            if loopNum == 66:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox52.SetValue(True)
                else:
                    self.checkBox52.SetValue(False)
                self.comboBox1_52.SetValue(txtLine.split(',')[1])
                self.textCtrl52.SetValue(Default[53])
                self.textCtrl1_52.SetValue(txtLine.split(',')[3])
                self.textCtrl2_52.SetValue(txtLine.split(',')[4])                                                                    
            if loopNum == 67:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox53.SetValue(True)
                else:
                    self.checkBox53.SetValue(False)
                self.comboBox1_53.SetValue(txtLine.split(',')[1])
                self.textCtrl53.SetValue(Default[54])
                self.textCtrl1_53.SetValue(txtLine.split(',')[3])
                self.textCtrl2_53.SetValue(txtLine.split(',')[4])                      
            if loopNum == 68:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox54.SetValue(True)
                else:
                    self.checkBox54.SetValue(False)
                self.comboBox1_54.SetValue(txtLine.split(',')[1])
                self.textCtrl54.SetValue(Default[55])
                self.textCtrl1_54.SetValue(txtLine.split(',')[3])
                self.textCtrl2_54.SetValue(txtLine.split(',')[4])                
            if loopNum == 69:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox55.SetValue(True)
                else:
                    self.checkBox55.SetValue(False)
                self.comboBox1_55.SetValue(txtLine.split(',')[1])
                self.textCtrl55.SetValue(Default[56])
                self.textCtrl1_55.SetValue(txtLine.split(',')[3])
                self.textCtrl2_55.SetValue(txtLine.split(',')[4])                            
            if loopNum == 70:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox56.SetValue(True)
                else:
                    self.checkBox56.SetValue(False)
                self.comboBox1_56.SetValue(txtLine.split(',')[1])
                self.textCtrl56.SetValue(Default[57])
                self.textCtrl1_56.SetValue(txtLine.split(',')[3])
                self.textCtrl2_56.SetValue(txtLine.split(',')[4]) 
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
        OPERdata=data[0:14]
        print data[70]
        print data[69]
    
        PARMdata=data[70:155]
                 
        f = open('Parameterization_Setup.inf', 'w')
        for i in range(0, 14):
            f.write(OPERdata[i])

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
                                                                                                                                                                
        if self.checkBox14.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_14.GetValue()+',')
        f.write(self.textCtrl14.GetValue() +',')
        f.write(self.textCtrl1_14.GetValue()+',')
        f.write(self.textCtrl2_14.GetValue()+',\n')       
        
        if self.checkBox15.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_15.GetValue()+',')
        f.write(self.textCtrl15.GetValue() +',')
        f.write(self.textCtrl1_15.GetValue()+',')
        f.write(self.textCtrl2_15.GetValue()+',\n')        
        
        if self.checkBox16.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_16.GetValue()+',')
        f.write(self.textCtrl16.GetValue() +',')
        f.write(self.textCtrl1_16.GetValue()+',')
        f.write(self.textCtrl2_16.GetValue()+',\n')           
        
        if self.checkBox17.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_17.GetValue()+',')
        f.write(self.textCtrl17.GetValue() +',')
        f.write(self.textCtrl1_17.GetValue()+',')
        f.write(self.textCtrl2_17.GetValue()+',\n')          
        
        if self.checkBox18.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_18.GetValue()+',')
        f.write(self.textCtrl18.GetValue() +',')
        f.write(self.textCtrl1_18.GetValue()+',')
        f.write(self.textCtrl2_18.GetValue()+',\n')          
        
        if self.checkBox19.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_19.GetValue()+',')
        f.write(self.textCtrl19.GetValue() +',')
        f.write(self.textCtrl1_19.GetValue()+',')
        f.write(self.textCtrl2_19.GetValue()+',\n')          
       
        if self.checkBox20.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_20.GetValue()+',')
        f.write(self.textCtrl20.GetValue() +',')
        f.write(self.textCtrl1_20.GetValue()+',')
        f.write(self.textCtrl2_20.GetValue()+',\n')          
        
        if self.checkBox21.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_21.GetValue()+',')
        f.write(self.textCtrl21.GetValue() +',')
        f.write(self.textCtrl1_21.GetValue()+',')
        f.write(self.textCtrl2_21.GetValue()+',\n')            
        
        if self.checkBox22.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_22.GetValue()+',')
        f.write(self.textCtrl22.GetValue() +',')
        f.write(self.textCtrl1_22.GetValue()+',')
        f.write(self.textCtrl2_22.GetValue()+',\n')    
        
        if self.checkBox23.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_23.GetValue()+',')
        f.write(self.textCtrl23.GetValue() +',')
        f.write(self.textCtrl1_23.GetValue()+',')
        f.write(self.textCtrl2_23.GetValue()+',\n')    
        
        if self.checkBox24.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_24.GetValue()+',')
        f.write(self.textCtrl24.GetValue() +',')
        f.write(self.textCtrl1_24.GetValue()+',')
        f.write(self.textCtrl2_24.GetValue()+',\n')                                    
                                                                                

        if self.checkBox25.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_25.GetValue()+',')
        f.write(self.textCtrl25.GetValue() +',')
        f.write(self.textCtrl1_25.GetValue()+',')
        f.write(self.textCtrl2_25.GetValue()+',\n')                                    
                                                               
        if self.checkBox26.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_26.GetValue()+',')
        f.write(self.textCtrl26.GetValue() +',')
        f.write(self.textCtrl1_26.GetValue()+',')
        f.write(self.textCtrl2_26.GetValue()+',\n')                                    
                                                                       
        if self.checkBox27.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_27.GetValue()+',')
        f.write(self.textCtrl27.GetValue() +',')
        f.write(self.textCtrl1_27.GetValue()+',')
        f.write(self.textCtrl2_27.GetValue()+',\n')                                    
                                                                               
        if self.checkBox28.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_28.GetValue()+',')
        f.write(self.textCtrl28.GetValue() +',')
        f.write(self.textCtrl1_28.GetValue()+',')
        f.write(self.textCtrl2_28.GetValue()+',\n')                                    
                                                                                       
        if self.checkBox29.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_29.GetValue()+',')
        f.write(self.textCtrl29.GetValue() +',')
        f.write(self.textCtrl1_29.GetValue()+',')
        f.write(self.textCtrl2_29.GetValue()+',\n')                                    
                                                                                               
        if self.checkBox30.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_30.GetValue()+',')
        f.write(self.textCtrl30.GetValue() +',')
        f.write(self.textCtrl1_30.GetValue()+',')
        f.write(self.textCtrl2_30.GetValue()+',\n')                                    
                                                                                                       
        if self.checkBox31.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_31.GetValue()+',')
        f.write(self.textCtrl31.GetValue() +',')
        f.write(self.textCtrl1_31.GetValue()+',')
        f.write(self.textCtrl2_31.GetValue()+',\n') 
        
        if self.checkBox32.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_32.GetValue()+',')
        f.write(self.textCtrl32.GetValue() +',')
        f.write(self.textCtrl1_32.GetValue()+',')
        f.write(self.textCtrl2_32.GetValue()+',\n')                                                                                       
                                                                                                                                                      
        if self.checkBox33.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_33.GetValue()+',')
        f.write(self.textCtrl33.GetValue() +',')
        f.write(self.textCtrl1_33.GetValue()+',')
        f.write(self.textCtrl2_33.GetValue()+',\n')                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                    
        if self.checkBox34.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_34.GetValue()+',')
        f.write(self.textCtrl34.GetValue() +',')
        f.write(self.textCtrl1_34.GetValue()+',')
        f.write(self.textCtrl2_34.GetValue()+',\n')        
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        if self.checkBox35.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_35.GetValue()+',')
        f.write(self.textCtrl35.GetValue() +',')
        f.write(self.textCtrl1_35.GetValue()+',')
        f.write(self.textCtrl2_35.GetValue()+',\n')                
        
        if self.checkBox36.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_36.GetValue()+',')
        f.write(self.textCtrl36.GetValue() +',')
        f.write(self.textCtrl1_36.GetValue()+',')
        f.write(self.textCtrl2_36.GetValue()+',\n')                

        if self.checkBox37.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_37.GetValue()+',')
        f.write(self.textCtrl37.GetValue() +',')
        f.write(self.textCtrl1_37.GetValue()+',')
        f.write(self.textCtrl2_37.GetValue()+',\n')          
                
        if self.checkBox38.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_38.GetValue()+',')
        f.write(self.textCtrl38.GetValue() +',')
        f.write(self.textCtrl1_38.GetValue()+',')
        f.write(self.textCtrl2_38.GetValue()+',\n')                          
                                
        if self.checkBox39.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_39.GetValue()+',')
        f.write(self.textCtrl39.GetValue() +',')
        f.write(self.textCtrl1_39.GetValue()+',')
        f.write(self.textCtrl2_39.GetValue()+',\n')                                          

        if self.checkBox40.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_40.GetValue()+',')
        f.write(self.textCtrl40.GetValue() +',')
        f.write(self.textCtrl1_40.GetValue()+',')
        f.write(self.textCtrl2_40.GetValue()+',\n')                                                          
                                                                                                                
        if self.checkBox41.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_41.GetValue()+',')
        f.write(self.textCtrl41.GetValue() +',')
        f.write(self.textCtrl1_41.GetValue()+',')
        f.write(self.textCtrl2_41.GetValue()+',\n')                                                                                                                                                                                                                                     
        
        
        if self.checkBox42.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_42.GetValue()+',')
        f.write(self.textCtrl42.GetValue() +',')
        f.write(self.textCtrl1_42.GetValue()+',')
        f.write(self.textCtrl2_42.GetValue()+',\n')             
        
        if self.checkBox43.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_43.GetValue()+',')
        f.write(self.textCtrl43.GetValue() +',')
        f.write(self.textCtrl1_43.GetValue()+',')
        f.write(self.textCtrl2_43.GetValue()+',\n')             
        
        if self.checkBox44.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_44.GetValue()+',')
        f.write(self.textCtrl44.GetValue() +',')
        f.write(self.textCtrl1_44.GetValue()+',')
        f.write(self.textCtrl2_44.GetValue()+',\n')             
        
        if self.checkBox45.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_45.GetValue()+',')
        f.write(self.textCtrl45.GetValue() +',')
        f.write(self.textCtrl1_45.GetValue()+',')
        f.write(self.textCtrl2_45.GetValue()+',\n')    
        
        if self.checkBox46.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_46.GetValue()+',')
        f.write(self.textCtrl46.GetValue() +',')
        f.write(self.textCtrl1_46.GetValue()+',')
        f.write(self.textCtrl2_46.GetValue()+',\n')              
          
        if self.checkBox47.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_47.GetValue()+',')
        f.write(self.textCtrl47.GetValue() +',')
        f.write(self.textCtrl1_47.GetValue()+',')
        f.write(self.textCtrl2_47.GetValue()+',\n')                 
                
        if self.checkBox48.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_48.GetValue()+',')
        f.write(self.textCtrl48.GetValue() +',')
        f.write(self.textCtrl1_48.GetValue()+',')
        f.write(self.textCtrl2_48.GetValue()+',\n')             
        
        if self.checkBox49.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_49.GetValue()+',')
        f.write(self.textCtrl49.GetValue() +',')
        f.write(self.textCtrl1_49.GetValue()+',')
        f.write(self.textCtrl2_49.GetValue()+',\n')             

        if self.checkBox50.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_50.GetValue()+',')
        f.write(self.textCtrl50.GetValue() +',')
        f.write(self.textCtrl1_50.GetValue()+',')
        f.write(self.textCtrl2_50.GetValue()+',\n')             
                
        if self.checkBox51.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_51.GetValue()+',')
        f.write(self.textCtrl51.GetValue() +',')
        f.write(self.textCtrl1_51.GetValue()+',')
        f.write(self.textCtrl2_51.GetValue()+',\n')                             
                                        
        if self.checkBox52.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_52.GetValue()+',')
        f.write(self.textCtrl52.GetValue() +',')
        f.write(self.textCtrl1_52.GetValue()+',')
        f.write(self.textCtrl2_52.GetValue()+',\n')  
        
        if self.checkBox53.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_53.GetValue()+',')
        f.write(self.textCtrl53.GetValue() +',')
        f.write(self.textCtrl1_53.GetValue()+',')
        f.write(self.textCtrl2_53.GetValue()+',\n')  

        if self.checkBox54.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_54.GetValue()+',')
        f.write(self.textCtrl54.GetValue() +',')
        f.write(self.textCtrl1_54.GetValue()+',')
        f.write(self.textCtrl2_54.GetValue()+',\n')                  
                                
        if self.checkBox55.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_55.GetValue()+',')
        f.write(self.textCtrl55.GetValue() +',')
        f.write(self.textCtrl1_55.GetValue()+',')
        f.write(self.textCtrl2_55.GetValue()+',\n') 

        if self.checkBox56.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_56.GetValue()+',')
        f.write(self.textCtrl56.GetValue() +',')
        f.write(self.textCtrl1_56.GetValue()+',')
        f.write(self.textCtrl2_56.GetValue()+',\n')               
                
        for i in range(0, 85):
            f.write(PARMdata[i])              
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
            fSufi2Parm = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+ '\\SUFI2.IN\\' + 'par_inf.txt', 'a')            
            fPar_Name = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+ '\\Par_Name.OUT', 'a')
            counter=1
            if self.checkBox1.GetValue() == True:
                fSufi2Parm.write( self.comboBox1_1.GetValue()[0] + '_WA     ' + self.textCtrl1_1.GetValue() + '       ' + self.textCtrl2_1.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WA\n" )
                counter=counter+1
            
            if self.checkBox2.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_2.GetValue()[0] + '_HI     ' + self.textCtrl1_2.GetValue() + '       ' + self.textCtrl2_2.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :HI\n" )
                counter=counter+1            
                                
            if self.checkBox3.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_3.GetValue()[0] + '_TOPC     ' + self.textCtrl1_3.GetValue() + '       ' + self.textCtrl2_3.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :TOPC\n" )
                counter=counter+1            
                           
            if self.checkBox4.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_4.GetValue()[0] + '_TBSC     ' + self.textCtrl1_4.GetValue() + '       ' + self.textCtrl2_4.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :TBSC\n" )
                counter=counter+1            
                            
            if self.checkBox5.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_5.GetValue()[0]  + '_DMLA     ' + self.textCtrl1_5.GetValue() + '       ' + self.textCtrl2_5.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :DMLA\n" )
                counter=counter+1            
                            
            if self.checkBox6.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_6.GetValue()[0]  + '_DLAI     ' + self.textCtrl1_6.GetValue() + '       ' + self.textCtrl2_6.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :DLAI\n" )
                counter=counter+1            
                            
            if self.checkBox7.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_7.GetValue()[0]  + '_DLAP1     ' + self.textCtrl1_7.GetValue() + '       ' + self.textCtrl2_7.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :DLAP1\n" )
                counter=counter+1            
                            
            if self.checkBox8.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_8.GetValue()[0]  + '_DLAP2     ' + self.textCtrl1_8.GetValue() + '       ' + self.textCtrl2_8.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :DLAP2\n" )
                counter=counter+1            
                            
            if self.checkBox9.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_9.GetValue()[0]  + '_RLAD     ' + self.textCtrl1_9.GetValue() + '       ' + self.textCtrl2_9.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :RLAD\n" )
                counter=counter+1             
                            
            if self.checkBox10.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_10.GetValue()[0]  + '_RBMD     ' + self.textCtrl1_10.GetValue() + '       ' + self.textCtrl2_10.GetValue() + lineEnd)        
                fPar_Name.write(str(counter) + " :RBMD\n" )
                counter=counter+1             
                            
            if self.checkBox11.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_11.GetValue()[0]  + '_ALT     ' + self.textCtrl1_11.GetValue() + '       ' + self.textCtrl2_11.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :ALT\n" )
                counter=counter+1             
                            
            if self.checkBox12.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_12.GetValue()[0]  + '_GSI     ' + self.textCtrl1_12.GetValue() + '       ' + self.textCtrl2_12.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :GSI\n" )
                counter=counter+1             
                            
            if self.checkBox13.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_13.GetValue()[0] + '_CAF     ' + self.textCtrl1_13.GetValue() + '       ' + self.textCtrl2_13.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :CAF\n" )
                counter=counter+1             
                            
            if self.checkBox14.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_14.GetValue()[0]  + '_SDW     ' + self.textCtrl1_14.GetValue() + '       ' + self.textCtrl2_14.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :SDW\n" )
                counter=counter+1             
                            
            if self.checkBox15.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_15.GetValue()[0]  + '_HMX     ' + self.textCtrl1_15.GetValue() + '       ' + self.textCtrl2_15.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :HMX\n" )
                counter=counter+1             
                            
            if self.checkBox16.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_16.GetValue()[0]  + '_RDMX     ' + self.textCtrl1_16.GetValue() + '       ' + self.textCtrl2_16.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :RDMX\n" )
                counter=counter+1             
                            
            if self.checkBox17.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_17.GetValue()[0]  + '_WAC2     ' + self.textCtrl1_17.GetValue() + '       ' + self.textCtrl2_17.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WAC2\n" )
                counter=counter+1             
                            
            if self.checkBox18.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_18.GetValue()[0]  + '_CNY     ' + self.textCtrl1_18.GetValue() + '       ' + self.textCtrl2_18.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :CNY\n" )
                counter=counter+1             
                                
            if self.checkBox19.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_19.GetValue()[0]  + '_CPY     ' + self.textCtrl1_19.GetValue() + '       ' + self.textCtrl2_19.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :CPY\n" )
                counter=counter+1             
                            
            if self.checkBox20.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_20.GetValue()[0]  + '_CKY     ' + self.textCtrl1_20.GetValue() + '       ' + self.textCtrl2_20.GetValue() + lineEnd)       
                fPar_Name.write(str(counter) + " :CKY\n" )
                counter=counter+1             
                            
            if self.checkBox21.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_21.GetValue()[0]  + '_WSYF     ' + self.textCtrl1_21.GetValue() + '       ' + self.textCtrl2_21.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WSYF\n" )
                counter=counter+1  
                            
            if self.checkBox22.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_22.GetValue()[0]  + '_PST     ' + self.textCtrl1_22.GetValue() + '       ' + self.textCtrl2_22.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PST\n" )
                counter=counter+1             
                            
            if self.checkBox23.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_23.GetValue()[0]  + '_CSTS     ' + self.textCtrl1_23.GetValue() + '       ' + self.textCtrl2_23.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :CSTS\n" )
                counter=counter+1  
                            
            if self.checkBox24.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_24.GetValue()[0]  + '_PRYG     ' + self.textCtrl1_24.GetValue() + '       ' + self.textCtrl2_24.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PRYG\n" )
                counter=counter+1             
                            
            if self.checkBox25.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_25.GetValue()[0]  + '_PRYF     ' + self.textCtrl1_25.GetValue() + '       ' + self.textCtrl2_25.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PRYF\n" )
                counter=counter+1             
                            
            if self.checkBox26.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_26.GetValue()[0] + '_WCY     ' + self.textCtrl1_26.GetValue() + '       ' + self.textCtrl2_26.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WCY\n" )
                counter=counter+1             
                            
            if self.checkBox27.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_27.GetValue()[0] + '_BN1     ' + self.textCtrl1_27.GetValue() + '       ' + self.textCtrl2_27.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BN1\n" )
                counter=counter+1            
                            
            if self.checkBox28.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_28.GetValue()[0]  + '_BN2     ' + self.textCtrl1_28.GetValue() + '       ' + self.textCtrl2_28.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BN2\n" )
                counter=counter+1             
                            
            if self.checkBox29.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_29.GetValue()[0]  + '_BN3     ' + self.textCtrl1_29.GetValue() + '       ' + self.textCtrl2_29.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BN3\n" )
                counter=counter+1             
                            
            if self.checkBox30.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_30.GetValue()[0]  + '_BP1     ' + self.textCtrl1_30.GetValue() + '       ' + self.textCtrl2_30.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BP1\n" )
                counter=counter+1             
                        
            if self.checkBox31.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_31.GetValue()[0]  + '_BP2     ' + self.textCtrl1_31.GetValue() + '       ' + self.textCtrl2_31.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BP2\n" )
                counter=counter+1            
                            
            if self.checkBox32.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_32.GetValue()[0]  + '_BP3     ' + self.textCtrl1_32.GetValue() + '       ' + self.textCtrl2_32.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BP3\n" )
                counter=counter+1             
                            
            if self.checkBox33.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_33.GetValue()[0]  + '_BK1     ' + self.textCtrl1_33.GetValue() + '       ' + self.textCtrl2_33.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BK1\n" )
                counter=counter+1             
                            
            if self.checkBox34.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_34.GetValue()[0]  + '_BW2     ' + self.textCtrl1_34.GetValue() + '       ' + self.textCtrl2_34.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BW2\n" )
                counter=counter+1             
                            
            if self.checkBox35.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_35.GetValue()[0]  + '_BK3     ' + self.textCtrl1_35.GetValue() + '       ' + self.textCtrl2_35.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BK3\n" )
                counter=counter+1            
                            
            if self.checkBox36.GetValue() == True:
                fPar_Name.write(str(counter) + " :BW1\n" )
                counter=counter+1             
                            
            if self.checkBox37.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_37.GetValue()[0]  + '_BW2     ' + self.textCtrl1_37.GetValue() + '       ' + self.textCtrl2_37.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BW2\n" )
                counter=counter+1             
                            
            if self.checkBox38.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_38.GetValue()[0]  + '_BW3     ' + self.textCtrl1_38.GetValue() + '       ' + self.textCtrl2_38.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BW3\n" )
                counter=counter+1             
                            
            if self.checkBox39.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_39.GetValue()[0]  + '_IDC     ' + self.textCtrl1_39.GetValue() + '       ' + self.textCtrl2_39.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :IDC\n" )
                            
            if self.checkBox40.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_40.GetValue()[0]  + '_FRST1     ' + self.textCtrl1_40.GetValue() + '       ' + self.textCtrl2_40.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FRST1\n" )
                counter=counter+1             
                                        
            if self.checkBox41.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_41.GetValue()[0]  + '_FRST2     ' + self.textCtrl1_41.GetValue() + '       ' + self.textCtrl2_41.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FRST2\n" )
                counter=counter+1                         
            
            if self.checkBox42.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_42.GetValue()[0]  + '_WAVP     ' + self.textCtrl1_42.GetValue() + '       ' + self.textCtrl2_42.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WAVP\n" )
                counter=counter+1             
                            
            if self.checkBox43.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_43.GetValue()[0]  + '_VPTH     ' + self.textCtrl1_43.GetValue() + '       ' + self.textCtrl2_43.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :VPTH\n" )
                counter=counter+1             
                            
            if self.checkBox44.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_44.GetValue()[0]  + '_VPD2     ' + self.textCtrl1_44.GetValue() + '       ' + self.textCtrl2_44.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :VPD2\n" )
                counter=counter+1 
                                            
            if self.checkBox45.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_45.GetValue()[0]  + '_RWPC1     ' + self.textCtrl1_45.GetValue() + '       ' + self.textCtrl2_45.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :RWPC1\n" )
                counter=counter+1             
                            
            if self.checkBox46.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_46.GetValue()[0]  + '_RWPC2     ' + self.textCtrl1_46.GetValue() + '       ' + self.textCtrl2_46.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :RWPC2\n" )
                            
            if self.checkBox47.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_47.GetValue()[0]  + '_GMHU     ' + self.textCtrl1_47.GetValue() + '       ' + self.textCtrl2_47.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :GMHU\n" )
                counter=counter+1             
                            
            if self.checkBox48.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_48.GetValue()[0]  + '_PPLP1     ' + self.textCtrl1_48.GetValue() + '       ' + self.textCtrl2_48.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PPLP1\n" )
                counter=counter+1             
                            
            if self.checkBox49.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_49.GetValue()[0]  + '_PPLP2     ' + self.textCtrl1_49.GetValue() + '       ' + self.textCtrl2_49.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :PPLP2\n" )
                counter=counter+1             
                            
            if self.checkBox50.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_50.GetValue()[0]  + '_STX1     ' + self.textCtrl1_50.GetValue() + '       ' + self.textCtrl2_50.GetValue() + lineEnd) 
                fPar_Name.write(str(counter) + " :STX1\n" )
                counter=counter+1  
                                       
            if self.checkBox51.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_51.GetValue()[0]  + '_STX2     ' + self.textCtrl1_51.GetValue() + '       ' + self.textCtrl2_51.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :STX2\n" )
                counter=counter+1             
                            
            if self.checkBox52.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_52.GetValue()[0]  + '_BLG1     ' + self.textCtrl1_52.GetValue() + '       ' + self.textCtrl2_52.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BLG1\n" )
                counter=counter+1             
                                
            if self.checkBox53.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_53.GetValue()[0] + '_BLG2     ' + self.textCtrl1_53.GetValue() + '       ' + self.textCtrl2_53.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :BLG2\n" )
                counter=counter+1             
                            
            if self.checkBox54.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_54.GetValue()[0] + '_WUB     ' + self.textCtrl1_54.GetValue() + '       ' + self.textCtrl2_54.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :WUB\n" )
                counter=counter+1            
                            
            if self.checkBox55.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_55.GetValue() + '_FT0     ' + self.textCtrl1_55.GetValue() + '       ' + self.textCtrl2_55.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FT0\n" )
                counter=counter+1             

            if self.checkBox56.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_56.GetValue() + '_FLT    ' + self.textCtrl1_56.GetValue() + '       ' + self.textCtrl2_56.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :FLT\n" )
                counter=counter+1                                                                                                                              
            fSufi2Parm.close()
            fPar_Name.close()

        dlg = wx.MessageDialog(self, 'SUFI2 sampleing parameters have been created!', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnButton2Button(self, event):
        ### Create the wrapper files for calibration
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
        dlg = wx.MessageDialog(self, 'Wrapper files have created for calibration!', 'SUFI2 Calibration', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnButton3Button(self, event):
        event.Skip()

    def OnButton4Button(self, event):
        event.Skip()
