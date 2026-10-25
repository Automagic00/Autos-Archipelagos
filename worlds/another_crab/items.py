from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item

class ACTItemData(NamedTuple):
    name: str
    classification: ItemClassification = ItemClassification.filler
    quantity_in_item_pool: int = 0
    item_id: int = None # first id: 483021700, last used: 483021881, available: 483021882 
    item_group: str = None

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

collectable_items_data: ACTItemData = [
    # Progression
    ACTItemData("Fork", ItemClassification.progression, 1, 483021701, "Progression"),
    ACTItemData("Fishing Line", ItemClassification.progression, 1, 483021703, "Progression"),
    ACTItemData("Pristine Pearl", ItemClassification.progression, 1, 483021704, "Progression"), # activates fallen slacktide
    ACTItemData("Map Piece - Flotsam Vale", ItemClassification.progression, 1, 483021705, "Progression"),
    ACTItemData("Map Piece - Heikea", ItemClassification.progression, 1, 483021706, "Progression"), 
    ACTItemData("Map Piece - Pagurus", ItemClassification.progression, 1, 483021707, "Progression"),
    #ACTItemData("Heartkelp Pods", ItemClassification.progression, 1, 483021702, "Progression"), # heal ability normally obtained at beginning of game

    # Upgrades
    ACTItemData("Bloodstar Limb", ItemClassification.useful, 20, 483021708, "Upgrades"), # total in game: 25
    ACTItemData("Heartkelp Sprout", ItemClassification.useful, 7, 483021709, "Upgrades"), # total in game: 7
    ACTItemData("Old World Whorl", ItemClassification.useful, 11, 483021710, "Upgrades"),
    ACTItemData("Stainless Relic", ItemClassification.useful, 11, 483021711, "Upgrades"), # total in game: 16
    ACTItemData("Tackle Pouch", ItemClassification.useful, 5, 483021712, "Upgrades"), 

    # Stowaways
    ACTItemData("Anemone", ItemClassification.useful, 10, 483021713, "Stowaways"),
    ACTItemData("Anemone+", ItemClassification.useful, 4, 483021714, "Stowaways"),
    ACTItemData("Anemone++", ItemClassification.useful, 1, 483021715, "Stowaways"),
    ACTItemData("Another Crab", ItemClassification.useful, 5, 483021716, "Stowaways"),
    ACTItemData("Barnacle", ItemClassification.useful, 6, 483021717, "Stowaways"),
    ACTItemData("Barnacle+", ItemClassification.useful, 2, 483021718, "Stowaways"),
    ACTItemData("Barnacle++", ItemClassification.useful, 1, 483021719, "Stowaways"),
    ACTItemData("Bobber", ItemClassification.useful, 1, 483021721, "Stowaways"),
    ACTItemData("Chum", ItemClassification.progression, 1, 483021722, "Stowaways"),
    ACTItemData("Cockle", ItemClassification.useful, 3, 483021723, "Stowaways"),
    ACTItemData("Cockle+", ItemClassification.useful, 1, 483021813, "Stowaways"),
    ACTItemData("Contact Lens", ItemClassification.useful, 1, 483021724, "Stowaways"),
    ACTItemData("Cotton Ball", ItemClassification.useful, 1, 483021725, "Stowaways"),
    ACTItemData("Earthworm", ItemClassification.useful, 1, 483021814, "Stowaways"), 
    ACTItemData("Fredrick", ItemClassification.progression, 1, 483021726, "Stowaways"),
    ACTItemData("Fruit Sticker", ItemClassification.useful, 2, 483021727, "Stowaways"),
    ACTItemData("Fruit Sticker+", ItemClassification.useful, 1, 483021728, "Stowaways"),
    ACTItemData("Googly Eye", ItemClassification.useful, 3, 483021729, "Stowaways"),
    ACTItemData("Lil Isopod", ItemClassification.progression,3, 483021847,"Stowaways"),
    ACTItemData("Lamprey", ItemClassification.useful, 1, 483021730, "Stowaways"),
    ACTItemData("Lamprey+", ItemClassification.useful, 1, 483021731, "Stowaways"),
    ACTItemData("Lanternfish", ItemClassification.progression, 1, 483021732, "Stowaways"),
    ACTItemData("Limpet", ItemClassification.useful, 11, 483021733, "Stowaways"),
    ACTItemData("Limpet+", ItemClassification.useful, 2, 483021734, "Stowaways"),
    ACTItemData("Limpet++", ItemClassification.useful, 2, 483021735, "Stowaways"),
    ACTItemData("Lugnut", ItemClassification.useful, 1, 483021736, "Stowaways"),
    ACTItemData("Lumpsucker", ItemClassification.useful, 3, 483021737, "Stowaways"),
    ACTItemData("Lumpsucker+", ItemClassification.useful, 1, 483021738, "Stowaways"),
    ACTItemData("Mussel", ItemClassification.useful, 10, 483021739, "Stowaways",),
    ACTItemData("Mussel+", ItemClassification.useful, 5, 483021740, "Stowaways",),
    ACTItemData("Mussel++", ItemClassification.useful, 1, 483021741, "Stowaways",),
    ACTItemData("Oyster", ItemClassification.useful, 3, 483021742, "Stowaways"),
    ACTItemData("Packing Peanut", ItemClassification.useful, 1, 483021743, "Stowaways"),
    ACTItemData("Phytoplankton", ItemClassification.progression, 1, 483021744, "Stowaways"),
    ACTItemData("Phytoplankton+", ItemClassification.progression, 2, 483021745, "Stowaways"),
    ACTItemData("Puffer Quill", ItemClassification.useful, 3, 483021746, "Stowaways"),
    ACTItemData("Razor Blade", ItemClassification.useful, 1, 483021747, "Stowaways"),
    ACTItemData("Rubber Band", ItemClassification.useful, 1, 483021748, "Stowaways"),
    ACTItemData("Rusty Nail", ItemClassification.useful, 6, 483021749, "Stowaways"),
    ACTItemData("Rusty Nail+", ItemClassification.useful, 3, 483021750, "Stowaways"),
    ACTItemData("Salp", ItemClassification.useful, 3, 483021751, "Stowaways"),
    ACTItemData("Salp+", ItemClassification.useful, 2, 483021752, "Stowaways"),
    ACTItemData("Sand Dollar", ItemClassification.useful, 9, 483021753, "Stowaways"),
    ACTItemData("Sea Cucumber", ItemClassification.useful, 2, 483021754, "Stowaways"),
    ACTItemData("Seaslug", ItemClassification.useful, 1, 483021755, "Stowaways"),
    ACTItemData("Seastar", ItemClassification.useful, 7, 483021756, "Stowaways"),
    ACTItemData("Seastar+", ItemClassification.useful, 4, 483021757, "Stowaways"),
    ACTItemData("Seastar++", ItemClassification.useful, 1, 483021758, "Stowaways"),
    ACTItemData("Shark Tooth", ItemClassification.useful, 1, 483021759, "Stowaways"),
    ACTItemData("Shark Tooth+", ItemClassification.useful, 1, 483021760, "Stowaways"),
    ACTItemData("Sinker", ItemClassification.useful, 2, 483021761, "Stowaways"),
    ACTItemData("Sinker+", ItemClassification.useful, 3, 483021762, "Stowaways"),
    ACTItemData("Sinker++", ItemClassification.useful, 1, 483021763, "Stowaways"),
    ACTItemData("Siphonophore", ItemClassification.useful, 2, 483021764, "Stowaways"),
    ACTItemData("Siphonophore+", ItemClassification.useful, 3, 483021765, "Stowaways"),
    ACTItemData("Small Battery", ItemClassification.useful, 1, 483021766, "Stowaways"),
    ACTItemData("Small Battery+", ItemClassification.useful, 1, 483021767, "Stowaways"),
    ACTItemData("Sponge", ItemClassification.progression, 3, 483021768, "Stowaways"),
    ACTItemData("Sponge+", ItemClassification.progression, 1, 483021769, "Stowaways"),
    ACTItemData("Turtle Shell Shard", ItemClassification.useful, 2, 483021770, "Stowaways"),
    ACTItemData("Used Bandage", ItemClassification.useful, 1, 483021772, "Stowaways"),
    ACTItemData("Used Bandage+", ItemClassification.useful, 1, 483021773, "Stowaways"),
    ACTItemData("Wad of Gum", ItemClassification.useful, 1, 483021774, "Stowaways"),
    ACTItemData("Whelk", ItemClassification.useful, 3, 483021775, "Stowaways"),
    ACTItemData("Whelk+", ItemClassification.useful, 2, 483021776, "Stowaways"),
    ACTItemData("Whelk++", ItemClassification.useful, 2, 483021777, "Stowaways"),
    ACTItemData("Zooplankton", ItemClassification.progression, 1, 483021778, "Stowaways"),
    ACTItemData("Zooplankton+", ItemClassification.progression, 1, 483021779, "Stowaways"),
    #ACTItemData("Bleached Phytoplankton", ItemClassification.useful, 1, 483021720, "Stowaways"), # Not used in base game
    #ACTItemData("UR", ItemClassification.useful, 1, 483021771, "Stowaways"), # Not used in base game, overpowered, presumably for testing

    # NG+ Stowaways
    ACTItemData("Streaker's Sigil", ItemClassification.progression, 1, 483021848, "StowawaysNGPlus"),
    ACTItemData("Sentinel's Sigil", ItemClassification.progression, 1, 483021849, "StowawaysNGPlus"),
    ACTItemData("Sicko's Sigil", ItemClassification.progression, 1, 483021850, "StowawaysNGPlus"),
    ACTItemData("Shadow's Sigil", ItemClassification.progression, 1, 483021851, "StowawaysNGPlus"),
    ACTItemData("Sorcerer's Sigil", ItemClassification.progression, 1, 483021852, "StowawaysNGPlus"),
    ACTItemData("Anemone+++", ItemClassification.progression, 1, 483021853, "StowawaysNGPlus"),
    ACTItemData("Barnacle+++", ItemClassification.progression, 1, 483021854, "StowawaysNGPlus"),
    ACTItemData("Cockle++", ItemClassification.progression, 1, 483021855, "StowawaysNGPlus"),
    ACTItemData("Fruit Sticker++", ItemClassification.progression, 1, 483021856, "StowawaysNGPlus"),
    ACTItemData("Fruit Sticker+++", ItemClassification.progression, 1, 483021857, "StowawaysNGPlus"),
    ACTItemData("Lamprey++", ItemClassification.progression, 1, 483021858, "StowawaysNGPlus"),
    ACTItemData("Lamprey+++", ItemClassification.progression, 1, 483021859, "StowawaysNGPlus"),
    ACTItemData("Limpet+++", ItemClassification.progression, 1, 483021860, "StowawaysNGPlus"),
    ACTItemData("Mussel+++", ItemClassification.progression, 1, 483021861, "StowawaysNGPlus"),
    ACTItemData("Oyster+", ItemClassification.progression, 1, 483021862, "StowawaysNGPlus"),
    ACTItemData("Oyster++", ItemClassification.progression, 1, 483021863, "StowawaysNGPlus"),
    ACTItemData("Puffer Quil+", ItemClassification.progression, 1, 483021864, "StowawaysNGPlus"),
    ACTItemData("Rusty Nail++", ItemClassification.progression, 1, 483021865, "StowawaysNGPlus"),
    ACTItemData("Rusty Nail+++", ItemClassification.progression, 1, 483021866, "StowawaysNGPlus"),
    ACTItemData("Sea Cucumber+", ItemClassification.progression, 1, 483021867, "StowawaysNGPlus"),
    ACTItemData("Seastar+++", ItemClassification.progression, 1, 483021868, "StowawaysNGPlus"),
    ACTItemData("Shark Tooth++", ItemClassification.progression, 1, 483021869, "StowawaysNGPlus"),
    ACTItemData("Sinker+++", ItemClassification.progression, 1, 483021870, "StowawaysNGPlus"),
    ACTItemData("Siphonophore++", ItemClassification.progression, 1, 483021871, "StowawaysNGPlus"),
    ACTItemData("Siphonophore+++", ItemClassification.progression, 1, 483021872, "StowawaysNGPlus"),
    ACTItemData("Used Bandage++", ItemClassification.progression, 1, 483021873, "StowawaysNGPlus"),
    ACTItemData("Wad of Gum+", ItemClassification.progression, 1, 483021874, "StowawaysNGPlus"),
    ACTItemData("Whelk+++", ItemClassification.progression, 1, 483021875, "StowawaysNGPlus"),

    # Currency
    ACTItemData("Breadclaw", ItemClassification.filler, 5, 483021780, "Currency"), # 250 microplastics
    ACTItemData("Chipclaw", ItemClassification.filler, 5, 483021781, "Currency"), # 500 microplastics
    ACTItemData("Hairclaw", ItemClassification.filler, 5, 483021782, "Currency"),  # 1000 microplastics
    ACTItemData("Clothesclaw", ItemClassification.filler, 4, 483021783, "Currency"), # 2500 microplastics
    ACTItemData("Paperclaw", ItemClassification.filler, 3, 483021784, "Currency"), # 5000 microplastics
    ACTItemData("Stapleclaw", ItemClassification.filler, 2, 483021785, "Currency"), # 10000 microplastics
    ACTItemData("Carclaw", ItemClassification.filler, 1, 483021786, "Currency"), # 20000 microplastics

    # Consumables
    ACTItemData("Barbed Hook", ItemClassification.filler, 10, 483021787, "Consumable"), # total in game: 113
    ACTItemData("Shark Egg", ItemClassification.filler, 4, 483021835, "Consumable"), # total in game: 4

    # Costumes
    ACTItemData("Captain", ItemClassification.filler, 1, 483021789, "Costume"), # Found by nephro spawn
    ACTItemData("Dr Kril", ItemClassification.filler, 1, 483021790, "Costume"), 
    ACTItemData("Exiled Flame", ItemClassification.filler, 1, 483021791, "Costume"), # Found near pinbarge wreckage in unfathom
    ACTItemData("Intern", ItemClassification.filler, 1, 483021794, "Costume"), # Found in village building on the left
    ACTItemData("Sunlight", ItemClassification.filler, 1, 483021795, "Costume"), # Found by blank moonsnail shell in sands between
    ACTItemData("Krillionaire", ItemClassification.filler, 1, 483021796, "Costume"), # Found after you are revived in unfathom
    ACTItemData("Cowfishboy", ItemClassification.filler, 1, 483021801, "Costume"), 
    ACTItemData("Blue Collar", ItemClassification.filler, 1, 483021803, "Costume"), # Inside scuttleport lockers
    ACTItemData("Clown", ItemClassification.filler, 1, 483021804, "Costume"), # in hidden area in sands between
    #ACTItemData("Midnight", ItemClassification.filler, 1, 483021797, "Costume"), # shellfish desires 10000 microplastics
    #ACTItemData("Maid Kril", ItemClassification.filler, 1, 483021798, "Costume"), # shellfish desires 15000 microplastics
    #ACTItemData("Rainbow Crabitalism", ItemClassification.filler, 1, 483021799, "Costume"), # shellfish desires 2500 microplastics
    #ACTItemData("Mr Kril", ItemClassification.filler, 1, 483021800, "Costume"), # shellfish desires 7500 microplastics
    #ACTItemData("Cult Leader", ItemClassification.filler, 1, 483021802, "Costume"), # shellfish desires 10000 microplastics
    #ACTItemData("Blackout Poncho", ItemClassification.filler, 1, 483021792, "Costume"), # shellfish desires 2500 microplastics
    #ACTItemData("Ivory Poncho", ItemClassification.filler, 1, 483021793, "Costume"), # shellfish desires 2500 microplastics
    #ACTItemData("Plastic Poncho", ItemClassification.filler, 1, 483021788, "Costume"), # Given when picking up fork

    # Adaptations
    ACTItemData("Royal Wave", ItemClassification.progression, 1, 483021805, "Adapations"), # Magista
    ACTItemData("Bobbit Trap", ItemClassification.useful, 1, 483021806, "Adapations"), # Bobbit Mound in Shallows
    ACTItemData("Bubble Bullet", ItemClassification.progression, 1, 483021807, "Adapations"), # Ceviche Sisters
    ACTItemData("Eelectrocute", ItemClassification.progression, 1, 483021808, "Adapations"), # Voltai
    ACTItemData("Mantis Punch", ItemClassification.progression, 1, 483021809, "Adapations"), # Topoda
    ACTItemData("Snail Sanctum", ItemClassification.useful, 1, 483021810, "Adapations"), # Petroch
    ACTItemData("Spectral Tentacle", ItemClassification.useful, 1, 483021811, "Adapations"), # Consortium
    ACTItemData("Urchin Toss", ItemClassification.progression, 1, 483021812, "Adapations"), # Urchin in New Carcinia

    # Skills
    ACTItemData("Shelleport", ItemClassification.progression, 1, 483021833, "Skills"),
    ACTItemData("Parry", ItemClassification.useful, 1, 483021836, "Skills"),
    ACTItemData("Riposte", ItemClassification.useful, 1, 483021837, "Skills"),
    ACTItemData("Natural Defenses", ItemClassification.useful, 1, 483021815, "Skills"),
    ACTItemData("Aggravation", ItemClassification.useful, 1, 483021816, "Skills"),
    ACTItemData("Self Repair", ItemClassification.useful, 1, 483021817, "Skills"),
    ACTItemData("Kintsugi", ItemClassification.useful, 1, 483021818, "Skills"),
    ACTItemData("Skewer", ItemClassification.useful, 1, 483021819, "Skills"),
    ACTItemData("Plunge", ItemClassification.useful, 1, 483021820, "Skills"),
    ACTItemData("Scrap Hammer", ItemClassification.useful, 1, 483021821, "Skills"),
    ACTItemData("Dispatch", ItemClassification.useful, 1, 483021822, "Skills"),
    ACTItemData("Spearfishing", ItemClassification.progression, 1, 483021823, "Skills"),
    ACTItemData("Wave Breaker", ItemClassification.useful, 1, 483021824, "Skills"),
    ACTItemData("Streamline", ItemClassification.useful, 1, 483021825, "Skills"),
    ACTItemData("Housewarming", ItemClassification.useful, 1, 483021826, "Skills"),
    ACTItemData("Circle of Life", ItemClassification.useful, 1, 483021827, "Skills"),
    ACTItemData("Elusive Prey", ItemClassification.useful, 1, 483021828, "Skills"),
    ACTItemData("Skeddadle", ItemClassification.useful, 1, 483021834, "Skills"),
    ACTItemData("Ebb and Flow", ItemClassification.useful, 1, 483021829, "Skills"),
    ACTItemData("Umami Training 1", ItemClassification.useful, 1, 483021830, "Skills"),
    ACTItemData("Umami Training 2", ItemClassification.useful, 1, 483021831, "Skills"),
    ACTItemData("Umami Training 3", ItemClassification.useful, 1, 483021832, "Skills"),

    # traps
    ACTItemData("Gunk Trap", ItemClassification.trap, 0, 483021838, "Traps"),
    ACTItemData("Scour Trap", ItemClassification.trap, 0, 483021839, "Traps"),
    ACTItemData("Bleached Trap", ItemClassification.trap, 0, 483021840, "Traps"),
    ACTItemData("Fear Trap", ItemClassification.trap, 0, 483021841, "Traps"),
    ACTItemData("Clutz Trap", ItemClassification.trap, 0, 483021842, "Traps"),
    ACTItemData("Test Trap", ItemClassification.trap, 0, 483021843, "Traps"),
    ACTItemData("Shell Shatter Trap", ItemClassification.trap, 0, 483021844, "Traps"),
    ACTItemData("Poison Cocktail Trap", ItemClassification.trap, 0, 483021845, "Traps"),
    ACTItemData("Taser Trap", ItemClassification.trap, 0, 483021846, "Traps")

    # Other
    #ACTItemData("Acquire Any Shell", ItemClassification.progression, 0, 483021879, "Event"),
    #ACTItemData("Spin Attack", ItemClassification.useful, 0, 483021880, "Spoof") # r1 air attack that allows for more distance and height from jumps
    #ACTItemData("Pagurus Allergy", ItemClassification.useful, 0, 483021881, "Spoof") # used later when we randomise pagurus allergy
]

