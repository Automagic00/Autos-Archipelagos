from typing import Dict, Set

ACT_regions: Dict[str, Set[str]] = {
    "Menu": {
        "Tide Pool"
    },
    "Tide Pool": {
        "Central Shallows"
    },
    "Central Shallows": {
        "Central Shallows - Items Behind Grapple",
        "Fort Slacktide - Before Destruction"
    },
    "Central Shallows - Items Behind Grapple": set(),
    "Fort Slacktide - Before Destruction": {
        "Fort Slacktide - After Destruction",
        "Moon Snail's Cave",
        "Reef's Edge"
    },
    "Moon Snail's Cave": set(),
    "Fort Slacktide - After Destruction": {
        "Reef's Edge"
    },
    "Reef's Edge": {
        "Reef's Edge - Items Behind Grapple"
    },
    "Reef's Edge - Items Behind Grapple": {
        "New Carcinia"
    },
    "New Carcinia": {
        "The Sands Between"
    },
    "The Sands Between": {
        "The Sands Between - Post Pagurus",
        "The Sands Between - Grapple to East of Grove",
        "Secluded Ridge",
        "Trashbin Plateau",
        "Southern Town Ridge",
        "Expired Grove",
        "Flotsam Vale"
    },
    "The Sands Between - Grapple to East of Grove": {
        "Shell - Coffee Pod",
        "Shell - Legal Brick",
        "Shell - Ink Cartridge"
    },
    "The Sands Between - Post Pagurus": set(),
    "Secluded Ridge": {
        "Secluded Ridge - Past Eelectrocute"
    },
    "Secluded Ridge - Past Eelectrocute": {
        "Shell - Spring",
        "Shell - Shotgun Shell"
    }, 
    "Trashbin Plateau": set(),
    "Southern Town Ridge": {
        "Shell - Legal Brick"
    },
    "Expired Grove": {
        "Expired Grove - Village",
        "Expired Grove - Raised Platforms",
        "Flotsam Vale - Consortium Arena",
        "Shell - Coffee Pod",
    },
    "Expired Grove - Raised Platforms": set(),
    "Expired Grove - Village": set(),
    "Flotsam Vale": {
        "Pinbarge",
        "Flotsam Vale - Post Ceviche Sisters",
        "Flotsam Vale - Consortium Arena",
        "Scuttleport",
        "Shell - Plug Fuse",
        "Shell - Spring",
        "Shell - Shotgun Shell",
        "Shell - Legal Brick",
        "Shell - Salt Shaker"
    },
    "Flotsam Vale - Post Ceviche Sisters": set(),
    "Flotsam Vale - Consortium Arena": {
        "Shell - Salt Shaker",
        "Shell - Spring",
        "Shell - Rubber Duck"
    },
    "Scuttleport": {
        "Shell - Plug Fuse",
        "Shell - Rubber Duck"
    },
    "Pinbarge": {
        "The Unfathom",
        "Shell - Ink Cartridge",
    },
    "The Unfathom": {
        "Abyssal Plains"
    },
    "Abyssal Plains": {
        "The Old Ocean"
    },
    "The Old Ocean": {
        "Bottom of The Drain"
    },
    "Bottom of The Drain": {
        "Trash Island"
    },
    "Trash Island": {
        "Carcinia Ruins"
    },
    "Carcinia Ruins": set(),
    "Shell - Plug Fuse": set(),
    "Shell - Coffee Pod": set(),
    "Shell - Legal Brick": set(),
    "Shell - Ink Cartridge": set(),
    "Shell - Spring": set(),
    "Shell - Shotgun Shell": set(),
    "Shell - Salt Shaker": set(),
    "Shell - Rubber Duck": set()
}

