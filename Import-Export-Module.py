# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class Import_Export_PT_main_panel(bpy.types.Panel):
    bl_label = 'File Management'
    bl_idname = 'Import_Export_PT_main_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'File Management'
    bl_order = 0
    bl_ui_units_x=0

    def draw(self, context):
        layout = self.layout
        col_7A5E7 = layout.column(heading='', align=True)
        col_7A5E7.alert = False
        col_7A5E7.enabled = True
        col_7A5E7.active = True
        col_7A5E7.use_property_split = False
        col_7A5E7.use_property_decorate = False
        col_7A5E7.scale_x = 1.0
        col_7A5E7.scale_y = 1.0
        col_7A5E7.alignment = 'Expand'.upper()
        col_7A5E7.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_B9B4B = col_7A5E7.row(heading='', align=True)
        row_B9B4B.alert = False
        row_B9B4B.enabled = True
        row_B9B4B.active = True
        row_B9B4B.use_property_split = False
        row_B9B4B.use_property_decorate = False
        row_B9B4B.scale_x = 1.0
        row_B9B4B.scale_y = 1.5
        row_B9B4B.alignment = 'Expand'.upper()
        row_B9B4B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_B9B4B.operator('import_scene.fbx', text='Import', icon_value=706, emboss=True, depress=False)
        op.automatic_bone_orientation = True
        op.axis_forward = 'Y'
        op.axis_up = 'Z'
        op = row_B9B4B.operator('export_scene.fbx', text='Export', icon_value=707, emboss=True, depress=False)
        op.apply_unit_scale = False
        # Dont have to change blender scene units if we set this here
        op.global_scale=0.01
        op.use_space_transform = False
        op.bake_space_transform = True
        op.mesh_smooth_type = 'OFF'
        op.add_leaf_bones = False
        op.primary_bone_axis = 'X'
        op.secondary_bone_axis = '-Y'
        # Y Forward for unreal characters
        op.axis_forward = 'Y'
        op.axis_up = 'Z'


classes = [Import_Export_PT_main_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()