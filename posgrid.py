import wx.grid as grid

class PicPosGridTable(grid.PyGridTableBase):
    def __init__(self, datas):
        grid.PyGridTableBase.__init__(self)
        
        self.datas = datas
        self.colLabels = [u'文件名', u'纬度', u'经度', u'高度']

        pass
