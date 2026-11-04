from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class Goal(Choice):
    """Choose your goal for the multiworld
    - Home: Defeat the final boss and equip the Home shell
    - Roland: Defeat Roland on the Pinbarge
    - Voltai: Defeat Voltai in Scuttleport
    - Magista: Defeat Magista in Slacktide"""
    display_name: str = "Goal"
    option_home = 0
    option_roland = 1
    option_voltai = 2
    option_magista = 3
    default = 0

# might be worth finding a way to combine ForkLocation and AllowForkless into one option for simplicity's sake

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set. Does nothing if [Allow Forkless] option is enabled.
    - Shuffled Early Local: Forces Fork location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Fork location to be somewhere early in any game.
    - Vanilla Location: Forces Fork to be placed at its intended location."""
    display_name: str = "Fork Location"
    option_vanilla_location = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    default = 0

class AllowForkless(Choice):
    """If enabled, allows for the Fork to not be required early on, meaning you may have to play some amount of the game without it. Ignores [Fork Location] option and shuffles Fork into item pool if enabled.
    - Disabled: Fork is required to fight early bosses, meaning that it will be placed early in your run.
    - Forkless Easy: Ensures that the intended forkless strategy is not too advanced (Includes logic for adaptation and shellspell focused builds)
    - Forkless Hard: Allows for the possibility of more advanced forkless strategies to be necessary (Includes logic for rolling attack and summon focused builds)"""
    display_name: str = "Allow Forkless"
    option_disabled = 0
    option_forkless_easy = 1
    option_forkless_hard = 2
    default = 0

class LogicRules(Choice):
    """Set the preferred logic rules for your game
    - Vanilla: Standard logic, no skips/glitches required to complete the goal.
    - Glitchless: Allows for the following parkour-based skips (list of glitchless rules here) to be required to complete the goal.
    - Restricted: In addition to the list under glitchless, allows for (list of easy glitches/skips here) to be required to complete the goal.
    - Unrestricted: In addition to the lists under both glitchless and restricted, allows for (list of hard glitches/skips here) to be required to complete the goal."""
    display_name:str = "Logic Rules"
    option_vanilla = 0
    option_glitchless = 1
    option_restricted = 2
    option_unrestricted = 3
    default = 0
 
class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location is set
    - Shuffled: Shelleport is placed into the item pool.
    - Shuffled Early Local: Forces Shelleport location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Shelleport location to somewhere early in any game.
    - Starting Items: Places Shelleport in your starting inventory.
    - Vanilla Location: Forces Shelleport to be placed at its intended location"""
    display_name: str = "Shelleport Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_starting_items = 3
    option_vanilla_location = 4
    default = 1

class FishingLineLocation(Choice):
    """Choose where the Fishing Line (grapple) location is set
    - Shuffled: Fishing Line is placed into item pool.
    - Shuffled Early Local: Forces Fishing Line location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Fishing Line location to somewhere early in any game.
    - Starting Items: Places Fishing Line in your starting inventory.
    - Vanilla Location: Forces Fishing Line to be placed at its intended location"""
    display_name: str = "Fishing Line Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_starting_items = 3
    option_vanilla_location = 4
    default = 0

class PristinePearlLocation(Choice):
    """Choose where the Pristine Pearl (Fallen Slacktide Trigger) location is set
    - Shuffled: Pristine Pearl is placed into item pool.
    - Shuffled Early Local: Forces Pristine Pearl location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Pristine Pearl location to somewhere early in any game.
    - Vanilla Location: Forces Pristine Pearl to be placed at its intended location"""
    display_name: str = "Pristine Pearl Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_vanilla_location = 3
    default = 0

class RandomShells(Toggle):
    """Choose whether or not shells will be randomized. Only randomizes shells within other shell locations."""
    display_name: str = "Random Shells"
    default: bool = True
    
class RandomFuse(Toggle):
    """Choose if the location of the Plug Fuse shell is randomized when using the shell randomizer. Does nothing if [RandomShells] is set to false"""
    display_name: str = "Random Fuse"
    default: bool = True

class ConchShell(Toggle):
    """Choose whether to lock access to The Old Ocean region behind an item requirement.
    If enabled, The Old Ocean will require the Conch's Shell item to be obtained before the lift to access it can be used.
    The required item is randomized and can be any item in the item pool."""
    display_name: str = "Conch's Shell"
    default: bool = False

class CrownOfABleachedKing(Toggle):
    """Choose whether to lock access to the Camtscha boss fight at the end of The Old Ocean behind an item requirement.
    If enabled, the Camtscha boss fight will require the Crown of a Bleached King item to be obtained before it can be accessed.
    The required item is randomized and can be any item in the item pool."""
    display_name: str = "Crown of a Bleached King"
    default: bool = False

class RemoveCostumes(Toggle):
    """Choose whether to include Costumes in the item pool. Set to true to remove them."""
    display_name: str = "Remove Costumes"
    default: bool = False

class MicroplasticMultiplier(Range):
    """Multiplies the amount of microplastics received from all sources. Only supports integer values."""
    display_name: str = "Microplastic Multiplier"
    range_start: int = 1
    range_end: int = 100
    default: int = 1

class TrapAmount(Range):
    """Defines a percentage of the filler items to be replaced with trap items
    Set to 0 to not include any traps"""
    display_name: str = "Trap Amount"
    range_start: int = 0
    range_end: int = 100
    default: int = 0

class DeathLink(Toggle):
    """Enables Death Link"""
    display_name: str = "Death Link"
    default: bool = False

class NGPlusBosses(Toggle):
    """Replaces all bosses with their NG+ variants.
    This can make runs significantly more difficult, especially early on."""
    display_name: str = "NG+ Bosses"
    default: bool = False

class NGPlusStowaways(Toggle):
    """Adds New Game+ stowaways to the item pool."""
    display_name: str = "NG+ Stowaways"
    default: bool = False

class NGPlusStowawaySlots(Toggle):
    """Determines stowaway capacity and slots
    False = NG (3 Stowaways, 9 Slot Max)
    True = NG+ (4 Stowaways, 12 Slot Max)"""
    display_name: str = "NG+ Stowaway Capacity"
    default: bool = False

@dataclass
class ACTGameOptions(PerGameCommonOptions):
    goal: Goal
    fork_location: ForkLocation
    allow_forkless: AllowForkless
    logic_rules: LogicRules
    shelleport_location: ShelleportLocation
    fishing_line_location: FishingLineLocation
    pristine_pearl_location: PristinePearlLocation
    randomshells: RandomShells
    randomfuse: RandomFuse
    conch_shell: ConchShell
    crown_of_a_bleached_king: CrownOfABleachedKing
    remove_costumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    trapamount: TrapAmount
    deathlink: DeathLink
    ngplus_bosses: NGPlusBosses
    ngplus_stowaways: NGPlusStowaways
    ngplus_slots: NGPlusStowawaySlots