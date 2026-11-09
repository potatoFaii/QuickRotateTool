import maya.cmds as cmds
import maya.mel as mel

QRT_labelName = 'QuickRotateTool'
QRT_annot = 'QuickRotate'
QRT_imagePath = 'commandButton.png'
QRT_imageLabel = 'QuickRotate'
QRT_sourceScript = 'python'
QRT_buttonName = 'QuickRotate_button'

def myTool():
    cmds.warning("My Tool is running!")
    
def createShelfButton():
    QRT_shelf = mel.eval('$gShelfTopLevel=$gShelfTopLevel')
    QRT_currentShelf = cmds.tabLayout(QRT_shelf,q=True,selectTab=True)
    QRT_btnPath = QRT_currentShelf + '|' + QRT_buttonName
    if cmds.control(QRT_btnPath, exists=True):
        cmds.deleteUI(QRT_btnPath)
        
    command = '''# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel

class QRT_Orientation_Script_Func:
    QRT_ORIENT_WINDOW = "QRT_Orient_Window"
    COLOR_GREEN = [0.3, 0.9, 0.3]
    COLOR_RED   = [0.9, 0.3, 0.3]
    COLOR_BLUE  = [0.3, 0.3, 0.9]
    
    def __init__(self, *args):
        self.__class__.show_window(self)
        
    @classmethod 
    def delete_existing(cls):
        if cmds.window(cls.QRT_ORIENT_WINDOW,q=True,exists=True):
            cmds.deleteUI("{}".format(cls.QRT_ORIENT_WINDOW),window=True)
    
    def show_window(self,*args):
        self.delete_existing()
        cmds.window(self.QRT_ORIENT_WINDOW,menuBar=True,sizeable=False,toolbox=False,resizeToFitChildren=False,mnb=False,mxb=False,widthHeight=(290,105))
        first_FL = cmds.formLayout()
        
        float_Grp = cmds.floatFieldGrp("rbgManualTweak", l="Manual Tweak: ", nf=3, v1=0.0, v2=0.0, v3=0.0, cw4=(90,60,60,60))
        plus_Btn1 = cmds.button("btnPlusX", l="+", w=25, h=20, c=lambda _:self.addInXValue())
        minus_Btn1 = cmds.button("btnMinusX", l="-", w=25, h=20, c=lambda _:self.minusInXValue())
        plus_Btn2 = cmds.button("btnPlusY", l="+", w=25, h=20, c=lambda _:self.addInYValue())
        minus_Btn2 = cmds.button("btnMinusY", l="-", w=25, h=20, c=lambda _:self.minusInYValue())
        plus_Btn3 = cmds.button("btnPlusZ", l="+", w=25, h=20, c=lambda _:self.addInZValue())
        minus_Btn3 = cmds.button("btnMinusZ", l="-", w=25, h=20, c=lambda _:self.minusInZValue())
        
        plusAll_Btn = cmds.button("btnPlusAll", l="Tweak All +", w=120, h=20, c=lambda _:self.rotateAxisManualTweakPlus())
        minusAll_Btn = cmds.button("btnMinusAll", l="Tweak All -", w=120, h=20, c=lambda _:self.rotateAxisManualTweakMinus())
        
        wind_sep = cmds.separator(style='double')
        tmp_text = cmds.text(l='@ Orient Rotation',font='smallObliqueLabelFont',en=False)
        
        cmds.formLayout(first_FL,e=True,attachControl = [(plus_Btn1,'top',2,float_Grp),
                                                         (minus_Btn1,'top',2,float_Grp),(minus_Btn1,'left',3,plus_Btn1),
                                                         (plus_Btn2,'top',1,float_Grp),(plus_Btn2,'left',10,minus_Btn1),
                                                         (minus_Btn2,'top',1,float_Grp),(minus_Btn2,'left',3,plus_Btn2),
                                                         (plus_Btn3,'top',1,float_Grp),(plus_Btn3,'left',10,minus_Btn2),
                                                         (minus_Btn3,'top',1,float_Grp),(minus_Btn3,'left',3,plus_Btn3),
                                                         (plusAll_Btn,'top',3,plus_Btn1),
                                                         (minusAll_Btn,'top',3,plus_Btn1),
                                                         (wind_sep,'top',5,plusAll_Btn),
                                                         (tmp_text,'top',0,wind_sep)],
                                           attachForm = [(float_Grp,'top',5),
                                                         (plus_Btn1,'left',96),
                                                         (plusAll_Btn,'left',10),
                                                         (minusAll_Btn,'right',12),
                                                         (wind_sep,'left',0),(wind_sep,'right',0),
                                                         (tmp_text,'left',0),(tmp_text,'right',0),],
                                       attachPosition = [(plusAll_Btn, "right", 0, 49.5),(minusAll_Btn, "left", 0, 50.5)])
        cmds.showWindow(self.QRT_ORIENT_WINDOW)

    def addInXValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v1=(cmds.floatFieldGrp("rbgManualTweak", q=True, v1=True) + 0.1))
    def minusInXValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v1=(cmds.floatFieldGrp("rbgManualTweak", q=True, v1=True) - 0.1))
    def addInYValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v2=(cmds.floatFieldGrp("rbgManualTweak", q=True, v2=True) + 0.1))
    def minusInYValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v2=(cmds.floatFieldGrp("rbgManualTweak", q=True, v2=True) - 0.1))
    def addInZValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v3=(cmds.floatFieldGrp("rbgManualTweak", q=True, v3=True) + 0.1))
    def minusInZValue(self):
        cmds.floatFieldGrp("rbgManualTweak", e=True, v3=(cmds.floatFieldGrp("rbgManualTweak", q=True, v3=True) - 0.1))

    def rotateFloatQuery(self):
        rV_X = cmds.floatFieldGrp("rbgManualTweak", q=True, v1=True)
        rV_Y = cmds.floatFieldGrp("rbgManualTweak", q=True, v2=True)
        rV_Z = cmds.floatFieldGrp("rbgManualTweak", q=True, v3=True)
        return rV_X,rV_Y,rV_Z
    
    def rotateAxisManualTweakPlus(self):
        cmds.undoInfo(ock=True)
        
        rX,rY,rZ = self.rotateFloatQuery()
        rotationValues = [rX, rY, rZ]
        
        selection = cmds.ls(sl=True) or []
        if not selection:
            cmds.warning("NO SELECTION")
            cmds.undoInfo(cck=True)
            return
        
        self.rotateAxisManualTweak(selection, rotationValues)
        cmds.select(selection, r=True)
        cmds.undoInfo(cck=True)
    
    def rotateAxisManualTweakMinus(self):
        cmds.undoInfo(ock=True)
    
        rX,rY,rZ = self.rotateFloatQuery()
        rotationValues = [rX*-1, rY*-1, rZ*-1]

        selection = cmds.ls(sl=True) or []
        if not selection:
            cmds.warning("NO SELECTION")
            cmds.undoInfo(cck=True)
            return
        
        self.rotateAxisManualTweak(selection, rotationValues)
        cmds.select(selection, r=True)
        cmds.undoInfo(cck=True)

    def rotateAxisManualTweak(self,selection,rotationValues):
        for each in selection:
            rotate_attrs = (
                ('rotateX', rotationValues[0]),
                ('rotateY', rotationValues[1]),
                ('rotateZ', rotationValues[2]),
            )

            for attr_name, attr_value in rotate_attrs:
                attr_path = '{}.{}'.format(each, attr_name)
                if cmds.getAttr(attr_path, lock=True):
                    continue

                current_rotate_value = cmds.getAttr(attr_path)
                cmds.setAttr(attr_path, current_rotate_value + attr_value)

QRT_Orientation_Script_Func()
'''

    cmds.shelfButton(QRT_buttonName,
                     parent=QRT_currentShelf,
    				 label=QRT_labelName,
    				 annotation=QRT_annot,
    				 image=QRT_imagePath,
    				 imageOverlayLabel=QRT_imageLabel,
    				 overlayLabelColor=(1, 1, 1),
    				 overlayLabelBackColor=(0.6, 0.5, 0.2, 0.85),
    				 command=command,
    				 sourceType=QRT_sourceScript
					)

def onMayaDroppedPythonFile(*args):
    createShelfButton()
    cmds.inViewMessage(amg='<hl>Default</hl> installed successfully!',pos='topCenter',fade=True)
    cmds.warning("{} installation complete.".format(QRT_labelName))