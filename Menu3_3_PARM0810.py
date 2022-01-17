#Boa:Dialog:Dialog1

import wx, os, shutil
import subprocess, stat
import numpy as np
import platform
from shutil import copyfile

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, 
 
 wxID_DIALOG1CHECKBOX1,wxID_DIALOG1CHECKBOX2,wxID_DIALOG1CHECKBOX3,wxID_DIALOG1CHECKBOX4,wxID_DIALOG1CHECKBOX5,wxID_DIALOG1CHECKBOX7,wxID_DIALOG1CHECKBOX6,wxID_DIALOG1CHECKBOX8,wxID_DIALOG1CHECKBOX9,wxID_DIALOG1CHECKBOX10,
 wxID_DIALOG1CHECKBOX11,wxID_DIALOG1CHECKBOX12,wxID_DIALOG1CHECKBOX13,wxID_DIALOG1CHECKBOX14,wxID_DIALOG1CHECKBOX15,wxID_DIALOG1CHECKBOX16,wxID_DIALOG1CHECKBOX17,wxID_DIALOG1CHECKBOX18,wxID_DIALOG1CHECKBOX19,wxID_DIALOG1CHECKBOX20,
 wxID_DIALOG1CHECKBOX21,wxID_DIALOG1CHECKBOX22,wxID_DIALOG1CHECKBOX23,wxID_DIALOG1CHECKBOX24,wxID_DIALOG1CHECKBOX25,wxID_DIALOG1CHECKBOX26,wxID_DIALOG1CHECKBOX27,wxID_DIALOG1CHECKBOX28,wxID_DIALOG1CHECKBOX29,wxID_DIALOG1CHECKBOX30, 
 wxID_DIALOG1CHECKBOX31,wxID_DIALOG1CHECKBOX32,wxID_DIALOG1CHECKBOX33,wxID_DIALOG1CHECKBOX34,wxID_DIALOG1CHECKBOX35,wxID_DIALOG1CHECKBOX36,wxID_DIALOG1CHECKBOX37,wxID_DIALOG1CHECKBOX38,wxID_DIALOG1CHECKBOX39,wxID_DIALOG1CHECKBOX40, 
 wxID_DIALOG1CHECKBOX41,wxID_DIALOG1CHECKBOX42,wxID_DIALOG1CHECKBOX43,wxID_DIALOG1CHECKBOX44, wxID_DIALOG1CHECKBOX45,wxID_DIALOG1CHECKBOX46,wxID_DIALOG1CHECKBOX47,wxID_DIALOG1CHECKBOX48,wxID_DIALOG1CHECKBOX49,wxID_DIALOG1CHECKBOX50,
 wxID_DIALOG1CHECKBOX51,wxID_DIALOG1CHECKBOX52,wxID_DIALOG1CHECKBOX53,wxID_DIALOG1CHECKBOX54,wxID_DIALOG1CHECKBOX55,wxID_DIALOG1CHECKBOX56,wxID_DIALOG1CHECKBOX57,wxID_DIALOG1CHECKBOX58,wxID_DIALOG1CHECKBOX59,
 wxID_DIALOG1CHECKBOX60,wxID_DIALOG1CHECKBOX61,wxID_DIALOG1CHECKBOX62,wxID_DIALOG1CHECKBOX63,wxID_DIALOG1CHECKBOX64,wxID_DIALOG1CHECKBOX65,wxID_DIALOG1CHECKBOX66,wxID_DIALOG1CHECKBOX67,wxID_DIALOG1CHECKBOX68,
 wxID_DIALOG1CHECKBOX69,wxID_DIALOG1CHECKBOX70,wxID_DIALOG1CHECKBOX71,wxID_DIALOG1CHECKBOX72,wxID_DIALOG1CHECKBOX73,wxID_DIALOG1CHECKBOX74,wxID_DIALOG1CHECKBOX75,wxID_DIALOG1CHECKBOX76,wxID_DIALOG1CHECKBOX77,
 wxID_DIALOG1CHECKBOX78,wxID_DIALOG1CHECKBOX79,wxID_DIALOG1CHECKBOX80,wxID_DIALOG1CHECKBOX81,wxID_DIALOG1CHECKBOX82,wxID_DIALOG1CHECKBOX83,wxID_DIALOG1CHECKBOX84,wxID_DIALOG1CHECKBOX85,

wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2,wxID_DIALOG1STATICTEXT3,wxID_DIALOG1STATICTEXT4,wxID_DIALOG1STATICTEXT5,wxID_DIALOG1STATICTEXT6,wxID_DIALOG1STATICTEXT7,wxID_DIALOG1STATICTEXT8,
 wxID_DIALOG1STATICTEXT9,wxID_DIALOG1STATICTEXT10,

wxID_DIALOG1TEXTCTRL1,wxID_DIALOG1TEXTCTRL2, wxID_DIALOG1TEXTCTRL3, wxID_DIALOG1TEXTCTRL4, wxID_DIALOG1TEXTCTRL5, wxID_DIALOG1TEXTCTRL6, wxID_DIALOG1TEXTCTRL7, wxID_DIALOG1TEXTCTRL8,
wxID_DIALOG1TEXTCTRL9,wxID_DIALOG1TEXTCTRL10, wxID_DIALOG1TEXTCTRL11, wxID_DIALOG1TEXTCTRL12, wxID_DIALOG1TEXTCTRL13, wxID_DIALOG1TEXTCTRL14, wxID_DIALOG1TEXTCTRL15, wxID_DIALOG1TEXTCTRL16,
wxID_DIALOG1TEXTCTRL17,wxID_DIALOG1TEXTCTRL18, wxID_DIALOG1TEXTCTRL19, wxID_DIALOG1TEXTCTRL20, wxID_DIALOG1TEXTCTRL21, wxID_DIALOG1TEXTCTRL22, wxID_DIALOG1TEXTCTRL23, wxID_DIALOG1TEXTCTRL24,
wxID_DIALOG1TEXTCTRL25,wxID_DIALOG1TEXTCTRL26, wxID_DIALOG1TEXTCTRL27, wxID_DIALOG1TEXTCTRL28, wxID_DIALOG1TEXTCTRL29, wxID_DIALOG1TEXTCTRL30, wxID_DIALOG1TEXTCTRL31, wxID_DIALOG1TEXTCTRL32,
wxID_DIALOG1TEXTCTRL33,wxID_DIALOG1TEXTCTRL34, wxID_DIALOG1TEXTCTRL35, wxID_DIALOG1TEXTCTRL36, wxID_DIALOG1TEXTCTRL37, wxID_DIALOG1TEXTCTRL38, wxID_DIALOG1TEXTCTRL39, wxID_DIALOG1TEXTCTRL40,
wxID_DIALOG1TEXTCTRL41,wxID_DIALOG1TEXTCTRL42, wxID_DIALOG1TEXTCTRL43, wxID_DIALOG1TEXTCTRL44, wxID_DIALOG1TEXTCTRL45, wxID_DIALOG1TEXTCTRL46, wxID_DIALOG1TEXTCTRL47, wxID_DIALOG1TEXTCTRL48,
wxID_DIALOG1TEXTCTRL49,wxID_DIALOG1TEXTCTRL50, wxID_DIALOG1TEXTCTRL51, wxID_DIALOG1TEXTCTRL52, wxID_DIALOG1TEXTCTRL53, wxID_DIALOG1TEXTCTRL54, wxID_DIALOG1TEXTCTRL55,wxID_DIALOG1TEXTCTRL56,
wxID_DIALOG1TEXTCTRL57,wxID_DIALOG1TEXTCTRL58,wxID_DIALOG1TEXTCTRL59,wxID_DIALOG1TEXTCTRL60,wxID_DIALOG1TEXTCTRL61,wxID_DIALOG1TEXTCTRL62,wxID_DIALOG1TEXTCTRL63,wxID_DIALOG1TEXTCTRL64,
wxID_DIALOG1TEXTCTRL65,wxID_DIALOG1TEXTCTRL66,wxID_DIALOG1TEXTCTRL67,wxID_DIALOG1TEXTCTRL68,wxID_DIALOG1TEXTCTRL69,wxID_DIALOG1TEXTCTRL70,wxID_DIALOG1TEXTCTRL71,wxID_DIALOG1TEXTCTRL72,
wxID_DIALOG1TEXTCTRL73,wxID_DIALOG1TEXTCTRL74,wxID_DIALOG1TEXTCTRL75,wxID_DIALOG1TEXTCTRL76,wxID_DIALOG1TEXTCTRL77,wxID_DIALOG1TEXTCTRL78,wxID_DIALOG1TEXTCTRL79,wxID_DIALOG1TEXTCTRL80,
wxID_DIALOG1TEXTCTRL81,wxID_DIALOG1TEXTCTRL82,wxID_DIALOG1TEXTCTRL83,wxID_DIALOG1TEXTCTRL84,wxID_DIALOG1TEXTCTRL85,
                                
wxID_DIALOG1TEXTCTRL1_1,wxID_DIALOG1TEXTCTRL1_2, wxID_DIALOG1TEXTCTRL1_3, wxID_DIALOG1TEXTCTRL1_4, wxID_DIALOG1TEXTCTRL1_5, wxID_DIALOG1TEXTCTRL1_6, wxID_DIALOG1TEXTCTRL1_7, wxID_DIALOG1TEXTCTRL1_8,
wxID_DIALOG1TEXTCTRL1_9,wxID_DIALOG1TEXTCTRL1_10, wxID_DIALOG1TEXTCTRL1_11, wxID_DIALOG1TEXTCTRL1_12, wxID_DIALOG1TEXTCTRL1_13, wxID_DIALOG1TEXTCTRL1_14, wxID_DIALOG1TEXTCTRL1_15, wxID_DIALOG1TEXTCTRL1_16,
wxID_DIALOG1TEXTCTRL1_17,wxID_DIALOG1TEXTCTRL1_18, wxID_DIALOG1TEXTCTRL1_19, wxID_DIALOG1TEXTCTRL1_20, wxID_DIALOG1TEXTCTRL1_21, wxID_DIALOG1TEXTCTRL1_22, wxID_DIALOG1TEXTCTRL1_23, wxID_DIALOG1TEXTCTRL1_24,
wxID_DIALOG1TEXTCTRL1_25,wxID_DIALOG1TEXTCTRL1_26, wxID_DIALOG1TEXTCTRL1_27, wxID_DIALOG1TEXTCTRL1_28, wxID_DIALOG1TEXTCTRL1_29, wxID_DIALOG1TEXTCTRL1_30, wxID_DIALOG1TEXTCTRL1_31, wxID_DIALOG1TEXTCTRL1_32,
wxID_DIALOG1TEXTCTRL1_33,wxID_DIALOG1TEXTCTRL1_34, wxID_DIALOG1TEXTCTRL1_35, wxID_DIALOG1TEXTCTRL1_36, wxID_DIALOG1TEXTCTRL1_37, wxID_DIALOG1TEXTCTRL1_38, wxID_DIALOG1TEXTCTRL1_39, wxID_DIALOG1TEXTCTRL1_40,
wxID_DIALOG1TEXTCTRL1_41,wxID_DIALOG1TEXTCTRL1_42, wxID_DIALOG1TEXTCTRL1_43, wxID_DIALOG1TEXTCTRL1_44, wxID_DIALOG1TEXTCTRL1_45, wxID_DIALOG1TEXTCTRL1_46, wxID_DIALOG1TEXTCTRL1_47, wxID_DIALOG1TEXTCTRL1_48,
wxID_DIALOG1TEXTCTRL1_49,wxID_DIALOG1TEXTCTRL1_50, wxID_DIALOG1TEXTCTRL1_51, wxID_DIALOG1TEXTCTRL1_52, wxID_DIALOG1TEXTCTRL1_53, wxID_DIALOG1TEXTCTRL1_54, wxID_DIALOG1TEXTCTRL1_55,wxID_DIALOG1TEXTCTRL1_56,
wxID_DIALOG1TEXTCTRL1_57,wxID_DIALOG1TEXTCTRL1_58,wxID_DIALOG1TEXTCTRL1_59,wxID_DIALOG1TEXTCTRL1_60,wxID_DIALOG1TEXTCTRL1_61,wxID_DIALOG1TEXTCTRL1_62,wxID_DIALOG1TEXTCTRL1_63,wxID_DIALOG1TEXTCTRL1_64,
wxID_DIALOG1TEXTCTRL1_65,wxID_DIALOG1TEXTCTRL1_66,wxID_DIALOG1TEXTCTRL1_67,wxID_DIALOG1TEXTCTRL1_68,wxID_DIALOG1TEXTCTRL1_69,wxID_DIALOG1TEXTCTRL1_70,wxID_DIALOG1TEXTCTRL1_71,wxID_DIALOG1TEXTCTRL1_72,
wxID_DIALOG1TEXTCTRL1_73,wxID_DIALOG1TEXTCTRL1_74,wxID_DIALOG1TEXTCTRL1_75,wxID_DIALOG1TEXTCTRL1_76,wxID_DIALOG1TEXTCTRL1_77,wxID_DIALOG1TEXTCTRL1_78,wxID_DIALOG1TEXTCTRL1_79,wxID_DIALOG1TEXTCTRL1_80,
wxID_DIALOG1TEXTCTRL1_81,wxID_DIALOG1TEXTCTRL1_82,wxID_DIALOG1TEXTCTRL1_83,wxID_DIALOG1TEXTCTRL1_84,wxID_DIALOG1TEXTCTRL1_85,

