from typing import Dict, Set
from .names import shell_names as sname

ACT_regions: Dict[str, Set[str]] = {
    "Menu": {
        "Tide Pool"
    },
    "Tide Pool": {
        "Central Shallows"
    },
    "Central Shallows": {
        "Central Shallows - Items Behind Grapple",
        "Fort Slacktide - Before Destruction",
        sname.soda_can
    },
    "Central Shallows - Items Behind Grapple": set(),
    "Fort Slacktide - Before Destruction": {
        "Fort Slacktide - After Destruction",
        "Moon Snail's Cave",
        "Reef's Edge",
        sname.soda_can,
        sname.coconut,
        sname.banana_peel,
        sname.tin_can
    },
    "Moon Snail's Cave": {
        sname.soda_can,
        sname.bottle_cap,
        sname.shot_glass,
        sname.party_hat
    },
    "Fort Slacktide - After Destruction": {
        "Reef's Edge",
        sname.teacup
    },
    "Reef's Edge": {
        "Reef's Edge - Items Behind Grapple",
        sname.sauce_nozzle
    },
    "Reef's Edge - Items Behind Grapple": {
        "New Carcinia",
        sname.thimble,
        sname.tennis_ball
    },
    "New Carcinia": {
        "The Sands Between",
        sname.f_key,
        sname.conchiglie,
        sname.shuttlecock,
        sname.bartholomew,
        sname.lil_bro,
        sname.piggy_bank,
        sname.imposter,
        sname.felix_cube,
        sname.baby_shoe,
        sname.trophy,
        sname.matryoshka_large
    },
    "The Sands Between": {
        "The Sands Between - Post Pagurus",
        "The Sands Between - Grapple to East of Grove",
        "Secluded Ridge",
        "Trashbin Plateau",
        "Southern Town Ridge",
        "Expired Grove",
        "Flotsam Vale",
        sname.yoccult,
        sname.mason_jar,
        sname.bebop_cup,
        sname.disco_ball,
        sname.lil_red_cup,
        sname.valve
    },
    "The Sands Between - Grapple to East of Grove": {
        sname.coffee_pod,
        sname.legal_brick,
        sname.ink_cartridge
    },
    "The Sands Between - Post Pagurus": set(),
    "Secluded Ridge": {
        "Secluded Ridge - Past Eelectrocute"
    },
    "Secluded Ridge - Past Eelectrocute": {
        sname.shotgun_shell,
        sname.legal_brick,
        sname.spring
    }, 
    "Trashbin Plateau": set(),
    "Southern Town Ridge": {
        sname.legal_brick
    },
    "Expired Grove": {
        "Expired Grove - Village",
        "Expired Grove - Raised Platforms",
        "Flotsam Vale - Consortium Arena",
        sname.coffee_mug,
        sname.cascadia_roll,
        sname.wafer_cone,
        sname.egg_shell,
        sname.coffee_pod
    },
    "Expired Grove - Raised Platforms": set(),
    "Expired Grove - Village": {
        sname.skull,
        sname.ham_tin,
        sname.crab_husk
    },
    "Flotsam Vale": {
        "Pinbarge",
        "Flotsam Vale - Post Ceviche Sisters",
        "Flotsam Vale - Consortium Arena",
        "Scuttleport",
        "Scuttleport - Plug Fuse Pipes",
        sname.boxing_glove,
        sname.tissue_box,
        sname.cardboard_box,
        sname.salt_shaker,
        sname.spring, 
        sname.shotgun_shell,
        sname.legal_brick
    },
    "Scuttleport - Plug Fuse Pipes": {
        sname.plug_fuse
    },
    "Flotsam Vale - Post Ceviche Sisters": set(),
    "Flotsam Vale - Consortium Arena": {
        sname.salt_shaker,
        sname.spring,
        sname.rubber_duck
    },
    "Scuttleport": {
        "Scuttleport - Plug Fuse Pipes",
        sname.dumptruck,
        sname.rubber_duck
    },
    "Pinbarge": {
        "The Unfathom",
        sname.gacha_capsule,
        sname.ink_cartridge
    },
    "The Unfathom": {
        "Abyssal Plains",
        sname.doll_head,
        sname.lightbulb,
        sname.mouse,
        sname.sock,
        sname.going_under_64,
        sname.party_popper,
        sname.service_bell
    },
    "Abyssal Plains": {
        "The Old Ocean"
    },
    "The Old Ocean": {
        "Bottom of The Drain",
        sname.ultrasoft,
        sname.pill_bottle,
        sname.scrub_aggie,
        sname.knights_helmet,
        sname.snow_globe,
        sname.detergent_cap,
        sname.champagne_flute,
        sname.dentures,
        sname.dish_scrubber
    },
    "Bottom of The Drain": {
        "Trash Island"
    },
    "Trash Island": {
        "Carcinia Ruins"
    },
    "Carcinia Ruins": set(),
    sname.soda_can: set(),
    sname.bottle_cap: set(),
    sname.tin_can : set(),
    sname.shot_glass : set(),
    sname.banana_peel : set(),
    sname.party_hat : set(),
    sname.coconut: set(),
    sname.teacup: set(),
    sname.sauce_nozzle : set(),
    sname.thimble: set(),
    sname.bebop_cup : set(),
    sname.tennis_ball: set(),
    sname.f_key : set(),
    sname.mason_jar : set(),
    sname.salt_shaker : set(),
    sname.conchiglie : set(),
    sname.bartholomew : set(),
    sname.disco_ball : set(),
    sname.baby_shoe : set(),
    sname.lil_bro : set(),
    sname.matryoshka_large : set(),
    sname.shuttlecock : set(),
    sname.felix_cube : set(),
    sname.piggy_bank : set(),
    sname.trophy : set(),
    sname.imposter : set(),
    sname.lil_red_cup : set(),
    sname.wafer_cone : set(),
    sname.yoccult : set(),
    sname.coffee_pod : set(),
    sname.egg_shell : set(),
    sname.coffee_mug : set(),
    sname.cascadia_roll : set(),
    sname.ham_tin : set(),
    sname.skull : set(),
    sname.crab_husk : set(),
    sname.legal_brick : set(),
    sname.spring : set(),
    sname.shotgun_shell : set(),
    sname.rubber_duck: set(),
    sname.boxing_glove : set(),
    sname.cardboard_box : set(),
    sname.tissue_box: set(),
    sname.valve : set(),
    sname.dumptruck: set(),
    sname.ink_cartridge: set(),
    sname.gacha_capsule: set(),
    sname.lightbulb: set(),
    sname.mouse : set(),
    sname.going_under_64 : set(),
    sname.sock : set(),
    sname.doll_head : set(),
    sname.service_bell : set(),
    sname.party_popper : set(),
    sname.scrub_aggie : set(),
    sname.dentures: set(),
    sname.pill_bottle : set(),
    sname.detergent_cap: set(),
    sname.ultrasoft: set(),
    sname.champagne_flute: set(),
    sname.dish_scrubber: set(),
    sname.snow_globe : set(),
    sname.knights_helmet : set(),
    sname.plug_fuse: set()
}

