import maya.cmds as mc
import maya.utils as mu
import maya.mel as mel
import JKTool.JKTMenu as jktm

# def createMyMenu():
	# gMainWindow = mel.eval('$tmpVar=$gMainWindow')
	# mc.menu("JKTool_UI", label="JKTool", tearOff=True, parent=gMainWindow )
	
#createMyMenu()
# mu.executeDeferred(createMyMenu)
mu.executeDeferred(jktm.createMyMenu)