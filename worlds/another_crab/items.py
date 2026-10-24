from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item

from .names import item_names as iname, shell_names as sname

item_base_id: int = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id: int
    item_group: str = ""

class ACTItem(Item):
    game: str = "Another Crabs Treasure"
    data: ACTItemData

    def __init__(
            self,
            player: int,
            data: ACTItemData,
            classification = None):
        super().__init__(data.name, classification or data.classification, data.item_id, player)
        self.data = data

item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, 483021701, "Progression"), 
    #iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, 483021702, "Progression"), 
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, 483021703, "Progression"),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, 483021704, "Progression"),
    iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, 483021705, "Progression"),
    iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, 483021706, "Progression"), 
    iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, 483021707, "Progression"), 

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 20, 483021708, "Upgrades"), # total in game: 25
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, 483021709, "Upgrades"), # total in game: 7
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, 483021710, "Upgrades"),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 11, 483021711, "Upgrades"), # total in game: 16
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 5, 483021712, "Upgrades"),

    # stowaways
    iname.anemone: ACTItemData(ItemClassification.useful, 10, 483021713, "Stowaways"),
    iname.anemone_plus: ACTItemData(ItemClassification.useful, 4, 483021714, "Stowaways"),
    iname.anemone_plus_plus: ACTItemData(ItemClassification.useful, 1, 483021715, "Stowaways"),
    iname.another_crab: ACTItemData(ItemClassification.useful, 5, 483021716, "Stowaways"),
    iname.barnacle: ACTItemData(ItemClassification.useful, 6, 483021717, "Stowaways"),
    iname.barnacle_plus: ACTItemData(ItemClassification.useful, 2, 483021718, "Stowaways"),
    iname.barnacle_plusplus: ACTItemData(ItemClassification.useful, 1, 483021719, "Stowaways"),
    #iname.bleached_phytoplankton: ACTItemData(ItemClassification.useful, 1, 483021720, "Stowaways"), #Not used in base game
    iname.bobber: ACTItemData(ItemClassification.useful, 1, 483021721, "Stowaways"),
    iname.chum: ACTItemData(ItemClassification.progression, 1, 483021722, "Stowaways"),
    iname.cockle: ACTItemData(ItemClassification.useful, 3, 483021723, "Stowaways"),
    iname.cockle_plus: ACTItemData(ItemClassification.useful, 1, 483021813, "Stowaways"),
    iname.contact_lens: ACTItemData(ItemClassification.useful, 1, 483021724, "Stowaways"),
    iname.cotton_ball: ACTItemData(ItemClassification.useful, 1, 483021725, "Stowaways"),
    iname.earthworm: ACTItemData(ItemClassification.useful, 1, 483021814, "Stowaways"), 
    iname.fredrick: ACTItemData(ItemClassification.progression, 1, 483021726, "Stowaways"),
    iname.fruit_sticker: ACTItemData(ItemClassification.useful, 2, 483021727, "Stowaways"),
    iname.fruit_sticker_plus: ACTItemData(ItemClassification.useful, 1, 483021728, "Stowaways"),
    iname.googly_eye: ACTItemData(ItemClassification.useful, 3, 483021729, "Stowaways"),
    iname.lil_isopod: ACTItemData(ItemClassification.progression,3, 483021847,"Stowaways"),
    iname.lamprey: ACTItemData(ItemClassification.useful, 1, 483021730, "Stowaways"),
    iname.lamprey_plus: ACTItemData(ItemClassification.useful, 1, 483021731, "Stowaways"),
    iname.lanternfish: ACTItemData(ItemClassification.progression, 1, 483021732, "Stowaways"),
    iname.limpet: ACTItemData(ItemClassification.useful, 11, 483021733, "Stowaways"),
    iname.limpet_plus: ACTItemData(ItemClassification.useful, 2, 483021734, "Stowaways"),
    iname.limpet_plus_plus: ACTItemData(ItemClassification.useful, 2, 483021735, "Stowaways"),
    iname.lugnut: ACTItemData(ItemClassification.useful, 1, 483021736, "Stowaways"),
    iname.lumpsucker: ACTItemData(ItemClassification.useful, 3, 483021737, "Stowaways"),
    iname.lumpsucker_plus: ACTItemData(ItemClassification.useful, 1, 483021738, "Stowaways"),
    iname.mussel: ACTItemData(ItemClassification.useful, 10, 483021739, "Stowaways",),
    iname.mussel_plus: ACTItemData(ItemClassification.useful, 5, 483021740, "Stowaways",),
    iname.mussel_plus_plus: ACTItemData(ItemClassification.useful, 1, 483021741, "Stowaways",),
    iname.oyster: ACTItemData(ItemClassification.useful, 3, 483021742, "Stowaways"),
    iname.packing_peanut: ACTItemData(ItemClassification.useful, 1, 483021743, "Stowaways"),
    iname.phytoplankton: ACTItemData(ItemClassification.progression, 1, 483021744, "Stowaways"),
    iname.phytoplankton_plus: ACTItemData(ItemClassification.progression, 2, 483021745, "Stowaways"),
    iname.puffer_quill: ACTItemData(ItemClassification.useful, 3, 483021746, "Stowaways"),
    iname.razor_blade: ACTItemData(ItemClassification.useful, 1, 483021747, "Stowaways"),
    iname.rubber_band: ACTItemData(ItemClassification.useful, 1, 483021748, "Stowaways"),
    iname.rusty_nail: ACTItemData(ItemClassification.useful, 6, 483021749, "Stowaways"),
    iname.rusty_nail_plus: ACTItemData(ItemClassification.useful, 3, 483021750, "Stowaways"),
    iname.salp: ACTItemData(ItemClassification.useful, 3, 483021751, "Stowaways"),
    iname.salp_plus: ACTItemData(ItemClassification.useful, 2, 483021752, "Stowaways"),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 9, 483021753, "Stowaways"),
    iname.sea_cucumber: ACTItemData(ItemClassification.useful, 2, 483021754, "Stowaways"),
    iname.seaslug: ACTItemData(ItemClassification.useful, 1, 483021755, "Stowaways"),
    iname.seastar: ACTItemData(ItemClassification.useful, 7, 483021756, "Stowaways"),
    iname.seastar_plus: ACTItemData(ItemClassification.useful, 4, 483021757, "Stowaways"),
    iname.seastar_plus_plus: ACTItemData(ItemClassification.useful, 1, 483021758, "Stowaways"),
    iname.shark_tooth: ACTItemData(ItemClassification.useful, 1, 483021759, "Stowaways"),
    iname.shark_tooth_plus: ACTItemData(ItemClassification.useful, 1, 483021760, "Stowaways"),
    iname.sinker: ACTItemData(ItemClassification.useful, 2, 483021761, "Stowaways"),
    iname.sinker_plus: ACTItemData(ItemClassification.useful, 3, 483021762, "Stowaways"),
    iname.sinker_plus_plus: ACTItemData(ItemClassification.useful, 1, 483021763, "Stowaways"),
    iname.siphonophore: ACTItemData(ItemClassification.useful, 2, 483021764, "Stowaways"),
    iname.siphonophore_plus: ACTItemData(ItemClassification.useful, 3, 483021765, "Stowaways"),
    iname.small_battery: ACTItemData(ItemClassification.useful, 1, 483021766, "Stowaways"),
    iname.small_battery_plus: ACTItemData(ItemClassification.useful, 1, 483021767, "Stowaways"),
    iname.sponge: ACTItemData(ItemClassification.progression, 3, 483021768, "Stowaways"),
    iname.sponge_plus: ACTItemData(ItemClassification.progression, 1, 483021769, "Stowaways"),
    iname.turtle_shell_shard: ACTItemData(ItemClassification.useful, 2, 483021770, "Stowaways"),
    #iname.ur: ACTItemData(ItemClassification.useful, 1, 483021771, "Stowaways"), # Not used in base game
    iname.used_bandage: ACTItemData(ItemClassification.useful, 1, 483021772, "Stowaways"),
    iname.used_bandage_plus: ACTItemData(ItemClassification.useful, 1, 483021773, "Stowaways"),
    iname.wad_of_gum: ACTItemData(ItemClassification.useful, 1, 483021774, "Stowaways"),
    iname.whelk: ACTItemData(ItemClassification.useful, 3, 483021775, "Stowaways"),
    iname.whelk_plus: ACTItemData(ItemClassification.useful, 2, 483021776, "Stowaways"),
    iname.whelk_plus_plus: ACTItemData(ItemClassification.useful, 2, 483021777, "Stowaways"),
    iname.zooplankton: ACTItemData(ItemClassification.progression, 1, 483021778, "Stowaways"),
    iname.zooplankton_plus: ACTItemData(ItemClassification.progression, 1, 483021779, "Stowaways"),

    #NG+ stowaways
    iname.streakers_sigil: ACTItemData(ItemClassification.progression, 1, 483021848, "StowawaysNGPlus"),
    iname.sentinels_sigil: ACTItemData(ItemClassification.progression, 1, 483021849, "StowawaysNGPlus"),
    iname.sickos_sigil: ACTItemData(ItemClassification.progression, 1, 483021850, "StowawaysNGPlus"),
    iname.shadows_sigil: ACTItemData(ItemClassification.progression, 1, 483021851, "StowawaysNGPlus"),
    iname.sorcerers_sigil: ACTItemData(ItemClassification.progression, 1, 483021852, "StowawaysNGPlus"),
    iname.anemone_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021853, "StowawaysNGPlus"),
    iname.barnacle_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021854, "StowawaysNGPlus"),
    iname.cockle_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021855, "StowawaysNGPlus"),
    iname.fruit_sticker_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021856, "StowawaysNGPlus"),
    iname.fruit_sticker_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021857, "StowawaysNGPlus"),
    iname.lamprey_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021858, "StowawaysNGPlus"),
    iname.lamprey_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021859, "StowawaysNGPlus"),
    iname.limpet_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021860, "StowawaysNGPlus"),
    iname.mussel_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021861, "StowawaysNGPlus"),
    iname.oyster_plus: ACTItemData(ItemClassification.progression, 1, 483021862, "StowawaysNGPlus"),
    iname.oyster_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021863, "StowawaysNGPlus"),
    iname.puffer_quill_plus: ACTItemData(ItemClassification.progression, 1, 483021864, "StowawaysNGPlus"),
    iname.rusty_nail_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021865, "StowawaysNGPlus"),
    iname.rusty_nail_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021866, "StowawaysNGPlus"),
    iname.sea_cucumber_plus: ACTItemData(ItemClassification.progression, 1, 483021867, "StowawaysNGPlus"),
    iname.seastar_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021868, "StowawaysNGPlus"),
    iname.shark_tooth_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021869, "StowawaysNGPlus"),
    iname.sinker_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021870, "StowawaysNGPlus"),
    iname.siphonophore_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021871, "StowawaysNGPlus"),
    iname.siphonophore_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021872, "StowawaysNGPlus"),
    iname.used_bandage_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021873, "StowawaysNGPlus"),
    iname.wad_of_gum_plus: ACTItemData(ItemClassification.progression, 1, 483021874, "StowawaysNGPlus"),
    iname.whelk_plus_plus_plus: ACTItemData(ItemClassification.progression, 1, 483021875, "StowawaysNGPlus"),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 5, 483021780, "Currency"), 
    iname.chipclaw: ACTItemData(ItemClassification.filler, 5, 483021781, "Currency"), 
    iname.hairclaw: ACTItemData(ItemClassification.filler, 5, 483021782, "Currency"), 
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 4, 483021783, "Currency"),
    iname.paperclaw: ACTItemData(ItemClassification.filler, 3, 483021784, "Currency"),
    iname.stapleclaw: ACTItemData(ItemClassification.filler, 2, 483021785, "Currency"),
    iname.carclaw: ACTItemData(ItemClassification.filler, 1, 483021786, "Currency"),

    # consumable
    iname.barbed_hook: ACTItemData(ItemClassification.filler, 10, 483021787, "Consumable"), # total in game: 113
    iname.shark_egg: ACTItemData(ItemClassification.filler, 4, 483021835, "Consumable"), # total in game: 4

    # costume
    #iname.plastic_poncho: ACTItemData(ItemClassification.filler, 1, 483021788, "Costume"),
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, 483021789, "Costume"),
    iname.dr_kril: ACTItemData(ItemClassification.filler, 1, 483021790, "Costume"),
    iname.exiled_flame: ACTItemData(ItemClassification.filler, 1, 483021791, "Costume"),
    #iname.blackout_poncho: ACTItemData(ItemClassification.filler, 1, 483021792, "Costume"),
    #iname.ivory_poncho: ACTItemData(ItemClassification.filler, 1, 483021793, "Costume"),
    iname.intern: ACTItemData(ItemClassification.filler, 1, 483021794, "Costume"),
    iname.sunlight: ACTItemData(ItemClassification.filler, 1, 483021795, "Costume"),
    iname.krillionaire: ACTItemData(ItemClassification.filler, 1, 483021796, "Costume"),
    #iname.midnight: ACTItemData(ItemClassification.filler, 1, 483021797, "Costume"),
    #iname.maid_kril: ACTItemData(ItemClassification.filler, 1, 483021798, "Costume"),
    #iname.rainbow_crabitalism: ACTItemData(ItemClassification.filler, 1, 483021799, "Costume"),
    #iname.mr_kril: ACTItemData(ItemClassification.filler, 1, 483021800, "Costume"),
    iname.cowfishboy: ACTItemData(ItemClassification.filler, 1, 483021801, "Costume"),
    #iname.cult_leader: ACTItemData(ItemClassification.filler, 1, 483021802, "Costume"),
    iname.blue_collar: ACTItemData(ItemClassification.filler, 1, 483021803, "Costume"),
    iname.clown: ACTItemData(ItemClassification.filler, 1, 483021804, "Costume"),

    # adaptations
    iname.royal_wave: ACTItemData(ItemClassification.progression, 1, 483021805, "Adapations"),
    iname.bobbit_trap: ACTItemData(ItemClassification.useful, 1, 483021806, "Adapations"),
    iname.bubble_bullet: ACTItemData(ItemClassification.progression, 1, 483021807, "Adapations"),
    iname.eelectrocute: ACTItemData(ItemClassification.progression, 1, 483021808, "Adapations"),
    iname.mantis_punch: ACTItemData(ItemClassification.progression, 1, 483021809, "Adapations"),
    iname.snail_sanctum: ACTItemData(ItemClassification.useful, 1, 483021810, "Adapations"),
    iname.spectral_tentacle: ACTItemData(ItemClassification.useful, 1, 483021811, "Adapations"),
    iname.urchin_toss: ACTItemData(ItemClassification.progression, 1, 483021812, "Adapations"),

    iname.shelleport: ACTItemData(ItemClassification.progression, 1, 483021833, "Skills"),
    iname.parry: ACTItemData(ItemClassification.useful, 1, 483021836, "Skills"),
    iname.riposte: ACTItemData(ItemClassification.useful, 1, 483021837, "Skills"),
    iname.natural_defenses: ACTItemData(ItemClassification.useful, 1, 483021815, "Skills"),
    iname.aggravation: ACTItemData(ItemClassification.useful, 1, 483021816, "Skills"),
    iname.self_repair: ACTItemData(ItemClassification.useful, 1, 483021817, "Skills"),
    iname.kintsugi: ACTItemData(ItemClassification.useful, 1, 483021818, "Skills"),
    iname.skewer: ACTItemData(ItemClassification.useful, 1, 483021819, "Skills"),
    iname.plunge: ACTItemData(ItemClassification.useful, 1, 483021820, "Skills"),
    iname.scrap_hammer: ACTItemData(ItemClassification.useful, 1, 483021821, "Skills"),
    iname.dispatch: ACTItemData(ItemClassification.useful, 1, 483021822, "Skills"),
    iname.spearfishing: ACTItemData(ItemClassification.progression, 1, 483021823, "Skills"),
    iname.wave_breaker: ACTItemData(ItemClassification.useful, 1, 483021824, "Skills"),
    iname.streamline: ACTItemData(ItemClassification.useful, 1, 483021825, "Skills"),
    iname.housewarming: ACTItemData(ItemClassification.useful, 1, 483021826, "Skills"),
    iname.circle_of_life: ACTItemData(ItemClassification.useful, 1, 483021827, "Skills"),
    iname.elusive_prey: ACTItemData(ItemClassification.useful, 1, 483021828, "Skills"),
    iname.skeddadle: ACTItemData(ItemClassification.useful, 1, 483021834, "Skills"),
    iname.ebb_and_flow: ACTItemData(ItemClassification.useful, 1, 483021829, "Skills"),
    iname.umami_training1: ACTItemData(ItemClassification.useful, 1, 483021830, "Skills"),
    iname.umami_training2: ACTItemData(ItemClassification.useful, 1, 483021831, "Skills"),
    iname.umami_training3: ACTItemData(ItemClassification.useful, 1, 483021832, "Skills"),

    # traps
    iname.gunk_trap: ACTItemData(ItemClassification.trap, 0, 483021838, "Traps"),
    iname.scour_trap: ACTItemData(ItemClassification.trap, 0, 483021839, "Traps"),
    iname.bleached_trap: ACTItemData(ItemClassification.trap, 0, 483021840, "Traps"),
    iname.fear_trap: ACTItemData(ItemClassification.trap, 0, 483021841, "Traps"),
    iname.clutz_trap: ACTItemData(ItemClassification.trap, 0, 483021842, "Traps"),
    iname.text_trap: ACTItemData(ItemClassification.trap, 0, 483021843, "Traps"),
    iname.shell_shatter_trap: ACTItemData(ItemClassification.trap, 0, 483021844, "Traps"),
    iname.poison_cocktail_trap: ACTItemData(ItemClassification.trap, 0, 483021845, "Traps"),
    iname.taser_trap: ACTItemData(ItemClassification.trap, 0, 483021846, "Traps"),

    # shells
    # might be worth trying to use event items for these
    sname.soda_can: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bottle_cap: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.tin_can: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shot_glass: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.banana_peel: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.party_hat: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coconut: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.teacup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.sauce_nozzle: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.thimble: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bebop_cup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.tennis_ball: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.f_key: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.mason_jar: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.salt_shaker: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.conchiglie: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.bartholomew: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.disco_ball: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.baby_shoe: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.lil_bro: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.matryoshka_large: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.matryoshka_medium: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.matryoshka_small: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shuttlecock: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.felix_cube: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.piggy_bank: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.trophy: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.imposter: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.lil_red_cup: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.wafer_cone: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.yoccult: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coffee_pod: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.egg_shell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.coffee_mug: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.cascadia_roll: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ham_tin: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.skull: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.crab_husk: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.legal_brick: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.spring: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.shotgun_shell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.rubber_duck: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.boxing_glove: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.cardboard_box: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.tissue_box: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.valve: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dumptruck: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ink_cartridge: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.gacha_capsule: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.lightbulb: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.mouse: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.going_under_64: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.sock: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.doll_head: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.service_bell: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.party_popper: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.scrub_aggie: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dentures: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.pill_bottle: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.detergent_cap: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.ultrasoft: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.champagne_flute: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.dish_scrubber: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.snow_globe: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    sname.knights_helmet: ACTItemData(ItemClassification.progression, 0, None, "Shells"),
    #sname.spirit_conch: ACTItemData(ItemClassification.filler, 0, None, "Shells"),
    sname.plug_fuse: ACTItemData(ItemClassification.progression, 0, None, "Shells")

}

def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]

costume_items: List[str] = [name for name in filler_items if get_item_group(name) == "Costume"]

shell_items: List[str] = [name for name,data in item_table.items() if get_item_group(name) == "Shells"]

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

item_limited_group = [iname.umami_training1,iname.umami_training2,iname.umami_training3,iname.googly_eye,iname.used_bandage]