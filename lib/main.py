import os
import sys
import PIL
import random
import tkinter
import tkinter.messagebox

from PIL import Image
from functools import partial
from tkinter import filedialog


# all rectangular block textures in 1.16.1 vanilla Minecraft
blocks = ['acacia_door_bottom.png', 'acacia_door_top.png', 'acacia_leaves.png', 'acacia_log.png', 'acacia_log_top.png', 'acacia_planks.png', 'acacia_sapling.png', 'acacia_trapdoor.png', 'activator_rail.png', 'activator_rail_on.png', 'allium.png', 'ancient_debris_side.png', 'ancient_debris_top.png', 'andesite.png', 'anvil.png', 'anvil_top.png', 'attached_melon_stem.png', 'attached_pumpkin_stem.png', 'azure_bluet.png', 'bamboo_large_leaves.png', 'bamboo_singleleaf.png', 'bamboo_small_leaves.png', 'bamboo_stage0.png', 'bamboo_stalk.png', 'barrel_bottom.png', 'barrel_side.png', 'barrel_top.png', 'barrel_top_open.png', 'basalt_side.png', 'basalt_top.png', 'beacon.png', 'bedrock.png', 'beehive_end.png', 'beehive_front.png', 'beehive_front_honey.png', 'beehive_side.png', 'beetroots_stage0.png', 'beetroots_stage1.png', 'beetroots_stage2.png', 'beetroots_stage3.png', 'bee_nest_bottom.png', 'bee_nest_front.png', 'bee_nest_front_honey.png', 'bee_nest_side.png', 'bee_nest_top.png', 'bell_bottom.png', 'bell_side.png', 'bell_top.png', 'birch_door_bottom.png', 'birch_door_top.png', 'birch_leaves.png', 'birch_log.png', 'birch_log_top.png', 'birch_planks.png', 'birch_sapling.png', 'birch_trapdoor.png', 'blackstone.png', 'blackstone_top.png', 'black_concrete.png', 'black_concrete_powder.png', 'black_glazed_terracotta.png', 'black_shulker_box.png', 'black_stained_glass.png', 'black_stained_glass_pane_top.png', 'black_terracotta.png', 'black_wool.png', 'blast_furnace_front.png', 'blast_furnace_side.png', 'blast_furnace_top.png', 'blue_concrete.png', 'blue_concrete_powder.png', 'blue_glazed_terracotta.png', 'blue_ice.png', 'blue_orchid.png', 'blue_shulker_box.png', 'blue_stained_glass.png', 'blue_stained_glass_pane_top.png', 'blue_terracotta.png', 'blue_wool.png', 'bone_block_side.png', 'bone_block_top.png', 'bookshelf.png', 'brain_coral.png', 'brain_coral_block.png', 'brain_coral_fan.png', 'brewing_stand.png', 'brewing_stand_base.png', 'bricks.png', 'brown_concrete.png', 'brown_concrete_powder.png', 'brown_glazed_terracotta.png', 'brown_mushroom.png', 'brown_mushroom_block.png', 'brown_shulker_box.png', 'brown_stained_glass.png', 'brown_stained_glass_pane_top.png', 'brown_terracotta.png', 'brown_wool.png', 'bubble_coral.png', 'bubble_coral_block.png', 'bubble_coral_fan.png', 'cactus_bottom.png', 'cactus_side.png', 'cactus_top.png', 'cake_bottom.png', 'cake_inner.png', 'cake_side.png', 'cake_top.png', 'campfire_log.png', 'carrots_stage0.png', 'carrots_stage1.png', 'carrots_stage2.png', 'carrots_stage3.png', 'cartography_table_side1.png', 'cartography_table_side2.png', 'cartography_table_side3.png', 'cartography_table_top.png', 'carved_pumpkin.png', 'cauldron_bottom.png', 'cauldron_inner.png', 'cauldron_side.png', 'cauldron_top.png', 'chain.png', 'chipped_anvil_top.png', 'chiseled_nether_bricks.png', 'chiseled_polished_blackstone.png', 'chiseled_quartz_block.png', 'chiseled_quartz_block_top.png', 'chiseled_red_sandstone.png', 'chiseled_sandstone.png', 'chiseled_stone_bricks.png', 'chorus_flower.png', 'chorus_flower_dead.png', 'chorus_plant.png', 'clay.png', 'coal_block.png', 'coal_ore.png', 'coarse_dirt.png', 'cobblestone.png', 'cobweb.png', 'cocoa_stage0.png', 'cocoa_stage1.png', 'cocoa_stage2.png', 'comparator.png', 'comparator_on.png', 'composter_bottom.png', 'composter_compost.png', 'composter_ready.png', 'composter_side.png', 'composter_top.png', 'conduit.png', 'cornflower.png', 'cracked_nether_bricks.png', 'cracked_polished_blackstone_bricks.png', 'cracked_stone_bricks.png', 'crafting_table_front.png', 'crafting_table_side.png', 'crafting_table_top.png', 'crimson_door_bottom.png', 'crimson_door_top.png', 'crimson_fungus.png', 'crimson_nylium.png', 'crimson_nylium_side.png', 'crimson_planks.png', 'crimson_roots.png', 'crimson_roots_pot.png', 'crimson_stem_top.png', 'crimson_trapdoor.png', 'crying_obsidian.png', 'cut_red_sandstone.png', 'cut_sandstone.png', 'cyan_concrete.png', 'cyan_concrete_powder.png', 'cyan_glazed_terracotta.png', 'cyan_shulker_box.png', 'cyan_stained_glass.png', 'cyan_stained_glass_pane_top.png', 'cyan_terracotta.png', 'cyan_wool.png', 'damaged_anvil_top.png', 'dandelion.png', 'dark_oak_door_bottom.png', 'dark_oak_door_top.png', 'dark_oak_leaves.png', 'dark_oak_log.png', 'dark_oak_log_top.png', 'dark_oak_planks.png', 'dark_oak_sapling.png', 'dark_oak_trapdoor.png', 'dark_prismarine.png', 'daylight_detector_inverted_top.png', 'daylight_detector_side.png', 'daylight_detector_top.png', 'dead_brain_coral.png', 'dead_brain_coral_block.png', 'dead_brain_coral_fan.png', 'dead_bubble_coral.png', 'dead_bubble_coral_block.png', 'dead_bubble_coral_fan.png', 'dead_bush.png', 'dead_fire_coral.png', 'dead_fire_coral_block.png', 'dead_fire_coral_fan.png', 'dead_horn_coral.png', 'dead_horn_coral_block.png', 'dead_horn_coral_fan.png', 'dead_tube_coral.png', 'dead_tube_coral_block.png', 'dead_tube_coral_fan.png', 'debug.png', 'debug2.png', 'destroy_stage_0.png', 'destroy_stage_1.png', 'destroy_stage_2.png', 'destroy_stage_3.png', 'destroy_stage_4.png', 'destroy_stage_5.png', 'destroy_stage_6.png', 'destroy_stage_7.png', 'destroy_stage_8.png', 'destroy_stage_9.png', 'detector_rail.png', 'detector_rail_on.png', 'diamond_block.png', 'diamond_ore.png', 'diorite.png', 'dirt.png', 'dispenser_front.png', 'dispenser_front_vertical.png', 'dragon_egg.png', 'dried_kelp_bottom.png', 'dried_kelp_side.png', 'dried_kelp_top.png', 'dropper_front.png', 'dropper_front_vertical.png', 'emerald_block.png', 'emerald_ore.png', 'enchanting_table_bottom.png', 'enchanting_table_side.png', 'enchanting_table_top.png', 'end_portal_frame_eye.png', 'end_portal_frame_side.png', 'end_portal_frame_top.png', 'end_rod.png', 'end_stone.png', 'end_stone_bricks.png', 'farmland.png', 'farmland_moist.png', 'fern.png', 'fire_coral.png', 'fire_coral_block.png', 'fire_coral_fan.png', 'fletching_table_front.png', 'fletching_table_side.png', 'fletching_table_top.png', 'flower_pot.png', 'frosted_ice_0.png', 'frosted_ice_1.png', 'frosted_ice_2.png', 'frosted_ice_3.png', 'furnace_front.png', 'furnace_front_on.png', 'furnace_side.png', 'furnace_top.png', 'gilded_blackstone.png', 'glass.png', 'glass_pane_top.png', 'glowstone.png', 'gold_block.png', 'gold_ore.png', 'granite.png', 'grass.png', 'grass_block_side.png', 'grass_block_side_overlay.png', 'grass_block_snow.png', 'grass_block_top.png', 'grass_path_side.png', 'grass_path_top.png', 'gravel.png', 'gray_concrete.png', 'gray_concrete_powder.png', 'gray_glazed_terracotta.png', 'gray_shulker_box.png', 'gray_stained_glass.png', 'gray_stained_glass_pane_top.png', 'gray_terracotta.png', 'gray_wool.png', 'green_concrete.png', 'green_concrete_powder.png', 'green_glazed_terracotta.png', 'green_shulker_box.png', 'green_stained_glass.png', 'green_stained_glass_pane_top.png', 'green_terracotta.png', 'green_wool.png', 'grindstone_pivot.png', 'grindstone_round.png', 'grindstone_side.png', 'hay_block_side.png', 'hay_block_top.png', 'honeycomb_block.png', 'honey_block_bottom.png', 'honey_block_side.png', 'honey_block_top.png', 'hopper_inside.png', 'hopper_outside.png', 'hopper_top.png', 'horn_coral.png', 'horn_coral_block.png', 'horn_coral_fan.png', 'ice.png', 'iron_bars.png', 'iron_block.png', 'iron_door_bottom.png', 'iron_door_top.png', 'iron_ore.png', 'iron_trapdoor.png', 'item_frame.png', 'jack_o_lantern.png', 'jigsaw_bottom.png', 'jigsaw_lock.png', 'jigsaw_side.png', 'jigsaw_top.png', 'jukebox_side.png', 'jukebox_top.png', 'jungle_door_bottom.png', 'jungle_door_top.png', 'jungle_leaves.png', 'jungle_log.png', 'jungle_log_top.png', 'jungle_planks.png', 'jungle_sapling.png', 'jungle_trapdoor.png', 'ladder.png', 'lapis_block.png', 'lapis_ore.png', 'large_fern_bottom.png', 'large_fern_top.png', 'lectern_base.png', 'lectern_front.png', 'lectern_sides.png', 'lectern_top.png', 'lever.png', 'light_blue_concrete.png', 'light_blue_concrete_powder.png', 'light_blue_glazed_terracotta.png', 'light_blue_shulker_box.png', 'light_blue_stained_glass.png', 'light_blue_stained_glass_pane_top.png', 'light_blue_terracotta.png', 'light_blue_wool.png', 'light_gray_concrete.png', 'light_gray_concrete_powder.png', 'light_gray_glazed_terracotta.png', 'light_gray_shulker_box.png', 'light_gray_stained_glass.png', 'light_gray_stained_glass_pane_top.png', 'light_gray_terracotta.png', 'light_gray_wool.png', 'lilac_bottom.png', 'lilac_top.png', 'lily_of_the_valley.png', 'lily_pad.png', 'lime_concrete.png', 'lime_concrete_powder.png', 'lime_glazed_terracotta.png', 'lime_shulker_box.png', 'lime_stained_glass.png', 'lime_stained_glass_pane_top.png', 'lime_terracotta.png', 'lime_wool.png', 'lodestone_side.png', 'lodestone_top.png', 'loom_bottom.png', 'loom_front.png', 'loom_side.png', 'loom_top.png', 'magenta_concrete.png', 'magenta_concrete_powder.png', 'magenta_glazed_terracotta.png', 'magenta_shulker_box.png', 'magenta_stained_glass.png', 'magenta_stained_glass_pane_top.png', 'magenta_terracotta.png', 'magenta_wool.png', 'melon_side.png', 'melon_stem.png', 'melon_top.png', 'mossy_cobblestone.png', 'mossy_stone_bricks.png', 'mushroom_block_inside.png', 'mushroom_stem.png', 'mycelium_side.png', 'mycelium_top.png', 'netherite_block.png', 'netherrack.png', 'nether_bricks.png', 'nether_gold_ore.png', 'nether_quartz_ore.png', 'nether_sprouts.png', 'nether_wart_block.png', 'nether_wart_stage0.png', 'nether_wart_stage1.png', 'nether_wart_stage2.png', 'note_block.png', 'oak_door_bottom.png', 'oak_door_top.png', 'oak_leaves.png', 'oak_log.png', 'oak_log_top.png', 'oak_planks.png', 'oak_sapling.png', 'oak_trapdoor.png', 'observer_back.png', 'observer_back_on.png', 'observer_front.png', 'observer_side.png', 'observer_top.png', 'obsidian.png', 'orange_concrete.png', 'orange_concrete_powder.png', 'orange_glazed_terracotta.png', 'orange_shulker_box.png', 'orange_stained_glass.png', 'orange_stained_glass_pane_top.png', 'orange_terracotta.png', 'orange_tulip.png', 'orange_wool.png', 'oxeye_daisy.png', 'packed_ice.png', 'peony_bottom.png', 'peony_top.png', 'pink_concrete.png',
'pink_concrete_powder.png', 'pink_glazed_terracotta.png', 'pink_shulker_box.png', 'pink_stained_glass.png', 'pink_stained_glass_pane_top.png', 'pink_terracotta.png', 'pink_tulip.png', 'pink_wool.png', 'piston_bottom.png', 'piston_inner.png', 'piston_side.png', 'piston_top.png', 'piston_top_sticky.png', 'podzol_side.png', 'podzol_top.png', 'polished_andesite.png', 'polished_basalt_side.png', 'polished_basalt_top.png', 'polished_blackstone.png', 'polished_blackstone_bricks.png', 'polished_diorite.png', 'polished_granite.png', 'poppy.png', 'potatoes_stage0.png', 'potatoes_stage1.png', 'potatoes_stage2.png', 'potatoes_stage3.png', 'powered_rail.png', 'powered_rail_on.png', 'prismarine_bricks.png', 'pumpkin_side.png', 'pumpkin_stem.png', 'pumpkin_top.png', 'purple_concrete.png', 'purple_concrete_powder.png', 'purple_glazed_terracotta.png', 'purple_shulker_box.png', 'purple_stained_glass.png', 'purple_stained_glass_pane_top.png', 'purple_terracotta.png', 'purple_wool.png', 'purpur_block.png', 'purpur_pillar.png', 'purpur_pillar_top.png', 'quartz_block_bottom.png', 'quartz_block_side.png', 'quartz_block_top.png', 'quartz_bricks.png', 'quartz_pillar.png', 'quartz_pillar_top.png', 'rail.png', 'rail_corner.png', 'redstone_block.png', 'redstone_dust_dot.png', 'redstone_dust_line0.png', 'redstone_dust_line1.png', 'redstone_dust_overlay.png', 'redstone_lamp.png', 'redstone_lamp_on.png', 'redstone_ore.png', 'redstone_torch.png', 'redstone_torch_off.png', 'red_concrete.png', 'red_concrete_powder.png', 'red_glazed_terracotta.png', 'red_mushroom.png', 'red_mushroom_block.png', 'red_nether_bricks.png', 'red_sand.png', 'red_sandstone.png', 'red_sandstone_bottom.png', 'red_sandstone_top.png', 'red_shulker_box.png', 'red_stained_glass.png', 'red_stained_glass_pane_top.png', 'red_terracotta.png', 'red_tulip.png', 'red_wool.png', 'repeater.png', 'repeater_on.png', 'respawn_anchor_bottom.png', 'respawn_anchor_side0.png', 'respawn_anchor_side1.png', 'respawn_anchor_side2.png', 'respawn_anchor_side3.png', 'respawn_anchor_side4.png', 'respawn_anchor_top_off.png', 'rose_bush_bottom.png', 'rose_bush_top.png', 'sand.png', 'sandstone.png', 'sandstone_bottom.png', 'sandstone_top.png', 'scaffolding_bottom.png', 'scaffolding_side.png', 'scaffolding_top.png', 'sea_pickle.png', 'shroomlight.png', 'shulker_box.png', 'slime_block.png', 'smithing_table_bottom.png', 'smithing_table_front.png', 'smithing_table_side.png', 'smithing_table_top.png', 'smoker_bottom.png', 'smoker_front.png', 'smoker_side.png', 'smoker_top.png', 'smooth_stone.png', 'smooth_stone_slab_side.png', 'snow.png', 'soul_sand.png', 'soul_soil.png', 'soul_torch.png', 'spawner.png', 'sponge.png', 'spruce_door_bottom.png', 'spruce_door_top.png', 'spruce_leaves.png', 'spruce_log.png', 'spruce_log_top.png', 'spruce_planks.png', 'spruce_sapling.png', 'spruce_trapdoor.png', 'stone.png', 'stonecutter_bottom.png', 'stonecutter_side.png', 'stonecutter_top.png', 'stone_bricks.png', 'stripped_acacia_log.png', 'stripped_acacia_log_top.png', 'stripped_birch_log.png', 'stripped_birch_log_top.png', 'stripped_crimson_stem.png', 'stripped_crimson_stem_top.png', 'stripped_dark_oak_log.png', 'stripped_dark_oak_log_top.png', 'stripped_jungle_log.png', 'stripped_jungle_log_top.png', 'stripped_oak_log.png', 'stripped_oak_log_top.png', 'stripped_spruce_log.png', 'stripped_spruce_log_top.png', 'stripped_warped_stem.png', 'stripped_warped_stem_top.png', 'structure_block.png', 'structure_block_corner.png', 'structure_block_data.png', 'structure_block_load.png', 'structure_block_save.png', 'sugar_cane.png', 'sunflower_back.png', 'sunflower_bottom.png', 'sunflower_front.png', 'sunflower_top.png', 'sweet_berry_bush_stage0.png', 'sweet_berry_bush_stage1.png', 'sweet_berry_bush_stage2.png', 'sweet_berry_bush_stage3.png', 'tall_grass_bottom.png', 'tall_grass_top.png', 'target_side.png', 'target_top.png', 'terracotta.png', 'tnt_bottom.png', 'tnt_side.png', 'tnt_top.png', 'torch.png', 'tripwire.png', 'tripwire_hook.png', 'tube_coral.png', 'tube_coral_block.png', 'tube_coral_fan.png', 'turtle_egg.png', 'turtle_egg_slightly_cracked.png', 'turtle_egg_very_cracked.png', 'twisting_vines.png', 'twisting_vines_plant.png', 'vine.png', 'warped_door_bottom.png', 'warped_door_top.png', 'warped_fungus.png', 'warped_nylium.png', 'warped_nylium_side.png', 'warped_planks.png', 'warped_roots.png', 'warped_roots_pot.png', 'warped_stem_top.png', 'warped_trapdoor.png', 'warped_wart_block.png', 'water_overlay.png', 'weeping_vines.png', 'weeping_vines_plant.png', 'wet_sponge.png', 'wheat_stage0.png', 'wheat_stage1.png', 'wheat_stage2.png', 'wheat_stage3.png', 'wheat_stage4.png', 'wheat_stage5.png', 'wheat_stage6.png', 'wheat_stage7.png', 'white_concrete.png', 'white_concrete_powder.png', 'white_glazed_terracotta.png', 'white_shulker_box.png', 'white_stained_glass.png', 'white_stained_glass_pane_top.png', 'white_terracotta.png', 'white_tulip.png', 'white_wool.png', 'wither_rose.png', 'yellow_concrete.png', 'yellow_concrete_powder.png', 'yellow_glazed_terracotta.png', 'yellow_shulker_box.png', 'yellow_stained_glass.png', 'yellow_stained_glass_pane_top.png', 'yellow_terracotta.png', 'yellow_wool.png']


