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

bl_info = {
    "name" : "HATs Import/Export",
    "author" : "ElizaByteVR", 
    "description" : "Import/Export Models for Unreal Engine",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class SNA_PT_FILE_MANAGEMENT_6D4A9(bpy.types.Panel):
    bl_label = 'File Management'
    bl_idname = 'SNA_PT_FILE_MANAGEMENT_6D4A9'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'File Management'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

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
        op.use_space_transform = False
        op.bake_space_transform = True
        op.mesh_smooth_type = 'OFF'
        op.add_leaf_bones = False
        op.primary_bone_axis = 'X'
        op.secondary_bone_axis = '-Y'
        op.axis_forward = '-Y'
        op.axis_up = 'Z'


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_FILE_MANAGEMENT_6D4A9)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_FILE_MANAGEMENT_6D4A9)