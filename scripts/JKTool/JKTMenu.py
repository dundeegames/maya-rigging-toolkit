import maya.cmds as mc
import maya.mel as mel


def createMyMenu():
	gMainWindow = mel.eval('$tmpVar=$gMainWindow')
	mc.menu("JKTool_UI", label="JKTool", tearOff=True, parent=gMainWindow )
	mc.menuItem( label="Run", command="mc.JKTRun()" )
	mc.menuItem( label='Update', enable=False )
	# mc.menuItem( label='Save' )
	mc.menuItem( divider=True )
	mc.menuItem( label='Help', enable=False )

def deleteMyMenu():
	mc.deleteUI("JKTool_UI")