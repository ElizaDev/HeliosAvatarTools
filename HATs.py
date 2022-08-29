import bpy

bl_info = {
    "name": "Helios Avatar Tools",
    "description": "Helios Avatar Tools",
    "author": "ElizaByteVR, CascadianWorks",
    "version": (0, 1),
    "blender": (3, 2, 2),
    "location": "View 3D > Properties Panel",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "3D View",
}

class MyProperties(bpy.types.PropertyGroup):

    def filter_armature_objects(self, object):
        return object.type == 'ARMATURE' # Return true only if object contains an Armature

    armature_list : bpy.props.PointerProperty(
        name = "Armature",
        type = bpy.types.Object,
        poll = filter_armature_objects # Use poll to filter through selection
    )


class HATS_PT_main_panel(bpy.types.Panel):
    """Helios Avatar Tools"""
    bl_label = "Helios Avatar Tools"
    bl_idname = "HATS_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HATs"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool


        layout.prop(mytool, "armature_list")


        row = layout.row()
        row.operator("hats.myop_operator")


class HATS_OT_my_op(bpy.types.Operator):
    bl_label = "Fix Rig"
    bl_idname = "hats.myop_operator"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        #print(mytool.armature_list)

        if mytool.armature_list == None:
            print('No Armature Selected')
            self.report({'INFO'}, "No Armature Selected")

        if mytool.armature_list != None:
            print(bpy.context.scene.my_tool.armature_list)
            
            # Check to make sure The first bone in the armature is named "Root". If not, add new root bone and parent hips to it.
            error = RootBoneCheck(self)
            if error == True:
                return {'CANCELLED'}

            # Set scene Unit Scale to 0.01
            bpy.context.scene.unit_settings.scale_length = 0.01
            
            # Select armature and resize using selected reference
            bpy.context.scene.my_tool.armature_list.select_set(True)
            bpy.ops.transform.resize(value=(100, 100, 100))
            
            #apply transforms using selected object
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            

        return {'FINISHED'}


def RootBoneCheck(self):
    
    rootName = bpy.context.scene.my_tool.armature_list.data.bones[0].name.lower() # Get name of first bone in hierarchy
    bpy.context.scene.my_tool.armature_list.select_set(True)
    armatureObj = bpy.context.active_object
    bpy.ops.object.mode_set(mode='EDIT', toggle=False) # Switch to Edit Mode
    ebs = armatureObj.data.edit_bones
    
    if "root" not in rootName or "hip" in rootName: # Check if root already exits by name
        eb = ebs.new("Root")
        eb.head = (0, 0, 0)
        eb.tail = (0, 0, 50)
        ebs[0].parent = eb # Parent (presumed) Hips to new Root bone
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False) # Back to Object Mode
        return False

    scale = armatureObj.scale[0] # Armature scale so the root offset check will work if the model is nt a scale of 1.
    if "root" in rootName and ebs[0].head.z > 0.1 / scale: # Check to see if root bone is very offset form the armature origin
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False) # Back to Object Mode
        self.report({'WARNING'}, "Root bone not at base of model!")
        return True
        
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False) # Back to Object Mode



classes = [MyProperties, HATS_OT_my_op, HATS_PT_main_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
