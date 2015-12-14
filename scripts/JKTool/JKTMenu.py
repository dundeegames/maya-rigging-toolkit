import maya.cmds as mc
import maya.mel as mel

def createMyMenu():
	gMainWindow = mel.eval('$tmpVar=$gMainWindow')
	mc.menu("JKTool_UI", label="JKTool", tearOff=True, parent=gMainWindow )
	

def deleteMyMenu():
	mc.deleteUI("JKTool_UI")