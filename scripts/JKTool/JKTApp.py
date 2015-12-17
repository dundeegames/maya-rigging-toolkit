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


def RunApp():

	def createCtrlShape(*args):
		selected = mc.ls(selection=True)

		if (len(selected) != 1) or not( mc.objectType( selected[0], isType="joint" )):
			# "question", "information", "warning" and "critical"
			mc.confirmDialog( title='Error', message="Select one Joint", button=['OK'], icon="warning" )
			return
		else:
			joint = selected[0]
			
		# Find the name partition
		name_part = joint.partition("_")
		
		if name_part[0] == "jnt":
			ctrl_name = "ctrl_" + name_part[2]
			grp_name = "grp_" + name_part[2]
			
			
			#query selected colour_menu
			temp_CLR = mc.optionMenu(colour_menu, query = True, value = True)
			
			if(temp_CLR == "Yellow"):
				shapeColour = 17
			elif(temp_CLR == "Red"):
				shapeColour = 13
			elif(temp_CLR == "Blue"):
				shapeColour = 6
			else:
				mc.confirmDialog( title='Error', message="Not such Colour option!", button=['OK'], icon="warning" )
				return
			
			#query selected shape_menu
			temp_SHP = mc.optionMenu(shape_menu, query = True, value = True)
			
			if(temp_SHP == "Base"):
				ctrl_shape = jktc.baseShape(ctrl_name)
			elif(temp_SHP == "Circle"):
				ctrl_shape = jktc.circleShape(ctrl_name)
			elif(temp_SHP == "Cube"):
				ctrl_shape = jktc.cubeShape(ctrl_name)
			elif(temp_SHP == "Left Foot"):
				ctrl_shape = jktc.footShapeL(ctrl_name)
			elif(temp_SHP == "Right Foot"):
				ctrl_shape = jktc.footShapeR(ctrl_name)
			elif(temp_SHP == "Left Eye"):
				ctrl_shape = jktc.eyeShapeL(ctrl_name)
			elif(temp_SHP == "Right Eye"):
				ctrl_shape = jktc.eyeShapeR(ctrl_name)
			elif(temp_SHP == "Sight"):
				ctrl_shape = jktc.sightShape(ctrl_name)
			elif(temp_SHP == "4-Way Flat Arrow"):
				ctrl_shape = jktc.flatArrow4(ctrl_name)
			elif(temp_SHP == "4-Way Bend Arrow"):
				ctrl_shape = jktc.bendArrow4(ctrl_name)
			elif(temp_SHP == "Chest"):
				ctrl_shape = jktc.chestShape(ctrl_name)				
			elif(temp_SHP == "Hips"):
				ctrl_shape = jktc.hipShape(ctrl_name)
			elif(temp_SHP == "Neck"):
				ctrl_shape = jktc.hipShape(ctrl_name)
			elif(temp_SHP == "Head"):
				ctrl_shape = jktc.headShape(ctrl_name)
			elif(temp_SHP == "Chin"):
				ctrl_shape = jktc.chinShape(ctrl_name)
			elif(temp_SHP == "Sphere"):
				ctrl_shape = jktc.sphereShape(ctrl_name)
			elif(temp_SHP == "Cross"):
				ctrl_shape = jktc.crossShape(ctrl_name)
			elif(temp_SHP == "Cog Wheel"):
				ctrl_shape = jktc.cogWheelShape(ctrl_name)
			elif(temp_SHP == "Square"):
				ctrl_shape = jktc.squareShape(ctrl_name)
			elif(temp_SHP == "Triangle"):
				ctrl_shape = jktc.triangleShape(ctrl_name)
			elif(temp_SHP == "Right Hand"):
				ctrl_shape = jktc.handShape(ctrl_name)
			else:
				mc.confirmDialog( title='Error', message="Not such Shape option!", button=['OK'], icon="warning" )
				return
			
			# create shape at origin on the y-z plane
			# to follow x as pripary local rot-axis
			#ctrl_shape = mc.curve(name=ctrl_name, p=[(-6.48, -11.196, -14.382), (-6.569, -11.395, 14.165), (-14.765, 10.208, 14.29), (-14.677, 10.407, -14.257), (9.632, 9.237, -13.355), (9.549, 9.05, 13.523), (-14.765, 10.208, 14.29), (9.549, 9.05, 13.523), (15.588, -8.116, 14.877), (-6.569, -11.395, 14.165), (15.588, -8.116, 14.877), (15.68, -7.908, -14.91), (-6.48, -11.196, -14.382), (15.68, -7.908, -14.91), (9.632, 9.237, -13.355), (-14.677, 10.407, -14.257), (-6.48, -11.196, -14.382)],d=1)


			mc.setAttr(ctrl_shape + '.overrideEnabled', 1)
			mc.setAttr(ctrl_shape + '.overrideColor', shapeColour)	# color 17 is yellow, 6 - blue, 13 - red
			#The enums are sorted as the colors in the attribute editor, so 0 is grey, 1 is black, 2 is dark grey, 3 is light grey, 4 is magenta etc. etc. 
			
			
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
	colour_menu = mc.optionMenu( label="Colour" )
	mc.menuItem( parent=colour_menu, label="Yellow" )
	mc.menuItem( parent=colour_menu, label="Red" )
	mc.menuItem( parent=colour_menu, label="Blue" )

	shape_menu = mc.optionMenu( label="Shape" )
	mc.menuItem( parent=shape_menu, label="Base" )
	mc.menuItem( parent=shape_menu, label="Circle" )
	mc.menuItem( parent=shape_menu, label="Cube" )
	mc.menuItem( parent=shape_menu, label="Left Foot" )
	mc.menuItem( parent=shape_menu, label="Right Foot" )
	mc.menuItem( parent=shape_menu, label="Left Eye" )
	mc.menuItem( parent=shape_menu, label="Right Eye" )
	mc.menuItem( parent=shape_menu, label="Sight" )
	mc.menuItem( parent=shape_menu, label="4-Way Flat Arrow" )
	mc.menuItem( parent=shape_menu, label="4-Way Bend Arrow" )
	mc.menuItem( parent=shape_menu, label="Chest" )
	mc.menuItem( parent=shape_menu, label="Hips" )
	mc.menuItem( parent=shape_menu, label="Neck" )
	mc.menuItem( parent=shape_menu, label="Head" )
	mc.menuItem( parent=shape_menu, label="Chin" )
	mc.menuItem( parent=shape_menu, label="Sphere" )
	mc.menuItem( parent=shape_menu, label="Cross" )
	mc.menuItem( parent=shape_menu, label="Cog Wheel" )
	mc.menuItem( parent=shape_menu, label="Square" )
	mc.menuItem( parent=shape_menu, label="Triangle" )
	mc.menuItem( parent=shape_menu, label="Right Hand" )

	mc.rowLayout(numberOfColumns=3, adjustableColumn=True, width=160)
	mc.button(label="Create", height=30, command=createCtrlShape)
	mc.button(label="Undo", height=30, command="mc.undo()")


	mc.showWindow( window )