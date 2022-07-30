bl_info = {
    "name": "Helios Avatar Tools",
    "author": "ElizaByteVR",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "N-Panel",
    "description": "Adds various tools to help with Helios VR Conversion",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
    }

import bpy


class MyProperties(bpy.types.PropertyGroup):

    armature_list : bpy.props.PointerProperty(
        name= "Armature",
        type= bpy.types.Armature
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

        print(mytool.armature_list)

        if mytool.armature_list == None:
            print('No Armature Selected')
            self.report({'INFO'}, "No Armature Selected")

        if mytool.armature_list != None:
            print('Congrats you selected an armature')
            bpy.context.scene.unit_settings.scale_length = 0.01
            bpy.ops.transform.resize(value=(100, 100, 100))
            bpy.context.scene.my_tool.armature_list = None
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


        return {'FINISHED'}


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