wxID_DIALOG1TEXTCTRL2_1,wxID_DIALOG1TEXTCTRL2_2, wxID_DIALOG1TEXTCTRL2_3, wxID_DIALOG1TEXTCTRL2_4, wxID_DIALOG1TEXTCTRL2_5, wxID_DIALOG1TEXTCTRL2_6, wxID_DIALOG1TEXTCTRL2_7, wxID_DIALOG1TEXTCTRL2_8,
wxID_DIALOG1TEXTCTRL2_9,wxID_DIALOG1TEXTCTRL2_10, wxID_DIALOG1TEXTCTRL2_11, wxID_DIALOG1TEXTCTRL2_12, wxID_DIALOG1TEXTCTRL2_13, wxID_DIALOG1TEXTCTRL2_14, wxID_DIALOG1TEXTCTRL2_15, wxID_DIALOG1TEXTCTRL2_16,
wxID_DIALOG1TEXTCTRL2_17,wxID_DIALOG1TEXTCTRL2_18, wxID_DIALOG1TEXTCTRL2_19, wxID_DIALOG1TEXTCTRL2_20, wxID_DIALOG1TEXTCTRL2_21, wxID_DIALOG1TEXTCTRL2_22, wxID_DIALOG1TEXTCTRL2_23, wxID_DIALOG1TEXTCTRL2_24,
wxID_DIALOG1TEXTCTRL2_25,wxID_DIALOG1TEXTCTRL2_26, wxID_DIALOG1TEXTCTRL2_27, wxID_DIALOG1TEXTCTRL2_28, wxID_DIALOG1TEXTCTRL2_29, wxID_DIALOG1TEXTCTRL2_30, wxID_DIALOG1TEXTCTRL2_31, wxID_DIALOG1TEXTCTRL2_32,
wxID_DIALOG1TEXTCTRL2_33,wxID_DIALOG1TEXTCTRL2_34, wxID_DIALOG1TEXTCTRL2_35, wxID_DIALOG1TEXTCTRL2_36, wxID_DIALOG1TEXTCTRL2_37, wxID_DIALOG1TEXTCTRL2_38, wxID_DIALOG1TEXTCTRL2_39, wxID_DIALOG1TEXTCTRL2_40,
wxID_DIALOG1TEXTCTRL2_41,wxID_DIALOG1TEXTCTRL2_42, wxID_DIALOG1TEXTCTRL2_43, wxID_DIALOG1TEXTCTRL2_44, wxID_DIALOG1TEXTCTRL2_45, wxID_DIALOG1TEXTCTRL2_46, wxID_DIALOG1TEXTCTRL2_47, wxID_DIALOG1TEXTCTRL2_48,
wxID_DIALOG1TEXTCTRL2_49,wxID_DIALOG1TEXTCTRL2_50, wxID_DIALOG1TEXTCTRL2_51, wxID_DIALOG1TEXTCTRL2_52, wxID_DIALOG1TEXTCTRL2_53, wxID_DIALOG1TEXTCTRL2_54, wxID_DIALOG1TEXTCTRL2_55,wxID_DIALOG1TEXTCTRL2_56,
wxID_DIALOG1TEXTCTRL2_57,wxID_DIALOG1TEXTCTRL2_58,wxID_DIALOG1TEXTCTRL2_59,wxID_DIALOG1TEXTCTRL2_60,wxID_DIALOG1TEXTCTRL2_61,wxID_DIALOG1TEXTCTRL2_62,wxID_DIALOG1TEXTCTRL2_63,wxID_DIALOG1TEXTCTRL2_64,
wxID_DIALOG1TEXTCTRL2_65,wxID_DIALOG1TEXTCTRL2_66,wxID_DIALOG1TEXTCTRL2_67,wxID_DIALOG1TEXTCTRL2_68,wxID_DIALOG1TEXTCTRL2_69,wxID_DIALOG1TEXTCTRL2_70,wxID_DIALOG1TEXTCTRL2_71,wxID_DIALOG1TEXTCTRL2_72,
wxID_DIALOG1TEXTCTRL2_73,wxID_DIALOG1TEXTCTRL2_74,wxID_DIALOG1TEXTCTRL2_75,wxID_DIALOG1TEXTCTRL2_76,wxID_DIALOG1TEXTCTRL2_77,wxID_DIALOG1TEXTCTRL2_78,wxID_DIALOG1TEXTCTRL2_79,wxID_DIALOG1TEXTCTRL2_80,
wxID_DIALOG1TEXTCTRL2_81,wxID_DIALOG1TEXTCTRL2_82,wxID_DIALOG1TEXTCTRL2_83,wxID_DIALOG1TEXTCTRL2_84,wxID_DIALOG1TEXTCTRL2_85,

