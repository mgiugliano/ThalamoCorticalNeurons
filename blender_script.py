#
# Authored by Dr. Justas BIRGIOLAS (The Ronin Institute, USA)
#

# Import modules (Blender Python Scripting, math for 'pi', and numpy)
import bpy
from math import pi
import numpy as np


# Delete the default 'cube' object if it exists
if 'Cube' in bpy.data.objects:
    bpy.data.objects['Cube'].select = True
    bpy.ops.object.delete(use_global=False)


# Get list of cells from NRN
bpy.ops.blenderneuron.get_cell_list_from_neuron()

# Get a reference to the cell group
group = bpy.data.scenes["Scene"].BlenderNEURON.groups[0]

# Tell BN to collect section variable values over time
group.record_activity = True

# Collect activity from each section
group.recording_granularity = 'Section'

# When to collect activity (in simulation ms)
group.recording_time_start = 0
group.recording_time_end = 5

# How often to collect section variables (in simulation ms)
group.recording_period = 0.1


# How many Blender frames to use for each ms of simulation
group.frames_per_ms = 10

# Set Blender last frame to the total frames (e.g. 5ms @ 10 frames/ms = 50 frames)
bpy.data.scenes['Scene'].frame_end = group.recording_time_end * \
    group.frames_per_ms

# Which NEURON variable to record for each section
# replace this with any other section var that can be accessed like section_name.v(0.5)
group.record_variable = 'v'

# The smallest value of record_variable to use for color range
# Since 'v' is the target, the values are in mV
group.animation_range_low = -70

# The largest value of recorded variable for color range (plotting v, so mV units)
group.animation_range_high = 0

# Color to use to represent the maximum value of recorded variable
# (corresponds to animation_range_high)
bpy.data.materials['Group.000_color_ramp'].diffuse_ramp.elements[1].color \
    = [1, 1, 1, 1]  # RGBA White

# Color for min value (animation_range_low)
bpy.data.materials['Group.000_color_ramp'].diffuse_ramp.elements[0].color \
    = [0.02, 0.67, 0.67, 1]  # RGBA Light Blue


# Hit "Run" in NEURON and import simulation results
bpy.ops.blenderneuron.import_groups()

# Show camera perspective
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        area.spaces[0].region_3d.view_perspective = 'CAMERA'
        break

# Lock camera to view
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        area.spaces.active.lock_camera = True

# Move/rotate camera to show imported cell
bpy.data.objects['Camera'].location = [1.21, 284.07, 1458.86]  # XYZ
bpy.data.objects['Camera'].rotation_euler \
    = np.array([0, 0, 90]) * pi/180  # In radians

# Set render background color (dark for contrast with cell)
bpy.data.worlds['World'].use_sky_blend = True
bpy.data.worlds['World'].zenith_color = [0, 0, 0]  # Black
bpy.data.worlds['World'].horizon_color = [0, 0, 0.011]  # Dark blue

# Set render resolution
width = 1920
# Set this to 100 for full resolution (slower, high q)
bpy.data.scenes['Scene'].render.resolution_percentage = 25
bpy.data.scenes['Scene'].render.resolution_x = width
bpy.data.scenes['Scene'].render.resolution_y = width * 0.5625

# Set video file directory (can also be a specific file name)
bpy.data.scenes['Scene'].render.filepath = './results/'
# was bpy.data.scenes['Scene'].render.filepath = '/tmp/'

# Video format
bpy.data.scenes['Scene'].render.image_settings.file_format = 'FFMPEG'

# Add "neon" effect to increase contrast for activity animations
bpy.ops.blenderneuron.add_neon_effect()

# Render animation to video file
bpy.ops.render.render(animation=True)

# Quit blender
# bpy.ops.wm.quit_blender()