win = tkinter.Tk()
tempPath = os.getcwd() + "\\temp\\" # Path for temporary files

infoTxt = tkinter.Label(win, text="Generate a 1.16 texturepack", font=20)
infoTxt.pack()

chooseTxt = tkinter.Label(win, text="Choose a rectangular and not transparent PNG file:")
chooseTxt.pack()

chooseBtn = tkinter.Button(win, text="Choose input file")
def pathChoose(): # choose input picture
    inPath = filedialog.askopenfilename(filetypes=(("PNG Files", "*.png"),("All files", "*.*")))
    if inPath != "":
        chooseBtn["text"] = inPath.split("/")[-1]
        chooseBtn["fg"] = "green"

        with open(tempPath + "inPath","w") as tempFile:
            tempFile.write(inPath)
    else:
        tkinter.messagebox.showwarning("Invalid path","Please select a file.")        

chooseBtn["command"] = pathChoose
chooseBtn.pack()

pixelTxt = tkinter.Label(win, text="Picture dimensions in pixels (recommended: 16)")
pixelTxt.pack()

pixelInp = tkinter.Entry(win)
pixelInp.pack()

genBtn = tkinter.Button(win, text="Convert picture")

def generatePicture():
    with open(tempPath + "inPath") as tempFile:
        inPath = tempFile.read()
    validSizes = ["2", "4", "8", "16", "32", "64", "128", "256"]
    if pixelInp.get() in validSizes:
        try:
            # following code is by https://opensource.com/life/15/2/resize-images-python
            # I mean, this is so complicated so yeah
            outSize = int(pixelInp.get())
            img = Image.open(inPath)
            wpercent = (outSize / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((outSize, hsize), PIL.Image.NEAREST)
            img.save(tempPath + "out.png")
            genBtn["fg"] = "green"

        except Exception as errorCode:
            tkinter.messagebox.showerror("Could not convert.",f"Errorcode: {errorCode}")
            genBtn["fg"] = "red"

    else:
        genBtn["fg"] = "red"
        tkinter.messagebox.showerror("Invalid size error",f"Supported sizes: {str(validSizes)}")
        print("Invalid size error.")

genBtn["command"] = generatePicture
genBtn.pack()

nameTxt = tkinter.Label(win, text="Choose a pack name:")
nameTxt.pack()

nameInp = tkinter.Entry(win)
nameInp.pack()

createBtn = tkinter.Button(win, text="Generate Texturepack")
def createPack():
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft")    
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures\\block")

    packMetaContent = '''{
	"pack": {
		"pack_format": 6,
		"description": [{"text":"1.16","color":"gold"},{"text":"\\nCreated by TPReplace","color":"yellow"}]
	}
}
        '''
    with open(os.getenv("APPDATA") + f'\\.minecraft\\resourcepacks\\{nameInp.get()}\\pack.mcmeta',"w") as metaFile:
        metaFile.write(packMetaContent)

    with open(tempPath + "out.png", "rb") as inBinaryFile:
        inBinary =  inBinaryFile.read() # the input picture in binary format


    blockNo = 0 # for the progress bar
    for block in blocks:
        win.title(f"Generating... [{blockNo} out of {len(blocks)}]")
        with open(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures\\block\\" + block, "wb") as blockFile:
            blockFile.write(random.choice())
        blockNo += 1

createBtn["command"] = createPack
createBtn.pack()

randomizerBtn = tkinter.Button(win, text="Randomize!")
def randomPack():
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft")    
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures")
    os.mkdir(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures\\block")

    packMetaContent = '''{
	"pack": {
		"pack_format": 6,
		"description": [{"text":"1.16","color":"gold"},{"text":"\\nCreated by TPReplace","color":"yellow"}]
	}
}
        '''
    with open(os.getenv("APPDATA") + f'\\.minecraft\\resourcepacks\\{nameInp.get()}\\pack.mcmeta',"w") as metaFile:
        metaFile.write(packMetaContent)

    blockNo = 0 # for the progress bar
    for block in blocks:
        win.title(f"Generating... [{blockNo} out of {len(blocks)}]")
        with open(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\Default 1.16.3\\assets\\minecraft\\textures\\block\\" + random.choice(blocks), "rb") as blockFile:
            inBinary = blockFile.read()

        with open(os.getenv("APPDATA") + f"\\.minecraft\\resourcepacks\\{nameInp.get()}\\assets\\minecraft\\textures\\block\\" + block, "wb") as blockFile:
            blockFile.write(inBinary)
        blockNo += 1

randomizerBtn["command"] = randomPack
randomizerBtn.pack()



win.mainloop()