wxID_DIALOG2COMBOBOX1_1,wxID_DIALOG2COMBOBOX1_2,wxID_DIALOG2COMBOBOX1_3,wxID_DIALOG2COMBOBOX1_4,wxID_DIALOG2COMBOBOX1_5,wxID_DIALOG2COMBOBOX1_6,wxID_DIALOG2COMBOBOX1_7,wxID_DIALOG2COMBOBOX1_8,
wxID_DIALOG2COMBOBOX1_9,wxID_DIALOG2COMBOBOX1_10,wxID_DIALOG2COMBOBOX1_11,wxID_DIALOG2COMBOBOX1_12,wxID_DIALOG2COMBOBOX1_13,wxID_DIALOG2COMBOBOX1_14,wxID_DIALOG2COMBOBOX1_15,wxID_DIALOG2COMBOBOX1_16,
wxID_DIALOG2COMBOBOX1_17,wxID_DIALOG2COMBOBOX1_18,wxID_DIALOG2COMBOBOX1_19,wxID_DIALOG2COMBOBOX1_20,wxID_DIALOG2COMBOBOX1_21,wxID_DIALOG2COMBOBOX1_22,wxID_DIALOG2COMBOBOX1_23,wxID_DIALOG2COMBOBOX1_24,
wxID_DIALOG2COMBOBOX1_25,wxID_DIALOG2COMBOBOX1_26,wxID_DIALOG2COMBOBOX1_27,wxID_DIALOG2COMBOBOX1_28,wxID_DIALOG2COMBOBOX1_29,wxID_DIALOG2COMBOBOX1_30,wxID_DIALOG2COMBOBOX1_31,wxID_DIALOG2COMBOBOX1_32,
wxID_DIALOG2COMBOBOX1_33,wxID_DIALOG2COMBOBOX1_34,wxID_DIALOG2COMBOBOX1_35,wxID_DIALOG2COMBOBOX1_36,wxID_DIALOG2COMBOBOX1_37,wxID_DIALOG2COMBOBOX1_38,wxID_DIALOG2COMBOBOX1_39,wxID_DIALOG2COMBOBOX1_40,
wxID_DIALOG2COMBOBOX1_41,wxID_DIALOG2COMBOBOX1_42,wxID_DIALOG2COMBOBOX1_43,wxID_DIALOG2COMBOBOX1_44,wxID_DIALOG2COMBOBOX1_45,wxID_DIALOG2COMBOBOX1_46,wxID_DIALOG2COMBOBOX1_47,wxID_DIALOG2COMBOBOX1_48,
wxID_DIALOG2COMBOBOX1_49,wxID_DIALOG2COMBOBOX1_50,wxID_DIALOG2COMBOBOX1_51,wxID_DIALOG2COMBOBOX1_52,wxID_DIALOG2COMBOBOX1_53,wxID_DIALOG2COMBOBOX1_54,wxID_DIALOG2COMBOBOX1_55,wxID_DIALOG2COMBOBOX1_56,
wxID_DIALOG2COMBOBOX1_57,wxID_DIALOG2COMBOBOX1_58,wxID_DIALOG2COMBOBOX1_59,wxID_DIALOG2COMBOBOX1_60,wxID_DIALOG2COMBOBOX1_61,wxID_DIALOG2COMBOBOX1_62,wxID_DIALOG2COMBOBOX1_63,wxID_DIALOG2COMBOBOX1_64,
wxID_DIALOG2COMBOBOX1_65,wxID_DIALOG2COMBOBOX1_66,wxID_DIALOG2COMBOBOX1_67,wxID_DIALOG2COMBOBOX1_68,wxID_DIALOG2COMBOBOX1_69,wxID_DIALOG2COMBOBOX1_70,wxID_DIALOG2COMBOBOX1_71,wxID_DIALOG2COMBOBOX1_72,
wxID_DIALOG2COMBOBOX1_73,wxID_DIALOG2COMBOBOX1_74,wxID_DIALOG2COMBOBOX1_75,wxID_DIALOG2COMBOBOX1_76,wxID_DIALOG2COMBOBOX1_77,wxID_DIALOG2COMBOBOX1_78,wxID_DIALOG2COMBOBOX1_79,wxID_DIALOG2COMBOBOX1_80,
wxID_DIALOG2COMBOBOX1_81,wxID_DIALOG2COMBOBOX1_82,wxID_DIALOG2COMBOBOX1_83,wxID_DIALOG2COMBOBOX1_84,wxID_DIALOG2COMBOBOX1_85] = [wx.NewId() for _init_ctrls in range(437)]

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
        
        parent.AddWindow(self.checkBox57, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_57, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl57, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_57, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_57, 0, border=0, flag=0)
        
        parent.AddWindow(self.checkBox58, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_58, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl58, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_58, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_58, 0, border=0, flag=0)                                                        
    
        parent.AddWindow(self.checkBox59, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_59, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl59, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_59, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_59, 0, border=0, flag=0)     
    
        parent.AddWindow(self.checkBox60, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_60, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl60, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_60, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_60, 0, border=0, flag=0)     
    
        parent.AddWindow(self.checkBox61, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_61, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl61, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_61, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_61, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox62, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_62, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl62, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_62, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_62, 0, border=0, flag=0)    
    
        parent.AddWindow(self.checkBox63, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_63, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl63, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_63, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_63, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox64, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_64, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl64, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_64, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_64, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox65, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_65, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl65, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_65, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_65, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox66, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_66, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl66, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_66, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_66, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox67, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_67, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl67, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_67, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_67, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox68, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_68, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl68, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_68, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_68, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox69, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_69, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl69, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_69, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_69, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox70, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_70, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl70, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_70, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_70, 0, border=0, flag=0)        
    
        parent.AddWindow(self.checkBox71, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_71, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl71, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_71, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_71, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox72, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_72, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl72, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_72, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_72, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox73, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_73, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl73, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_73, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_73, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox74, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_74, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl74, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_74, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_74, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox75, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_75, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl75, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_75, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_75, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox76, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_76, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl76, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_76, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_76, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox77, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_77, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl77, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_77, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_77, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox78, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_78, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl78, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_78, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_78, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox79, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_79, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl79, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_79, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_79, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox80, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_80, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl80, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_80, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_80, 0, border=0, flag=0)       
    
        parent.AddWindow(self.checkBox81, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_81, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl81, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_81, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_81, 0, border=0, flag=0)   
        
        parent.AddWindow(self.checkBox82, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_82, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl82, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_82, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_82, 0, border=0, flag=0)               
                
        parent.AddWindow(self.checkBox83, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_83, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl83, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_83, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_83, 0, border=0, flag=0)                       

        parent.AddWindow(self.checkBox84, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_84, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl84, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_84, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_84, 0, border=0, flag=0)               
                
        parent.AddWindow(self.checkBox85, 0, border=0, flag=0)
        parent.AddWindow(self.comboBox1_85, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl85, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1_85, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl2_85, 0, border=0, flag=0)                                                                                      
                                                                                                                
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
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,pos=wx.Point(0, 0), size=wx.Size(800, 850),style=wx.DEFAULT_DIALOG_STYLE,title=u'EPIC parameters')
        self.SetClientSize(wx.Size(850, 953))
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
        self.comboBox1_57 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_57, parent=self, size=wx.Size(90, 21), style=0)        
        self.comboBox1_58 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_58, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_59 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_59, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_60 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_60, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_61 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_61, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_62 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_62, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_63 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_63, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_64 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_64, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_65 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_65, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_66 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_66, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_67 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_67, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_68 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_68, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_69 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_69, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_70 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_70, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_71 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_71, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_72 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_72, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_73 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_73, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_74 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_74, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_75 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_75, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_76 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_76, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_77 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_77, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_78 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_78, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_79 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_79, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_80 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_80, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_81 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_81, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_82 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_82, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_83 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_83, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_84 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_84, parent=self, size=wx.Size(90, 21), style=0)
        self.comboBox1_85 = wx.ComboBox(choices=[], id=wxID_DIALOG2COMBOBOX1_85, parent=self, size=wx.Size(90, 21), style=0)
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
        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1, label=u'PARM01', name='checkBox1', parent=self, size=wx.Size(80, 20), style=wx.ALIGN_LEFT)
        self.checkBox2 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX2, label=u'PARM02', name='checkBox2', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox3 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX3, label=u'PARM03', name='checkBox3', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox4 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX4, label=u'PARM04', name='checkBox4', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox5 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX5, label=u'PARM05',name='checkBox5', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox6 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX6, label=u'PARM06', name='checkBox6', parent=self, size=wx.Size(80, 20), style=wx.CAPTION)
        self.checkBox7 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX7, label=u'PARM07', name='checkBox7', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox8 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX8, label=u'PARM08', name='checkBox8', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox9 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX9, label=u'PARM09',name='checkBox9', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox10 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX10, label=u'PARM10', name='checkBox10', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox11 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX11, label=u'PARM11',name='checkBox11', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox12 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX12, label=u'PARM12', name='checkBox12', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox13 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX13, label=u'PARM13', name='checkBox13', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox14 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX14, label=u'PARM14', name='checkBox14', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox15 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX15, label=u'PARM15', name='checkBox15', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox16 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX16, label=u'PARM16', name='checkBox16', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox17 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX17, label=u'PARM17',name='checkBox17', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox18 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX18, label=u'PARM18',  name='checkBox18', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox19 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX19, label=u'PARM19',name='checkBox19', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox20 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX20, label=u'PARM20',name='checkBox20', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox21 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX21, label=u'PARM21', name='checkBox21', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox22 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX22, label=u'PARM22',name='checkBox22', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox23 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX23, label=u'PARM23',name='checkBox23', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox24 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX24, label=u'PARM24', name='checkBox24', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox25 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX25, label=u'PARM25', name='checkBox25', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox26 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX26, label=u'PARM26',name='checkBox26', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox27 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX27, label=u'PARM27', name='checkBox27', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox28 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX28, label=u'PARM28', name='checkBox28', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox29 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX29, label=u'PARM29', name='checkBox29', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox30 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX30, label=u'PARM30',  name='checkBox30', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox31 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX31, label=u'PARM31',  name='checkBox31', parent=self,  size=wx.Size(80, 20), style=0)
        self.checkBox32 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX32, label=u'PARM32', name='checkBox32', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox33 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX33, label=u'PARM33',name='checkBox33', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox34 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX34, label=u'PARM34',name='checkBox34', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox35 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX35, label=u'PARM35',name='checkBox35', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox36 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX36, label=u'PARM36',name='checkBox36', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox37 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX37, label=u'PARM37',name='checkBox37', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox38 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX38, label=u'PARM38',name='checkBox38', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox39 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX39, label=u'PARM39',name='checkBox39', parent=self,size=wx.Size(80, 20), style=0)
        self.checkBox40 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX40, label=u'PARM40',name='checkBox40', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox41 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX41, label=u'PARM41',name='checkBox41', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox42 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX42, label=u'PARM42',name='checkBox42', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox43 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX43, label=u'PARM43',name='checkBox43', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox44 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX44, label=u'PARM44',name='checkBox44', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox45 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX45, label=u'PRAM45',name='checkBox45', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox46 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX46, label=u'PARM46',name='checkBox46', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox47 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX47, label=u'PARM47',name='checkBox47', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox48 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX48, label=u'PARM48', name='checkBox48', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox49 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX49, label=u'PARM49',name='checkBox49', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox50 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX50, label=u'PARM50',name='checkBox50', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox51 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX51, label=u'PARM51', name='checkBox51', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox52 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX52, label=u'PARM52', name='checkBox52', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox53 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX53, label=u'PARM53',name='checkBox53', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox54 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX54, label=u'PARM54', name='checkBox54', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox55 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX55, label=u'PARM55', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox56 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX56, label=u'PARM56',name='checkBox56', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox57 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX57, label=u'PARM57', name='checkBox51', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox58 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX58, label=u'PARM58', name='checkBox52', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox59 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX59, label=u'PARM59',name='checkBox59', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox60 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX60, label=u'PARM60', name='checkBox54', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox61 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX61, label=u'PARM61', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox62 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX62, label=u'PARM62', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox63 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX63, label=u'APRM63', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox64 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX64, label=u'PARM64', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox65 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX65, label=u'PARM65', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox66 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX66, label=u'PARM66', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox67 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX67, label=u'PARM67', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox68 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX68, label=u'PARM68', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox69 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX69, label=u'PARM69', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox70 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX70, label=u'PARM70', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox71 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX71, label=u'PARM71', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox72 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX72, label=u'PARM72', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox73 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX73, label=u'PARM73', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox74 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX74, label=u'PARM74', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox75 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX75, label=u'PARM75', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox76 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX76, label=u'PARM76', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox77 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX77, label=u'PARM77', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox78 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX78, label=u'PARM78', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox79 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX79, label=u'PARM79', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox80 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX80, label=u'PARM80', name='checkBox55', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox81 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX81, label=u'PARM81', name='checkBox81', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox82 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX82, label=u'PARM82', name='checkBox82', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox83 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX83, label=u'PARM83', name='checkBox83', parent=self, size=wx.Size(80, 20), style=0)   
        self.checkBox84 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX84, label=u'PARM84', name='checkBox82', parent=self, size=wx.Size(80, 20), style=0)
        self.checkBox85 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX85, label=u'PARM85', name='checkBox83', parent=self, size=wx.Size(80, 20), style=0)         
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
        self.textCtrl56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL56,name='textCtrl56', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl46')
        self.textCtrl57 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL57,name='textCtrl57', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl47')
        self.textCtrl58 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL58,name='textCtrl58', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl48')
        self.textCtrl59 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL59, name='textCtrl59', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl49')
        self.textCtrl60 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL60, name='textCtrl50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl50')
        self.textCtrl61 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL61, name='textCtrl51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl51')
        self.textCtrl62 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL62, name='textCtrl52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl52')
        self.textCtrl63 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL63, name='textCtrl63', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl53')
        self.textCtrl64 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL64,  name='textCtrl64', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl54')
        self.textCtrl65 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL65, name='textCtrl65', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl55')
        self.textCtrl66 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL66,name='textCtrl66', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl46')
        self.textCtrl67 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL67,name='textCtrl67', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl47')
        self.textCtrl68 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL68,name='textCtrl68', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl48')
        self.textCtrl69 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL69, name='textCtrl69', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl49')
        self.textCtrl70 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL70, name='textCtrl70', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl50')
        self.textCtrl71 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL71, name='textCtrl71', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl51')
        self.textCtrl72 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL72, name='textCtrl72', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl52')
        self.textCtrl73 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL73, name='textCtrl73', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl53')
        self.textCtrl74 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL74,  name='textCtrl74', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl54')
        self.textCtrl75 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL75, name='textCtrl75', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl55')
        self.textCtrl76 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL76,name='textCtrl76', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl46')
        self.textCtrl77 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL77,name='textCtrl77', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl47')
        self.textCtrl78 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL78,name='textCtrl78', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl48')
        self.textCtrl79 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL79, name='textCtrl79', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl49')
        self.textCtrl80 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL80, name='textCtrl80', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl50')
        self.textCtrl81 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL81, name='textCtrl81', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl51')
        self.textCtrl82 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL82, name='textCtrl82', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl52')
        self.textCtrl83 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL83, name='textCtrl83', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl53')
        self.textCtrl84 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL84, name='textCtrl84', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl52')
        self.textCtrl85 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL85, name='textCtrl85', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl85')

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
        self.textCtrl1_56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_56,name='textCtrl1_46', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0, value='textCtrl1_46')
        self.textCtrl1_57 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_57,name='textCtrl1_47', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_47')
        self.textCtrl1_58 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_58,name='textCtrl1_48', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_48')
        self.textCtrl1_59 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_59, name='textCtrl1_49', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_49')
        self.textCtrl1_60 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_50, name='textCtrl1_50', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_50')
        self.textCtrl1_61 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_61, name='textCtrl1_51', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_51')
        self.textCtrl1_62 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_62, name='textCtrl1_52', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_52')
        self.textCtrl1_63 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_63, name='textCtrl1_53', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_53')
        self.textCtrl1_64 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_64,  name='textCtrl1_64', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_54')
        self.textCtrl1_65 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_65, name='textCtrl1_65', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_55')
        self.textCtrl1_66 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_66,name='textCtrl1_46', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0)
        self.textCtrl1_67 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_67,name='textCtrl1_47', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_47')
        self.textCtrl1_68 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_68,name='textCtrl1_48', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_48')
        self.textCtrl1_69 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_69, name='textCtrl1_49', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_49')
        self.textCtrl1_70 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_70, name='textCtrl1_50', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_50')
        self.textCtrl1_71 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_71, name='textCtrl1_51', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_51')
        self.textCtrl1_72 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_72, name='textCtrl1_52', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_52')
        self.textCtrl1_73 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_73, name='textCtrl1_53', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_53')
        self.textCtrl1_74 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_74,  name='textCtrl1_54', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_54')
        self.textCtrl1_75 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_75, name='textCtrl1_55', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_55')
        self.textCtrl1_76 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_76,name='textCtrl1_46', parent=self, pos=wx.Point(310, 440),size=wx.Size(80, 20), style=0)
        self.textCtrl1_77 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_77,name='textCtrl1_47', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_47')
        self.textCtrl1_78 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_78,name='textCtrl1_48', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_48')
        self.textCtrl1_79 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_79, name='textCtrl1_49', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_49')
        self.textCtrl1_80 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_80, name='textCtrl1_50', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_50')
        self.textCtrl1_81 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_81, name='textCtrl1_51', parent=self, size=wx.Size(80, 20), style=0, value='textCtrl1_51')
        self.textCtrl1_82 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_82, name='textCtrl1_52', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_52')        
        self.textCtrl1_83 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_83, name='textCtrl1_83', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_52')                
        self.textCtrl1_84 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_84, name='textCtrl1_84', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_83')        
        self.textCtrl1_85 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1_85, name='textCtrl1_85', parent=self,  size=wx.Size(80, 20), style=0, value='textCtrl1_85') 

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
        self.textCtrl2_56 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_56,name='textCtrl2_46', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl2_46')
        self.textCtrl2_57 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_57,name='textCtrl2_47', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_47')
        self.textCtrl2_58 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_58,name='textCtrl2_48', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_48')
        self.textCtrl2_59 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_59, name='textCtrl2_49', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_49')
        self.textCtrl2_60 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_60, name='textCtrl2_50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_50')
        self.textCtrl2_61 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_61, name='textCtrl2_51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl2_51')
        self.textCtrl2_62 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_62, name='textCtrl2_52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_52')
        self.textCtrl2_63 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_63, name='textCtrl2_53', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_53')
        self.textCtrl2_64 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_64,  name='textCtrl2_54', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl2_54')
        self.textCtrl2_65 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_65, name='textCtrl2_55', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl2_55')
        self.textCtrl2_66 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_66,name='textCtrl2_46', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl2_46')
        self.textCtrl2_67 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_67,name='textCtrl2_47', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_47')
        self.textCtrl2_68 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_68,name='textCtrl2_48', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_48')
        self.textCtrl2_69 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_69, name='textCtrl2_49', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_49')
        self.textCtrl2_70 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_70, name='textCtrl2_50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_50')
        self.textCtrl2_71 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_71, name='textCtrl2_51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl2_51')
        self.textCtrl2_72 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_72, name='textCtrl2_52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_52')
        self.textCtrl2_73 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_73, name='textCtrl2_53', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_53')
        self.textCtrl2_74 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_74,  name='textCtrl2_54', parent=self, pos=wx.Point(50, 240),size=wx.Size(80, 20), style=0, value='textCtrl2_54')
        self.textCtrl2_75 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_75, name='textCtrl2_55', parent=self, pos=wx.Point(310, 240), size=wx.Size(80, 20), style=0, value='textCtrl2_55')        
        self.textCtrl2_76 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_76,name='textCtrl2_46', parent=self, pos=wx.Point(50, 200), size=wx.Size(80, 20), style=0, value='textCtrl2_46')
        self.textCtrl2_77 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_77,name='textCtrl2_47', parent=self, pos=wx.Point(310, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_47')
        self.textCtrl2_78 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_78,name='textCtrl2_48', parent=self, pos=wx.Point(570, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_48')
        self.textCtrl2_79 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_79, name='textCtrl2_49', parent=self, pos=wx.Point(830, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_49')
        self.textCtrl2_80 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_80, name='textCtrl2_50', parent=self, pos=wx.Point(1090, 200),size=wx.Size(80, 20), style=0, value='textCtrl2_50')
        self.textCtrl2_81 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_81, name='textCtrl2_51', parent=self, pos=wx.Point(50, 220),  size=wx.Size(80, 20), style=0, value='textCtrl2_51')
        self.textCtrl2_82 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_82, name='textCtrl2_52', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_52')
        self.textCtrl2_83 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_83, name='textCtrl2_53', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_53')
        self.textCtrl2_84 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_84, name='textCtrl2_84', parent=self, pos=wx.Point(310, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_52')
        self.textCtrl2_85 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2_85, name='textCtrl2_85', parent=self, pos=wx.Point(570, 220), size=wx.Size(80, 20), style=0, value='textCtrl2_85')

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
        self.comboBox1_57.SetItems(TOP)  
        self.comboBox1_58.SetItems(TOP)  
        self.comboBox1_59.SetItems(TOP)  
        self.comboBox1_60.SetItems(TOP)  
        self.comboBox1_61.SetItems(TOP)  
        self.comboBox1_62.SetItems(TOP)  
        self.comboBox1_63.SetItems(TOP)  
        self.comboBox1_64.SetItems(TOP)  
        self.comboBox1_65.SetItems(TOP)  
        self.comboBox1_66.SetItems(TOP)  
        self.comboBox1_67.SetItems(TOP)  
        self.comboBox1_68.SetItems(TOP)  
        self.comboBox1_69.SetItems(TOP)  
        self.comboBox1_70.SetItems(TOP)  
        self.comboBox1_71.SetItems(TOP)  
        self.comboBox1_72.SetItems(TOP)  
        self.comboBox1_73.SetItems(TOP)  
        self.comboBox1_74.SetItems(TOP)  
        self.comboBox1_75.SetItems(TOP)          
        self.comboBox1_76.SetItems(TOP)  
        self.comboBox1_77.SetItems(TOP)  
        self.comboBox1_78.SetItems(TOP)  
        self.comboBox1_79.SetItems(TOP)  
        self.comboBox1_80.SetItems(TOP)  
        self.comboBox1_81.SetItems(TOP)  
        self.comboBox1_82.SetItems(TOP)  
        self.comboBox1_83.SetItems(TOP)                   
        self.comboBox1_84.SetItems(TOP)  
        self.comboBox1_85.SetItems(TOP)  
        with open('modelGUISetup.inf','r') as file:
            ADD=file.readlines() 
        with open(ADD[13].strip(os.linesep)  +'\\PARM0810.DAT','r') as file:
            data=file.readlines()                                             
        Default1=data[30].split() 
        Default2=data[31].split()       
        Default3=data[32].split() 
        Default4=data[33].split() 
        Default5=data[34].split()       
        Default6=data[35].split() 
        Default7=data[36].split() 
        Default8=data[37].split()       
        Default9=data[38].split()           
        fSetup = open('Parameterization_Setup.inf', readCode)
        loopNum = 1
        for txtLine in fSetup:
            if loopNum == 71:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox1.SetValue(True)
                else:
                    self.checkBox1.SetValue(False)
                self.comboBox1_1.SetValue(txtLine.split(',')[1])
                self.textCtrl1.SetValue(Default1[0])
                self.textCtrl1_1.SetValue(txtLine.split(',')[3])
                self.textCtrl2_1.SetValue(txtLine.split(',')[4])
            if loopNum == 72:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox2.SetValue(True)
                else:
                    self.checkBox2.SetValue(False)
                self.comboBox1_2.SetValue(txtLine.split(',')[1])
                self.textCtrl2.SetValue(Default1[1])
                self.textCtrl1_2.SetValue(txtLine.split(',')[3])
                self.textCtrl2_2.SetValue(txtLine.split(',')[4])                
            if loopNum == 73:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox3.SetValue(True)
                else:
                    self.checkBox3.SetValue(False)
                self.comboBox1_3.SetValue(txtLine.split(',')[1])
                self.textCtrl3.SetValue(Default1[2])
                self.textCtrl1_3.SetValue(txtLine.split(',')[3])
                self.textCtrl2_3.SetValue(txtLine.split(',')[4])
            if loopNum == 74:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox4.SetValue(True)
                else:
                    self.checkBox4.SetValue(False)
                self.comboBox1_4.SetValue(txtLine.split(',')[1])
                self.textCtrl4.SetValue(Default1[3])
                self.textCtrl1_4.SetValue(txtLine.split(',')[3])
                self.textCtrl2_4.SetValue(txtLine.split(',')[4])
            
            if loopNum == 75:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox5.SetValue(True)
                else:
                    self.checkBox5.SetValue(False)
                self.comboBox1_5.SetValue(txtLine.split(',')[1])
                self.textCtrl5.SetValue(Default1[4])
                self.textCtrl1_5.SetValue(txtLine.split(',')[3])
                self.textCtrl2_5.SetValue(txtLine.split(',')[4])            
            if loopNum == 76:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox6.SetValue(True)
                else:
                    self.checkBox6.SetValue(False)
                self.comboBox1_6.SetValue(txtLine.split(',')[1])
                self.textCtrl6.SetValue(Default1[5])
                self.textCtrl1_6.SetValue(txtLine.split(',')[3])
                self.textCtrl2_6.SetValue(txtLine.split(',')[4])
            if loopNum == 77:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox7.SetValue(True)
                else:
                    self.checkBox7.SetValue(False)
                self.comboBox1_7.SetValue(txtLine.split(',')[1])
                self.textCtrl7.SetValue(Default1[6])
                self.textCtrl1_7.SetValue(txtLine.split(',')[3])
                self.textCtrl2_7.SetValue(txtLine.split(',')[4])                                        
            if loopNum == 78:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox8.SetValue(True)
                else:
                    self.checkBox8.SetValue(False)
                self.comboBox1_8.SetValue(txtLine.split(',')[1])
                self.textCtrl8.SetValue(Default1[7])
                self.textCtrl1_8.SetValue(txtLine.split(',')[3])
                self.textCtrl2_8.SetValue(txtLine.split(',')[4])            
            if loopNum == 79:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox9.SetValue(True)
                else:
                    self.checkBox9.SetValue(False)
                self.comboBox1_9.SetValue(txtLine.split(',')[1])
                self.textCtrl9.SetValue(Default1[8])
                self.textCtrl1_9.SetValue(txtLine.split(',')[3])
                self.textCtrl2_9.SetValue(txtLine.split(',')[4])            
            if loopNum == 80:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox10.SetValue(True)
                else:
                    self.checkBox10.SetValue(False)
                self.comboBox1_10.SetValue(txtLine.split(',')[1])
                self.textCtrl10.SetValue(Default1[9])
                self.textCtrl1_10.SetValue(txtLine.split(',')[3])
                self.textCtrl2_10.SetValue(txtLine.split(',')[4])            
            if loopNum == 81:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox11.SetValue(True)
                else:
                    self.checkBox11.SetValue(False)
                self.comboBox1_11.SetValue(txtLine.split(',')[1])
                self.textCtrl11.SetValue(Default2[0])
                self.textCtrl1_11.SetValue(txtLine.split(',')[3])
                self.textCtrl2_11.SetValue(txtLine.split(',')[4])            
            if loopNum == 82:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox12.SetValue(True)
                else:
                    self.checkBox12.SetValue(False)
                self.comboBox1_12.SetValue(txtLine.split(',')[1])
                self.textCtrl12.SetValue(Default2[1])
                self.textCtrl1_12.SetValue(txtLine.split(',')[3])
                self.textCtrl2_12.SetValue(txtLine.split(',')[4])            
            if loopNum == 83:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox13.SetValue(True)
                else:
                    self.checkBox13.SetValue(False)
                self.comboBox1_13.SetValue(txtLine.split(',')[1])
                self.textCtrl13.SetValue(Default2[2])
                self.textCtrl1_13.SetValue(txtLine.split(',')[3])
                self.textCtrl2_13.SetValue(txtLine.split(',')[4])            
            if loopNum == 84:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox14.SetValue(True)
                else:
                    self.checkBox14.SetValue(False)
                self.comboBox1_14.SetValue(txtLine.split(',')[1])
                self.textCtrl14.SetValue(Default2[3])
                self.textCtrl1_14.SetValue(txtLine.split(',')[3])
                self.textCtrl2_14.SetValue(txtLine.split(',')[4])                
            if loopNum == 85:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox15.SetValue(True)
                else:
                    self.checkBox15.SetValue(False)
                self.comboBox1_15.SetValue(txtLine.split(',')[1])
                self.textCtrl15.SetValue(Default2[4])
                self.textCtrl1_15.SetValue(txtLine.split(',')[3])
                self.textCtrl2_15.SetValue(txtLine.split(',')[4])                    
            if loopNum == 86:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox16.SetValue(True)
                else:
                    self.checkBox16.SetValue(False)
                self.comboBox1_16.SetValue(txtLine.split(',')[1])
                self.textCtrl16.SetValue(Default2[5])
                self.textCtrl1_16.SetValue(txtLine.split(',')[3])
                self.textCtrl2_16.SetValue(txtLine.split(',')[4])    
            if loopNum == 87:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox17.SetValue(True)
                else:
                    self.checkBox17.SetValue(False)
                self.comboBox1_17.SetValue(txtLine.split(',')[1])
                self.textCtrl17.SetValue(Default2[6])
                self.textCtrl1_17.SetValue(txtLine.split(',')[3])
                self.textCtrl2_17.SetValue(txtLine.split(',')[4]) 
            if loopNum == 88:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox18.SetValue(True)
                else:
                    self.checkBox18.SetValue(False)
                self.comboBox1_18.SetValue(txtLine.split(',')[1])
                self.textCtrl18.SetValue(Default2[7])
                self.textCtrl1_18.SetValue(txtLine.split(',')[3])
                self.textCtrl2_18.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                     
            if loopNum == 89:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox19.SetValue(True)
                else:
                    self.checkBox19.SetValue(False)
                self.comboBox1_19.SetValue(txtLine.split(',')[1])
                self.textCtrl19.SetValue(Default2[8])
                self.textCtrl1_19.SetValue(txtLine.split(',')[3])
                self.textCtrl2_19.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                     
            if loopNum == 90:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox20.SetValue(True)
                else:
                    self.checkBox20.SetValue(False)
                self.comboBox1_20.SetValue(txtLine.split(',')[1])
                self.textCtrl20.SetValue(Default2[9])
                self.textCtrl1_20.SetValue(txtLine.split(',')[3])
                self.textCtrl2_20.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            if loopNum == 91:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox21.SetValue(True)
                else:
                    self.checkBox21.SetValue(False)
                self.comboBox1_21.SetValue(txtLine.split(',')[1])
                self.textCtrl21.SetValue(Default3[0])
                self.textCtrl1_21.SetValue(txtLine.split(',')[3])
                self.textCtrl2_21.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if loopNum == 92:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox22.SetValue(True)
                else:
                    self.checkBox22.SetValue(False)
                self.comboBox1_22.SetValue(txtLine.split(',')[1])
                self.textCtrl22.SetValue(Default3[1])
                self.textCtrl1_22.SetValue(txtLine.split(',')[3])
                self.textCtrl2_22.SetValue(txtLine.split(',')[4])                                                                                                                                                        
            if loopNum == 93:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox23.SetValue(True)
                else:
                    self.checkBox23.SetValue(False)
                self.comboBox1_23.SetValue(txtLine.split(',')[1])
                self.textCtrl23.SetValue(Default3[2])
                self.textCtrl1_23.SetValue(txtLine.split(',')[3])
                self.textCtrl2_23.SetValue(txtLine.split(',')[4])                            
            if loopNum == 94:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox24.SetValue(True)
                else:
                    self.checkBox24.SetValue(False)
                self.comboBox1_24.SetValue(txtLine.split(',')[1])
                self.textCtrl24.SetValue(Default3[3])
                self.textCtrl1_24.SetValue(txtLine.split(',')[3])
                self.textCtrl2_24.SetValue(txtLine.split(',')[4])                            
            if loopNum == 95:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox25.SetValue(True)
                else:
                    self.checkBox25.SetValue(False)
                self.comboBox1_25.SetValue(txtLine.split(',')[1])
                self.textCtrl25.SetValue(Default3[4])
                self.textCtrl1_25.SetValue(txtLine.split(',')[3])
                self.textCtrl2_25.SetValue(txtLine.split(',')[4])                
            if loopNum == 96:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox26.SetValue(True)
                else:
                    self.checkBox26.SetValue(False)
                self.comboBox1_26.SetValue(txtLine.split(',')[1])
                self.textCtrl26.SetValue(Default3[5])
                self.textCtrl1_26.SetValue(txtLine.split(',')[3])
                self.textCtrl2_26.SetValue(txtLine.split(',')[4])                
            if loopNum == 97:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox27.SetValue(True)
                else:
                    self.checkBox27.SetValue(False)
                self.comboBox1_27.SetValue(txtLine.split(',')[1])
                self.textCtrl27.SetValue(Default3[6])
                self.textCtrl1_27.SetValue(txtLine.split(',')[3])
                self.textCtrl2_27.SetValue(txtLine.split(',')[4])                
            if loopNum == 98:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox28.SetValue(True)
                else:
                    self.checkBox28.SetValue(False)
                self.comboBox1_28.SetValue(txtLine.split(',')[1])
                self.textCtrl28.SetValue(Default3[7])
                self.textCtrl1_28.SetValue(txtLine.split(',')[3])
                self.textCtrl2_28.SetValue(txtLine.split(',')[4])                
            if loopNum == 99:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox29.SetValue(True)
                else:
                    self.checkBox29.SetValue(False)
                self.comboBox1_29.SetValue(txtLine.split(',')[1])
                self.textCtrl29.SetValue(Default3[8])
                self.textCtrl1_29.SetValue(txtLine.split(',')[3])
                self.textCtrl2_29.SetValue(txtLine.split(',')[4])   
            if loopNum == 100:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox30.SetValue(True)
                else:
                    self.checkBox30.SetValue(False)
                self.comboBox1_30.SetValue(txtLine.split(',')[1])
                self.textCtrl30.SetValue(Default3[9])
                self.textCtrl1_30.SetValue(txtLine.split(',')[3])
                self.textCtrl2_30.SetValue(txtLine.split(',')[4])                                                 
            if loopNum == 101:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox31.SetValue(True)
                else:
                    self.checkBox31.SetValue(False)
                self.comboBox1_31.SetValue(txtLine.split(',')[1])
                self.textCtrl31.SetValue(Default4[0])
                self.textCtrl1_31.SetValue(txtLine.split(',')[3])
                self.textCtrl2_31.SetValue(txtLine.split(',')[4])                                                                                                                               
            if loopNum ==102:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox32.SetValue(True)
                else:
                    self.checkBox32.SetValue(False)
                self.comboBox1_32.SetValue(txtLine.split(',')[1])
                self.textCtrl32.SetValue(Default4[1])
                self.textCtrl1_32.SetValue(txtLine.split(',')[3])
                self.textCtrl2_32.SetValue(txtLine.split(',')[4])                                                                                                                                                                                   
            if loopNum == 103:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox33.SetValue(True)
                else:
                    self.checkBox33.SetValue(False)
                self.comboBox1_33.SetValue(txtLine.split(',')[1])
                self.textCtrl33.SetValue(Default4[2])
                self.textCtrl1_33.SetValue(txtLine.split(',')[3])
                self.textCtrl2_33.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                    
            if loopNum == 104:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox34.SetValue(True)
                else:
                    self.checkBox34.SetValue(False)
                self.comboBox1_34.SetValue(txtLine.split(',')[1])
                self.textCtrl34.SetValue(Default4[3])
                self.textCtrl1_34.SetValue(txtLine.split(',')[3])
                self.textCtrl2_34.SetValue(txtLine.split(',')[4])                            
            if loopNum == 105:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox35.SetValue(True)
                else:
                    self.checkBox35.SetValue(False)
                self.comboBox1_35.SetValue(txtLine.split(',')[1])
                self.textCtrl35.SetValue(Default4[4])
                self.textCtrl1_35.SetValue(txtLine.split(',')[3])
                self.textCtrl2_35.SetValue(txtLine.split(',')[4])                            
            if loopNum == 106:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox36.SetValue(True)
                else:
                    self.checkBox36.SetValue(False)
                self.comboBox1_36.SetValue(txtLine.split(',')[1])
                self.textCtrl36.SetValue(Default4[5])
                self.textCtrl1_36.SetValue(txtLine.split(',')[3])
                self.textCtrl2_36.SetValue(txtLine.split(',')[4])                            
            if loopNum == 107:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox37.SetValue(True)
                else:
                    self.checkBox37.SetValue(False)
                self.comboBox1_37.SetValue(txtLine.split(',')[1])
                self.textCtrl37.SetValue(Default4[6])
                self.textCtrl1_37.SetValue(txtLine.split(',')[3])
                self.textCtrl2_37.SetValue(txtLine.split(',')[4])                            
            if loopNum == 108:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox38.SetValue(True)
                else:
                    self.checkBox38.SetValue(False)
                self.comboBox1_38.SetValue(txtLine.split(',')[1])
                self.textCtrl38.SetValue(Default4[7])
                self.textCtrl1_38.SetValue(txtLine.split(',')[3])
                self.textCtrl2_38.SetValue(txtLine.split(',')[4])                            
            if loopNum == 109:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox39.SetValue(True)
                else:
                    self.checkBox39.SetValue(False)
                self.comboBox1_39.SetValue(txtLine.split(',')[1])
                self.textCtrl39.SetValue(Default4[8])
                self.textCtrl1_39.SetValue(txtLine.split(',')[3])
                self.textCtrl2_39.SetValue(txtLine.split(',')[4])                            
            if loopNum == 110:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox40.SetValue(True)
                else:
                    self.checkBox40.SetValue(False)
                self.comboBox1_40.SetValue(txtLine.split(',')[1])
                self.textCtrl40.SetValue(Default4[9])
                self.textCtrl1_40.SetValue(txtLine.split(',')[3])
                self.textCtrl2_40.SetValue(txtLine.split(',')[4])                    
            if loopNum == 111:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox41.SetValue(True)
                else:
                    self.checkBox41.SetValue(False)
                self.comboBox1_41.SetValue(txtLine.split(',')[1])
                self.textCtrl41.SetValue(Default5[0])
                self.textCtrl1_41.SetValue(txtLine.split(',')[3])
                self.textCtrl2_41.SetValue(txtLine.split(',')[4])                                                        
            if loopNum == 112:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox42.SetValue(True)
                else:
                    self.checkBox42.SetValue(False)
                self.comboBox1_42.SetValue(txtLine.split(',')[1])
                self.textCtrl42.SetValue(Default5[1])
                self.textCtrl1_42.SetValue(txtLine.split(',')[3])
                self.textCtrl2_42.SetValue(txtLine.split(',')[4])                            
            if loopNum == 113:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox43.SetValue(True)
                else:
                    self.checkBox43.SetValue(False)
                self.comboBox1_43.SetValue(txtLine.split(',')[1])
                self.textCtrl43.SetValue(Default5[2])
                self.textCtrl1_43.SetValue(txtLine.split(',')[3])
                self.textCtrl2_43.SetValue(txtLine.split(',')[4])                            
            if loopNum == 114:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox44.SetValue(True)
                else:
                    self.checkBox44.SetValue(False)
                self.comboBox1_44.SetValue(txtLine.split(',')[1])
                self.textCtrl44.SetValue(Default5[3])
                self.textCtrl1_44.SetValue(txtLine.split(',')[3])
                self.textCtrl2_44.SetValue(txtLine.split(',')[4])                            
            if loopNum == 115:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox45.SetValue(True)
                else:
                    self.checkBox45.SetValue(False)
                self.comboBox1_45.SetValue(txtLine.split(',')[1])
                self.textCtrl45.SetValue(Default5[4])
                self.textCtrl1_45.SetValue(txtLine.split(',')[3])
                self.textCtrl2_45.SetValue(txtLine.split(',')[4])                   
            if loopNum == 116:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox46.SetValue(True)
                else:
                    self.checkBox46.SetValue(False)
                self.comboBox1_46.SetValue(txtLine.split(',')[1])
                self.textCtrl46.SetValue(Default5[5])
                self.textCtrl1_46.SetValue(txtLine.split(',')[3])
                self.textCtrl2_46.SetValue(txtLine.split(',')[4])                                                                  
            if loopNum == 117:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox47.SetValue(True)
                else:
                    self.checkBox47.SetValue(False)
                self.comboBox1_47.SetValue(txtLine.split(',')[1])
                self.textCtrl47.SetValue(Default5[6])
                self.textCtrl1_47.SetValue(txtLine.split(',')[3])
                self.textCtrl2_47.SetValue(txtLine.split(',')[4])                                                                                                                  
            if loopNum == 118:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox48.SetValue(True)
                else:
                    self.checkBox48.SetValue(False)
                self.comboBox1_48.SetValue(txtLine.split(',')[1])
                self.textCtrl48.SetValue(Default5[7])
                self.textCtrl1_48.SetValue(txtLine.split(',')[3])
                self.textCtrl2_48.SetValue(txtLine.split(',')[4])                                                                                                        
            if loopNum == 119:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox49.SetValue(True)
                else:
                    self.checkBox49.SetValue(False)
                self.comboBox1_49.SetValue(txtLine.split(',')[1])
                self.textCtrl49.SetValue(Default5[8])
                self.textCtrl1_49.SetValue(txtLine.split(',')[3])
                self.textCtrl2_49.SetValue(txtLine.split(',')[4])                
            if loopNum == 120:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox50.SetValue(True)
                else:
                    self.checkBox50.SetValue(False)
                self.comboBox1_50.SetValue(txtLine.split(',')[1])
                self.textCtrl50.SetValue(Default5[9])
                self.textCtrl1_50.SetValue(txtLine.split(',')[3])
                self.textCtrl2_50.SetValue(txtLine.split(',')[4])    
            if loopNum == 121:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox51.SetValue(True)
                else:
                    self.checkBox51.SetValue(False)
                self.comboBox1_51.SetValue(txtLine.split(',')[1])
                self.textCtrl51.SetValue(Default6[0])
                self.textCtrl1_51.SetValue(txtLine.split(',')[3])
                self.textCtrl2_51.SetValue(txtLine.split(',')[4])                                                
            if loopNum == 122:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox52.SetValue(True)
                else:
                    self.checkBox52.SetValue(False)
                self.comboBox1_52.SetValue(txtLine.split(',')[1])
                self.textCtrl52.SetValue(Default6[1])
                self.textCtrl1_52.SetValue(txtLine.split(',')[3])
                self.textCtrl2_52.SetValue(txtLine.split(',')[4])                                                                    
            if loopNum == 123:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox53.SetValue(True)
                else:
                    self.checkBox53.SetValue(False)
                self.comboBox1_53.SetValue(txtLine.split(',')[1])
                self.textCtrl53.SetValue(Default6[2])
                self.textCtrl1_53.SetValue(txtLine.split(',')[3])
                self.textCtrl2_53.SetValue(txtLine.split(',')[4])                
            if loopNum == 124:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox54.SetValue(True)
                else:
                    self.checkBox54.SetValue(False)
                self.comboBox1_54.SetValue(txtLine.split(',')[1])
                self.textCtrl54.SetValue(Default6[3])
                self.textCtrl1_54.SetValue(txtLine.split(',')[3])
                self.textCtrl2_54.SetValue(txtLine.split(',')[4])                
            if loopNum == 125:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox55.SetValue(True)
                else:
                    self.checkBox55.SetValue(False)
                self.comboBox1_55.SetValue(txtLine.split(',')[1])
                self.textCtrl55.SetValue(Default6[4])
                self.textCtrl1_55.SetValue(txtLine.split(',')[3])
                self.textCtrl2_55.SetValue(txtLine.split(',')[4])                
            if loopNum == 126:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox56.SetValue(True)
                else:
                    self.checkBox56.SetValue(False)
                self.comboBox1_56.SetValue(txtLine.split(',')[1])
                self.textCtrl56.SetValue(Default6[5])
                self.textCtrl1_56.SetValue(txtLine.split(',')[3])
                self.textCtrl2_56.SetValue(txtLine.split(',')[4])                                         
                                    
            if loopNum == 127:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox57.SetValue(True)
                else:
                    self.checkBox57.SetValue(False)
                self.comboBox1_57.SetValue(txtLine.split(',')[1])
                self.textCtrl57.SetValue(Default6[6])
                self.textCtrl1_57.SetValue(txtLine.split(',')[3])
                self.textCtrl2_57.SetValue(txtLine.split(',')[4])                                                     
                                                            
            if loopNum == 128:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox58.SetValue(True)
                else:
                    self.checkBox58.SetValue(False)
                self.comboBox1_58.SetValue(txtLine.split(',')[1])
                self.textCtrl58.SetValue(Default6[7])
                self.textCtrl1_58.SetValue(txtLine.split(',')[3])
                self.textCtrl2_58.SetValue(txtLine.split(',')[4])                                                                             
                                                                                    
            if loopNum == 129:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox59.SetValue(True)
                else:
                    self.checkBox59.SetValue(False)
                self.comboBox1_59.SetValue(txtLine.split(',')[1])
                self.textCtrl59.SetValue(Default6[8])
                self.textCtrl1_59.SetValue(txtLine.split(',')[3])
                self.textCtrl2_59.SetValue(txtLine.split(',')[4])                                                                                                     
                                                                                                            
            if loopNum == 130:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox60.SetValue(True)
                else:
                    self.checkBox60.SetValue(False)
                self.comboBox1_60.SetValue(txtLine.split(',')[1])
                self.textCtrl60.SetValue(Default6[9])
                self.textCtrl1_60.SetValue(txtLine.split(',')[3])
                self.textCtrl2_60.SetValue(txtLine.split(',')[4])                                                                                                                             
                                                                                                                                    
            if loopNum == 131:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox61.SetValue(True)
                else:
                    self.checkBox61.SetValue(False)
                self.comboBox1_61.SetValue(txtLine.split(',')[1])
                self.textCtrl61.SetValue(Default7[0])
                self.textCtrl1_61.SetValue(txtLine.split(',')[3])
                self.textCtrl2_61.SetValue(txtLine.split(',')[4])                                                                                                                                                   
                                                                                                                                                            
            if loopNum == 132:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox62.SetValue(True)
                else:
                    self.checkBox62.SetValue(False)
                self.comboBox1_62.SetValue(txtLine.split(',')[1])
                self.textCtrl62.SetValue(Default7[1])
                self.textCtrl1_62.SetValue(txtLine.split(',')[3])
                self.textCtrl2_62.SetValue(txtLine.split(',')[4])                                                                                                                                                                           
                                                                                                                                                                                    
            if loopNum == 133:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox63.SetValue(True)
                else:
                    self.checkBox63.SetValue(False)
                self.comboBox1_63.SetValue(txtLine.split(',')[1])
                self.textCtrl63.SetValue(Default7[2])
                self.textCtrl1_63.SetValue(txtLine.split(',')[3])
                self.textCtrl2_63.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                  
                                                                                                                                                                                                            
            if loopNum == 134:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox64.SetValue(True)
                else:
                    self.checkBox64.SetValue(False)
                self.comboBox1_64.SetValue(txtLine.split(',')[1])
                self.textCtrl64.SetValue(Default7[3])
                self.textCtrl1_64.SetValue(txtLine.split(',')[3])
                self.textCtrl2_64.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                          
                                                                                                                                                                                                                                    
            if loopNum == 135:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox65.SetValue(True)
                else:
                    self.checkBox65.SetValue(False)
                self.comboBox1_65.SetValue(txtLine.split(',')[1])
                self.textCtrl65.SetValue(Default7[4])
                self.textCtrl1_65.SetValue(txtLine.split(',')[3])
                self.textCtrl2_65.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                  

            if loopNum == 136:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox66.SetValue(True)
                else:
                    self.checkBox66.SetValue(False)
                self.comboBox1_66.SetValue(txtLine.split(',')[1])
                self.textCtrl66.SetValue(Default7[5])
                self.textCtrl1_66.SetValue(txtLine.split(',')[3])
                self.textCtrl2_66.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            if loopNum == 137:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox67.SetValue(True)
                else:
                    self.checkBox67.SetValue(False)
                self.comboBox1_67.SetValue(txtLine.split(',')[1])
                self.textCtrl67.SetValue(Default7[6])
                self.textCtrl1_67.SetValue(txtLine.split(',')[3])
                self.textCtrl2_67.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            if loopNum == 138:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox68.SetValue(True)
                else:
                    self.checkBox68.SetValue(False)
                self.comboBox1_68.SetValue(txtLine.split(',')[1])
                self.textCtrl68.SetValue(Default7[7])
                self.textCtrl1_68.SetValue(txtLine.split(',')[3])
                self.textCtrl2_68.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            if loopNum == 139:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox69.SetValue(True)
                else:
                    self.checkBox69.SetValue(False)
                self.comboBox1_69.SetValue(txtLine.split(',')[1])
                self.textCtrl69.SetValue(Default7[8])
                self.textCtrl1_69.SetValue(txtLine.split(',')[3])
                self.textCtrl2_69.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            if loopNum == 140:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox70.SetValue(True)
                else:
                    self.checkBox70.SetValue(False)
                self.comboBox1_70.SetValue(txtLine.split(',')[1])
                self.textCtrl70.SetValue(Default7[9])
                self.textCtrl1_70.SetValue(txtLine.split(',')[3])
                self.textCtrl2_70.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            if loopNum == 141:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox71.SetValue(True)
                else:
                    self.checkBox71.SetValue(False)
                self.comboBox1_71.SetValue(txtLine.split(',')[1])
                self.textCtrl71.SetValue(Default8[0])
                self.textCtrl1_71.SetValue(txtLine.split(',')[3])
                self.textCtrl2_71.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            if loopNum == 142:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox72.SetValue(True)
                else:
                    self.checkBox72.SetValue(False)
                self.comboBox1_72.SetValue(txtLine.split(',')[1])
                self.textCtrl72.SetValue(Default8[1])
                self.textCtrl1_72.SetValue(txtLine.split(',')[3])
                self.textCtrl2_72.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            if loopNum == 143:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox73.SetValue(True)
                else:
                    self.checkBox73.SetValue(False)
                self.comboBox1_73.SetValue(txtLine.split(',')[1])
                self.textCtrl73.SetValue(Default8[2])
                self.textCtrl1_73.SetValue(txtLine.split(',')[3])
                self.textCtrl2_73.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if loopNum == 144:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox74.SetValue(True)
                else:
                    self.checkBox74.SetValue(False)
                self.comboBox1_74.SetValue(txtLine.split(',')[1])
                self.textCtrl74.SetValue(Default8[3])
                self.textCtrl1_74.SetValue(txtLine.split(',')[3])
                self.textCtrl2_74.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                                                       
            
            if loopNum == 145:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox75.SetValue(True)
                else:
                    self.checkBox75.SetValue(False)
                self.comboBox1_75.SetValue(txtLine.split(',')[1])
                self.textCtrl75.SetValue(Default8[4])
                self.textCtrl1_75.SetValue(txtLine.split(',')[3])
                self.textCtrl2_75.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 146:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox76.SetValue(True)
                else:
                    self.checkBox76.SetValue(False)
                self.comboBox1_76.SetValue(txtLine.split(',')[1])
                self.textCtrl76.SetValue(Default8[5])
                self.textCtrl1_76.SetValue(txtLine.split(',')[3])
                self.textCtrl2_76.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 147:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox77.SetValue(True)
                else:
                    self.checkBox77.SetValue(False)
                self.comboBox1_77.SetValue(txtLine.split(',')[1])
                self.textCtrl77.SetValue(Default8[6])
                self.textCtrl1_77.SetValue(txtLine.split(',')[3])
                self.textCtrl2_77.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 148:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox78.SetValue(True)
                else:
                    self.checkBox78.SetValue(False)
                self.comboBox1_78.SetValue(txtLine.split(',')[1])
                self.textCtrl78.SetValue(Default8[7])
                self.textCtrl1_78.SetValue(txtLine.split(',')[3])
                self.textCtrl2_78.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 149:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox79.SetValue(True)
                else:
                    self.checkBox79.SetValue(False)
                self.comboBox1_79.SetValue(txtLine.split(',')[1])
                self.textCtrl79.SetValue(Default8[8])
                self.textCtrl1_79.SetValue(txtLine.split(',')[3])
                self.textCtrl2_79.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 150:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox80.SetValue(True)
                else:
                    self.checkBox80.SetValue(False)
                self.comboBox1_80.SetValue(txtLine.split(',')[1])
                self.textCtrl80.SetValue(Default8[9])
                self.textCtrl1_80.SetValue(txtLine.split(',')[3])
                self.textCtrl2_80.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 151:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox81.SetValue(True)
                else:
                    self.checkBox81.SetValue(False)
                self.comboBox1_81.SetValue(txtLine.split(',')[1])
                self.textCtrl81.SetValue(Default9[0])
                self.textCtrl1_81.SetValue(txtLine.split(',')[3])
                self.textCtrl2_81.SetValue(txtLine.split(',')[4])               
            
            if loopNum == 152:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox82.SetValue(True)
                else:
                    self.checkBox82.SetValue(False)
                self.comboBox1_82.SetValue(txtLine.split(',')[1])
                self.textCtrl82.SetValue(Default9[1])
                self.textCtrl1_82.SetValue(txtLine.split(',')[3])
                self.textCtrl2_82.SetValue(txtLine.split(',')[4])    
                
            if loopNum == 153:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox83.SetValue(True)
                else:
                    self.checkBox83.SetValue(False)
                self.comboBox1_83.SetValue(txtLine.split(',')[1])
                self.textCtrl83.SetValue(Default9[2])
                self.textCtrl1_83.SetValue(txtLine.split(',')[3])
                self.textCtrl2_83.SetValue(txtLine.split(',')[4])
                  
            if loopNum == 154:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox84.SetValue(True)
                else:
                    self.checkBox84.SetValue(False)
                self.comboBox1_84.SetValue(txtLine.split(',')[1])
                self.textCtrl84.SetValue(Default9[3])
                self.textCtrl1_84.SetValue(txtLine.split(',')[3])
                self.textCtrl2_84.SetValue(txtLine.split(',')[4])                     

            if loopNum == 155:
                if txtLine.split(',')[0] == 'Y':
                    self.checkBox85.SetValue(True)
                else:
                    self.checkBox85.SetValue(False)
                self.comboBox1_85.SetValue(txtLine.split(',')[1])
                self.textCtrl85.SetValue(Default9[4])
                self.textCtrl1_85.SetValue(txtLine.split(',')[3])
                self.textCtrl2_85.SetValue(txtLine.split(',')[4])                                                                                                                                                                                                                                                             
            loopNum += 1
        fSetup.close()
        
    def OnDialog1Close(self, parent):
        if os.linesep == "\r\n":
            lineEnd = '\n'
            readCode = "r"
            pathSep = "/"
        elif os.linesep == "\n":
            lineEnd = os.linesep
            readCode = "U"
            pathSep = os.path.sep
        
        parent = self.GetParent()

        with open('Parameterization_Setup.inf','r') as file:
            data=file.readlines()        
        CROPdata=data[0:70]    
        f = open('Parameterization_Setup.inf', 'w')  
        for i in range(0, 70):
            f.write(CROPdata[i])
        
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
                
        if self.checkBox57.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_57.GetValue()+',')
        f.write(self.textCtrl57.GetValue() +',')
        f.write(self.textCtrl1_57.GetValue()+',')
        f.write(self.textCtrl2_57.GetValue()+',\n')            
        
        if self.checkBox58.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_58.GetValue()+',')
        f.write(self.textCtrl58.GetValue() +',')
        f.write(self.textCtrl1_58.GetValue()+',')
        f.write(self.textCtrl2_58.GetValue()+',\n')            
        
        if self.checkBox59.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_59.GetValue()+',')
        f.write(self.textCtrl59.GetValue() +',')
        f.write(self.textCtrl1_59.GetValue()+',')
        f.write(self.textCtrl2_59.GetValue()+',\n')         
        
        if self.checkBox60.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_60.GetValue()+',')
        f.write(self.textCtrl60.GetValue() +',')
        f.write(self.textCtrl1_60.GetValue()+',')
        f.write(self.textCtrl2_60.GetValue()+',\n')         
        
        if self.checkBox61.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_61.GetValue()+',')
        f.write(self.textCtrl61.GetValue() +',')
        f.write(self.textCtrl1_61.GetValue()+',')
        f.write(self.textCtrl2_61.GetValue()+',\n')         
                
        if self.checkBox62.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_62.GetValue()+',')
        f.write(self.textCtrl62.GetValue() +',')
        f.write(self.textCtrl1_62.GetValue()+',')
        f.write(self.textCtrl2_62.GetValue()+',\n')           
        
        if self.checkBox63.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_63.GetValue()+',')
        f.write(self.textCtrl63.GetValue() +',')
        f.write(self.textCtrl1_63.GetValue()+',')
        f.write(self.textCtrl2_63.GetValue()+',\n')          
        
        if self.checkBox64.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_64.GetValue()+',')
        f.write(self.textCtrl64.GetValue() +',')
        f.write(self.textCtrl1_64.GetValue()+',')
        f.write(self.textCtrl2_64.GetValue()+',\n')          
        
        if self.checkBox65.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_65.GetValue()+',')
        f.write(self.textCtrl65.GetValue() +',')
        f.write(self.textCtrl1_65.GetValue()+',')
        f.write(self.textCtrl2_65.GetValue()+',\n')          
        
        if self.checkBox66.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_66.GetValue()+',')
        f.write(self.textCtrl66.GetValue() +',')
        f.write(self.textCtrl1_66.GetValue()+',')
        f.write(self.textCtrl2_66.GetValue()+',\n')          
        
        if self.checkBox67.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_67.GetValue()+',')
        f.write(self.textCtrl67.GetValue() +',')
        f.write(self.textCtrl1_67.GetValue()+',')
        f.write(self.textCtrl2_67.GetValue()+',\n')          
        
        if self.checkBox68.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_68.GetValue()+',')
        f.write(self.textCtrl68.GetValue() +',')
        f.write(self.textCtrl1_68.GetValue()+',')
        f.write(self.textCtrl2_68.GetValue()+',\n')          
        
        if self.checkBox69.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_69.GetValue()+',')
        f.write(self.textCtrl69.GetValue() +',')
        f.write(self.textCtrl1_69.GetValue()+',')
        f.write(self.textCtrl2_69.GetValue()+',\n')          
        
        if self.checkBox70.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_70.GetValue()+',')
        f.write(self.textCtrl70.GetValue() +',')
        f.write(self.textCtrl1_70.GetValue()+',')
        f.write(self.textCtrl2_70.GetValue()+',\n')          
        
        if self.checkBox71.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_71.GetValue()+',')
        f.write(self.textCtrl71.GetValue() +',')
        f.write(self.textCtrl1_71.GetValue()+',')
        f.write(self.textCtrl2_71.GetValue()+',\n')          
                
        if self.checkBox72.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_72.GetValue()+',')
        f.write(self.textCtrl72.GetValue() +',')
        f.write(self.textCtrl1_72.GetValue()+',')
        f.write(self.textCtrl2_72.GetValue()+',\n')          
                
        if self.checkBox73.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_73.GetValue()+',')
        f.write(self.textCtrl73.GetValue() +',')
        f.write(self.textCtrl1_73.GetValue()+',')
        f.write(self.textCtrl2_73.GetValue()+',\n')          
                
        if self.checkBox74.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_74.GetValue()+',')
        f.write(self.textCtrl74.GetValue() +',')
        f.write(self.textCtrl1_74.GetValue()+',')
        f.write(self.textCtrl2_74.GetValue()+',\n')          
                
        if self.checkBox75.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_75.GetValue()+',')
        f.write(self.textCtrl75.GetValue() +',')
        f.write(self.textCtrl1_75.GetValue()+',')
        f.write(self.textCtrl2_75.GetValue()+',\n')            
        
        if self.checkBox76.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_76.GetValue()+',')
        f.write(self.textCtrl76.GetValue() +',')
        f.write(self.textCtrl1_76.GetValue()+',')
        f.write(self.textCtrl2_76.GetValue()+',\n')            
        
        if self.checkBox77.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_77.GetValue()+',')
        f.write(self.textCtrl77.GetValue() +',')
        f.write(self.textCtrl1_77.GetValue()+',')
        f.write(self.textCtrl2_77.GetValue()+',\n')               
        
        if self.checkBox78.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_78.GetValue()+',')
        f.write(self.textCtrl78.GetValue() +',')
        f.write(self.textCtrl1_78.GetValue()+',')
        f.write(self.textCtrl2_78.GetValue()+',\n')               
        
        if self.checkBox79.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_79.GetValue()+',')
        f.write(self.textCtrl79.GetValue() +',')
        f.write(self.textCtrl1_79.GetValue()+',')
        f.write(self.textCtrl2_79.GetValue()+',\n')               
        
        if self.checkBox80.GetValue() == True:
            f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_80.GetValue()+',')
        f.write(self.textCtrl80.GetValue() +',')
        f.write(self.textCtrl1_80.GetValue()+',')
        f.write(self.textCtrl2_80.GetValue()+',\n')               
        
        if self.checkBox81.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_81.GetValue()+',')
        f.write(self.textCtrl81.GetValue() +',')
        f.write(self.textCtrl1_81.GetValue()+',')
        f.write(self.textCtrl2_81.GetValue()+',\n')          
        
        if self.checkBox82.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_82.GetValue()+',')
        f.write(self.textCtrl82.GetValue() +',')
        f.write(self.textCtrl1_82.GetValue()+',')
        f.write(self.textCtrl2_82.GetValue()+',\n')          
        
        if self.checkBox83.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_83.GetValue()+',')
        f.write(self.textCtrl83.GetValue() +',')
        f.write(self.textCtrl1_83.GetValue()+',')
        f.write(self.textCtrl2_83.GetValue()+',\n')          
        
        if self.checkBox84.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_84.GetValue()+',')
        f.write(self.textCtrl84.GetValue() +',')
        f.write(self.textCtrl1_84.GetValue()+',')
        f.write(self.textCtrl2_84.GetValue()+',\n')          
        
        if self.checkBox85.GetValue() == True:
              f.write('Y,')
        else:
            f.write('N,')        
        f.write(self.comboBox1_85.GetValue()+',')
        f.write(self.textCtrl85.GetValue() +',')
        f.write(self.textCtrl1_85.GetValue()+',')
        f.write(self.textCtrl2_85.GetValue()+',')          
        f.close()
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\inputList.txt", readCode) 
        for lin1 in fList1:
            s1=lin1.split(',')[1] 
            copyfile("Parameterization_Setup.inf", parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\Parameterization_Setup.inf")
        self.Destroy()

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
        ### Inherit attributes from parent class        
        parent = self.GetParent()
        fList1 = open(parent.textCtrl2.GetValue()+ "\\Simulation\\Input\\" + parent.textCtrl1_1.GetValue() + "\\inputList.txt", readCode)       
        for lin1 in fList1: 
            s1=lin1.split(',')[1]
            fSufi2Parm = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+ '\\SUFI2.IN\\' + 'par_inf.txt', 'a')            
            fPar_Name = open(parent.textCtrl2.GetValue() + "\\Simulation\\CalibrationRuns\\" + parent.textCtrl1_1.GetValue()  + '\\' + s1 +".Sufi2.SwatCup\\"+ '\\Par_Name.OUT', 'a')
            counter=1
            if self.checkBox1.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_1.GetValue()[0] + '_Param01     ' + self.textCtrl1_1.GetValue() + '       ' + self.textCtrl2_1.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param01\n" )
                counter=counter+1
            
            if self.checkBox2.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_2.GetValue()[0] + '_Param02     ' + self.textCtrl1_2.GetValue() + '       ' + self.textCtrl2_2.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param02\n" )
                counter=counter+1            
                                
            if self.checkBox3.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_3.GetValue()[0] + '_Param03     ' + self.textCtrl1_3.GetValue() + '       ' + self.textCtrl2_3.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param03\n" )
                counter=counter+1            
                           
            if self.checkBox4.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_4.GetValue()[0] + '_Param04     ' + self.textCtrl1_4.GetValue() + '       ' + self.textCtrl2_4.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param04\n" )
                counter=counter+1            

            if self.checkBox5.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_5.GetValue()[0]  + '_Param05     ' + self.textCtrl1_5.GetValue() + '       ' + self.textCtrl2_5.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param05\n" )
                counter=counter+1            
                            
            if self.checkBox6.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_6.GetValue()[0]  + '_Param06     ' + self.textCtrl1_6.GetValue() + '       ' + self.textCtrl2_6.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param06\n" )
                counter=counter+1            
                            
            if self.checkBox7.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_7.GetValue()[0]  + '_Param07     ' + self.textCtrl1_7.GetValue() + '       ' + self.textCtrl2_7.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param07\n" )
                counter=counter+1            
                            
            if self.checkBox8.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_8.GetValue()[0]  + '_Param08     ' + self.textCtrl1_8.GetValue() + '       ' + self.textCtrl2_8.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param08\n" )
                counter=counter+1            
                            
            if self.checkBox9.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_9.GetValue()[0]  + '_Param09     ' + self.textCtrl1_9.GetValue() + '       ' + self.textCtrl2_9.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param09\n" )
                counter=counter+1             
                            
            if self.checkBox10.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_10.GetValue()[0]  + '_Param10     ' + self.textCtrl1_10.GetValue() + '       ' + self.textCtrl2_10.GetValue() + lineEnd)        
                fPar_Name.write(str(counter) + " :Param10\n" )
                counter=counter+1             
                            
            if self.checkBox11.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_11.GetValue()[0]  + '_Param11     ' + self.textCtrl1_11.GetValue() + '       ' + self.textCtrl2_11.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param11\n" )
                counter=counter+1             
                            
            if self.checkBox12.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_12.GetValue()[0]  + '_Param12     ' + self.textCtrl1_12.GetValue() + '       ' + self.textCtrl2_12.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param12\n" )
                counter=counter+1             
                            
            if self.checkBox13.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_13.GetValue()[0] + '_Param13     ' + self.textCtrl1_13.GetValue() + '       ' + self.textCtrl2_13.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param13\n" )
                counter=counter+1             
                            
            if self.checkBox14.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_14.GetValue()[0]  + '_Param14      ' + self.textCtrl1_14.GetValue() + '       ' + self.textCtrl2_14.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param14\n" )
                counter=counter+1             
                            
            if self.checkBox15.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_15.GetValue()[0]  + '_Param15      ' + self.textCtrl1_15.GetValue() + '       ' + self.textCtrl2_15.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param15\n" )
                counter=counter+1             
                            
            if self.checkBox16.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_16.GetValue()[0]  + '_Param16     ' + self.textCtrl1_16.GetValue() + '       ' + self.textCtrl2_16.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param16\n" )
                counter=counter+1             
                            
            if self.checkBox17.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_17.GetValue()[0]  + '_Param17      ' + self.textCtrl1_17.GetValue() + '       ' + self.textCtrl2_17.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param17\n" )
                counter=counter+1             
                            
            if self.checkBox18.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_18.GetValue()[0]  + '_Param18      ' + self.textCtrl1_18.GetValue() + '       ' + self.textCtrl2_18.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param18\n" )
                counter=counter+1             
                                
            if self.checkBox19.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_19.GetValue()[0]  + '_Param19     ' + self.textCtrl1_19.GetValue() + '       ' + self.textCtrl2_19.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param19\n" )
                counter=counter+1             
                            
            if self.checkBox20.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_20.GetValue()[0]  + '_Param20     ' + self.textCtrl1_20.GetValue() + '       ' + self.textCtrl2_20.GetValue() + lineEnd)       
                fPar_Name.write(str(counter) + " :Param20\n" )
                counter=counter+1             
                            
            if self.checkBox21.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_21.GetValue()[0]  + '_Param21     ' + self.textCtrl1_21.GetValue() + '       ' + self.textCtrl2_21.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param21\n" )
                counter=counter+1             
                            
            if self.checkBox22.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_22.GetValue()[0]  + '_Param22     ' + self.textCtrl1_22.GetValue() + '       ' + self.textCtrl2_22.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param22\n" )
                counter=counter+1             
                            
            if self.checkBox23.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_23.GetValue()[0]  + '_Param23     ' + self.textCtrl1_23.GetValue() + '       ' + self.textCtrl2_23.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param23\n" )
                counter=counter+1             
                            
            if self.checkBox24.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_24.GetValue()[0]  + '_Param24     ' + self.textCtrl1_24.GetValue() + '       ' + self.textCtrl2_24.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param24\n" )
                counter=counter+1             
                            
            if self.checkBox25.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_25.GetValue()[0]  + '_Param25     ' + self.textCtrl1_25.GetValue() + '       ' + self.textCtrl2_25.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param25\n" )
                counter=counter+1             
                            
            if self.checkBox26.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_26.GetValue()[0] + '_Param26     ' + self.textCtrl1_26.GetValue() + '       ' + self.textCtrl2_26.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param26\n" )
                counter=counter+1             
                            
            if self.checkBox27.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_27.GetValue()[0] + '_Param27     ' + self.textCtrl1_27.GetValue() + '       ' + self.textCtrl2_27.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param27\n" )
                counter=counter+1            
                            
            if self.checkBox28.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_28.GetValue()[0]  + '_Param28    ' + self.textCtrl1_28.GetValue() + '       ' + self.textCtrl2_28.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param28\n" )
                counter=counter+1             
                            
            if self.checkBox29.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_29.GetValue()[0]  + '_Param29     ' + self.textCtrl1_29.GetValue() + '       ' + self.textCtrl2_29.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param29\n" )
                counter=counter+1             
                            
            if self.checkBox30.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_30.GetValue()[0]  + '_Param30     ' + self.textCtrl1_30.GetValue() + '       ' + self.textCtrl2_30.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param30\n" )
                counter=counter+1             
                        
            if self.checkBox31.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_31.GetValue()[0]  + '_Param31     ' + self.textCtrl1_31.GetValue() + '       ' + self.textCtrl2_31.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param31\n" )
                counter=counter+1            
                            
            if self.checkBox32.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_32.GetValue()[0]  + '_Param32    ' + self.textCtrl1_32.GetValue() + '       ' + self.textCtrl2_32.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param32\n" )
                counter=counter+1             
                            
            if self.checkBox33.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_33.GetValue()[0]  + '_Param33     ' + self.textCtrl1_33.GetValue() + '       ' + self.textCtrl2_33.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param33\n" )
                counter=counter+1             
                            
            if self.checkBox34.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_34.GetValue()[0]  + '_Param34     ' + self.textCtrl1_34.GetValue() + '       ' + self.textCtrl2_34.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param34\n" )
                counter=counter+1             
                            
            if self.checkBox35.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_35.GetValue()[0]  + '_Param35     ' + self.textCtrl1_35.GetValue() + '       ' + self.textCtrl2_35.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param35\n" )
                counter=counter+1            
                            
            if self.checkBox36.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_36.GetValue()[0]  + '_Param36     ' + self.textCtrl1_36.GetValue() + '       ' + self.textCtrl2_36.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param36\n" )
                counter=counter+1             
                            
            if self.checkBox37.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_37.GetValue()[0]  + '_Param37     ' + self.textCtrl1_37.GetValue() + '       ' + self.textCtrl2_37.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param37\n" )
                counter=counter+1             
                            
            if self.checkBox38.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_38.GetValue()[0]  + '_Param38     ' + self.textCtrl1_38.GetValue() + '       ' + self.textCtrl2_38.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param38\n" )
                counter=counter+1             
                            
            if self.checkBox39.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_39.GetValue()[0]  + '_Param39     ' + self.textCtrl1_39.GetValue() + '       ' + self.textCtrl2_39.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param39\n" )
                counter=counter+1             
                            
            if self.checkBox40.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_40.GetValue()[0]  + '_Param40     ' + self.textCtrl1_40.GetValue() + '       ' + self.textCtrl2_40.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param40\n" )
                counter=counter+1             
                                        
            if self.checkBox41.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_41.GetValue()[0]  + '_Param41     ' + self.textCtrl1_41.GetValue() + '       ' + self.textCtrl2_41.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param41\n" )
                counter=counter+1                       
            
            if self.checkBox42.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_42.GetValue()[0]  + '_Param42     ' + self.textCtrl1_42.GetValue() + '       ' + self.textCtrl2_42.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param42\n" )
                counter=counter+1             
                            
            if self.checkBox43.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_43.GetValue()[0]  + '_Param43     ' + self.textCtrl1_43.GetValue() + '       ' + self.textCtrl2_43.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param43\n" )
                counter=counter+1             
                            
            if self.checkBox44.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_44.GetValue()[0]  + '_Param44     ' + self.textCtrl1_44.GetValue() + '       ' + self.textCtrl2_44.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param44\n" )
                counter=counter+1 
                                            
            if self.checkBox45.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_45.GetValue()[0]  + '_Param45     ' + self.textCtrl1_45.GetValue() + '       ' + self.textCtrl2_45.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :RWPC1\n" )
                counter=counter+1             
                            
            if self.checkBox46.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_46.GetValue()[0]  + '_Param46     ' + self.textCtrl1_46.GetValue() + '       ' + self.textCtrl2_46.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param46\n" )
                counter=counter+1             
                            
            if self.checkBox47.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_47.GetValue()[0]  + '_Param47    ' + self.textCtrl1_47.GetValue() + '       ' + self.textCtrl2_47.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param47\n" )
                counter=counter+1             
                            
            if self.checkBox48.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_48.GetValue()[0]  + '_Param48     ' + self.textCtrl1_48.GetValue() + '       ' + self.textCtrl2_48.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param48\n" )
                counter=counter+1             
                            
            if self.checkBox49.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_49.GetValue()[0]  + '_Param49     ' + self.textCtrl1_49.GetValue() + '       ' + self.textCtrl2_49.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param49\n" )
                counter=counter+1             
                            
            if self.checkBox50.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_50.GetValue()[0]  + '_Param50     ' + self.textCtrl1_50.GetValue() + '       ' + self.textCtrl2_50.GetValue() + lineEnd) 
                fPar_Name.write(str(counter) + " :Param50\n" )
                counter=counter+1             
                                       
            if self.checkBox51.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_51.GetValue()[0]  + '_Param51      ' + self.textCtrl1_51.GetValue() + '       ' + self.textCtrl2_51.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param51\n" )
                counter=counter+1             
                            
            if self.checkBox52.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_52.GetValue()[0]  + '_Param52     ' + self.textCtrl1_52.GetValue() + '       ' + self.textCtrl2_52.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param52\n" )
                counter=counter+1             
                                
            if self.checkBox53.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_53.GetValue()[0] + '_Param53     ' + self.textCtrl1_53.GetValue() + '       ' + self.textCtrl2_53.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param53\n" )
                counter=counter+1             
                            
            if self.checkBox54.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_54.GetValue()[0] + '_Param54     ' + self.textCtrl1_54.GetValue() + '       ' + self.textCtrl2_54.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param54\n" )
                counter=counter+1            
                            
            if self.checkBox55.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_55.GetValue() + '_Param55     ' + self.textCtrl1_55.GetValue() + '       ' + self.textCtrl2_55.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param55\n" )
                counter=counter+1             
                            
            if self.checkBox56.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_56.GetValue() + '_Param56     ' + self.textCtrl1_56.GetValue() + '       ' + self.textCtrl2_56.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param56\n" )
                counter=counter+1                                     
            
            if self.checkBox57.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_57.GetValue() + '_Param57     ' + self.textCtrl1_57.GetValue() + '       ' + self.textCtrl2_57.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param57\n" )
                counter=counter+1                         
            
            if self.checkBox58.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_58.GetValue() + '_Param58     ' + self.textCtrl1_58.GetValue() + '       ' + self.textCtrl2_58.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param57\n" )
                counter=counter+1                         
            
            if self.checkBox59.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_59.GetValue() + '_Param59     ' + self.textCtrl1_59.GetValue() + '       ' + self.textCtrl2_59.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param59\n" )
                counter=counter+1                        
            
            if self.checkBox60.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_60.GetValue() + '_Param60     ' + self.textCtrl1_60.GetValue() + '       ' + self.textCtrl2_60.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param60\n" )
                counter=counter+1                       
            
            if self.checkBox61.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_61.GetValue() + '_Param61     ' + self.textCtrl1_61.GetValue() + '       ' + self.textCtrl2_61.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param61\n" )
                counter=counter+1                            
            
            if self.checkBox62.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_62.GetValue() + '_Param62     ' + self.textCtrl1_62.GetValue() + '       ' + self.textCtrl2_62.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param62\n" )
                counter=counter+1                          
            
            if self.checkBox63.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_63.GetValue() + '_Param63     ' + self.textCtrl1_63.GetValue() + '       ' + self.textCtrl2_63.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param63\n" )
                counter=counter+1                  
            
            if self.checkBox64.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_64.GetValue() + '_Param64     ' + self.textCtrl1_64.GetValue() + '       ' + self.textCtrl2_64.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param64\n" )
                counter=counter+1                     
            
            if self.checkBox65.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_65.GetValue() + '_Param65     ' + self.textCtrl1_65.GetValue() + '       ' + self.textCtrl2_65.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param62\n" )
                counter=counter+1                    
            
            if self.checkBox66.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_66.GetValue() + '_Param66     ' + self.textCtrl1_66.GetValue() + '       ' + self.textCtrl2_66.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param66\n" )
                counter=counter+1             
                            
            if self.checkBox67.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_67.GetValue() + '_Param67     ' + self.textCtrl1_67.GetValue() + '       ' + self.textCtrl2_67.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param67\n" )
                counter=counter+1                     
            
            if self.checkBox68.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_68.GetValue() + '_Param68     ' + self.textCtrl1_68.GetValue() + '       ' + self.textCtrl2_68.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param68\n" )
                counter=counter+1             

            if self.checkBox69.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_69.GetValue() + '_Param69     ' + self.textCtrl1_69.GetValue() + '       ' + self.textCtrl2_69.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param69\n" )
                counter=counter+1                
            
            if self.checkBox70.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_70.GetValue() + '_Param70     ' + self.textCtrl1_70.GetValue() + '       ' + self.textCtrl2_70.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param70\n" )
                counter=counter+1                  
            
            if self.checkBox71.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_71.GetValue() + '_Param71     ' + self.textCtrl1_71.GetValue() + '       ' + self.textCtrl2_71.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param71\n" )
                counter=counter+1                      
            
            if self.checkBox72.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_72.GetValue() + '_Param72     ' + self.textCtrl1_72.GetValue() + '       ' + self.textCtrl2_72.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param72\n" )
                counter=counter+1                        
            
            if self.checkBox73.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_73.GetValue() + '_Param73     ' + self.textCtrl1_73.GetValue() + '       ' + self.textCtrl2_73.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param73\n" )
                counter=counter+1                        
            
            if self.checkBox74.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_74.GetValue() + '_Param74     ' + self.textCtrl1_74.GetValue() + '       ' + self.textCtrl2_74.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param74\n" )
                counter=counter+1                        
            
            if self.checkBox75.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_75.GetValue() + '_Param75     ' + self.textCtrl1_75.GetValue() + '       ' + self.textCtrl2_75.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param75\n" )
                counter=counter+1                
            
            if self.checkBox76.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_76.GetValue() + '_Param76     ' + self.textCtrl1_76.GetValue() + '       ' + self.textCtrl2_76.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param76\n" )            
            
            if self.checkBox77.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_77.GetValue() + '_Param77     ' + self.textCtrl1_77.GetValue() + '       ' + self.textCtrl2_77.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param77\n" )
                counter=counter+1                       
            
            if self.checkBox78.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_78.GetValue() + '_Param78     ' + self.textCtrl1_78.GetValue() + '       ' + self.textCtrl2_78.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param78\n" )
                counter=counter+1                        
            
            if self.checkBox79.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_79.GetValue() + '_Param79     ' + self.textCtrl1_79.GetValue() + '       ' + self.textCtrl2_79.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param79\n" )
                counter=counter+1             
            
            if self.checkBox80.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_80.GetValue() + '_Param80     ' + self.textCtrl1_80.GetValue() + '       ' + self.textCtrl2_80.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param80\n" )
                counter=counter+1                                    
                                    
            if self.checkBox81.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_81.GetValue() + '_Param81     ' + self.textCtrl1_81.GetValue() + '       ' + self.textCtrl2_81.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param81\n" )
                counter=counter+1                                                         
                                                                        
            if self.checkBox82.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_82.GetValue() + '_Param82     ' + self.textCtrl1_82.GetValue() + '       ' + self.textCtrl2_82.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param82\n" )
                counter=counter+1                         
            
            if self.checkBox83.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_83.GetValue() + '_Param83     ' + self.textCtrl1_83.GetValue() + '       ' + self.textCtrl2_83.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param83\n" )
                counter=counter+1             
                            
            if self.checkBox84.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_84.GetValue() + '_Param84     ' + self.textCtrl1_84.GetValue() + '       ' + self.textCtrl2_84.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param84\n" )
                counter=counter+1                       
            
            if self.checkBox85.GetValue() == True:
                fSufi2Parm.write(self.comboBox1_85.GetValue() + '_Param85     ' + self.textCtrl1_85.GetValue() + '       ' + self.textCtrl2_85.GetValue() + lineEnd)
                fPar_Name.write(str(counter) + " :Param85\n" )
                counter=counter+1             
            
            
            fSufi2Parm.close()

        dlg = wx.MessageDialog(self, 'SUFI2 sampleing parameters have been created!', 'Message', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()



    def OnButton3Button(self, event):
        event.Skip()

    def OnButton4Button(self, event):
        event.Skip()
