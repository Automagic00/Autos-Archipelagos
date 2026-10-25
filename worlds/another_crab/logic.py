from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import ACTGameOptions

if TYPE_CHECKING:
    from . import ACTWorld

### Check if regions are accessible based on current glitch category and items (try to only invoke options in rules)
def can_skip_some_grapples(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Fishing Line", player) or are_skips_allowed(options)

def is_slacktide_before_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.can_reach_location("Nephro, Captain of the Guard", player) or are_skips_allowed(options)

def is_reefs_edge_accessible_vanilla(state: CollectionState, player: int) -> bool:
    return state.has_all({"Fishing Line", "Pristine Pearl"}, player) and state.can_reach_location("Magista, Tyrant of Slacktide", player)
 
# This allows I-beam/decoy (skips), or CAL (glitch) to enter cave
def is_moonsnail_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_reach_moonsnail(options, state, player) and can_pink_crab(options, state, player)
    
def can_reach_moonsnail(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Fishing Line", player) or are_skips_allowed(options)
    
def is_post_ceviche_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.can_reach_location("Ceviche Sisters", player) or can_sisters_skip(options, state, player) or can_sisters_skip_glitches(options,state,player)
    
def is_consortium_accessible_vale(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_big_boost_jump(options, state, player) 
    
def is_consortium_accessible_grove(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return is_consortium_accessible_grove_vanilla(state,player) or is_consortium_accessible_grove_skips(options,state,player) or can_CAL(options, state, player)
    
def is_consortium_accessible_grove_skips(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has_all({"Fishing Line", "Fork"},player) and are_skips_allowed(options)

def is_consortium_accessible_grove_vanilla(state: CollectionState, player: int) -> bool:
    return state.has_all({"Mantis Punch", "Fishing Line"},player)
    
def is_southern_town_ridge_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return is_southern_town_ridge_accessible_restricted(options, state, player) or state.has("Eelectrocute", player)
    
def is_southern_town_ridge_accessible_restricted(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_razor_CAL(options,state,player)
    
def is_secluded_ridge_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Mantis Punch", player) or are_skips_allowed(options)
    
def is_secluded_ridge_eel_accessible(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Eelectrocute", player) or can_CAL(options, state, player)
    
def can_access_scuttleport(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Plug Fuse", player)
    
def has_all_maps(state: CollectionState, player: int) -> bool:
    return state.has_all({"Map Piece - Flotsam Vale", "Map Piece - Heikea", "Map Piece - Pagurus"}, player)


#Check if specific skips are executable
#Magista skip
def can_magista_skip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_magista_skip_grapple(options, state, player) or can_magista_skip_grappleless(options, state, player)) and options.goal != "magista" 

def can_magista_skip_grapple(options: ACTGameOptions, state: CollectionState, player: int) -> bool:   
    return state.has("Fishing Line", player) and are_skips_allowed(options)
    
def can_magista_skip_grappleless(options: ACTGameOptions, state: CollectionState, player: int) -> bool: #may be possible without CAL
    return can_CAL(options, state, player) and can_shell_clip(options, state, player) 
    
#Sisters skip 
def can_sisters_skip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has_any(["Fork", "Streamline"], player) and state.has("Fishing Line", player) and are_skips_allowed(options)
    
def can_sisters_skip_glitches(options:ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_CAL(options,state,player)

#Can bypass/kill pink crab by moonsnail
def can_pink_crab(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return can_reach_msg_dmg_shells(state,player) or  has_adaptation(state,player) or can_shell_clip(options, state, player)

def can_pagurus_quick_kill(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return are_skips_allowed(options)

def can_heikia_quick_kill(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return are_glitches_allowed(options) and state.has_all({"Fishing Line", "Spearfishing"}, player)

### Check if specific tricks are executable
# CAL
def can_CAL(options: ACTGameOptions, state: CollectionState, player: int) ->  bool:
    return state.has("Fork", player) and are_glitches_allowed(options)
    
def can_razor_CAL(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Razor Blade", player) and can_CAL(options, state, player)

#Shell Clip (clip may be possible with other shells, need to check)
def can_shell_clip(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return state.has("Soda Can", player) and are_glitches_allowed(options) 
    
#Bombs Away or Decoy
def can_boost_jump(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_bombs_away(state, player) or can_decoy(state, player)) and are_skips_allowed(options)

#Bombs Away or Matrioshka
def can_big_boost_jump(options: ACTGameOptions, state: CollectionState, player: int) -> bool:
    return (can_bombs_away(state, player) or state.has("Matryoshka Large",player)) and are_skips_allowed(options)


### Check if glitch category is one of several 
def are_skips_allowed(options: ACTGameOptions) -> bool:
    return options.logic_rules != "vanilla"
    
def are_glitches_allowed(options: ACTGameOptions) -> bool:
    return options.logic_rules == "restricted" or options.logic_rules == "unrestricted"

### Checks to see if the player can logically consistently deal damage
def can_deal_damage_hard(state: CollectionState,player:int) -> bool:
    return can_rolling_attack(state,player) | can_magic_damage(state,player) | can_atk_damage_shell(state,player) | has_summon(state,player)  | state.has("Fork",player)

def can_deal_damage_easy(state: CollectionState,player:int) -> bool:
    return can_magic_damage(state,player) | can_atk_damage_shell(state,player) | state.has("Fork",player)

def can_rolling_attack(state: CollectionState, player: int) -> bool:
    return can_reach_rolling_shells(state,player) and (state.has("Lil Isopod",player,2))

### Checks if the player has any of the summonable fish stowaways
def has_summon(state: CollectionState, player: int) -> bool:
    summon_count: int = 0
    if state.has("Chum",player):
        summon_count += 1
    
    if state.has("Fredrick",player):
        summon_count += 1

    if state.has("Lanternfish",player):
        summon_count += 1

    return summon_count >= 2

### Checks if the player has adaptations
#Skips Snail Sanctum since it needs lvl 2 to deal damage
#Skips Tactical Tentacle since it may need the fork to attack
#Skips Bobbit Trap since it may not do enough dmg at lvl 1
def has_adaptation(state: CollectionState, player: int) -> bool:
    return state.has_any({"Royal Wave", "Urchin Toss", "Mantis Punch", "Bubble Bullet", "Eelectrocute"},player) # TODO: filter through array in items.py instead

def can_magic_damage(state: CollectionState, player: int) -> bool:
    return (can_reach_magic_shells(state,player) ) and can_regen_umami(state,player) #| has_adaptation(state,player)

def can_regen_umami(state: CollectionState, player: int) -> bool:
    return state.has_any_count({"Phytoplankton+":1,"Zooplankton":2,"Zooplankton+":1,"Phytoplankton+":2},player)

def can_reach_magic_shells(state: CollectionState, player: int) -> bool:
    return can_twist_top(state,player) | can_pop_off(state,player) | can_rollout(state,player) | can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_msg_dmg_shells(state: CollectionState, player: int) -> bool:
    return can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_rolling_shells(state: CollectionState, player: int) -> bool:
    rolling_shells = ["Soda Can","Bottle Cap","Lil' Red Cup","Shuttlecock","Bebop Cup","Tin Can","Shot Glass","Party Hat","Coconut","Teacup","Sauce Nozzle","Thimble","Tennis Ball","Mason Jar","Salt Shaker","Conchiglie","Disco Ball","Lil Bro","Matryoshka Large","Wafer Cone","Yoccult","Coffee Pod","Egg Shell","Coffee Mug","Cascadia Roll","Skull","Spring","Shotgun Shell","Dumptruck","Gacha Capsule","Lightbulb","Doll Head","Service Bell","Party Popper","Scrub Aggie","Pill Bottle","Detergent Cap","Ultrasoft","Champagne Flute","Dish Scrubber","Snow Globe","Knights Helmet","Snail Sanctum","Plug Fuse","Piggy Bank"]
    return state.has_any(rolling_shells,player)

def can_atk_damage_shell(state: CollectionState, player: int) -> bool:
    sponge_val: int = 0
    sponge_val += state.count("Sponge",player)
    sponge_val += state.count("Sponge+",player) * 2
    return can_twist_top(state,player) | (can_pop_off(state,player) and sponge_val >= 3) | (can_rollout(state,player) and sponge_val >= 3) | (can_party_time(state,player) and sponge_val >= 3)


### Check if Shell Spells are Reachable

#Twist Top
def can_twist_top(state: CollectionState, player: int) -> bool:
    twist_top_shells = ["Sauce Nozzle", "Shuttlecock","Felix Cube","Dish Scrubber"]
    return state.has_any(twist_top_shells,player)

#Pop Off
def can_pop_off(state: CollectionState, player: int) -> bool:
    pop_off_shells = ["Bottle Cap","F Key","Ham Tin","Legal Brick","Spring","Detergent Cap"]
    return state.has_any(pop_off_shells,player)

#Rollout
def can_rollout(state: CollectionState, player: int) -> bool:
    rollout_shells = ["Coconut","Tennis Ball", "Dumptruck", "Gacha Capsule", "Ultrasoft"]
    return state.has_any(rollout_shells,player)

#Bombs Away
def can_bombs_away(state: CollectionState, player: int) -> bool:
    bombs_away_shells = ["Bartholomew","Shotgun Shell"]
    return state.has_any(bombs_away_shells,player)

#Decoy
def can_decoy(state: CollectionState, player: int) -> bool:
    decoy_shells = ["Matryoshka Large","Piggy Bank","Crab Husk","Rubber Duck"]
    return state.has_any(decoy_shells,player)

#Fizzle
def can_fizzle(state: CollectionState, player: int) -> bool:
    fizzle_shells = ["Soda Can","Valve","Going Under 64"]
    return state.has_any(fizzle_shells,player)

#Party Time
def can_party_time(state: CollectionState, player: int) -> bool:
    party_time_shells = ["Party Hat","Trophy","Party Popper"]
    return state.has_any(party_time_shells,player)

#Shards
def can_shards(state: CollectionState, player: int) -> bool:
    shards_shells = ["Shot Glass","Mason Jar","Salt Shaker"]
    return state.has_any(shards_shells,player)

#Squash
def can_squash(state: CollectionState, player: int) -> bool:
    squash_shells = ["Boxing Glove","Sock"]
    return state.has_any(squash_shells,player)

#Twinkle
def can_twinkle(state: CollectionState, player: int) -> bool:
    twinkle_shells = ["Disco Ball","Spirit Conch"]
    return state.has_any(twinkle_shells,player)
