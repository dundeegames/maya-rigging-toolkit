"""Main Window Module
@file JKTApp.py
@details    creates Window with UI for my tool

@author     Jiri Klic
@version    1.0
@date       December 2015
@pre        
@post       
@bug        No known bugs
@warning    
@todo       

@copyright  University of Abertay - Dundee.2013.
			Intellectual Property Policy.[online].Available from: 
			http://www.abertay.ac.uk/media/Intellectual-Property-Policy-v2-01.pdf
			[Accessed 22 April 2015].
"""

import maya.cmds as mc
import JKTool.JKTCurves as jktc

def createCtrlShape():
	selected = mc.ls(selection=True)

	if len(selected) != 2:
		# "question", "information", "warning" and "critical"
		mc.confirmDialog( title='Error', message='Select 2 objects: Control Shape and Joint', button=['OK'], icon="warning" )
	elif not( mc.objectType( selected[0], isType='joint' ) and  mc.objectType( selected[1], isType='transform' ) ):
		mc.confirmDialog( title='Error', message='Select first Control Shape and then one Joint', button=['OK'], icon="warning" )		
	else:
		joint = selected[0]
		ctrl_shape = selected[1]
		

	#print joint
	name_part = joint.partition("_")
	#print name_part
	#print name_part[2]
	if name_part[0] == "jnt":
		ctrl_name = "ctrl_" + name_part[2]
		grp_name = "grp_" + name_part[2]
		
		# create full circle at origin on the y-z plane
		# to follow x as pripary local rot-axis
		#ctrl_shape = mc.circle( name=ctrl_name, nr=(1, 0, 0), c=(0, 0, 0), r=7.0 )
		#ctrl_shape = mc.curve(p=[(-14.274, -9.897, -10.278), (14.274, -9.897, -10.278), (14.274, -12.373, 12.695), (-14.274, -12.373, 12.695), (-13.439, 10.857, 5.431), (13.439, 10.857, 5.431), (14.274, -12.373, 12.695), (13.439, 10.857, 5.431), (14.894, 12.373, -12.695), (14.274, -9.897, -10.278), (14.894, 12.373, -12.695), (-14.894, 12.373, -12.695), (-14.274, -9.897, -10.278), (-14.894, 12.373, -12.695), (-13.439, 10.857, 5.431), (-14.274, -12.373, 12.695), (-14.274, -9.897, -10.278)],d=1)
		ctrl_shape = mc.curve(name=ctrl_name, p=[(-6.48, -11.196, -14.382), (-6.569, -11.395, 14.165), (-14.765, 10.208, 14.29), (-14.677, 10.407, -14.257), (9.632, 9.237, -13.355), (9.549, 9.05, 13.523), (-14.765, 10.208, 14.29), (9.549, 9.05, 13.523), (15.588, -8.116, 14.877), (-6.569, -11.395, 14.165), (15.588, -8.116, 14.877), (15.68, -7.908, -14.91), (-6.48, -11.196, -14.382), (15.68, -7.908, -14.91), (9.632, 9.237, -13.355), (-14.677, 10.407, -14.257), (-6.48, -11.196, -14.382)],d=1)


		mc.setAttr(ctrl_shape + '.overrideEnabled', 1)
		mc.setAttr(ctrl_shape + '.overrideColor', 17)	# color 17 is yellow, 6 - blue, 13 - red
		
		#The enums are sorted as the colors in the attribute editor, so 0 is grey, 1 is black, 2 is dark grey, 3 is light grey, 4 is magenta etc. etc. 
		#mc.setAttr(ctrl_name + ".overrideColor",1);
		
		
		#group the ctrl_shape
		offset_group = mc.group(ctrl_shape, name=grp_name)
		
		#parent offset_group to joint
		mc.parent(offset_group, joint)
		
		mc.setAttr(grp_name + ".translateX", 0)
		mc.setAttr(grp_name + ".translateY", 0)
		mc.setAttr(grp_name + ".translateZ", 0)
		
		mc.setAttr(grp_name + ".rotateX", 0)
		mc.setAttr(grp_name + ".rotateY", 0)
		mc.setAttr(grp_name + ".rotateZ", 0)
		
		#unparent offset_group from joint
		mc.parent(offset_group, world=True)


# def printNewMenuItem(*args):
	# temp_CLR = cmds.optionMenu(colour_menu, query = True, value = True)
	# temp_SHP = cmds.optionMenu(shape_menu, query = True, value = True)
	# print "Colour is: %s" % temp_CLR
	# print "Shape is: %s" % temp_SHP
		

		
def RunApp():


	def printNewMenuItem(*args):
		temp_CLR = mc.optionMenu(colour_menu, query = True, value = True)
		temp_SHP = mc.optionMenu(shape_menu, query = True, value = True)
		print "Colour is: %s" % temp_CLR
		print "Shape is: %s" % temp_SHP


	#check if it already exists. If it does, delete it.
	wnd_name = "myWindow"
	if mc.window(wnd_name, exists=True):
		mc.deleteUI(wnd_name)

	#Maya will also save the window size for the tool to the preferences.
	#If we don't want this we need to remove them
	if mc.windowPref(wnd_name, exists=True):
		mc.windowPref(wnd_name, remove=True)

	#create the window, include the name of the window
	window = mc.window(wnd_name, title="JKTool", widthHeight=[162, 90])


	mc.columnLayout(adjustableColumn=True)
	colour_menu = mc.optionMenu( label='Colour' )
	mc.menuItem( parent=colour_menu, label='Yellow' )
	mc.menuItem( parent=colour_menu, label='Red' )
	mc.menuItem( parent=colour_menu, label='Blue' )

	shape_menu = mc.optionMenu( label='Shape' )
	mc.menuItem( parent=shape_menu, label="Base" )
	mc.menuItem( parent=shape_menu, label="Cube" )
	mc.menuItem( parent=shape_menu, label="Foot" )
	mc.menuItem( parent=shape_menu, label="Left Eye" )
	mc.menuItem( parent=shape_menu, label="Right Eye" )
	mc.menuItem( parent=shape_menu, label="Sight" )
	mc.menuItem( parent=shape_menu, label="4-Way Flat Arrow" )
	mc.menuItem( parent=shape_menu, label="4-Way Bend Arrow" )
	mc.menuItem( parent=shape_menu, label="Chest" )
	mc.menuItem( parent=shape_menu, label="Hips" )
	mc.menuItem( parent=shape_menu, label="Neck" )
	mc.menuItem( parent=shape_menu, label="Chin" )
	mc.menuItem( parent=shape_menu, label="Sphere" )
	mc.menuItem( parent=shape_menu, label="Cross" )
	mc.menuItem( parent=shape_menu, label="Cog Wheel" )
	mc.menuItem( parent=shape_menu, label="Square" )
	mc.menuItem( parent=shape_menu, label="Triangle" )
	mc.menuItem( parent=shape_menu, label="Right Hand" )

	mc.rowLayout(numberOfColumns=3, adjustableColumn=True, width=160)
	mc.button(label="Create", height=30, command=printNewMenuItem)
	mc.button(label="Undo", height=30, command="mc.undo()")


	mc.showWindow( window )