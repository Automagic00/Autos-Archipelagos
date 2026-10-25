from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from BaseClasses import CollectionState

from .options import ACTGameOptions
from . import logic

if TYPE_CHECKING:
    from . import ACTWorld

def set_region_rules(world: "ACTWorld") -> None:
  multiworld = world.multiworld
  player = world.player
  options = world.options

  multiworld.get_entrance("Central Shallows -> Central Shallows - Items Behind Grapple", player).access_rule = \
    lambda state: logic.can_skip_some_grapples(options, state, player)
    
  multiworld.get_entrance("Central Shallows -> Fort Slacktide - Before Destruction", player).access_rule = \
    lambda state: logic.is_slacktide_before_accessible(options, state, player)

  multiworld.get_entrance("Fort Slacktide - Before Destruction -> Moon Snail's Cave", player).access_rule = \
    lambda state: logic.is_moonsnail_accessible(options, state, player)
   
  multiworld.get_entrance("Fort Slacktide - Before Destruction -> Fort Slacktide - After Destruction", player).access_rule = \
    lambda state: state.has("Pristine Pearl", player)
    
  multiworld.get_entrance("Fort Slacktide - Before Destruction -> Reef's Edge", player).access_rule = \
    lambda state: logic.can_magista_skip(options, state, player)
    
  multiworld.get_entrance("Fort Slacktide - After Destruction -> Reef's Edge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_reefs_edge_accessible_vanilla(state, player)
    
  multiworld.get_entrance("Reef's Edge -> Reef's Edge - Items Behind Grapple", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_skip_some_grapples(options, state, player)
    
  multiworld.get_entrance("The Sands Between -> Secluded Ridge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_secluded_ridge_accessible(options, state, player)

  multiworld.get_entrance("The Sands Between -> The Sands Between - Grapple to East of Grove", player).access_rule = \
    lambda state: (options.goal == "magista") or state.has_all({"Fishing Line", "Eelectrocute"}, player)

  multiworld.get_entrance("Secluded Ridge -> Secluded Ridge - Past Eelectrocute", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_secluded_ridge_eel_accessible(options, state, player)
    
  multiworld.get_entrance("The Sands Between -> Trashbin Plateau", player).access_rule = \
    lambda state: (options.goal == "magista") or state.has("Mantis Punch", player)
    
  multiworld.get_entrance("The Sands Between -> Southern Town Ridge", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_southern_town_ridge_accessible(options, state, player)
    
  multiworld.get_entrance("Expired Grove - Main -> Flotsam Vale - Consortium Arena",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_grove(options, state, player)
    
  multiworld.get_entrance("Expired Grove - Main -> Expired Grove - Raised Platforms",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_grove(options, state, player)
  
  multiworld.get_entrance("Flotsam Vale -> Flotsam Vale - Post Ceviche Sisters", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_post_ceviche_accessible(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Flotsam Vale - Consortium Arena", player).access_rule = \
    lambda state: (options.goal == "magista") or logic.is_consortium_accessible_vale(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Scuttleport",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.can_access_scuttleport(options, state, player)
    
  multiworld.get_entrance("Flotsam Vale -> Plug Fuse Pipes",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.has_all_maps(state,player)
    
  multiworld.get_entrance("Scuttleport -> Plug Fuse Pipes",player).access_rule = \
    lambda state: (options.goal == "magista") or logic.has_all_maps(state,player)
    
  multiworld.get_entrance("Flotsam Vale -> Pinbarge", player).access_rule = \
    lambda state: logic.has_all_maps(state,player) and state.has("Eelectrocute", player)
  
def set_location_rules(world: "ACTWorld") -> None:
  multiworld = world.multiworld
  player = world.player
  options = world.options

# ---- Forkless Logic ----

  #Forkless Disabled, ensures player has fork for bosses
  if options.allow_forkless == "disabled":
    set_rule(multiworld.get_location("Bloodstar Limb (Central Shallows - Help a Crab)",player),
           lambda state: state.has("Fork",player))

    set_rule(multiworld.get_location("Nephro, Captain of the Guard", player),
           lambda state: state.has("Fork",player))
    
    set_rule(multiworld.get_location("Polluted Platoon Pathfinder", player),
           lambda state: state.has("Fork",player))
    
    set_rule(multiworld.get_location("Royal Shellsplitter", player),
           lambda state: state.has("Fork",player))
    
    set_rule(multiworld.get_location("Magista, Tyrant of Slacktide", player),
           lambda state: state.has("Fork",player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location("Extremely Rude Snail", player), 
                lambda state: state.has("Fork",player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location("Pagurus, The Ravenous", player),
                lambda state: (state.has("Fork",player) or logic.can_pagurus_quick_kill(options,state,player))) #allow pagurus quick kill if not vanilla
        
        set_rule(multiworld.get_location("Diseased Lichenthrope", player),
                lambda state: state.has("Fork",player))
        
        set_rule(multiworld.get_location("Curdled Carbonara Connoisseur", player),
                lambda state: state.has("Fork",player))
        
        set_rule(multiworld.get_location("Heikea, Intimidation Crab", player),
                lambda state: (state.has("Fork",player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location("Grovekeeper Topoda", player),
                lambda state: state.has("Fork",player))
        
        set_rule(multiworld.get_location("The Consortium", player),
                lambda state: state.has("Fork",player))
        
        set_rule(multiworld.get_location("Scuttling Sludge Steamroller", player),
                lambda state: state.has("Fork",player))
        
        set_rule(multiworld.get_location("Ceviche Sisters", player),
                lambda state: state.has("Fork",player))

        set_rule(multiworld.get_location("Voltai, The Accumulator", player),
                lambda state: state.has("Fork",player))
                
        if options.goal != "voltai":        
                set_rule(multiworld.get_location("Roland, Venture Crabitalist", player),
                        lambda state: state.has("Fork",player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location("Petroch, The False Moon", player),
                                lambda state: state.has("Fork",player))
                        
                        set_rule(multiworld.get_location("Inkerton, Crab Hunter", player),
                                lambda state: state.has("Fork",player))
                        
                        set_rule(multiworld.get_location("Camtscha, The Bleached King", player),
                                lambda state: state.has("Fork",player))
                        
                        set_rule(multiworld.get_location("Praya Dubia, The Ocean's Agony", player),
                                lambda state: state.has("Fork",player))
                        
                        set_rule(multiworld.get_location("Firth, The Crab Who Stole The Whorl", player),
                                lambda state: state.has("Fork",player))
                        
                        

    #Forkless Enabled, ensures player has some means of dealing damage for bosses
  elif options.allow_forkless == "forkless_easy":
    set_rule(multiworld.get_location("Bloodstar Limb (Central Shallows - Help a Crab)", player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location("Nephro, Captain of the Guard", player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location("Royal Shellsplitter", player),
            lambda state: logic.can_deal_damage_easy(state,player))
    
    set_rule(multiworld.get_location("Polluted Platoon Pathfinder", player),
            lambda state: logic.can_deal_damage_easy(state,player))
      
    set_rule(multiworld.get_location("Magista, Tyrant of Slacktide", player),
            lambda state: logic.can_deal_damage_easy(state,player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location("Extremely Rude Snail", player),
                lambda state: logic.can_deal_damage_easy(state.player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location("Pagurus, The Ravenous", player),
                lambda state: (logic.can_deal_damage_easy(state,player) or logic.can_pagurus_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location("Diseased Lichenthrope", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("Curdled Carbonara Connoisseur", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("Heikea, Intimidation Crab", player),
                lambda state: (logic.can_deal_damage_easy(state,player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location("Grovekeeper Topoda", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("The Consortium", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("Scuttling Sludge Steamroller", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("Ceviche Sisters", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        set_rule(multiworld.get_location("Voltai, The Accumulator", player),
                lambda state: logic.can_deal_damage_easy(state,player))
        
        if options.goal != "voltai":
                set_rule(multiworld.get_location("Roland, Venture Crabitalist", player),
                        lambda state: logic.can_deal_damage_easy(state,player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location("Petroch, The False Moon", player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location("Inkerton, Crab Hunter", player),
                                lambda state: logic.can_deal_damage_easy(state,player)) 
                        
                        set_rule(multiworld.get_location("Camtscha, The Bleached King", player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location("Praya Dubia, The Ocean's Agony", player),
                                lambda state: logic.can_deal_damage_easy(state,player))
                        
                        set_rule(multiworld.get_location("Firth, The Crab Who Stole The Whorl", player),
                                lambda state: logic.can_deal_damage_easy(state,player))
  
  else:
    set_rule(multiworld.get_location("Bloodstar Limb (Central Shallows - Help a Crab)",player),
           lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location("Nephro, Captain of the Guard", player),
            lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location("Royal Shellsplitter", player),
            lambda state: logic.can_deal_damage_hard(state,player))
    
    set_rule(multiworld.get_location("Polluted Platoon Pathfinder", player),
            lambda state: logic.can_deal_damage_hard(state,player))
      
    set_rule(multiworld.get_location("Magista, Tyrant of Slacktide", player),
            lambda state: logic.can_deal_damage_hard(state,player))

    if options.ngplus_bosses:
        set_rule(multiworld.get_location("Extremely Rude Snail", player),
                lambda state: logic.can_deal_damage_easy(state.player))
    
    if options.goal != "magista":
        set_rule(multiworld.get_location("Pagurus, The Ravenous", player),
                lambda state: (logic.can_deal_damage_hard(state,player) or logic.can_pagurus_quick_kill(options)))
        
        set_rule(multiworld.get_location("Diseased Lichenthrope", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("Curdled Carbonara Connoisseur", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("Heikea, Intimidation Crab", player),
                lambda state: (logic.can_deal_damage_hard(state,player) or logic.can_heikia_quick_kill(options,state,player)))
        
        set_rule(multiworld.get_location("Grovekeeper Topoda", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("The Consortium", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("Scuttling Sludge Steamroller", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("Ceviche Sisters", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        set_rule(multiworld.get_location("Voltai, The Accumulator", player),
                lambda state: logic.can_deal_damage_hard(state,player))
        
        if options.goal !="voltai":
                set_rule(multiworld.get_location("Roland, Venture Crabitalist", player),
                        lambda state: logic.can_deal_damage_hard(state,player))
                
                if options.goal != "roland":
                        set_rule(multiworld.get_location("Petroch, The False Moon", player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location("Inkerton, Crab Hunter", player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location("Camtscha, The Bleached King", player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location("Praya Dubia, The Ocean's Agony", player),
                                lambda state: logic.can_deal_damage_hard(state,player))
                        
                        set_rule(multiworld.get_location("Firth, The Crab Who Stole The Whorl", player),
                                lambda state: logic.can_deal_damage_hard(state,player))
    
# ---- Cave of Respite ----
 # spearfishing
  set_rule(multiworld.get_location("Clothesclaw (Cave of Respite - Fishing Before Cave Entrance)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
  
  set_rule(multiworld.get_location("Chipclaw (Cave of Respite - Fishing Near Fork Pickup)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
  
  set_rule(multiworld.get_location("Mussel (Cave of Respite - Fishing In Crab Fight Tutorial)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
  
  set_rule(multiworld.get_location("Sand Dollar (Cave of Respite - Fishing on Path Before Cave)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))

# ---- Central Shallows ----
 # grapple   
  set_rule(multiworld.get_location("Chipclaw (Central Shallows - Southwest Sandcastle)", player),
            lambda state: state.has("Fishing Line", player))
    
  set_rule(multiworld.get_location("Bloodstar Limb (Central Shallow - Southwest Sandcastle Clam)", player),
            lambda state: state.has("Fishing Line", player))
    
  set_rule(multiworld.get_location("Another Crab (Central Shallows - Tall Pillar Near Royal Shellsplitter)", player),
            lambda state: state.has("Fishing Line", player) or logic.can_CAL(options,state,player))
    
  set_rule(multiworld.get_location("Sand Dollar (Central Shallows - South Arch Wall)", player),
            lambda state: state.has("Fishing Line", player))

  set_rule(multiworld.get_location("Clothesclaw (Central Shallows - Small Tower Outside Southwest Fort)", player),
            lambda state: (state.has("Fishing Line", player) and state.can_reach_location("Nephro, Captain of the Guard", player)) or logic.are_skips_allowed(options))

  set_rule(multiworld.get_location("Clothesclaw (Central Shallows - Small Tower Outside Southwest Fort)", player), 
            lambda state: state.has("Fishing Line", player) and state.can_reach_location("Nephro, Captain of the Guard", player))
 
 # spearfishing
  set_rule(multiworld.get_location("Mussel (Central Shallows - Dig Spot Near Southwest Sandcastle)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
    
  set_rule(multiworld.get_location("Breadclaw (Central Shallows - Fishing South of Slacktide Entrance)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
    
  set_rule(multiworld.get_location("Anemone (Central Shallows - Hidden Fishing on South-Eastern Wall of Castle on South-Western Plateau)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
    
  set_rule(multiworld.get_location("Razor Blade (Central Shallows - Fishing South West of Slacktide Near Bottles)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
    
  set_rule(multiworld.get_location("Anemone [Stowaway] (Central Shallow - Fishing West of Umbrella)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))

# ---- Fort Slacktide ----
 # grapple

  set_rule(multiworld.get_location("Magista, Tyrant of Slacktide",player),
            lambda state: state.has("Fishing Line", player))
 
  set_rule(multiworld.get_location("Limpet (Slacktide - Stairs Left of Main Hallway)", player),
            lambda state: state.has("Fishing Line", player))
   
  set_rule(multiworld.get_location("Seastar (Slacktide - Top of Fishing Line Room)", player),
            lambda state: state.has("Fishing Line", player))
    
  set_rule(multiworld.get_location("Barnacle (Slacktide - After Big Urchin Spiral Staircase)", player),
            lambda state: (state.has("Fishing Line", player) or logic.can_boost_jump(options, state, player)))
    
  set_rule(multiworld.get_location("Rusty Nail (Slacktide - Big Urchin Staircase Grapple Point)", player),
            lambda state: state.has("Fishing Line", player) or ((logic.can_big_boost_jump(options, state, player) and state.can_reach_region("Fort Slacktide - After Destruction",player))))
    
  set_rule(multiworld.get_location("Chipclaw (Fort Slacktide - Behind Broken Wall)", player),
            lambda state: state.has("Fishing Line", player))
    
  set_rule(multiworld.get_location("Bloodstar Limb (Slacktide - Clam Above Duchess's Chamber)", player),
            lambda state: state.has("Fishing Line", player))
    
 # spearfishing
  set_rule(multiworld.get_location("Breadclaw (Fort Slacktide - Path to Roof Hidden Fishing)", player),
            lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))

# Other
  set_rule(multiworld.get_location("Breadclaw (Fort Slacktide - On South Training Area Wall)", player), 
            lambda state: state.has("Pristine Pearl", player))

  if options.goal != "magista":
        # ---- Reef's Edge ----        
        # mantis punch
        set_rule(multiworld.get_location("Sea Star+ (Reef's Edge - Top of Large Hammer Crab Pole)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Hairclaw (Reef's Edge - Near I95 Sign On Ledge)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Reef's Edge - North Facing Cliff Near Seahorse)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Whelk+ (Reef's Edge - Near Orange Coral and Sponge)", player),
                lambda state: state.has("Mantis Punch", player))
        
        # ---- New Carcinia ----
        # grapple
        set_rule(multiworld.get_location("Sand Dollar (New Carcinia - Flat Coral Near/Above Hammerhead)", player),
                lambda state: state.has("Fishing Line", player))
        
        # ---- Sands Between ----
        # grapple
        set_rule(multiworld.get_location("Barbed Hook (The Sands Between - Top of Spire Near Grove Entrance)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Clown Costume (The Sands Between - Path of the Clown)", player),
                lambda state: state.has("Fishing Line", player))
        
        # mantis punch
        set_rule(multiworld.get_location("Rusty Nail+ (The Sands Between - Mantis Block near Central Vista)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Sea Star+ (The Sands Between - Mantis Block near Flotsam Vale Entrance)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Sea Slug (The Sands Between - Mantis Block below Crab Rave)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Sea Slug (The Sands Between - Mantis Block below Crab Rave)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Sinker+ (The Sands Between - Mantis Block North of Secluded Ridge)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Limpet+ (The Sands Between - Mantis Block at Grove Entrance)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Old World Whorl (The Sands Between - Mantis Block Pitfall North of Central Vista)", player),
                lambda state: state.has("Mantis Punch", player))
        
        # eelectrocute
        set_rule(multiworld.get_location("Lumpsucker+ (The Sands Between - On the anchor, after the electric crab)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Stainless Relic (The Sands Between - On Electric Crab Platform)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Tackle Pouch (The Sands Between - Eelectrocute Crab North of Chains)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Paperclaw (The Sands Between - Southern Eelectrocute Path, Near Shortcut)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Sinker+ (The Sands Between - South Eelectrocute Path)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Mussel+ (The Sands Between - South Eelectrocute Path First Jump)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Hairclaw (The Sands Between - South Eelectrocute Path Second Jump)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Hearkelp Sprout (The Sands Between - South Eelectrocute Path, Green Coral Side Path)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Barbed Hook (The Sands Between - South Eelectrocute Path Large Island)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Oyster (The Sands Between - South Eelectrocute Path Large Island Ashtray)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Barbed Hook (The Sands Between - South Eelectrocute Path Near Shellsplitter)", player),
                lambda state: state.has("Eelectrocute", player))
        
        set_rule(multiworld.get_location("Paperclaw (The Sands Between - Behind Trashbag Near Anchor)", player),
                lambda state: state.has("Eelectrocute", player))
        
        # spearfishing
        set_rule(multiworld.get_location("Hairclaw (The Sands Between - Fishing Near Anchor)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Chipclaw (The Sands Between - Fishing North East of Chains)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (The Sands Between - Fishing Near Propane Tank)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Mussel (The Sands Between - Fishing Near Bobbit Hill)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (The Sands Between - Fishing Between Central Vista and Anchor)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barnacle (The Sands Between - Fishing On Bobbit Hill 2nd Layer)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Breadclaw (The Sands Between - Fishing Near Nail)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Breadclaw (The Sands Between - Fishing In Wooden Pallet)", player),
                lambda state: state.has("Spearfishing", player))

        # spearfishing + eelectrocute
        set_rule(multiworld.get_location("Hairclaw (The Sands Between - South Eelectrocute Path Large Island Fishing)", player),
                lambda state: state.has_all({"Spearfishing", "Eelectrocute"}, player))
        
        set_rule(multiworld.get_location("Chipclaw (The Sands Between - Hidden Fishing on Stone Cliff Near Anchor)", player),
                lambda state: state.has_all({"Spearfishing", "Eelectrocute"}, player))

        # grapple + eelectrocute
        set_rule(multiworld.get_location("Whelk++ (The Sands Between - South Eelectrocute Path First Island Peak)", player),
                lambda state: state.has_all({"Fishing Line", "Eelectrocute"}, player))
        
        set_rule(multiworld.get_location("Salp+ (The Sands Between - Eelectrocute Path Near Grove Small Island)", player),
                lambda state: state.has_all({"Fishing Line", "Eelectrocute"}, player))
        
        set_rule(multiworld.get_location("Used Bandage (The Sands Between - Eelectrocute Path Near Grove)", player),
                lambda state: state.has_all({"Fishing Line", "Eelectrocute"}, player))

        # post-pag
        set_rule(multiworld.get_location("Bloodstar Limb (Post Pagurus - Crab Swarm Near Anchor)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Stapleclaw (Post Pagurus - Litterbox)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Hairclaw (Post Pagurus - Middle of Chains)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Post Pagurus - Middle of Chains)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - East of Chains)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Near Northeastern Chain)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Near Preserver East of Chains)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Rocks North-East of Central Vista)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Rocks North-West of Ridge Overlook)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Fence Near North-East Eelectrocute Path)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Hairclaw (Post Pagurus - North of Ridge Overlook)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Hairclaw (Post Pagurus - East of Central Vista)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - West of Playground)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Chipclaw (Post Pagurus - Preserver North-West of Propane)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - Near Secluded Ridge Entrance)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Post Pagurus - South-West of Central Vista)", player),
                lambda state: state.has("Map Piece - Pagurus", player))
        
        set_rule(multiworld.get_location("Paperclaw (Post Pagurus - South of Chains)", player),
                lambda state: state.has("Map Piece - Pagurus", player))


        # ---- Secluded Ridge and Trashbin Plateau ----
        # grapple
        set_rule(multiworld.get_location("Shark Egg (Secluded Ridge - Broom Spire Peak)", player),
                lambda state: state.has("Mantis Punch", player) and (logic.can_CAL(options, state, player) or state.has("Fishing Line", player)))
                
        set_rule(multiworld.get_location("Bobber (Secluded Ridge - Broom Spire Climb)", player),
                lambda state: state.has_all({"Mantis Punch","Fishing Line"}, player))
        
        # spearfishing
        set_rule(multiworld.get_location("Clothesclaw (Secluded Ridge - Fishing on Ridge Overlook)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Chipclaw [Currency] (Fishing South of Ridge Overlook)", player),
                lambda state: state.has("Spearfishing", player))
          
        set_rule(multiworld.get_location("Cockle (Secluded Ridge - Fishing on Eelectrocute Path)", player),
                lambda state: state.has("Spearfishing", player))

        # spearfishing + eelectrocute
        set_rule(multiworld.get_location("Stapleclaw (Trashbin Plateau - Eelectrocute Grapple Path Fishing)", player),
                lambda state: state.has_all({"Spearfishing", "Eelectrocute"}, player))

        # grapple + eelectrocute
        set_rule(multiworld.get_location("Barbed Hook (Trashbin Plateau - Eelectrocute Grapple Path)", player),
                lambda state: state.has_all({"Fishing Line", "Eelectrocute"}, player))
        
        # ---- Expired Grove Main ----
        # grapple        
        set_rule(multiworld.get_location("Hairclaw (Expired Grove Main - Milk Carton Urchins)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Breadclaw (Expired Grove Main - Grapple Near Top of Oil Drum)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Main - Main Pathway Around Oil Drum)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Shark Tooth (Expired Grove Main - Under Pizza Box)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Map Piece - Heikea", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Main - Shopping Cart Buildings)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Heartkelp Sprout (Expired Grove Main - Top of Shopping Cart Buildings)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Contact Lens (Expired Grove Main - Behind Shopping Cart Buildings)", player),
                lambda state: state.has("Fishing Line", player))
        
        # mantis punch
        set_rule(multiworld.get_location("Shark Egg (Expired Grove Main - Mantis Block on Left Path)", player),
                lambda state: state.has("Mantis Punch", player))
        
        set_rule(multiworld.get_location("Cotton Ball (Expired Grove Main - Mantis Block on Oil Drum Path)", player),
                lambda state: state.has("Mantis Punch", player))
        
        # spearfishing
        set_rule(multiworld.get_location("Mussel (Expired Grove Main - Fishing by Entrance)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Expired Grove Main - Fishing Near Mantis Block)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Sponge (Expired Grove Main - Fishing by Crystal Parkour)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Hairclaw (Expired Grove Main - Hidden Fishing Near Milk Carton)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Oyster (Expired Grove Main - River Fishing Under Bridge)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Limpet (Expired Grove Main - River Fishing Before Lichenthrope)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Expired Grove Main - River Fishing Near Carbonara Waterfall)", player),
                lambda state: state.has("Spearfishing", player))

        # ---- Expired Grove Village ----
        # grapple
        set_rule(multiworld.get_location("Hairclaw (Expired Grove Village - In North East High Milk Carton)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Tackle Pouch (Expired Grove Village - Clam Near Cave Shortcut)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Clotheclaw (Expired Grove Village - Upside Down Village)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Phytoplankton+ (Expired Grove Village - Top of Upside Down village)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - Above Village 1)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - Above Village 2)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - Above Village 3)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - In Bottle After Ornament Parkour)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - In Hammer Crab Cave)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Wad of Gum (Expired Grove Village - Gum Pile in Hammer Crab Cave)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Stainless Relic (Expired Grove Village - Clam in Hammer Crab Cave)", player),
                lambda state: state.has("Fishing Line", player))
        
        set_rule(multiworld.get_location("Anemone (Expired Grove Village - Near Seahorse)", player),
                lambda state: state.has("Fishing Line", player))
        
        # spearfishing
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - Hidden Fishing Near Shopping Cart Mantis Block)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Hairclaw (Expired Grove Village - River Fishing Before Oil Drum)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - River Fishing After Oil Drum)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Anemone (Expired Grove Village - River Fishing Near Cart Mantis Block)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Expired Grove Village - Dock Fishing Spot 1)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Mussel (Expired Grove Village - Dock Fishing Spot 2)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Expired Grove Village - Dock Fishing Spot 3)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Hairclaw (Expired Grove Village - Dock Fishing Spot 4)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Earthworm (Expired Grove Village - Dock Fishing Spot 5)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Expired Grove Village - Hidden Fishing on Topoda Path)", player),
                lambda state: state.has("Spearfishing", player))

        # mantis punch
        set_rule(multiworld.get_location("Old World Whorl (Expired Grove Village - Post-Topoda Mantis Block)", player),
                lambda state: state.has("Mantis Punch", player))
        
        # ---- Flotsam Vale ----

        # spearfishing
        set_rule(multiworld.get_location("Hairclaw (Flotsam Vale - Gunk Lake Fishing Outside Air Pocket Cave)",player),
                lambda state: state.has("Spearfishing", player))
                
        set_rule(multiworld.get_location("Lamprey (Flotsam Vale - Small Island Fishing East of Entrance)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Mussel (Flotsam Vale - Elevated Island Fishing)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Flotsam Vale - Upper Flotsam Vale Fishing Near Snail Shell)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Siphonophore+ (Flotsam Vale - Fishing Near Waterfall)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Flotsam Vale - North Gunk Lake Fishing)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Whelk (Flotsam Vale - West Gunk Lake Fishing)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Breadclaw (Flotsam Vale - West Gunk Lake Fishing Near Shore)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Flotsam Vale - North Gunk Lake Fishing Near Shore)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Flotsam Vale - Gunk Lake Fishing South of Sludge Steamroller)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Flotsam Vale - Gunk Lake Fishing West of Sludge Steamroller)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Anemone+ (Flotsam Vale - Gunk Lake Fishing Northwest of Sludge Steamroller)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Hairclaw (Flotsam Vale - Gunk Fishing Near Bridge)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Breadclaw (Flotsam Vale - Gunk Fishing on Docks)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Turtle Shell Shard (Flotsam Vale - Gunk Fishing by Priest)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Clothesclaw (Flotsam Vale - Gunk Fishing on Docks)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Flotsam Vale - Gunk Fishing Near Dock)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barbed Hook (Flotsam Vale - Gunk Fishing Near Sludge Steamroller)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Lil' Isopod (Flotsam Vale - Gunk Fishing on Docks)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Hairclaw (Flotsam Vale - Gunk Fishing Near Bridge)", player),
                lambda state: state.has("Spearfishing", player))
        
        # grapple + spearfishing
        set_rule(multiworld.get_location("Chipclaw (Flotsam Vale - Fishing Past Consortium)", player),
                lambda state: state.has_all({"Spearfishing", "Fishing Line"}, player))
        
        # ---- Scuttleport ----

        # grapple + eelectrocute (will add metal shell later)
        set_rule(multiworld.get_location("Old World Whorl (Scuttleport - Eelectrocute Room in Survivor's Camp Building)", player),
                lambda state: state.has("Eelectrocute", player) and (state.has("Fishing Line", player) or logic.can_CAL(options, state, player)))
                
        # grapple and spearfishing
        set_rule(multiworld.get_location("Mussel (Scuttleport - Fishing Next to First Magnet)",player),
                lambda state: state.has_all({"Fishing Line", "Spearfishing"}, player))

        set_rule(multiworld.get_location("Chipclaw (Scuttleport - Gunk Fishing Under Middle Tower)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Rusty Nail (Scuttleport - Gunk Fishing Near Blue Tower)", player),
                lambda state: state.has("Spearfishing", player))
        
        set_rule(multiworld.get_location("Barnacle (Scuttleport - Gunk Fishing Near Middle Tower)", player),
                lambda state: state.has("Spearfishing", player))
        
        if options.goal != "voltai" and options.goal != "roland":
        
                # ---- The Unfathom ----

                # grapple
                set_rule(multiworld.get_location("Tackle Pouch (Abyssal Plains - Across Grapple Hooks by Snail Shell)",player),
                        lambda state: state.has("Fishing Line",player) or logic.can_CAL(options,state,player))
                
                # spearfishing
                set_rule(multiworld.get_location("Salp (The Unfathom - Fishing Near Red Glowstick)", player),
                        lambda state: state.has("Spearfishing", player))
                
                set_rule(multiworld.get_location("Barnacle+ (The Unfathom - Fishing Near Pinbarge Shipwreck)", player),
                        lambda state: state.has("Spearfishing", player))
                
                # ---- Abyssal Plains ----

                # spearfishing
                set_rule(multiworld.get_location("Stapleclaw (Abyssal Plains - Fishing Southeast of Shortcut)", player),
                        lambda state: state.has("Spearfishing", player))
                
                # ---- The Old Ocean ----

                # mantis punch
                set_rule(multiworld.get_location("Whelk++ (The Old Ocean - Behind Mantis Punch Wall)", player),
                        lambda state: state.has("Mantis Punch", player))
                        
                # grapple
                set_rule(multiworld.get_location("Fruit Sticker+ (The Old Ocean - Beyond Lone House on Floating Island)", player),
                        lambda state: state.has("Fishing Line",player))
                        