shell_items_data: ACTItemData = [
    ACTItemData("Soda Can", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Bottle Cap", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Tin Can", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Shot Glass", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Banana Peel", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Party Hat", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Coconut", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Teacup", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Sauce Nozzle", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Thimble", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Bebop Cup", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Tennis Ball", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("F Key", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Mason Jar", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Salt Shaker", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Conchiglie", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Bartholomew", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Disco Ball", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Baby Shoe", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Lil' Bro", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Matryoshka Large", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Shuttlecock", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Felix Cube", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Piggy Bank", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Trophy", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Imposter", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Lil'Red Cup", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Wafer Cone", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Yoccult", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Coffee Pod", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Egg Shell", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Coffee Mug", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Cascadia Roll", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Ham Tin", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Skull", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Crab Husk", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Legal Brick", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Spring", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Shotgun Shell", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Rubber Duck", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Boxing Glove", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Cardboard Box", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Tissue Box", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Valve", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Dumptruck", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Ink Cartridge", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Gacha Capsule", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Lightbulb", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Mouse", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Going Under 64", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Sock", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Doll Head", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Service Bell", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Party Popper", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Scrub Aggy", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Dentures", ItemClassification.filler, 0, None, "Shells"),
    ACTItemData("Pill Bottle", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Detergent Cap", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("UltraSoft", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Champagne Flute", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Dish Scrubber", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Snow Globe", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Knight's Helmet", ItemClassification.progression, 0, None, "Shells"),
    ACTItemData("Plug Fuse", ItemClassification.progression, 0, None, "Shells")
    #ACTItemData("Spirit Conch", ItemClassification.filler, 0, None, "Shells"),
    #ACTItemData("Matryoshka Medium", ItemClassification.progression, 0, None, "Shells"),
    #ACTItemData("Matryoshka Small", ItemClassification.progression, 0, None, "Shells"),
    #ACTItemData("Gun", ItemClassification.useful, 0, None, "Shells")
]

item_table = {item_data.name: item_data for item_data in collectable_items_data + shell_items_data}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]

costume_items: List[str] = [name for name in filler_items if get_item_group(name) == "Costume"]

shell_items: List[str] = [name for name,data in item_table.items() if get_item_group(name) == "Shells"] #TODO: remove these list generations

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

item_limited_group = ["Umami Training 1", "Umami Training 2", "Umami Training 3", "Googly Eye", "Used Bandage"]  #TODO: what is this for?