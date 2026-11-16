from typing import Dict, List, NamedTuple, Optional, Set
from BaseClasses import ItemClassification, Item

ITEM_ID_BASE = 483021700

class ACTItemData(NamedTuple):
    name: str
    classification: ItemClassification = ItemClassification.filler
    quantity_in_item_pool: int = 0
    item_offset: Optional[int] = None
    item_group: List[str] = []

    @property
    def item_id(self) -> Optional[int]:
        if self.item_offset is None:
            return None
        return ITEM_ID_BASE + self.item_offset

class ACTItem(Item):
    game: str = "Another Crab's Treasure"
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
    ACTItemData("Fork", ItemClassification.progression, 1, 1, ["Progression"]),
    ACTItemData("Fishing Line", ItemClassification.progression, 1, 3, ["Progression"]),
    ACTItemData("Pristine Pearl", ItemClassification.progression, 1, 4, ["Progression"]), # activates fallen slacktide
    ACTItemData("Map Piece - Flotsam Vale", ItemClassification.progression, 1, 5, ["Progression"]),
    ACTItemData("Map Piece - Heikea", ItemClassification.progression, 1, 6, ["Progression"]),
    ACTItemData("Map Piece - Pagurus", ItemClassification.progression, 1, 7, ["Progression"]),
    #ACTItemData("Heartkelp Pods", ItemClassification.progression, 1, 2, "Progression"), # heal ability normally obtained at beginning of game

    # Upgrades
    ACTItemData("Bloodstar Limb", ItemClassification.useful, 20, 8, ["Upgrades"]), # total in game: 25
    ACTItemData("Heartkelp Sprout", ItemClassification.useful, 7, 9, ["Upgrades"]), # total in game: 7
    ACTItemData("Old World Whorl", ItemClassification.useful, 11, 10, ["Upgrades"]),
    ACTItemData("Stainless Relic", ItemClassification.useful, 11, 11, ["Upgrades"]), # total in game: 16
    ACTItemData("Tackle Pouch", ItemClassification.useful, 5, 12, ["Upgrades"]),

    # Stowaways
    ACTItemData("Anemone", ItemClassification.useful, 10, 13, ["Stowaways"]),
    ACTItemData("Anemone+", ItemClassification.useful, 4, 14, ["Stowaways"]),
    ACTItemData("Anemone++", ItemClassification.useful, 1, 15, ["Stowaways"]),
    ACTItemData("Another Crab", ItemClassification.useful, 5, 16, ["Stowaways"]),
    ACTItemData("Barnacle", ItemClassification.useful, 6, 17, ["Stowaways"]),
    ACTItemData("Barnacle+", ItemClassification.useful, 2, 18, ["Stowaways"]),
    ACTItemData("Barnacle++", ItemClassification.useful, 1, 19, ["Stowaways"]),
    ACTItemData("Bobber", ItemClassification.useful, 1, 21, ["Stowaways"]),
    ACTItemData("Chum", ItemClassification.progression, 1, 22, ["Stowaways"]),
    ACTItemData("Cockle", ItemClassification.useful, 3, 23, ["Stowaways"]),
    ACTItemData("Cockle+", ItemClassification.useful, 1, 113, ["Stowaways"]),
    ACTItemData("Contact Lens", ItemClassification.useful, 1, 24, ["Stowaways"]),
    ACTItemData("Cotton Ball", ItemClassification.useful, 1, 25, ["Stowaways"]),
    ACTItemData("Earthworm", ItemClassification.useful, 1, 114, ["Stowaways"]),
    ACTItemData("Fredrick", ItemClassification.progression, 1, 26, ["Stowaways"]),
    ACTItemData("Fruit Sticker", ItemClassification.useful, 2, 27, ["Stowaways"]),
    ACTItemData("Fruit Sticker+", ItemClassification.useful, 1, 28, ["Stowaways"]),
    ACTItemData("Googly Eye", ItemClassification.useful, 3, 29, ["Stowaways"]),
    ACTItemData("Lil' Isopod", ItemClassification.progression,3, 147,["Stowaways"]),
    ACTItemData("Lamprey", ItemClassification.useful, 1, 30, ["Stowaways"]),
    ACTItemData("Lamprey+", ItemClassification.useful, 1, 31, ["Stowaways"]),
    ACTItemData("Lanternfish", ItemClassification.progression, 1, 32, ["Stowaways"]),
    ACTItemData("Limpet", ItemClassification.useful, 11, 33, ["Stowaways"]),
    ACTItemData("Limpet+", ItemClassification.useful, 2, 34, ["Stowaways"]),
    ACTItemData("Limpet++", ItemClassification.useful, 2, 35, ["Stowaways"]),
    ACTItemData("Lugnut", ItemClassification.useful, 1, 36, ["Stowaways"]),
    ACTItemData("Lumpsucker", ItemClassification.useful, 3, 37, ["Stowaways"]),
    ACTItemData("Lumpsucker+", ItemClassification.useful, 1, 38, ["Stowaways"]),
    ACTItemData("Mussel", ItemClassification.useful, 10, 39, ["Stowaways"],),
    ACTItemData("Mussel+", ItemClassification.useful, 5, 40, ["Stowaways"],),
    ACTItemData("Mussel++", ItemClassification.useful, 1, 41, ["Stowaways"],),
    ACTItemData("Oyster", ItemClassification.useful, 3, 42, ["Stowaways"]),
    ACTItemData("Packing Peanut", ItemClassification.useful, 1, 43, ["Stowaways"]),
    ACTItemData("Phytoplankton", ItemClassification.progression, 1, 44, ["Stowaways"]),
    ACTItemData("Phytoplankton+", ItemClassification.progression, 2, 45, ["Stowaways"]),
    ACTItemData("Puffer Quill", ItemClassification.useful, 3, 46, ["Stowaways"]),
    ACTItemData("Razor Blade", ItemClassification.useful, 1, 47, ["Stowaways"]),
    ACTItemData("Rubber Band", ItemClassification.useful, 1, 48, ["Stowaways"]),
    ACTItemData("Rusty Nail", ItemClassification.useful, 6, 49, ["Stowaways"]),
    ACTItemData("Rusty Nail+", ItemClassification.useful, 3, 50, ["Stowaways"]),
    ACTItemData("Salp", ItemClassification.useful, 3, 51, ["Stowaways"]),
    ACTItemData("Salp+", ItemClassification.useful, 2, 52, ["Stowaways"]),
    ACTItemData("Sand Dollar", ItemClassification.useful, 9, 53, ["Stowaways"]),
    ACTItemData("Sea Cucumber", ItemClassification.useful, 2, 54, ["Stowaways"]),
    ACTItemData("Seaslug", ItemClassification.useful, 1, 55, ["Stowaways"]),
    ACTItemData("Seastar", ItemClassification.useful, 7, 56, ["Stowaways"]),
    ACTItemData("Seastar+", ItemClassification.useful, 4, 57, ["Stowaways"]),
    ACTItemData("Seastar++", ItemClassification.useful, 1, 58, ["Stowaways"]),
    ACTItemData("Shark Tooth", ItemClassification.useful, 1, 59, ["Stowaways"]),
    ACTItemData("Shark Tooth+", ItemClassification.useful, 1, 60, ["Stowaways"]),
    ACTItemData("Sinker", ItemClassification.useful, 2, 61, ["Stowaways"]),
    ACTItemData("Sinker+", ItemClassification.useful, 3, 62, ["Stowaways"]),
    ACTItemData("Sinker++", ItemClassification.useful, 1, 63, ["Stowaways"]),
    ACTItemData("Siphonophore", ItemClassification.useful, 2, 64, ["Stowaways"]),
    ACTItemData("Siphonophore+", ItemClassification.useful, 3, 65, ["Stowaways"]),
    ACTItemData("Small Battery", ItemClassification.useful, 1, 66, ["Stowaways"]),
    ACTItemData("Small Battery+", ItemClassification.useful, 1, 67, ["Stowaways"]),
    ACTItemData("Sponge", ItemClassification.progression, 3, 68, ["Stowaways"]),
    ACTItemData("Sponge+", ItemClassification.progression, 1, 69, ["Stowaways"]),
    ACTItemData("Turtle Shell Shard", ItemClassification.useful, 2, 70, ["Stowaways"]),
    ACTItemData("Used Bandage", ItemClassification.useful, 1, 72, ["Stowaways"]),
    ACTItemData("Used Bandage+", ItemClassification.useful, 1, 73, ["Stowaways"]),
    ACTItemData("Wad of Gum", ItemClassification.useful, 1, 74, ["Stowaways"]),
    ACTItemData("Whelk", ItemClassification.useful, 3, 75, ["Stowaways"]),
    ACTItemData("Whelk+", ItemClassification.useful, 2, 76, ["Stowaways"]),
    ACTItemData("Whelk++", ItemClassification.useful, 2, 77, ["Stowaways"]),
    ACTItemData("Zooplankton", ItemClassification.progression, 1, 78, ["Stowaways"]),
    ACTItemData("Zooplankton+", ItemClassification.progression, 1, 79, ["Stowaways"]),
    #ACTItemData("Bleached Phytoplankton", ItemClassification.useful, 1, 20, "Stowaways"), # Not used in base game
    #ACTItemData("UR", ItemClassification.useful, 1, 71, "Stowaways"), # Not used in base game, overpowered, presumably for testing

    # NG+ Stowaways
    ACTItemData("Streaker's Sigil", ItemClassification.progression, 1, 148, ["StowawaysNGPlus"]),
    ACTItemData("Sentinel's Sigil", ItemClassification.progression, 1, 149, ["StowawaysNGPlus"]),
    ACTItemData("Sicko's Sigil", ItemClassification.progression, 1, 150, ["StowawaysNGPlus"]),
    ACTItemData("Shadow's Sigil", ItemClassification.progression, 1, 151, ["StowawaysNGPlus"]),
    ACTItemData("Sorcerer's Sigil", ItemClassification.progression, 1, 152, ["StowawaysNGPlus"]),
    ACTItemData("Anemone+++", ItemClassification.progression, 1, 153, ["StowawaysNGPlus"]),
    ACTItemData("Barnacle+++", ItemClassification.progression, 1, 154, ["StowawaysNGPlus"]),
    ACTItemData("Cockle++", ItemClassification.progression, 1, 155, ["StowawaysNGPlus"]),
    ACTItemData("Fruit Sticker++", ItemClassification.progression, 1, 156, ["StowawaysNGPlus"]),
    ACTItemData("Fruit Sticker+++", ItemClassification.progression, 1, 157, ["StowawaysNGPlus"]),
    ACTItemData("Lamprey++", ItemClassification.progression, 1, 158, ["StowawaysNGPlus"]),
    ACTItemData("Lamprey+++", ItemClassification.progression, 1, 159, ["StowawaysNGPlus"]),
    ACTItemData("Limpet+++", ItemClassification.progression, 1, 160, ["StowawaysNGPlus"]),
    ACTItemData("Mussel+++", ItemClassification.progression, 1, 161, ["StowawaysNGPlus"]),
    ACTItemData("Oyster+", ItemClassification.progression, 1, 162, ["StowawaysNGPlus"]),
    ACTItemData("Oyster++", ItemClassification.progression, 1, 163, ["StowawaysNGPlus"]),
    ACTItemData("Puffer Quill+", ItemClassification.progression, 1, 164, ["StowawaysNGPlus"]),
    ACTItemData("Rusty Nail++", ItemClassification.progression, 1, 165, ["StowawaysNGPlus"]),
    ACTItemData("Rusty Nail+++", ItemClassification.progression, 1, 166, ["StowawaysNGPlus"]),
    ACTItemData("Sea Cucumber+", ItemClassification.progression, 1, 167, ["StowawaysNGPlus"]),
    ACTItemData("Seastar+++", ItemClassification.progression, 1, 168, ["StowawaysNGPlus"]),
    ACTItemData("Shark Tooth++", ItemClassification.progression, 1, 169, ["StowawaysNGPlus"]),
    ACTItemData("Sinker+++", ItemClassification.progression, 1, 170, ["StowawaysNGPlus"]),
    ACTItemData("Siphonophore++", ItemClassification.progression, 1, 171, ["StowawaysNGPlus"]),
    ACTItemData("Siphonophore+++", ItemClassification.progression, 1, 172, ["StowawaysNGPlus"]),
    ACTItemData("Used Bandage++", ItemClassification.progression, 1, 173, ["StowawaysNGPlus"]),
    ACTItemData("Wad of Gum+", ItemClassification.progression, 1, 174, ["StowawaysNGPlus"]),
    ACTItemData("Whelk+++", ItemClassification.progression, 1, 175, ["StowawaysNGPlus"]),

    # Currency
    ACTItemData("Breadclaw", ItemClassification.filler, 5, 80, ["Currency"]), # 250 microplastics
    ACTItemData("Chipclaw", ItemClassification.filler, 5, 81, ["Currency"]), # 500 microplastics
    ACTItemData("Hairclaw", ItemClassification.filler, 5, 82, ["Currency"]),  # 1000 microplastics
    ACTItemData("Clothesclaw", ItemClassification.filler, 4, 83, ["Currency"]), # 2500 microplastics
    ACTItemData("Paperclaw", ItemClassification.filler, 3, 84, ["Currency"]), # 5000 microplastics
    ACTItemData("Stapleclaw", ItemClassification.filler, 2, 85, ["Currency"]), # 10000 microplastics
    ACTItemData("Carclaw", ItemClassification.filler, 1, 86, ["Currency"]), # 20000 microplastics

    # Consumables
    ACTItemData("Barbed Hook", ItemClassification.filler, 10, 87, ["Consumable"]), # total in game: 113
    ACTItemData("Shark Egg", ItemClassification.filler, 4, 135, ["Consumable"]), # total in game: 4

    # Costumes
    ACTItemData("Captain", ItemClassification.filler, 1, 89, ["Costume"]), # Found by nephro spawn
    ACTItemData("Dr Kril", ItemClassification.filler, 1, 90, ["Costume"]),
    ACTItemData("Exiled Flame", ItemClassification.filler, 1, 91, ["Costume"]), # Found near pinbarge wreckage in unfathom
    ACTItemData("Intern", ItemClassification.filler, 1, 94, ["Costume"]), # Found in village building on the left
    ACTItemData("Sunlight", ItemClassification.filler, 1, 95, ["Costume"]), # Found by blank moonsnail shell in sands between
    ACTItemData("Krillionaire", ItemClassification.filler, 1, 96, ["Costume"]), # Found after you are revived in unfathom
    ACTItemData("Cowfishboy", ItemClassification.filler, 1, 101, ["Costume"]),
    ACTItemData("Blue Collar", ItemClassification.filler, 1, 103, ["Costume"]), # Inside scuttleport lockers
    ACTItemData("Clown", ItemClassification.filler, 1, 104, ["Costume"]), # in hidden area in sands between
    #ACTItemData("Midnight", ItemClassification.filler, 1, 97, ["Costume"]), # shellfish desires 10000 microplastics
    #ACTItemData("Maid Kril", ItemClassification.filler, 1, 98, ["Costume"]), # shellfish desires 15000 microplastics
    #ACTItemData("Rainbow Crabitalism", ItemClassification.filler, 1, 99, ["Costume"]), # shellfish desires 2500 microplastics
    #ACTItemData("Mr Kril", ItemClassification.filler, 1, 100, ["Costume"]), # shellfish desires 7500 microplastics
    #ACTItemData("Cult Leader", ItemClassification.filler, 1, 102, ["Costume"]), # shellfish desires 10000 microplastics
    #ACTItemData("Blackout Poncho", ItemClassification.filler, 1, 92, ["Costume"]), # shellfish desires 2500 microplastics
    #ACTItemData("Ivory Poncho", ItemClassification.filler, 1, 93, ["Costume"]), # shellfish desires 2500 microplastics
    #ACTItemData("Plastic Poncho", ItemClassification.filler, 1, 88, ["Costume"]), # Given when picking up fork

    # Adaptations
    ACTItemData("Royal Wave", ItemClassification.progression, 1, 105, ["Adaptations"]), # Magista
    ACTItemData("Bobbit Trap", ItemClassification.useful, 1, 106, ["Adaptations"]), # Bobbit Mound in Shallows
    ACTItemData("Bubble Bullet", ItemClassification.progression, 1, 107, ["Adaptations"]), # Ceviche Sisters
    ACTItemData("Eelectrocute", ItemClassification.progression, 1, 108, ["Adaptations"]), # Voltai
    ACTItemData("Mantis Punch", ItemClassification.progression, 1, 109, ["Adaptations"]), # Topoda
    ACTItemData("Snail Sanctum", ItemClassification.useful, 1, 110, ["Adaptations"]), # Petroch
    ACTItemData("Spectral Tentacle", ItemClassification.useful, 1, 111, ["Adaptations"]), # Consortium
    ACTItemData("Urchin Toss", ItemClassification.progression, 1, 112, ["Adaptations"]), # Urchin in New Carcinia

    # Skills
    ACTItemData("Shelleport", ItemClassification.progression, 1, 133, ["Skills"]),
    ACTItemData("Parry", ItemClassification.useful, 1, 136, ["Skills"]),
    ACTItemData("Riposte", ItemClassification.useful, 1, 137, ["Skills"]),
    ACTItemData("Natural Defenses", ItemClassification.useful, 1, 115, ["Skills"]),
    ACTItemData("Aggravation", ItemClassification.useful, 1, 116, ["Skills"]),
    ACTItemData("Self Repair", ItemClassification.useful, 1, 117, ["Skills"]),
    ACTItemData("Kintsugi", ItemClassification.useful, 1, 118, ["Skills"]),
    ACTItemData("Skewer", ItemClassification.useful, 1, 119, ["Skills"]),
    ACTItemData("Plunge", ItemClassification.useful, 1, 120, ["Skills"]),
    ACTItemData("Scrap Hammer", ItemClassification.useful, 1, 121, ["Skills"]),
    ACTItemData("Dispatch", ItemClassification.useful, 1, 122, ["Skills"]),
    ACTItemData("Spearfishing", ItemClassification.progression, 1, 123, ["Skills"]),
    ACTItemData("Wave Breaker", ItemClassification.useful, 1, 124, ["Skills"]),
    ACTItemData("Streamline", ItemClassification.useful, 1, 125, ["Skills"]),
    ACTItemData("Housewarming", ItemClassification.useful, 1, 126, ["Skills"]),
    ACTItemData("Circle of Life", ItemClassification.useful, 1, 127, ["Skills"]),
    ACTItemData("Elusive Prey", ItemClassification.useful, 1, 128, ["Skills"]),
    ACTItemData("Skedaddle", ItemClassification.useful, 1, 134, ["Skills"]),
    ACTItemData("Ebb and Flow", ItemClassification.useful, 1, 129, ["Skills"]),
    ACTItemData("Umami Training 1", ItemClassification.useful, 1, 130, ["Skills"]),
    ACTItemData("Umami Training 2", ItemClassification.useful, 1, 131, ["Skills"]),
    ACTItemData("Umami Training 3", ItemClassification.useful, 1, 132, ["Skills"]),

    # traps
    ACTItemData("Gunk Trap", ItemClassification.trap, 0, 138, ["Traps"]),
    ACTItemData("Scour Trap", ItemClassification.trap, 0, 139, ["Traps"]),
    ACTItemData("Bleached Trap", ItemClassification.trap, 0, 140, ["Traps"]),
    ACTItemData("Fear Trap", ItemClassification.trap, 0, 141, ["Traps"]),
    ACTItemData("Clutz Trap", ItemClassification.trap, 0, 142, ["Traps"]),
    ACTItemData("Text Trap", ItemClassification.trap, 0, 143, ["Traps"]),
    ACTItemData("Shell Shatter Trap", ItemClassification.trap, 0, 144, ["Traps"]),
    ACTItemData("Poison Cocktail Trap", ItemClassification.trap, 0, 145, ["Traps"]),
    ACTItemData("Taser Trap", ItemClassification.trap, 0, 146, ["Traps"]),

    # macguffins
    ACTItemData("Crown of a Bleached King", ItemClassification.progression, 0, 182), # Lock for Camtscha
    ACTItemData("Conch's Shell", ItemClassification.progression, 0, 183), # Lock for Old Ocean
    ACTItemData("Shell Dispenser Switch", ItemClassification.progression, 0, 184), # Lock plug fuse dispensers

    # Other
    #ACTItemData("Acquire Any Shell", ItemClassification.progression, 0, 179, ["Event"]),
    #ACTItemData("Spin Attack", ItemClassification.useful, 0, 180, ["Spoof"]) # r1 air attack that allows for more distance and height from jumps
    #ACTItemData("Pagurus Allergy", ItemClassification.useful, 0, 181, ["Spoof"]) # used later when we randomise pagurus allergy
]

