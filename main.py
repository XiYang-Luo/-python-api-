# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:32:23 2018

@author: luo xi yang
"""

import wx
import os
"""打开浏览器""" 
import webbrowser
from translate_class import Translate_api
TA=Translate_api()
cb,t1,t2,t3=TA.colour()
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Translate Tools',pos=(10,10),size=(230,340),style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)  
        self.create_text()#创建文本框
        self.create_menu()#主菜单创建
        self.create_statusbar()#创建状态栏
        self.create_button()#按钮创建
        self.event_bind_button()
        self.create_slider()
        self.event_bind_slider()
        self.event_bind_MainMenu()
        #self.SetBackgroundColour('MEDIUM TURQUOISE')
        self.SetBackgroundColour(cb)
        self.SetTransparent(230)#设置透明
        self.SetMaxSize((600,330))#设置窗口大小固定
        #self.SetMinSize((230,280))
        
        hbox1=wx.BoxSizer()
        hbox1.Add(self.button_translate,proportion=0)
        hbox1.Add(self.main_text,proportion=1,flag=wx.LEFT,border=5)
        hbox2=wx.BoxSizer()
        hbox2.Add(self.button_translated,proportion=0)
        hbox2.Add(self.translate_text,proportion=1,flag=wx.LEFT,border=5)
        vbox=wx.BoxSizer(wx.VERTICAL)
        
        vbox.Add(hbox1,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
      
        vbox.Add(hbox2,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
        vbox.Add(self.sld,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
        self.SetSizer(vbox)
        
         
    def create_text(self):
        self.main_text=wx.TextCtrl(self,-1,"这里输入需要翻译的句子",pos=(25,10),size=(180,80),style=wx.TE_MULTILINE)
        self.main_text.SetBackgroundColour(t1)
        self.main_text.SetForegroundColour(t3)
        self.translate_text=wx.TextCtrl(self,-1,pos=(25,80),size=(180,100),style=wx.TE_MULTILINE)
        self.translate_text.SetBackgroundColour(t2)
        self.translate_text.SetForegroundColour(t3)
    def create_button(self):
        self.button_translate=wx.Button(self, -1,"", pos = (5, 11),size=(17,17),style = wx.RB_GROUP)
        self.button_translated=wx.Button(self, -1,"", pos = (5, 105),size=(17,17),style = wx.RB_GROUP)
    def create_slider(self):
        self.sld = wx.Slider(self, pos=(25,260),size=(180,5),value =230, minValue = 1, maxValue = 255,style = wx.SL_HORIZONTAL|wx.SL_LABELS) 
    def create_menu(self):
        self.menubar=wx.MenuBar()
        self.menu1=wx.Menu()
        self.menu2=wx.Menu()
        self.menu3=wx.Menu()
        self.color=wx.Menu()
           
        self.color_red=self.color.Append(-1,'Red')
        self.color_blue=self.color.Append(-1,'Blue')
        self.color_yellow=self.color.Append(-1,'Yellow')
        self.color_green=self.color.Append(-1,'Green')
        self.color_purple=self.color.Append(-1,'Purple')
        self.color_orange=self.color.Append(-1,'Orange')
        self.color_pink=self.color.Append(-1,'Pink')
        """STEP3在菜单下面，建立选项栏，使用Append（-1，“name”）"""
        self.m1SetColor=self.menu1.Append(-1,u'SetColor',self.color)
        self.m1quit = self.menu1.Append(-1,'Quit')
        self.m2about=self.menu2.Append(-1,"About")
        
        self.m3googleTranslate=self.menu3.Append(-1,"谷歌翻译在线")
        self.m3baiduTranslate=self.menu3.Append(-1,"百度翻译在线")
        self.m3NCBI=self.menu3.Append(-1,'NCBI')
        self.m3PDB=self.menu3.Append(-1,'PDB')
        self.m3EMBOSS=self.menu3.Append(-1,'EMBOSS Explorer')
        self.m3ibilinux=self.menu3.Append(-1,'cqupt_ibi_linux_study')
        self.m3ibiCQUPT=self.menu3.Append(-1,"IBI CQUPT")
        
        """STEP4将建好的菜单添加到菜单栏下面去，使用Append(菜单，“name”)"""
        self.menubar.Append(self.menu1,"Quit")
        self.menubar.Append(self.menu2,"HELP")
        self.menubar.Append(self.menu3,"Online Web")
        """STEP5将菜单栏设置到主窗口中，使用SetMenuBar（）"""
        self.SetMenuBar(self.menubar)
        
    def create_statusbar(self):
        self.statusbar = self.CreateStatusBar()
        #self.statusbar.SetFieldsCount(3)
        #self.statusbar.SetStatusWidths([-1, -2, -1])
    
    def event_bind_MainMenu(self):
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuQuit,self.m1quit)
        
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorRed,self.color_red)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorBlue,self.color_blue)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorYellow,self.color_yellow)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorGreen,self.color_green)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorPurple,self.color_purple)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorOrange,self.color_orange)
        self.Bind(wx.EVT_MENU,self.OnMenuSetColorPink,self.color_pink)
        
        self.menu2.Bind(wx.EVT_MENU,self.OnMenuAbout,self.m2about)
        
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuGoogleT,self.m3googleTranslate)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuBT,self.m3baiduTranslate)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuNCBI,self.m3NCBI)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuPDB,self.m3PDB)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuEMBOSS,self.m3EMBOSS)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuCQUPTibiLinux,self.m3ibilinux)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuIBICQUPT,self.m3ibiCQUPT)
        
        
    def event_bind_button(self):
        self.button_translate.Bind(wx.EVT_BUTTON,self.OnButtonTranslate)
        self.button_translate.SetBackgroundColour("red")
        self.button_translated.Bind(wx.EVT_BUTTON,self.OnButtonTranslate)
        self.button_translated.SetBackgroundColour("pink")
        '''点击回车触发时间'''
        self.Bind(wx.EVT_TEXT_ENTER, self.OnButtonTranslate, self.main_text)
    def event_bind_slider(self):
        self.sld.Bind(wx.EVT_SLIDER, self.OnSliderScroll)
        
    def OnSliderScroll(self, e): 
        self.SetTransparent(self.sld.GetValue())#设置透明
    
    def OnMenuAbout(self,event):
        """子窗口界面创建wx.Dialog，在self.panel下面"""
        self.dialog_main_help=wx.Dialog(None,-1,title="Help",pos=(100,100),size=(450,200))
        listDatas = ['这个软件可以帮助在阅读英文文献时随时随地翻译生词','点击Transalte按钮将进行翻译:','Online Web菜单中有Google和百度翻译的在线地址，点击在浏览器中运行。','点击左上角的红色方形按钮也可以对框中的语句进行翻译。']
        self.help_listBox = wx.ListBox(self.dialog_main_help, -1, pos=(20, 20), size=(750, 430), style=wx.LB_SINGLE)
        """设置背景颜色和字体颜色"""
        self.help_listBox.SetBackgroundColour('white'), self.help_listBox.SetForegroundColour('sky blue') 
        self.help_listBox.SetTransparent(400)#设置透明
        #self.imagelist=wx.Image("helplistlogo.jpg",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.bmplist=wx.StaticBitmap(self.dialog_main_help,bitmap=self.imagelist)
        self.help_listBox.Append(listDatas)
        self.button_translate.SetBackgroundColour("red")
        self.button_translated.SetBackgroundColour("purple")
    
        """显示子窗口"""
        self.dialog_main_help.ShowModal()
        
    def OnButtonTranslate(self,event):
        TA=Translate_api();text=[]
        text.append(str(self.main_text.GetValue()))
        print(text[0].replace("\n"," "))
        ta=TA.translate(text[0].replace("\n"," "))
        self.button_translate.SetBackgroundColour("green")
        self.button_translated.SetBackgroundColour("yellow")
        print(ta)
        self.statusbar.SetStatusText(text[0].replace("\n"," "))
        self.main_text.Clear()
        self.translate_text.SetValue(ta)
        
        
    def OnMenuQuit(self,evt):
        os.sys.exit()
        
    def OnMenuSetColorRed(self,event):
        self.main_text.SetForegroundColour('red')
        self.translate_text.SetForegroundColour('red')
    def OnMenuSetColorBlue(self,event):
        self.main_text.SetForegroundColour('SLATE BLUE')
        self.translate_text.SetForegroundColour('SLATE BLUE')
    def OnMenuSetColorYellow(self,event):
        self.main_text.SetForegroundColour('YELLOW')
        self.translate_text.SetForegroundColour('YELLOW')
    def OnMenuSetColorGreen(self,event):
        self.main_text.SetForegroundColour('AQUAMARINE')
        self.translate_text.SetForegroundColour('AQUAMARINE')
    def OnMenuSetColorPurple(self,event):
        self.main_text.SetForegroundColour('PURPLE')
        self.translate_text.SetForegroundColour('PURPLE')
    def OnMenuSetColorOrange(self,event):
        self.main_text.SetForegroundColour('CORAL')
        self.translate_text.SetForegroundColour('CORAL')
    def OnMenuSetColorPink(self,event):
        self.main_text.SetForegroundColour('ORANGE RED')
        self.translate_text.SetForegroundColour('ORANGE RED')
    
    def OnMenuGoogleT(self,evt):
        webbrowser.open("https://translate.google.cn/")
        
    def OnMenuBT(self,evt):
        webbrowser.open("http://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#auto/zh/")
        
    def OnMenuNCBI(self,event):
        webbrowser.open("https://www.ncbi.nlm.nih.gov/")
        
    def OnMenuPDB(self,event):
        webbrowser.open("http://www.rcsb.org/")
        
    def OnMenuEMBOSS(self,event):
        webbrowser.open("http://www.bioinformatics.nl/emboss-explorer/")
        
    def OnMenuCQUPTibiLinux(self,event):
        webbrowser.open('http://ibi.cqupt.edu.cn/bioinfo/course/linux/')
        
    def OnMenuIBICQUPT(self,event):
        webbrowser.open('http://ibi.cqupt.edu.cn/new/')
         
app=wx.App()
win=MainFrame()
win.Show()
app.MainLoop()
