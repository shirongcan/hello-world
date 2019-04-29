
import wx
from posgrid import PicPosGridTable
import picpos 
import os
class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        self.pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        self.mypath = wx.StaticText(self.pnl, label="请选择要获取pos数据的文件夹", pos=(25,25))
        # 输出pos数据的文件名
        wx.StaticText(self.pnl,label="保存pos数据的文件名",pos=(25,60))
        
        self.myfilename = wx.TextCtrl(self.pnl, value="pos.txt",  pos=(150,58),size=(125, -1))

        # 创建一个button 打开文件所在目录
        self.mybutton2 = wx.Button(self.pnl,-1,label="打开所在目录",pos=(280,58))
        self.Bind(wx.EVT_BUTTON,self.onmybutton2Click,self.mybutton2)
        # 高度偏移
        wx.StaticText(self.pnl,-1,label="高度偏移：", pos=(25,90))
        self.myheightoffset = wx.TextCtrl(self.pnl,value="0",pos=(150,88),size=(125,-1))
        
        font = self.mypath.GetFont()
        font.PointSize += 2
        font = font.Bold()
        self.mypath.SetFont(font)


        # 创建一个button

        self.mybutton1 = wx.Button(self.pnl,label="获取pos数据",pos=(25,120))
        self.Bind(wx.EVT_BUTTON,self.Onmybutton1Click,self.mybutton1)
        
        
 
        self.listBox1 = wx.ListBox(self.pnl, -1, pos=(25, 155), size=(300, 420),  style=wx.LB_SINGLE)
        
      # 
        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("DJI 航拍图片坐标获取！")

    def Onmybutton1Click(self,event):
       # wx.MessageBox(self.mypath.Label)
        picpos.getpos(self.mypath.Label,self.myfilename.GetValue().strip(),int(self.myheightoffset.GetValue()))
        # 把获取的pos数据写入list中
        self.listBox1.Clear()
        self.addPosToListBox()

    def onmybutton2Click(self,event):
        os.startfile(self.mypath.Label)
       
    def addPosToListBox(self):
        with open(os.path.join(self.mypath.Label,self.myfilename.GetValue().strip()),"r" ) as infile:
            while True:
                line1 = infile.readline()
                if not line1:
                    break
                    pass
                else:
                    self.listBox1.Append(line1)

    def getHeightOffset(self):
        pass  
        
    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&选择文件夹...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
       # wx.MessageBox("Hello again from wxPython")
       # wx.FileDialog(self,"选择一个目录").ShowModal()
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.mypath.Label = dlg.GetPath()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Get DJI Images Pos',size=(400,700))
    frm.Show()
    app.MainLoop()