shell_items_data: ACTItemData = [
    ACTItemData("Soda Can", ItemClassification.progression, 0, None),
    ACTItemData("Bottle Cap", ItemClassification.progression, 0, None),
    ACTItemData("Tin Can", ItemClassification.progression, 0, None),
    ACTItemData("Shot Glass", ItemClassification.progression, 0, None),
    ACTItemData("Banana Peel", ItemClassification.filler, 0, None),
    ACTItemData("Party Hat", ItemClassification.progression, 0, None),
    ACTItemData("Coconut", ItemClassification.progression, 0, None),
    ACTItemData("Teacup", ItemClassification.progression, 0, None),
    ACTItemData("Sauce Nozzle", ItemClassification.progression, 0, None),
    ACTItemData("Thimble", ItemClassification.progression, 0, None),
    ACTItemData("Bebop Cup", ItemClassification.progression, 0, None),
    ACTItemData("Tennis Ball", ItemClassification.progression, 0, None),
    ACTItemData("F Key", ItemClassification.progression, 0, None),
    ACTItemData("Mason Jar", ItemClassification.progression, 0, None),
    ACTItemData("Salt Shaker", ItemClassification.progression, 0, None),
    ACTItemData("Conchiglie", ItemClassification.progression, 0, None),
    ACTItemData("Bartholomew", ItemClassification.progression, 0, None),
    ACTItemData("Disco Ball", ItemClassification.progression, 0, None),
    ACTItemData("Baby Shoe", ItemClassification.filler, 0, None),
    ACTItemData("Lil' Bro", ItemClassification.progression, 0, None),
    ACTItemData("Matryoshka Large", ItemClassification.progression, 0, None),
    ACTItemData("Shuttlecock", ItemClassification.progression, 0, None),
    ACTItemData("Felix Cube", ItemClassification.progression, 0, None),
    ACTItemData("Piggy Bank", ItemClassification.progression, 0, None),
    ACTItemData("Trophy", ItemClassification.progression, 0, None),
    ACTItemData("Imposter", ItemClassification.filler, 0, None),
    ACTItemData("Lil' Red Cup", ItemClassification.progression, 0, None),
    ACTItemData("Wafer Cone", ItemClassification.progression, 0, None),
    ACTItemData("Yoccult", ItemClassification.progression, 0, None),
    ACTItemData("Coffee Pod", ItemClassification.progression, 0, None),
    ACTItemData("Egg Shell", ItemClassification.progression, 0, None),
    ACTItemData("Coffee Mug", ItemClassification.progression, 0, None),
    ACTItemData("Cascadia Roll", ItemClassification.progression, 0, None),
    ACTItemData("Ham Tin", ItemClassification.progression, 0, None),
    ACTItemData("Skull", ItemClassification.progression, 0, None),
    ACTItemData("Crab Husk", ItemClassification.progression, 0, None),
    ACTItemData("Legal Brick", ItemClassification.progression, 0, None),
    ACTItemData("Spring", ItemClassification.progression, 0, None),
    ACTItemData("Shotgun Shell", ItemClassification.progression, 0, None),
    ACTItemData("Rubber Duck", ItemClassification.progression, 0, None),
    ACTItemData("Boxing Glove", ItemClassification.progression, 0, None),
    ACTItemData("Cardboard Box", ItemClassification.filler, 0, None),
    ACTItemData("Tissue Box", ItemClassification.filler, 0, None),
    ACTItemData("Valve", ItemClassification.progression, 0, None),
    ACTItemData("Dumptruck", ItemClassification.progression, 0, None),
    ACTItemData("Ink Cartridge", ItemClassification.filler, 0, None),
    ACTItemData("Gacha Capsule", ItemClassification.progression, 0, None),
    ACTItemData("Lightbulb", ItemClassification.progression, 0, None),
    ACTItemData("Mouse", ItemClassification.filler, 0, None),
    ACTItemData("Going Under 64", ItemClassification.progression, 0, None),
    ACTItemData("Sock", ItemClassification.progression, 0, None),
    ACTItemData("Doll Head", ItemClassification.progression, 0, None),
    ACTItemData("Service Bell", ItemClassification.progression, 0, None),
    ACTItemData("Party Popper", ItemClassification.progression, 0, None),
    ACTItemData("Scrub Aggy", ItemClassification.progression, 0, None),
    ACTItemData("Dentures", ItemClassification.filler, 0, None),
    ACTItemData("Pill Bottle", ItemClassification.progression, 0, None),
    ACTItemData("Detergent Cap", ItemClassification.progression, 0, None),
    ACTItemData("UltraSoft", ItemClassification.progression, 0, None),
    ACTItemData("Champagne Flute", ItemClassification.progression, 0, None),
    ACTItemData("Dish Scrubber", ItemClassification.progression, 0, None),
    ACTItemData("Snow Globe", ItemClassification.progression, 0, None),
    ACTItemData("Knight's Helmet", ItemClassification.progression, 0, None),
    ACTItemData("Plug Fuse", ItemClassification.progression, 0, None)
    #ACTItemData("Spirit Conch", ItemClassification.filler, 0, None),
    #ACTItemData("Matryoshka Medium", ItemClassification.progression, 0, None),
    #ACTItemData("Matryoshka Small", ItemClassification.progression, 0, None),
    #ACTItemData("Gun", ItemClassification.useful, 0, None)
]

item_table = {item_data.name: item_data for item_data in collectable_items_data + shell_items_data}


def get_item_groups(item_name: str) -> List[str]:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]

costume_items: List[str] = [name for name in filler_items if "Costume" in get_item_groups(name)]

shell_items: List[str] = [data.name for data in shell_items_data]

item_name_groups: Dict[str, Set[str]] = {
    group: names
    for group in sorted({group for data in item_table.values() for group in data.item_group if group})
    if (names := {name for name, data in item_table.items()
                  if data.item_id is not None and group in data.item_group})
}

item_limited_group = ["Umami Training 1", "Umami Training 2", "Umami Training 3", "Googly Eye", "Used Bandage"]  #TODO: what is this for?