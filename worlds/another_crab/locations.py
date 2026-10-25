from typing import Dict, List, NamedTuple, Set
from BaseClasses import Location, Region

class ACTLocationData(NamedTuple):
    name: str 
    region: str 
    location_id: int # first id: 483021700, last used id: 483022326, available: 483022327
    location_group: List[str] = []

class ACTLocation(Location):
    game: str = "Another Crabs Treasure"
    data: ACTLocationData

    def __init__(
            self,
            player: int,
            data: ACTLocationData,
            region: Region = None
            ):
        super().__init__(player, data.name, data.location_id, region),
        self.data = data

locations_data: List[ACTLocationData] = [
    # progression item locations
    ACTLocationData('Fork Pickup', 'Cave of Respite', 483021700), #73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools
    ACTLocationData('Fishing Line', 'Fort Slacktide - Before Destruction', 483021702),
    ACTLocationData('Polluted Platoon Pathfinder', "Moon Snail's Cave", 483021746), #default location for pristine pearl
    ACTLocationData('Map Piece - Heikea', 'Expired Grove', 483021952),
    ACTLocationData('Map Piece - Flotsam Vale', 'Flotsam Vale - Post Ceviche Sisters', 483022096),
    ACTLocationData('Pagurus, The Ravenous', 'The Sands Between', 483021748), #default location for third map piece
    #ACTLocationData("Heartkelp Pods Pickup", "Cave of Respite", 483021701), #950e628c-f657-48d4-b93b-f8717627f6b3-2_A-ShallowsTidePools

    # boss locations
    ACTLocationData('Nephro, Captain of the Guard', 'Central Shallows', 483021703),
    ACTLocationData('Magista, Tyrant of Slacktide', 'Fort Slacktide - After Destruction', 483021744),
    ACTLocationData('Royal Shellsplitter', 'Central Shallows', 483021747),
    ACTLocationData('Diseased Lichenthrope', 'Expired Grove', 483021749),
    ACTLocationData('Curdled Carbonara Connoisseur', 'Expired Grove', 483021750),
    ACTLocationData('Heikea, Intimidation Crab', 'Expired Grove', 483021751),
    ACTLocationData('Grovekeeper Topoda', 'Expired Grove - Village', 483021752),
    ACTLocationData('The Consortium', 'Flotsam Vale - Consortium Arena', 483021753),
    ACTLocationData('Scuttling Sludge Steamroller', 'Flotsam Vale', 483021754),
    ACTLocationData('Ceviche Sisters', 'Flotsam Vale', 483021755),
    ACTLocationData('Voltai, The Accumulator', 'Scuttleport', 483021756),
    ACTLocationData('Roland, Venture Crabitalist', 'Pinbarge', 483021757),
    ACTLocationData('Petroch, The False Moon', 'The Unfathom', 483021758),
    ACTLocationData('Inkerton, Crab Hunter', 'Abyssal Plains', 483021759),
    ACTLocationData('Camtscha, The Bleached King', 'The Old Ocean', 483021760),
    ACTLocationData("Praya Dubia, The Ocean's Agony", 'Bottom of The Drain', 483021761),
    ACTLocationData('Firth, The Crab Who Stole The Whorl', 'Trash Island', 483021762),
    ACTLocationData('Extremely Rude Snail', 'Central Shallows', 483022326),
    
    ##### currency item locations
    ACTLocationData('Breadclaw (Cave of Respite - Ledge)', 'Cave of Respite', 483021704), #73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools
    ACTLocationData('Chipclaw (Cave of Respite - Fishing Near Fork Pickup)', 'Cave of Respite', 483021820), #d985ffba-0ece-414d-8161-fa65241dd2b1-2_B-ShallowsBigSand
    ACTLocationData('Mussel (Cave of Respite - Fishing In Crab Fight Tutorial)', 'Cave of Respite', 483021821), #d1af097b-c6c9-44a4-9ced-4a09a973c0d5-2_B-ShallowsBigSand
    ACTLocationData('Clothesclaw (Cave of Respite - Fishing Before Cave Entrance)', 'Cave of Respite', 483021822), #0ac3fa03-5aab-4f12-86e4-8e9dfde8c04f-2_B-ShallowsBigSand
    ACTLocationData('Sand Dollar (Cave of Respite - Fishing on Path Before Cave)', 'Cave of Respite', 483021823), #9ef4b1f3-5a80-408c-962a-b3fed8c68770-2_B-ShallowsBigSand

    ACTLocationData('Breadclaw (Central Shallows - South Red Flip-Flop)', 'Central Shallows', 483021705),#0171a152-809a-47cf-9fcc-60ddb61511bb-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Along West Wall)', 'Central Shallows', 483021706), #ae27274c-c3f7-4721-9ddb-7c5a880578a4-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Red Flip-Flop Bridge)', 'Central Shallows', 483021707), #8b269a88-c6d1-4b2a-8e5f-9d60c6d6fd15-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Along East Wall)', 'Central Shallows', 483021708), #6aba5604-8269-46a5-b734-ef4dc3983265-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - East Red Flip-Flop)', 'Central Shallows', 483021709), #889c343a-b969-4295-b059-a837fc457444-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Cigarette Butts', 'Fort Slacktide - After Destruction', 483021710), #d1ddf122-d283-4509-8bfa-bff8fa209f35-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Along Fort Slacktide Wall)', 'Central Shallows', 483021711), #20bede55-9eae-40a3-a80a-63ee5b52d0bf-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - East Broken Fort Wall Piece)', 'Central Shallows', 483021712), #5732b602-c599-41b5-bc5d-93e88277a4b7-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Southeast Sandcastle)', 'Central Shallows - Items Behind Grapple', 483021713), #984eda06-d10e-4b2b-a5c4-389784ed18f6-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - East Grapple Ledge)', 'Central Shallows - Items Behind Grapple', 483021714), #51dbcbfd-4a82-4c22-b2ee-1a03deeca4cc-2_B-ShallowsBigSand
    ACTLocationData('Hairclaw (Central Shallows - Grapple to Castle Turret)', 'Central Shallows - Items Behind Grapple', 483021715), #b2d21ade-41ab-47fc-960b-0beb6d07359d-2_B-ShallowsBigSand
    ACTLocationData('Chipclaw (Central Shallows - Southwest Sandcastle)', 'Central Shallows', 483021716), #12c6e5c5-eee1-4f9a-a3c4-68c2bd098a14-2_B-ShallowsBigSand
    ACTLocationData('Clothesclaw (Central Shallows - Small Tower Outside Southwest Fort)', 'Central Shallows', 483021745), #e13e2c76-a638-4023-aa84-f6f29fd7bf65-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Sunken Tower near Flip-Flop Bridge)', 'Central Shallows', 483021824), #1e33dfd0-6445-47f9-b1bf-3e8be7897a79-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Central Shallows - Fishing South of Slacktide Entrance)', 'Central Shallows', 483021826), #0f64d031-4163-4979-9497-116cac06e234-2_B-ShallowsBigSand
    #ACTLocationData('Clothesclaw (Central Shallows - Defeat Royal Shellsplitter)', 'Central Shallows', 483021717), # TODO: custom boss script? No UUID given...

    ACTLocationData('Breadclaw (Fort Slacktide - Sand Crates and Barrels', 'Fort Slacktide - Before Destruction', 483021718), #8c1e68dc-eb15-41f4-9a5d-c1b20dd76f52-2_B-ShallowsBigSand
    ACTLocationData('Breadclaw (Fort Slacktide - On South Training Area Wall)', 'Fort Slacktide - Before Destruction', 483021830), #0ad90b46-ca8b-46ed-9cc6-f72ffcdb9d33-2_B-ShallowsBigSand

    ACTLocationData("Breadclaw (Moon Snail's Cave - Ledge Near Entrance)", "Moon Snail's Cave", 483021719), #5bb2169d-f820-41f0-9783-336c006861c6-2_D-MoonSnailShellCave
    ACTLocationData("Breadclaw (Moon Snail's Cave - Ledge Near Shortcut)", "Moon Snail's Cave", 483021720), #436eff44-09df-451e-93c8-3a5714ec55c2-2_D-MoonSnailShellCave
    ACTLocationData("Breadclaw (Moon Snail's Cave - Ledge Past Moon Jelly)", "Moon Snail's Cave", 483021721), #07977d86-44ec-40d0-b331-8b45b1d44838-2_D-MoonSnailShellCave

    ACTLocationData('Breadclaw (Fort Slacktide - Near Crab Trio)', 'Fort Slacktide - After Destruction', 483021722), #2af7f575-51f3-4da9-b3bf-eab9d32a3bd8-2_C-Slacktide2
    ACTLocationData('Chipclaw (Fort Slacktide - Behind Broken Wall)', 'Fort Slacktide - After Destruction', 483021723), #45f42ae3-41b6-4333-875f-3a9e8387e087-2_C-Slacktide2
    ACTLocationData('Breadclaw (Fort Slacktide - Path to Roof Hidden Fishing)', 'Fort Slacktide - After Destruction', 483021831), #59e2ec5a-b650-43fa-879d-3af1569fb640-2_B-ShallowsBigSand

    ACTLocationData("Chipclaw (Reef's Edge - Broken Bridge)", "Reef's Edge", 483021763), #e9bf56b8-1362-42a9-87a2-00bed3a6f5d2-2_A-NCTradeRoute
    ACTLocationData("Breadclaw (Reef's Edge - Near Thimble Crab)", "Reef's Edge - Items Behind Grapple", 483021767), #1f5a8d6b-10ab-4e4e-b240-284e2ec2c77a-2_A-NCTradeRoute
    ACTLocationData("Hairclaw (Reef's Edge - Near I95 Sign On Ledge)", "Reef's Edge", 483021771), #b478df52-084c-4c14-8a55-215fdbaeaffe-2_A-NCTradeRoute

    ACTLocationData('Breadclaw (New Carcinia - Top of Buildings Near Entrance)', 'New Carcinia', 483021774), #fb5e2e88-b498-4af4-b7a6-4f176eb4016c-2_B-NCCity
    ACTLocationData('Breadclaw (New Carcinia - Corner Near Hammerhead)', 'New Carcinia', 483021776), #e26a7cee-15af-4f6c-b6fb-253f8dfac6e4-2_B-NCCity
    ACTLocationData('Breadclaw (New Carcinia - Alleyway Near Bottom Feeders)', 'New Carcinia', 483021779), #4058fdd6-84f5-4f1e-b8f1-3dcccb288aa2-2_B-NCCity
    ACTLocationData('Breadclaw (New Carcinia - Alleyway Across from Prawn Shop)', 'New Carcinia', 483021780), #d538af5f-81e0-452c-8800-756bb635a16b-2_B-NCCity
    ACTLocationData('Chipclaw (New Carcinia - On Building Near Climbable Mannequin Leg)', 'New Carcinia', 483021781), #4f62e34e-df79-4e33-99bb-b65844e50304-2_B-NCCity
    ACTLocationData('Breadclaw (New Carcinia - On Tall Building Across from Prawn Shop)', 'New Carcinia', 483021782), #0e59ec85-36b5-4750-baf4-cc9899525ca6-2_B-NCCity
    ACTLocationData('Breadclaw (New Carcinia - On Short Building Across From Mannequin Leg)', 'New Carcinia', 483021783), #c91a3fa0-f774-4e5f-a43e-90dd9a1d5e3a-2_B-NCCity
    ACTLocationData('Chipclaw (New Carcinia - On Top of Prawn Shop)', 'New Carcinia', 483021784), #d2b95a55-ec16-48cc-bce4-c7e39a16a78a-2_B-NCCity

    ACTLocationData('Breadclaw (The Sands Between - Central Vista Base)', 'The Sands Between', 483021787), #4a22c058-bbb2-467a-b204-9c1a82dc0d9c-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - Above Bobbit Worm near Southern Reef)', 'The Sands Between', 483021794), #cc1a7d82-3803-474e-8f66-c149055c4cb9-2_A-OOGroveRadius
    ACTLocationData('Chipclaw (The Sands Between - Sands near Expired Grove Entrance)', 'The Sands Between', 483021802), #0bae76f4-e90b-435b-9089-356ef62ba0fa-2_A-OOGroveRadius
    ACTLocationData('Breadclaw (The Sands Between - West Edge near Chains)', 'The Sands Between', 483021806), #d78747bd-2da0-4421-add8-3c5842fa0f61-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Second Terrace in Bobbit Den)', 'The Sands Between', 483021807), #e128b8e9-0c20-426f-8f47-783043f829dc-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - Third Terrace in Bobbit Den near Bobbit Worm)', 'The Sands Between', 483021808), #8d9edda5-d554-4e75-8842-8239075a334a-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Rock Northwest of Central Vista)', 'The Sands Between', 483021811), #7e93197a-47f1-4bdd-b7f0-5d0ecffb39f4-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Cans near Expired Grove Entrance)', 'The Sands Between', 483021812), #cd2f3731-b9f4-4f88-abd2-44d142eca493-2_A-OOGroveRadius
    ACTLocationData('Breadclaw (The Sands Between - Cliff Near Propane)', 'The Sands Between', 483021835), #f553b94c-14ea-4852-8ae7-564b8d30b24d-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - North of Chains)', 'The Sands Between', 483021837), #7e4ef7d0-214a-4358-a0c3-866a869d71e0-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Pitfall Near Cooler Lid)', 'The Sands Between', 483021838), #9faef117-fd92-47cb-b4d8-cc2a07404a69-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - Pitfall South of Grove)', 'The Sands Between', 483021839), #305be10e-d5a7-42e6-88f1-2cebdd524bbb-2_A-OOGroveRadius
    ACTLocationData('Paperclaw (The Sands Between - Southern Eelectrocute Path, Near Shortcut)', 'Southern Town Ridge', 483021847), #0e2d558b-26a7-4213-be83-77355fe06128-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - South Eelectrocute Path Second Jump)', 'The Sands Between', 483021850), #5c8133eb-ddb3-4b24-9849-f4d3f03491e0-2_A-OOGroveRadius
    ACTLocationData('Paperclaw (The Sands Between - Behind Trashbag Near Anchor)', 'The Sands Between', 483021855), #98e4d994-92c4-4b3b-82b7-f460a49d604b-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - Fishing Near Anchor)', 'The Sands Between', 483021856), #cab91803-4006-456d-95c7-6ec17d90c26a-2_A-OOGroveRadius
    ACTLocationData('Chipclaw (The Sands Between - Fishing North East of Chains)', 'The Sands Between', 483021857), #b0bf9c58-ff96-404c-bd1b-361fb1711b64-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Fishing Near Propane Tank)', 'The Sands Between', 483021858), #17b29697-5b33-4568-a311-2dbfac60317a-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (The Sands Between - Fishing Between Central Vista and Anchor)', 'The Sands Between', 483021860), #628bf319-c5f3-448b-8ec0-71a173246a09-2_A-OOGroveRadius
    ACTLocationData('Breadclaw (The Sands Between - Fishing Near Nail)', 'The Sands Between', 483021862), #98c3bf98-c4bd-4c67-8678-0464e7095970-2_A-OOGroveRadius
    ACTLocationData('Breadclaw (The Sands Between - Fishing In Wooden Pallet)', 'The Sands Between', 483021863), #69ac316d-8d42-48a4-8d55-4ec4d6429c7c-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (The Sands Between - South Eelectrocute Path Large Island Fishing)', 'Southern Town Ridge', 483021864), #38edc1a4-dea8-4000-8683-6cda7f6ba3bc-2_A-OOGroveRadius
    ACTLocationData('Chipclaw (The Sands Between - Hidden Fishing on Stone Cliff Near Anchor)', 'The Sands Between', 483021865), #01999bed-4813-4fe3-ab9b-5ed19cce90f1-2_A-OOGroveRadius

    ACTLocationData('Stapleclaw (Post Pagurus - Litterbox)', 'The Sands Between - Post Pagurus', 483021870), #e872d437-5bdb-4e70-820a-030bc21d66d5-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (Post Pagurus - Middle of Chains)', 'The Sands Between - Post Pagurus', 483021871), #4e9d02aa-75f5-4b87-b029-6ee1e7d62f7a-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (Post Pagurus - Middle of Chains)', 'The Sands Between - Post Pagurus', 483021872), #2fa3fdd0-b3da-4c69-b579-a5d316075635-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (Post Pagurus - North of Ridge Overlook)', 'The Sands Between - Post Pagurus', 483021879), #55fafe55-5d22-49a8-8b2b-aea149468a61-2_A-OOGroveRadius
    ACTLocationData('Hairclaw (Post Pagurus - East of Central Vista)', 'The Sands Between - Post Pagurus', 483021880), #c2d06d3f-65f4-46cf-b069-0b4098b425d0-2_A-OOGroveRadius
    ACTLocationData('Chipclaw (Post Pagurus - Preserver North-West of Propane)', 'The Sands Between - Post Pagurus', 483021882), #45af0c47-a8e0-498f-8345-9c9ddabbd6b3-2_A-OOGroveRadius
    ACTLocationData('Paperclaw (Post Pagurus - South of Chains)', 'The Sands Between - Post Pagurus', 483021885), #16dfae13-103f-45eb-9661-3e6463a2b805-2_A-OOGroveRadius

    ACTLocationData('Clothesclaw (Secluded Ridge - North East Secluded Ridge)', 'Secluded Ridge', 483021889), #e2803d8a-feea-45a7-addf-3330748d9e4b-2_A-OOGroveRadius
    ACTLocationData('Paperclaw (Secluded Ridge - Hidden Crab near Ridge Overlook)', 'Secluded Ridge', 483021893), #f6db9d48-5df1-4a7f-9f17-b760901954c9-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (Secluded Ridge - Near Broom)', 'Secluded Ridge', 483021895), #3f8d4c85-202f-42dc-9105-434d601d1d75-2_A-OOGroveRadius
    ACTLocationData('Breadclaw (Secluded Ridge - Southern Path)', 'Secluded Ridge', 483021897), #d1883b57-b339-4c31-826a-e76a3de0ee4b-2_A-OOGroveRadius
    ACTLocationData('Clothesclaw (Secluded Ridge - Fishing on Ridge Overlook)', 'Secluded Ridge', 483021906), #4f737f9e-a952-490c-b54d-1f74735af9cc-2_A-OOGroveRadius
    ACTLocationData('Chipclaw [Currency] (Fishing South of Ridge Overlook)', 'Secluded Ridge', 483021907), #82043889-30eb-45f4-8f87-45dd2f5d69ed-2_A-OOGroveRadius

    ACTLocationData('Stapleclaw (Trashbin Plateau - Eelectrocute Grapple Path Fishing)', 'Trashbin Plateau', 483021909), #190034bb-c13e-42ec-bac4-037cc828fde3-2_A-OOGroveRadius

    ACTLocationData('Breadclaw (Expired Grove - East Takeout Container)', 'Expired Grove', 483021919), #7d3ea7ae-4d80-4618-b798-39ba032f7650-2_A-GroveForestLow
    ACTLocationData('Breadclaw (Expired Grove - Near Tire Archway)', 'Expired Grove', 483021924), #075bc58b-ab5e-41cc-b82b-89f7c897821a-2_A-GroveForestLow
    ACTLocationData('Chipclaw (Expired Grove - Plastic Silverware Near Entrance)', 'Expired Grove', 483021925), #af194776-481c-4198-aa8b-baf05f24de1b-2_A-GroveForestLow
    ACTLocationData('Clothesclaw (Expired Grove - Chocolate Milk Carton)', 'Expired Grove', 483021926), # 6ad0a92e-48c3-40e6-9f3c-746fd78cf376-2_A-GroveForestLow
    ACTLocationData('Breadclaw (Expired Grove - Inside Tire Archway)', 'Expired Grove', 483021927), #90bfa7e8-b69f-4e3b-b539-967c7df38523-2_A-GroveForestLow
    ACTLocationData('Chipclaw (Expired Grove - East Sniper Ledge)', 'Expired Grove', 483021945), #9ca18539-8fd5-4def-9418-c17bbb1f0d65-2_A-GroveForestLow
    ACTLocationData('Hairclaw (Expired Grove - Milk Carton Urchins)', 'Expired Grove', 483021946), #df6fcb07-437c-4b21-b207-5a9e8e37cccb-2_A-GroveForestLow
    ACTLocationData('Chipclaw (Expired Grove - Rotten Apple Cores)', 'Expired Grove', 483021932), #faa3c9ce-87c7-4f6d-b07e-be334c3bc447-2_A-GroveForestLow
    ACTLocationData('Chipclaw (Expired Grove - Shopping Cart Soda Cans)', 'Expired Grove', 483021933), #25737275-a222-4a6e-af6b-0c66c197cab7-2_A-GroveForestLow
    ACTLocationData('Hairclaw (Expired Grove - Shopping Cart Moonshine)', 'Expired Grove', 483021934), #1c84843a-ab7e-433f-b376-83a0373f5a97-2_A-GroveForestLow
    ACTLocationData('Chipclaw (Expired Grove - Circular Rock Past Shopping Cart)', 'Expired Grove', 483021938), #1b74ef4f-528c-484b-9a5f-abbb3434f133-2_A-GroveForestLow
    ACTLocationData('Clothesclaw (Expired Grove - Gunk River Alcove Near Waterfall)', 'Expired Grove', 483021939), #f99a120b-43c2-4e65-91fd-71cbfbf3e8f7-2_A-GroveForestLow
    ACTLocationData('Hairclaw (Expired Grove - Elevated Sniper Platform)', 'Expired Grove - Raised Platforms', 483021940), #8f4a1f33-e567-4c84-b34b-739353b3ba08-2_A-GroveForestLow
    ACTLocationData('Breadclaw (Expired Grove - Among Us Fries)', 'Expired Grove', 483021943), #c859129f-cc29-4624-a161-fdeffa00d0ca-2_B-GroveForestHigh
    ACTLocationData('Breadclaw (Expired Grove - Small Platform Next to Oil Drum)', 'Expired Grove', 483021944), #b85cb09c-f1d7-4396-85cb-fde4dc845acd-2_B-GroveForestHigh
    ACTLocationData('Breadclaw (Expired Grove - Grapple Near Top of Oil Drum)', 'Expired Grove', 483021949), #bc18b92b-a6c6-420c-9095-e15c34c2f921-2_B-GroveForestHigh
    ACTLocationData('Clothesclaw (Expired Grove - Fishing Near Mantis Block)', 'Expired Grove', 483021956), #789ed5bd-38ce-4539-8f1c-135cc3c89377-2_A-GroveForestLow
    ACTLocationData('Hairclaw (Expired Grove - Hidden Fishing Near Milk Carton)', 'Expired Grove', 483021957), #24079978-2320-428e-9096-71aa2d20fb9c-2_A-GroveForestLow
    ACTLocationData('Clothesclaw (Expired Grove - River Fishing Near Carbonara Waterfall)', 'Expired Grove', 483021958), #ebad553d-fbff-441e-8c1d-0ccc65fe81ae-2_A-GroveForestLow
    ACTLocationData('Clothesclaw (Expired Grove - Behind Waterfall Near Lycanthrope)', 'Expired Grove', 483022321), #cb589bcb-04b5-412d-a8a0-8502b584083b-2_A-GroveForestLow
    ACTLocationData('Hairclaw (Expired Grove - Ledge After Grapple Nets)', 'Secluded Ridge', 483021930), #886641b3-08c7-4460-97dc-56d52e2e24c9-2_A-GroveForestLow

    ACTLocationData('Breadclaw (Expired Grove Village - After Oil Drum)', 'Expired Grove - Village', 483021968), #66a4a627-ad3a-45d6-aaf1-1e505dac0495-2_B-GroveForestHigh
    ACTLocationData('Breadclaw (Expired Grove Village - In Bottle Near Cart Mantis Block 1)', 'Expired Grove - Village', 483021969), #a6e719fc-65b0-4c3a-830e-43065a819c7d-2_B-GroveForestHigh
    ACTLocationData('Breadclaw (Expired Grove Village - In Bottle Near Cart Mantis Block 2)', 'Expired Grove - Village', 483021970), #507a5ca4-3de6-4d85-ba51-04c1e42c891e-2_B-GroveForestHigh
    ACTLocationData('Chipclaw (Expired Grove Village - Near Net Orbs After Heikea)', 'Expired Grove - Village', 483021953), #df0386e0-99ee-478a-873d-b40e973fc16b-2_D-Caves
    ACTLocationData('Hairclaw (Expired Grove Village - River Fishing Before Oil Drum)', 'Expired Grove - Village', 483021972), #ec08fee3-e62f-45ee-9fbe-9101522d4f30-2_B-GroveForestHigh
    ACTLocationData('Chipclaw (Expired Grove Village - In North West Milk Carton)', 'Expired Grove - Village', 483021976), #4fc8b860-3980-4dba-9a04-622ca685f58a-2_C-Village
    ACTLocationData('Chipclaw (Expired Grove Village - In South East Milk Carton)', 'Expired Grove - Village', 483021981), #541eece9-d2ae-46c6-8799-6c8fce1038ba-2_C-Village
    ACTLocationData('Chipclaw (Expired Grove Village - In North East Milk Carton)', 'Expired Grove - Village', 483021983), #34fca9ff-ebdc-4e26-955b-acda73df419d-2_C-Village
    ACTLocationData('Breadclaw (Expired Grove Village - Near Cave Shortcut)', 'Expired Grove - Village', 483021989), #ff8f29f4-2859-4ff7-857f-54e0a9c185fa-2_D-Caves
    ACTLocationData('Chipclaw (Expired Grove Village - Near End of Cave)', 'Expired Grove - Village', 483021991), #6dbab2ee-2440-4b3d-944e-688f11a88199-2_D-Caves
    ACTLocationData('Hairclaw (Expired Grove Village - Near Village Entrance)', 'Expired Grove - Village', 483021992), #7434f4f5-8e47-40f0-b3a3-507ada236333-2_D-Caves
    ACTLocationData('Breadclaw (Expired Grove Village - In South Milk Carton)', 'Expired Grove - Village', 483021993), #a14ac78c-615a-45a5-a4f9-c286c98d99f8-2_C-Village
    ACTLocationData('Breadclaw (Expired Grove Village - Behind bottles at Village Entrance)', 'Expired Grove - Village', 483021994), #a4867b74-b444-42b0-ae95-be5e1044f19e-2_C-Village
    ACTLocationData('Hairclaw (Expired Grove Village - In North East High Milk Carton)', 'Expired Grove - Village', 483021997), #b7d86492-a9c9-43fd-bf07-5bd35196ce10-2_C-Village
    ACTLocationData('Clotheclaw (Expired Grove Village - Upside Down Village)', 'Expired Grove - Village', 483021999), #37b6c80a-20cc-4a2d-ba70-5e755ee13620-2_C-Village
    ACTLocationData('Clothesclaw (Expired Grove Village - Dock Fishing Spot 3)', 'Expired Grove - Village', 483022011), #b5f18ebb-b325-4b01-802c-8aac4a902cf0-2_C-Village
    ACTLocationData('Hairclaw (Expired Grove Village - Dock Fishing Spot 4)', 'Expired Grove - Village', 483022012), #26975cc9-71ac-4f09-a523-99331c45a6ae-2_C-Village
    ACTLocationData('Clothesclaw (Expired Grove Village - Hidden Fishing on Topoda Path)', 'Expired Grove - Village', 483022014), #3bd305d9-8d6b-43c4-99c7-1f2be904de06-2_E-Cliffs
    ACTLocationData('Carclaw (Expired Grove Village - In Topoda Arena)', 'Expired Grove - Village', 483022015), #2601baa3-999e-443b-ae33-ea619346413b-2_E-Cliffs

    ACTLocationData('Chipclaw (Flotsam Vale - Sheet Metal Near Main Entrance)', 'Flotsam Vale', 483022040),#2f65dc9d-5ea6-4480-b8fb-c9a9bcd779d6-2_B-LowSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Beach North of Main Entrance)', 'Flotsam Vale', 483022041), #39365f04-a3c8-44e8-a398-bff99a84d2a7-2_B-LowSwamp
    ACTLocationData('Breadclaw (Flotsam Vale - Gunk North of main Entrance)', 'Flotsam Vale', 483022042), #d0f6546a-c86e-4b9d-aa13-b45ce26abbba-2_B-LowSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Butane Tank Island East of Main Entrance)', 'Flotsam Vale', 483022045), #fbc91e55-5d3e-4c76-8566-458a9f3d1b20-2_B-LowSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Butane Tank Island East of Main Entrance)', 'Flotsam Vale', 483022047), #ee9133b1-c508-41d7-8a7d-0b19241e4ccf-2_B-LowSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Small Alcove Northeast of Main Entrance)', 'Flotsam Vale', 483022051), #6aa68025-641d-4fd7-a43b-7c0f3ccf4da4-2_B-LowSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Cave Path to Upper Flotsam Vale)', 'Flotsam Vale', 483022052), #06b1bae1-7bf1-4b78-97f7-82ac6d6de47f-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Cave Path to Upper Flotsam Vale)', 'Flotsam Vale', 483022053), #282e7092-dc21-45f0-805d-78ea29dfb0bd-2_A-HighSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Upper Flotsam Vale Near Snail Shell)', 'Flotsam Vale', 483022055), #99e59ba9-3c41-4133-bf7e-d09bc1957f04-2_A-HighSwamp
    ACTLocationData('Breadclaw (Flotsam Vale - Wooden Platform Above Sludge Steamroller)', 'Flotsam Vale', 483022059), #36d0180d-dfa2-49be-b5f0-9b65c5f05d7a-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Wooden Platform Above Sludge Steamroller)', 'Flotsam Vale', 483022061), #2546c006-fb9c-412e-99da-e1533b6c388e-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Wooden Platform Above Sludge Steamroller)', 'Flotsam Vale', 483022065), #19644b3e-d9b8-4cae-be53-7c2cae5a5ac8-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Trash Pile Near Sludge Steamroller)', 'Flotsam Vale', 483022066), #00718126-9001-4bba-980c-e1d20298a13e-2_A-HighSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Butane Tank South of Sludge Steamroller)', 'Flotsam Vale', 483022069), #cd5c1ed2-6f66-4d40-a23e-a4099f7890b1-2_A-HighSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Butane Tanks West of Sludge Steamroller)', 'Flotsam Vale', 483022073), #b361630f-a4b5-46fd-8bb3-faa583d0aa3b-2_A-HighSwamp
    ACTLocationData('Breadclaw (Flotsam Vale - Next to Crane Switch)', 'Flotsam Vale', 483022074), #cc22f484-88bf-4a0a-bf32-d5aa0d17ed32-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Butane Tanks Southwest of Mailbox)', 'Flotsam Vale', 483022076), #39e6038f-740f-4e90-acf5-2f1125ae318b-2_A-HighSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Elevated Platform Southwest of Mailbox)', 'Flotsam Vale', 483022080), #0696b1bf-ecc4-41c3-84fe-df54a0fcbccf-2_B-LowSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Air Pocket Cave Underwater 1)', 'Flotsam Vale', 483022081), #3190747b-d224-4e01-874f-3dbbac197adc-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Air Pocket Cave Above Water 1)', 'Flotsam Vale', 483022083), #ad3bbd24-6760-4afc-b988-40943e6f331f-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Air Pocket Cave Underwater 1)', 'Flotsam Vale', 483022084), #1704b510-b12f-4156-b688-e82cb02bd933-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Air Pocket Cave Underwater 2)', 'Flotsam Vale', 483022086), #6adbf701-160e-4112-a275-223bffeffb01-2_A-HighSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Air Pocket Cave Underwater 2)', 'Flotsam Vale', 483022088), #3e57df65-8b77-4402-b23e-b1eb7012e88c-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Air Pocket Cave Above Water)', 'Flotsam Vale', 483022089), #5c219ab5-99f1-4b63-88d0-684a6c5d68aa-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Air Pocket Cave Above Water 2)', 'Flotsam Vale', 483022094), #2112465c-60b4-423a-8bb7-301a64aec108-2_A-HighSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Under Shipping Port Dock)', 'Flotsam Vale', 483022100), #771c0772-2715-42c1-90b1-e033997895d1-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Trash Pile Past Shipping Dock)', 'Flotsam Vale', 483022101), #3ef191f5-0296-4760-b9ef-8d2fa99ac914-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Top of Cage Before Consortium)', 'Flotsam Vale - Consortium Arena', 483022104), #9d34e68d-94a3-417c-a919-ddaf13b1c257-2_B-LowSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Behind License Plate Billboard by Scuttleport)', 'Flotsam Vale', 483022106), #92744ee7-94a9-4abf-a3e2-93d91b82d02f-2_A-HighSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Past Consortium)', 'Flotsam Vale - Consortium Arena', 483022109), #ececfd87-e180-425f-9aaa-3a569bbfb5ea-2_B-LowSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - North Gunk Lake Fishing)', 'Flotsam Vale', 483022115), #98e712ca-a037-4b20-81b6-e18d8221581a-2_B-LowSwamp
    ACTLocationData('Breadclaw (Flotsam Vale - West Gunk Lake Fishing Near Shore)', 'Flotsam Vale', 483022117), #2cd9c105-6c9e-4225-92d0-68a3d9488a4c-2_B-LowSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - North Gunk Lake Fishing Near Shore)', 'Flotsam Vale', 483022118), #d4dcf093-3098-419f-83c6-72a4d0626cc3-2_B-LowSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Gunk Lake Fishing South of Sludge Steamroller)', 'Flotsam Vale', 483022119), #4cce8eec-cc51-43c3-b629-768b62a16314-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Gunk Lake Fishing Outside Air Pocket Cave)', 'Flotsam Vale', 483022122), #df4a99c6-a331-4b68-8ab3-33840fa40519-2_A-HighSwamp
    ACTLocationData('Chipclaw (Flotsam Vale - Fishing Past Consortium)', 'Flotsam Vale - Consortium Arena', 483022123), #2fd08de6-99fb-45f8-95e3-d32832180314-2_B-LowSwamp
    ACTLocationData('Paperclaw (Flotsam Vale - Near Upper Flotsam Vale)', 'Flotsam Vale', 483022306), #99e59ba9-3c41-4133-bf7e-d09bc1957f04-2_A-HighSwamp
    ACTLocationData('Breadclaw (Flotsam Vale - Gunk Fishing on Docks)', 'Flotsam Vale', 483022308), #669e8494-68f1-4de8-8814-6b41a0a69d18-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Flotsam Vale - Gunk Fishing on Docks)', 'Flotsam Vale', 483022310), #b4a9c83a-b0c6-4606-a785-16f4ff33d66e-2_A-HighSwamp
    ACTLocationData('Hairclaw (Flotsam Vale - Gunk Fishing Near Bridge)', 'Flotsam Vale', 483022314), #6db7743b-1b30-49c4-983a-bb8256959022-2_A-HighSwamp
    ACTLocationData('Chipclaw (Scuttleport - Gunk Fishing Under Middle Tower)', 'Scuttleport', 483022315), #adbf6e36-d142-458d-a2a4-3406168e3a12-2_C-Facilities

    ACTLocationData('Breadclaw (Scuttleport - Cubby in First Room)', 'Scuttleport', 483022124), #b5875ab1-4e89-4ba5-a9ea-6eca950d51f0-2_A-HighSwamp
    ACTLocationData('Clothesclaw (Scuttleport - Cubby in First Room)', 'Scuttleport', 483022125), #8f06cd49-3b2b-4883-b7a5-a421b38870ba-2_A-HighSwamp
    ACTLocationData('Hairclaw (Scuttleport - Between Cubbies in First Room)', 'Scuttleport', 483022126), #5c795be7-e38a-4986-bcfb-b72ea7e98787-2_A-HighSwamp
    ACTLocationData('Breadclaw (Scuttleport - On Grate Left of Firt Room)', 'Scuttleport', 483022131), #e5906936-1a8c-4f6e-8280-1be9d7f6f403-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - After First Magnet)', 'Scuttleport', 483022135), #62ab5a16-8e1f-411b-91d9-c71b45cd449e-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - Next to Electric Long-Legged Crab)', 'Scuttleport', 483022136), #12994a0d-c89b-4780-aaa9-48bf996c9348-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - Trash Island Under Second Magnet Dropoff)', 'Scuttleport', 483022146), #28baa847-9008-40e5-89b7-566612ca75f5-2_C-Facilities
    ACTLocationData('Paperclaw (Scuttleport - Elevator Under Second Magnet Dropoff)', 'Scuttleport', 483022147), #c2d88bae-4763-4c16-b79e-802f00a519a7-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - Near Edge of First Rooftop)', 'Scuttleport', 483022149), #7b5d1b34-3a32-45a5-9c39-77f389e19658-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - Between Trash Blocks on First Rooftop)', 'Scuttleport', 483022150), #3491a71f-e680-4455-b86c-16c4b46fd9e4-2_C-Facilities
    ACTLocationData("Hairclaw (Scuttleport - Edge of Survivor's Camp Rooftop)", 'Scuttleport', 483022152), #5ef755f7-50bb-423c-92b2-03455f92fd13-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - On Balcony Next to NPC Crab)', 'Scuttleport', 483022154), #f94ca676-2e0f-4ca1-acbf-06c327b51480-2_C-Facilities
    ACTLocationData("Chipclaw (Scuttleport - Inside Survivor's Camp Building)", 'Scuttleport', 483022157), #acec02a3-4585-4671-bab2-787caa9cf456-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - Mag-Rail Platform Building 1)', 'Scuttleport', 483022161), #12ff423d-092a-4b8f-a25e-c25ba1b6c1b1-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - Mag-Rail Platform Building 2)', 'Scuttleport', 483022162), #f6a613bf-a9e8-4561-86e6-7cb491a5796e-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - Mag-Rail Platform Building Rooftop 1)', 'Scuttleport', 483022163), #fdf786b1-912d-4d21-94a2-4b537df8a3a8-2_C-Facilities
    ACTLocationData('Paperclaw (Scuttleport - Trashblocks on Mag-Rail Building Platform Builing Rooftop)', 'Scuttleport', 483022166), #35fbece2-5d6b-40c1-b971-ede62272a563-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - Mag-Rail Platform Building Rooftop 2)', 'Scuttleport', 483022167), #7b3d0a88-815a-453b-95bb-ba41d5c06e46-2_C-Facilities
    ACTLocationData('Chipclaw (Scuttleport - Mag-Rail Platform Building Rooftop)', 'Scuttleport', 483022168), #f8892e4f-5b3e-4d02-9408-d061c129361e-2_C-Facilities
    ACTLocationData('Hairclaw (Scuttleport - Mag-Rail Platform Building)', 'Scuttleport', 483022172), #13b3ad68-84d2-408e-89ee-925827c3fca5-2_C-Facilities
    ACTLocationData('Chipclaw (Scuttleport - Inside Propane Tank Bridge)', 'Scuttleport', 483022173), #173d1895-0c4d-479c-9c1f-0b4e28ce8c76-2_C-Facilities
    ACTLocationData('Clothesclaw (Scuttleport - Inside Propane Tank Bridge)', 'Scuttleport', 483022175), #07d78994-2181-4def-b0ee-6a2c5a018757-2_C-Facilities

    ACTLocationData('Paperclaw (Pinbarge)', 'Pinbarge', 483022186), #fef13a6e-bf0d-4814-a8f5-965fb9c2cd31-2_A-PinBargeRunup
    ACTLocationData('Stapleclaw (Pinbarge)', 'Pinbarge', 483022188), #cc630ad8-cb67-4a50-9e84-2c04c0cc3e16-1_A-PinBargeRunup

    ACTLocationData('Stapleclaw (The Unfathom - Clam on Path to The East)', 'The Unfathom', 483022195), #5b51f2af-33e2-4ba2-a4f9-579e56decfbb-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Under the VCR)', 'The Unfathom', 483022197), #bc5df0c3-4f73-41a8-b348-eff29a1bcc15-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Clam Past Red Glowstick)', 'The Unfathom', 483022198), #bcfe64d6-10e9-4075-aa14-a694a798c76b-2_B-DarkCanyon
    ACTLocationData('Clothesclaw (The Unfathom - Cassette Tape Near Nemma Shortcut)', 'The Unfathom', 483022199), #163d1846-c7fb-4af8-b5b6-9100a5572f57-2_B-DarkCanyon
    ACTLocationData('Clothesclaw (The Unfathom - Nearby Pinbarge Shipwreck 1)', 'The Unfathom', 483022200), #f1ae9c92-60d7-40f1-8018-5041e0943cd7-2_B-DarkCanyon
    ACTLocationData('Clothesclaw (The Unfathom - Nearby Pinbarge Shipwreck 2)', 'The Unfathom', 483022201), #619e7f2e-dacb-459a-b942-3b3f9d3981cf-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Nearby Pinbarge Shipwreck)', 'The Unfathom', 483022202), #434f4643-5f2e-4e5a-810d-280840846d29-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Next to Second Shortcut)', 'The Unfathom', 483022206), #28d4bed3-bba1-43f5-a620-83c4dd4e14f1-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Next to Glowstick Northeast of Pinbarge)', 'The Unfathom', 483022208), #aaa567ea-297b-47ad-8402-8c0d57d10974-2_B-DarkCanyon
    ACTLocationData('Paperclaw (The Unfathom - Ledge Far Northeast of Pinbarge)', 'The Unfathom', 483022211), #b30c36b2-9a59-4dca-9d9b-f851f91070b8-2_B-DarkCanyon
    ACTLocationData('Clothesclaw (The Unfathom - Ledge North of Second Shortcut)', 'The Unfathom', 483022213), #d8080e8e-5cbc-4baf-acad-7e71091ccf3e-2_B-DarkCanyon
    ACTLocationData('Chipclaw (The Unfathom - Hill North of Second Shortcut)', 'The Unfathom', 483022214), #8b5392a6-4839-4960-858f-d5bddbb23381-2_B-DarkCanyon
    ACTLocationData('Hairclaw (The Unfathom - North of Second Shortcut)', 'The Unfathom', 483022215), #b2d86f0b-884e-4793-b9bd-39923f22205c-2_B-DarkCanyon
    ACTLocationData('Hairclaw (The Unfathom - Styrofoam North of Second Shortcut)', 'The Unfathom', 483022216), #501f2b1a-2dbe-4082-b537-ccf1f06c9d80-2_B-DarkCanyon

    ACTLocationData('Clothesclaw (Abyssal Plains - Near Entrance)', 'Abyssal Plains', 483022221), #ae92760b-940b-4925-a369-4112351781c7-2_D-SilentFlats
    ACTLocationData('Hairclaw (Abyssal Plains - North of Entrance)', 'Abyssal Plains', 483022222), #f045426f-2bb7-43d7-8ae9-45d5bd73b3a2-2_D-SilentFlats
    ACTLocationData('Hairclaw (Abyssal Plains - Near Shortcut)', 'Abyssal Plains', 483022224), #3c128651-7160-4ff8-9aaa-20f4fe9fa6ef-2_D-SilentFlats
    ACTLocationData('Stapleclaw (Abyssal Plains - Fishing Southeast of Shortcut)', 'Abyssal Plains', 483022237), #0fd36d2d-dbac-4284-b471-918f407d09aa-2_D-SilentFlats
    ACTLocationData('Stapleclaw (Abyssal Plains - North of Second CD)', 'Abyssal Plains', 483022318), #7b97c71e-bc63-4156-8077-851252c7383e-2_B-DarkCanyon

    ACTLocationData('Paperclaw (The Old Ocean - Styrofoam House North of Snail Shell)', 'The Old Ocean', 483022238), #451aaccb-f207-46fb-a1e0-87005f600a1d-2_A-BleachedCopse
    ACTLocationData('Hairclaw (The Old Ocean - Styrofoam House North of Snail Shell)', 'The Old Ocean', 483022239), #765182cb-9f6e-440c-8c71-b03fe998ea0e-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - Near Shortcut Along Main Path)', 'The Old Ocean', 483022240), #a003f790-11cb-4419-ac30-ec447187a2d0-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - Styrofoam House on Second Island)', 'The Old Ocean', 483022243), #29006be3-6d62-41f8-82aa-e44c906fcfa9-2_A-BleachedCopse
    ACTLocationData('Clothesclaw (The Old Ocean - Area Below First Bubble Jumps)', 'The Old Ocean', 483022246), #2a05d9c1-b7e2-4e2a-87b1-dac4ed775b8e-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - Near Large Shortcut)', 'The Old Ocean', 483022247), #db268ee6-76ac-4537-9c02-1996c291ff10-2_A-BleachedCopse
    ACTLocationData('Hairclaw (The Old Ocean - Near Large Shortcut)', 'The Old Ocean', 483022248), #12b952dd-aee3-4fec-b128-04636cf935a6-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - Styrofoam House South of Second Island)', 'The Old Ocean', 483022249), #dd859464-428d-44f7-a81f-a85ac671fe6f-2_A-BleachedCopse
    ACTLocationData('Carclaw (The Old Ocean - Clam Middle of Second Island)', 'The Old Ocean', 483022253), #560a19c0-374c-4c50-8ebf-ceaf556ac7b7-2_A-BleachedCopse
    ACTLocationData('Stapleclaw (The Old Ocean - On Broken Bridge to City)', 'The Old Ocean', 483022255), #e3c6fc65-0df9-4cba-98e2-14c698aa7a78-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - Upper Floor of House Near Cork)', 'The Old Ocean',483022324), #1a2f542b-c84a-45d2-9c5d-192bf49123b3-2_A-BleachedCopse
    ACTLocationData('Paperclaw (The Old Ocean - On Ledge by Scour Crab)', 'The Old Ocean', 483022258), #216137c4-ed27-4bc7-89fd-0818f0b5ce89-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - North of City Entrance)', 'The Old Ocean', 483022259), #e9e60f3d-0c0f-4481-ad22-827a32d9987e-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - Near City Entrance)', 'The Old Ocean', 483022260), #674cd75e-e914-4d6d-9bc3-9ead6219f833-2_B-GrandCourtyard
    ACTLocationData('Paperclaw (The Old Ocean - North of City Entrance)', 'The Old Ocean', 483022262), #aa69aafa-0b32-451d-9e5c-b8b0c8be14ff-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - Platform Past City Gates Snail Shell)', 'The Old Ocean', 483022266), #229063ed-5a23-4126-8b6e-ef7ade57e7b8-2_B-GrandCourtyard
    ACTLocationData('Paperclaw (The Old Ocean - Platform Past City Gates Snail Shell)', 'The Old Ocean', 483022267), #7596158d-e76e-4bdb-8e09-7739c73eeb3c-2_B-GrandCourtyard
    ACTLocationData('Clothesclaw (The Old Ocean - Southeast of City Gates Snail Shell)', 'The Old Ocean', 483022269), #9a975590-ea4b-4459-bb26-0df4a8cf6cc0-2_B-GrandCourtyard
    ACTLocationData('Clothesclaw (The Old Ocean - Ledge Near Seafoam Cans)', 'The Old Ocean', 483022274), #6b6e67f0-0d83-4a15-b8b7-30c7627bd0aa-2_B-GrandCourtyard
    ACTLocationData('Carclaw (The Old Ocean - Clam Near Seafoam Cans)', 'The Old Ocean', 483022275), #daa4bd21-8cec-4f2a-b259-35635c01c2f4-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - On Ledge Inside Broken Shell)', 'The Old Ocean', 483022277), #c1520c0d-eed7-4798-a341-f60dc1b99bf3-2_B-GrandCourtyard
    ACTLocationData('Breadclaw (The Old Ocean - Inside Teeth Trap in Hallway)', 'The Old Ocean', 483022278), #66972460-b506-45ca-86bb-c22ecf939ad2-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - Drop Down to Wooden Planks)', 'The Old Ocean', 483022280), #a2b25b1c-e993-4087-b8ae-fb6a35c6dd0e-2_B-GrandCourtyard
    ACTLocationData('Carclaw (The Old Ocean - Top of Building Behind Scour Crab)', 'The Old Ocean', 483022283), #48b919ed-4365-4459-b36b-faff6e0e3b77-2_B-GrandCourtyard
    ACTLocationData('Paperclaw (The Old Ocean - East of Snail Shell)', 'The Old Ocean', 483022285), #9d3c9660-ef88-475b-a2bf-b9af0b80ea43-2_B-GrandCourtyard
    ACTLocationData('Hairclaw (The Old Ocean - Floating Platform Next to Scour Crab)', 'The Old Ocean', 483022286), #9e62672b-4805-4b2b-8f23-914860ea4d5b-2_B-GrandCourtyard
    ACTLocationData('Paperclaw (The Old Ocean - Small Ledge Near Scour Crab)', 'The Old Ocean', 483022287), #3ab90ce5-fc9e-435e-b122-39684cc92962-2_B-GrandCourtyard
    ACTLocationData('Stapleclaw (The Old Ocean - Staircase Up to Long Parkour)', 'The Old Ocean', 483022289), #e815e31b-ec45-4f8b-8a67-fd469cb69dff-2_B-GrandCourtyard
    ACTLocationData('Stapleclaw (The Old Ocean - Drop Down in Middle Building)', 'The Old Ocean', 483022290), #9ef9ab02-0e47-455b-9b29-4e1cadcd2770-2_B-GrandCourtyard
    ACTLocationData('Carclaw (The Old Ocean - Outside Eastern Building)', 'The Old Ocean', 483022294), #467682ed-a7cd-4943-a524-07d75ef9fa0e-2_B-GrandCourtyard
    ACTLocationData("Carclaw (The Old Ocean - Outside Camtscha's Arena)", 'The Old Ocean', 483022296), #1cd3a773-d93a-43be-8b14-cb94ab1ae794-2_B-GrandCourtyard
    ACTLocationData('Stapleclaw (The Old Ocean - Ledge Outside Eastern Building)', 'The Old Ocean', 483022297), #6ab4d5f2-16d8-4212-b86b-4592e30ebb5e-2_B-GrandCourtyard
    ACTLocationData("Carclaw (The Old Ocean - Pathway to Camtscha's Arena)", 'The Old Ocean', 483022298), #0aec05f7-d626-4371-9faf-d24e89dc997e-2_B-GrandCourtyard
    ACTLocationData('Stapleclaw (The Old Ocean - Large Staircase in Front of Camtscha Arena)', 'The Old Ocean', 4830212299), #80bee4b6-92f0-4180-a7c1-090fe510d32d-2_B-GrandCourtyard
    ACTLocationData('Carclaw (The Old Ocean - Clam in Middle Building)', 'The Old Ocean', 4830212303), #d2452d82-3625-483d-a93e-401ce4745bbb-2_B-GrandCourtyard

    ##### upgrade item locations
    ACTLocationData('Bloodstar Limb (Central Shallows - Help a Crab)', 'Central Shallows', 483021724), #AUTO NEEDS TO DO QUEST SCRIPT
    ACTLocationData('Bloodstar Limb (Central Shallows - Parkour on Small Islands)', 'Central Shallows', 483021725),#ff9d47b6-7f55-4ad2-a110-e7c4492d87c1-2_B-ShallowsBigSand
    ACTLocationData('Bloodstar Limb (Central Shallows - Ledge Near Red Flip-Flop Bridge)', 'Central Shallows', 483021726),#32fb25ee-9262-4e87-98f9-2e64d369e7ae-2_B-ShallowsBigSand
    ACTLocationData('Bloodstar Limb (Central Shallow - Southwest Sandcastle Clam)', 'Central Shallows', 483021727), #0474f3a7-0eb7-4d3c-b61e-cbb782ceab03-2_B-ShallowsBigSand

    ACTLocationData("Heartkelp Sprout (Moon Snail's Cave - Moon Jelly Elevators)", "Moon Snail's Cave", 483021728), #15a2e4c0-4950-4de0-8b5c-e2b1400f76c1-2_D-MoonSnailShellCave
    ACTLocationData("Bloodstar Limb (Moon Snail's Cave - Just Before Platoon Pathfinder)", "Moon Snail's Cave", 483021729), #00fc94c3-320c-4d0a-a4e0-2b5eccd42d55-2_D-MoonSnailShellCave

    ACTLocationData("Bloodstar Limb (Slacktide - Clam Above Duchess's Chamber)", 'Fort Slacktide - After Destruction', 483021730), #451b4cfb-7176-4103-999f-358b09374e0c-2_B-ShallowsBigSand

    ACTLocationData("Stainless Relic (Reef's Edge - Flat Coral Near Entrance)", "Reef's Edge", 483021764), #d8433d6b-5400-4dec-aad0-032e27babdeb-2_A-NCTradeRoute

    ACTLocationData('Bloodstar Limb (The Sands Between - Cup House in Playground Town near Flotsam)', 'The Sands Between', 483021791), #6801f8fb-6dd9-4129-a182-791a7e66d1c2-2_A-OOGroveRadius
    ACTLocationData('Tackle Pouch (The Sands Between - Cooler on Southern Edge)', 'The Sands Between',483021797), #550401bf-30db-4deb-8267-ac73d522236d-2_A-OOGroveRadius
    ACTLocationData('Bloodstar Limb (The Sands Between - Rocks Southwest of Central Vista)', 'The Sands Between', 483021833), #956ad9a9-5b43-4f18-a7d9-f67f21c50137-2_A-OOGroveRadius
    ACTLocationData('Old World Whorl (The Sands Between - Mantis Block Pitfall North of Central Vista)', 'The Sands Between', 483021843), #8c7fdc4d-423b-4456-8869-56387a4d7665-2_A-OOGroveRadius
    ACTLocationData('Stainless Relic (The Sands Between - On Electric Crab Platform)', 'Southern Town Ridge', 483021845), #83daf909-77d3-4302-858b-6e92fe54fe74-2_A-OOGroveRadius
    ACTLocationData('Tackle Pouch (The Sands Between - Eelectrocute Crab North of Chains)', 'The Sands Between', 483021846), #699b7323-fe71-4bfe-864f-cdd0c9186bbd-2_A-OOGroveRadius
    ACTLocationData('Hearkelp Sprout (The Sands Between - South Eelectrocute Path, Green Coral Side Path)', 'Southern Town Ridge', 483021851), #a7c60b04-8f1b-4833-a6f4-d472e79748c5-2_A-OOGroveRadius

    ACTLocationData('Bloodstar Limb (Post Pagurus - Crab Swarm Near Anchor)', 'The Sands Between - Post Pagurus', 483021869), #29e54e45-4248-4a3d-96bf-ddf5cf6046c7-2_A-OOGroveRadius

    ACTLocationData('Stainless Relic (Secluded Ridge - Plate on Ridge Overlook)', 'Secluded Ridge', 483021886), #c56be461-0e5c-406e-8af0-83021f2f2fb6-2_A-OOGroveRadius
    ACTLocationData('Heartkelp Sprout (Secluded Ridge - End of Eelectrocute Path, Near Bobbit)', 'Secluded Ridge - Past Eelectrocute', 483021888), #d56339c0-fc26-4f53-a289-2c00b6f7ab38-2_A-OOGroveRadius
    ACTLocationData('Old World Whorl (Secluded Ridge - North Cliff Clam)', 'Secluded Ridge', 483021890), #8e381b9e-ab7a-44ad-81c3-19157c97e0c6-2_A-OOGroveRadius
    ACTLocationData('Old World Whorl (Secluded Ridge - Eelectrocute Clam)', 'Secluded Ridge - Past Eelectrocute', 483021905), #80e66e11-8e9a-4896-9db1-f8cd4a25fefc-2_A-OOGroveRadius

    ACTLocationData('Old World Whorl (Expired Grove - South Clam)', 'Expired Grove', 483021917), #e8b4805a-d793-4cd6-943e-bb51b0a6a7dd-2_A-GroveForestLow
    ACTLocationData('Bloodstar Limb (Expired Grove - Behind Gunk Waterfall)', 'Expired Grove', 483021929), #5053f259-8f89-44b2-a64e-6ad48884e569-2_A-GroveForestLow
    ACTLocationData('Heartkelp Sprout (Expired Grove - Top of Shopping Cart Buildings)', 'Expired Grove', 483021961), #7689fa51-f5c8-498f-a842-b302b47f806b-2_A-GroveForestLow

    ACTLocationData('Bloodstar Limb (Expired Grove Village - In Upper South Milk Carton)', 'Expired Grove - Village', 483021995), #ef8017ce-dab2-48d4-864a-7a53ea9a26a7-2_C-Village
    ACTLocationData('Tackle Pouch (Expired Grove Village - Clam Near Cave Shortcut)', 'Expired Grove - Village', 483021998), #c69ffc64-04af-44d1-b470-a867c5f06199-2_D-Caves
    ACTLocationData('Stainless Relic (Expired Grove Village - Clam in Hammer Crab Cave)', 'Expired Grove - Village', 483022007), #269526ef-6bb0-42cf-a93d-e2cac970e424-2_E-Cliffs
    ACTLocationData('Old World Whorl (Expired Grove Village - Post-Topoda Mantis Block)', 'Expired Grove - Village', 483022016), #8b9b3b77-b95f-46a2-adfd-ca962e8f0cef-2_E-Cliffs

    ACTLocationData('Bloodstar Limb (Flotsam Vale - North Submerged Butane Tank)', 'Flotsam Vale', 483022044), #45cca266-a175-4020-9dd7-e0b844421aff-2_B-LowSwamp
    ACTLocationData('Old World Whorl (Flotsam Vale - Cave Path to Upper Flotsam Vale Clam)', 'Flotsam Vale', 483022054), #53cea11a-cfb6-4894-8e18-375ea895caed-2_A-HighSwamp
    ACTLocationData('Old World Whorl (Flotsam Vale - Upper Flotsam Vale Past Snail Shell)', 'Flotsam Vale', 483022057), #32f43e6e-a382-4938-b068-f1eab35a0269-2_A-HighSwamp
    ACTLocationData('Bloodstar Limb (Flotsam Vale - Clam on Crane Platform Near Mailbox)', 'Flotsam Vale - Post Ceviche Sisters', 483022097), #bb7a792d-9933-49ce-93d0-6bf2762cdb69-2_A-HighSwamp
    ACTLocationData('Tacklepouch (Flotsam Vale - Behind Waterfall)', 'Flotsam Vale', 483022103), #b6c01d3a-31e3-457d-b53f-ecf0ff3b7e9f-2_B-LowSwamp

    ACTLocationData('Stainless Relic (Scuttleport - Clam on Left Path After First Magnet)', 'Scuttleport', 483022138), #5b38d7db-b409-4b96-98aa-e1a861365453-2_C-Facilities
    ACTLocationData('Bloodstar Limb (Scuttleport - Clam on Mag-Rail Platform Building Rooftop)', 'Scuttleport', 483022169), #fc60178b-0659-4d17-8360-4e51d468355e-2_C-Facilities
    ACTLocationData('Stainless Relic (Scuttleport - Mag-Rail Platform Building)', 'Scuttleport', 483022170), #7a52c7e5-0f02-4274-90b6-3bcc0b183d61-2_C-Facilities
    ACTLocationData('Stainless Relic (Scuttleport - Building Past Propane Tank Bridge)', 'Scuttleport', 483022181), #77ad1389-a337-45d7-a5e5-d6aa57f6295d-2_C-Facilities
    ACTLocationData("Old World Whorl (Scuttleport - Eelectrocute Room in Survivor's Camp Building)", 'Scuttleport', 483022183), #cb9dc74c-99b9-4a54-81b4-eb9997551ad2-2_C-Facilities

    ACTLocationData('Bloodstar Limb (The Unfathom - Path to The East)', 'The Unfathom', 483022194), #81a413d0-b588-49c7-9210-86d193c7eb6c-2_B-DarkCanyon
    ACTLocationData('Bloodstar Limb (The Unfathom - Past Second Shortcut)', 'The Unfathom', 483022205), #baba3ba3-395a-4547-b060-ddaf0e9fe966-2_B-DarkCanyon

    ACTLocationData('Stainless Relic (Abyssal Plains - Across Bouncy Sponges East of Petroch)', 'Abyssal Plains', 483022218), #e1d2aa11-415c-46c1-8a81-0ab60bb39847-2_C-HermitCave
    ACTLocationData('Stainless Relic (Abyssal Plains - Between Giant Sniper Crabs)', 'Abyssal Plains', 483022220), #f6f1900f-540b-4068-8c1a-7ca8e3f820d9-2_D-SilentFlats
    ACTLocationData('Old World Whorl (Abyssal Plains - Southeast of Shortcut)', 'Abyssal Plains', 483022232), #163cdd5b-be02-42e9-852c-0b657db299d8-2_D-SilentFlats
    ACTLocationData('Bloodstar Limb (Abyssal Plains - Clam in Cave East of Shortcut)', 'Abyssal Plains', 483022234), #214419e5-f322-4971-adaa-6f68e62ea0a9-2_D-SilentFlats
    ACTLocationData('Hearkelp Sprout (Abyssal Plains - Clam East of Petroch)', 'Abyssal Plains', 483022235), #2cb43e11-10dd-49af-8c42-f43ae2742bce-2_C-HermitCave
    ACTLocationData('Tackle Pouch (Abyssal Plains - Across Grapple Hooks by Snail Shell)', 'Abyssal Plains', 483022236), #dac6390a-11b4-411e-9c6e-a406ef5ae503-2_D-SilentFlats

    ACTLocationData('Old World Whorl (The Old Ocean - Clam on Ledge North of Snail Shell)', 'The Old Ocean', 483022241), #66709053-4a7a-4501-9473-f99bc9a250c0-2_A-BleachedCopse
    ACTLocationData('Bloodstar Limb (The Old Ocean - Under Broken Bridge to City)', 'The Old Ocean', 483022256), #d1befb56-8d22-4088-8eb2-a75fb79d112d-2_A-BleachedCopse
    ACTLocationData('Bloodstar Limb (The Old Ocean - Drop Down Southeast of City Gates Snail Shell)', 'The Old Ocean', 483022268), #76bb55d0-f301-42d2-8933-28613fa84d2f-2_B-GrandCourtyard
    ACTLocationData('Stainless Relic (The Old Ocean - Inside City Walls)', 'The Old Ocean', 483022272), #081787e6-513e-4428-847d-618a5a4323dc-2_B-GrandCourtyard
    ACTLocationData('Hearkelp Sprout (The Old Ocean - Clam Past Seafoam Parkour)', 'The Old Ocean', 483022276), #1705f88a-fcd1-4229-928f-61f0e4aca852-2_B-GrandCourtyard
    ACTLocationData('Stainless Relic (The Old Ocean - Clam on Top of Styrofoam Building)', 'The Old Ocean', 483022281), #e8ce25b8-c39a-4892-8573-e390fffc68d9-2_B-GrandCourtyard
    ACTLocationData('Bloodstar Limb (The Old Ocean - Inside Eastern Building)', 'The Old Ocean', 483022293), #c0807176-a8e5-4d89-bded-872bfb4660aa-2_B-GrandCourtyard
    ACTLocationData('Old World Whorl (The Old Ocean - Clam in Eastern Building)', 'The Old Ocean', 483022302), #b373a831-6880-4823-9ba4-c69a72c6e01f-2_B-GrandCourtyard

    ##### consumable item locations
    ACTLocationData("Barbed Hook (Reef's Edge - Under Coral Near Shot Glass Crab)", "Reef's Edge", 483021765), #c44729ce-4c25-4059-8432-212381ca6835-2_A-NCTradeRoute
    ACTLocationData("Barbed Hook (Reef's Edge - Coral Near Two Seahorses)", "Reef's Edge", 483021766), #08434b00-0100-4ea1-8f2a-f1567b84bdf2-2_A-NCTradeRoute
    ACTLocationData("Barbed Hook (Reef's Edge - Near Shortcut)", "Reef's Edge - Items Behind Grapple", 483021769), #2b4849b0-2798-4600-8db1-c5d6bf6952b1-2_A-NCTradeRoute
    ACTLocationData("Barbed Hook (Reef's Edge - North Facing Cliff Near Seahorse)", "Reef's Edge", 483021772), #76ad26b0-4305-498c-8510-4940ad569210-2_A-NCTradeRoute

    ACTLocationData('Barbed Hook (New Carcinia - Top of Building in City Center)', 'New Carcinia', 483021778), #c3b90e59-5289-4ca3-8639-a5c90d656403-2_B-NCCity

    ACTLocationData('Barbed Hook (The Sands Between - Central Vista Near Safety Tube)', 'The Sands Between', 483021788), #6c5631a3-d941-4990-818f-117140982384-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - Pizza Box near Southern Reef)', 'The Sands Between', 483021795), #20b38e81-1198-4905-809a-e42ac4e4759d-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook x3 (The Sands Between - North of Cooler)', 'The Sands Between', 483021798), #74dac1c4-2458-4cca-a280-11e643e610ce-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - Fence Southwest of Cooler)', 'The Sands Between', 483021799), #21b40d22-140c-493c-98e0-218a5ff29c02-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - Top of Spire Near Grove Entrance)', 'The Sands Between', 483021815), #c192eaf1-dd16-459b-a489-376899aabb9b-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - South of Central Vista, Near Fence)', 'The Sands Between', 483021832), #4ebb3072-53e8-4cff-9672-5f82f926035e-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - Base of Bobbit Hill)', 'The Sands Between', 483021834), #90171fe5-d483-4905-a440-a9ab5a7bc074-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - North of Secluded Ridge)', 'The Sands Between', 483021836), #f8b96a25-70ba-492b-bb87-7b51c81d6102-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - South Eelectrocute Path Large Island)', 'Southern Town Ridge', 483021852), #771e0942-ebf4-4938-a7e7-c03ce67f9c16-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (The Sands Between - South Eelectrocute Path Near Shellsplitter)', 'Southern Town Ridge', 483021854), #a53aefd5-fa6f-4675-a1b5-2f9e43f3fed0-2_A-OOGroveRadius

    ACTLocationData('Barbed Hook (Post Pagurus - Near Northeastern Chain)', 'The Sands Between - Post Pagurus', 483021873), #a5c14863-82c3-47d0-b0e1-a67c93da96b8-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - East of Chains)', 'The Sands Between - Post Pagurus', 483021874), #d2cd8afa-4bf2-490e-8542-cb92331800d6-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - Near Preserver East of Chains)', 'The Sands Between - Post Pagurus', 483021875), #b03e7050-778b-4029-ab54-f82207d724fa-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - Rocks North-East of Central Vista)', 'The Sands Between - Post Pagurus', 483021876), #2738d986-20cb-4a09-b6c5-7076a3918283-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - Rocks North-West of Ridge Overlook)', 'The Sands Between - Post Pagurus', 483021877), #a8513df4-5533-4a1e-8fa0-b0423757f162-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - Fence Near North-East Eelectrocute Path)', 'The Sands Between - Post Pagurus', 483021878), #f14d696d-88a4-471e-a512-b5770c3cfbad-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - Near Secluded Ridge Entrance)', 'The Sands Between - Post Pagurus', 483021881), #9ecea6b6-f3db-48f8-a753-6644bbbf1aaf-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - West of Playground)', 'The Sands Between - Post Pagurus', 483021883), #ecea05b3-9908-4b63-b422-d999b78c87e1-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Post Pagurus - South-West of Central Vista)', 'The Sands Between - Post Pagurus', 483021884), #7563f2eb-e052-4107-b787-de2f67a40f2f-2_A-OOGroveRadius

    ACTLocationData('Barbed Hook (Secluded Ridge - Near Secluded Ridge Moon Snail Shell)', 'Secluded Ridge', 483021887), #97a24ab6-20a3-4f21-b0af-55bf243f33f0-2_A-OOGroveRadius
    ACTLocationData('Barbed Hook (Secluded Ridge - Path to Ridge Overlook)', 'Secluded Ridge', 483021892), #d9ee8d70-3493-4e7b-91b3-b42278ff0ad4-2_A-OOGroveRadius
    ACTLocationData('Shark Egg (Secluded Ridge - Broom Spire Peak)', 'Secluded Ridge', 483021912), #dcc6b99e-1d47-481f-86ca-e14a5743f460-2_A-OOGroveRadius

    ACTLocationData('Barbed Hook (Trashbin Plateau - Eelectrocute Grapple Path)', 'Trashbin Plateau', 483021910), #2bccca10-1f27-4762-9a9b-8e628586e0a4-2_A-OOGroveRadius

    ACTLocationData('Barbed Hook (Expired Grove - Next to Sniper Crab)', 'Secluded Ridge', 483021914), #1a0f7d65-c345-4ab2-b447-9a33d5f3acca-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Ledge Near Gunk River)', 'Secluded Ridge', 483021915), #84480f21-e1d7-46d2-9c43-9669ed805a22-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - In Sand Near Gunk River)', 'Secluded Ridge', 483021916), #9b359e06-c812-437d-b03b-175dd8ef77de-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Behind Diseased Lichenthrope)', 'Secluded Ridge', 483021921), #7f4c117f-b387-42cc-a689-8ace39284f5d-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Ledge East of Lichenthrope)', 'Secluded Ridge', 483021922), #dc6c6660-a95a-4587-85cd-cb012292d260-2_A-GroveForestLoww
    ACTLocationData('Barbed Hook (Expired Grove - Crushed Soda Cans)', 'Secluded Ridge', 483021923), #80a22472-1b49-42d0-8ad5-a38ce1c7be8c-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Ledge Across Gunk River)', 'Secluded Ridge', 483021928), #c662e7b9-1f80-4a66-ae70-e0ba31f14a37-2_A-GroveForestLow
    
    ACTLocationData('Barbed Hook (Expired Grove - Ledge After Shopping Cart)', 'Secluded Ridge', 483021935), #dc13eb69-ac98-4de9-9fe0-7f16a03d4ebb-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Bottles on Ledge After Shopping Cart)', 'Secluded Ridge', 483021937), #a5b6f3f6-6e1c-4934-9006-26da6cee47f4-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Paper Plate Near River)', 'Secluded Ridge', 483021941), #776881ba-f61b-4400-8cf5-f11fb11b6f94-2_B-GroveForestHigh
    ACTLocationData('Barbed Hook (Expired Grove - Main Pathway Around Oil Drum)', 'Secluded Ridge', 483021942), #12c73a88-beef-4bfb-a2d1-c159c91d8304-2_B-GroveForestHigh
    ACTLocationData('Barbed Hook  (Expired Grove - Carton Canopy)', 'Expired Grove - Raised Platforms', 483021948), #75b98171-82f1-4559-ac2a-d0a63cccfab2-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Near Top of Oil Drum)', 'Secluded Ridge', 483021950), #3a1e7a2c-5111-4360-b168-cc5e84088b6a-2_B-GroveForestHigh
    ACTLocationData('Barbed Hook (Expired Grove - Shopping Cart Buildings)', 'Expired Grove', 483021959), #bfe46822-3646-4b65-872d-718ab758ab6c-2_A-GroveForestLow
    ACTLocationData('Shark Egg (Expired Grove - Mantis Block on Left Path)', 'Expired Grove', 483021960), #1bace4e0-6ae9-4c89-a583-3d2a9dab800e-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Parkour at Grove Entrance', 'Expired Grove', 4830223620), #9a2f64f8-cba8-41a4-acac-8cc3e6e9583d-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Bottle Near Paper Plate)', 'Expired Grove', 483022322), #6440b99a-9998-4191-961a-32d9f1ecd9e4-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Bottles Over River From Shopping Cart)', 'Expired Grove', 483022323), #f446f24d-71ec-4f13-a6a0-ad5834080de6-2_A-GroveForestLow
    ACTLocationData('Barbed Hook (Expired Grove - Small Connecting Hallway)', 'Expired Grove', 483021931), #cf1311a6-d64c-4d03-b32e-f6440bb9e247-2_A-GroveForestLow

    ACTLocationData('Barbed Hook (Expired Grove Village - In Cave After Heikea)', 'Expired Grove - Village', 483021987), #bcfabbd4-8575-4a6a-8325-7259996a7d68-2_D-Caves
    ACTLocationData('Barbed Hook (Expired Grove Village - Hidden Fishing Near Shopping Cart Mantis Block)', 'Expired Grove - Village', 483021971), #7a38fbf2-47a9-4bf6-85d1-f8d4f58b8d66-2_B-GroveForestHigh
    ACTLocationData('Barbed Hook (Expired Grove Village - River Fishing After Oil Drum)', 'Expired Grove - Village', 483021973), #9c983d04-ac83-40f0-8220-d92f76ea7099-2_B-GroveForestHigh
    ACTLocationData('Barbed Hook (Expired Grove Village - Bottles Before Heikea)', 'Expired Grove - Village', 483021975), #0cf8ca63-6a57-411d-92d5-b476c1446e9b-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - Between Two Crabs)', 'Expired Grove - Village', 483021977), #9614ea8c-152a-4aea-96df-697628c6d639-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - In Center Milk Carton)', 'Expired Grove - Village', 483021978), #d55b82a8-3eb1-4d71-9cc7-75dc837924a9-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - In Center Near Corpse)', 'Expired Grove - Village', 483021979), #a587f40e-b255-4fb5-a1ee-863082e603a4-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - On Center Path)', 'Expired Grove - Village', 483021980), #655d7880-1c82-441f-9929-807cd45187a3-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - In North Milk Carton)', 'Expired Grove - Village', 483021982), #18b63b27-1174-4759-a11f-0a50ef5758e4-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - In South West Milk Carton)', 'Expired Grove - Village', 483021984), #a73325d0-5e3f-49bf-8f45-4c2466073010-2_C-Village
    ACTLocationData('Shark Egg (Expired Grove Village - Near Village Sniper)', 'Expired Grove - Village', 483021985), #db0d1b3f-21fe-4d48-85d0-54d250bfa8a0-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - Under Heikea Boat)', 'Expired Grove - Village', 483021986), #99c33625-2da4-4f69-a0af-8a8d2da3b399-2_D-Caves
    ACTLocationData('Barbed Hook (Expired Grove Village - Butter Carton in Cave)', 'Expired Grove - Village', 483021990), #10eae42f-9cca-447a-8cb8-9cffcba11ecd-2_D-Caves
    ACTLocationData('Barbed Hook (Expired Grove Village - Above Village 1)', 'Expired Grove - Village', 483022001), #b571bdc4-1f34-476e-a4f3-149858da1108-2_C-Village
    ACTLocationData('Barbed Hook (Expired Grove Village - Above Village 2)', 'Expired Grove - Village', 483022002), #0177d8ef-8849-4ea4-b1b3-08a1c3134a99-2_E-Cliffs
    ACTLocationData('Barbed Hook (Expired Grove Village - Above Village 3)', 'Expired Grove - Village', 483022003), #b3a776e1-52ab-4dc8-adc1-55c95eca9972-2_E-Cliffs
    ACTLocationData('Barbed Hook (Expired Grove Village - In Bottle After Ornament Parkour)', 'Expired Grove - Village', 483022004), #ce1700e2-d9d0-462a-af23-cb55828b062a-2_E-Cliffs
    ACTLocationData('Barbed Hook (Expired Grove Village - In Hammer Crab Cave)', 'Expired Grove - Village', 483022005), #235b691b-0f18-4f35-bd8a-7536e12fabfe-2_E-Cliffs
    ACTLocationData('Barbed Hook (Expired Grove Village - Dock Fishing Spot 1)', 'Expired Grove - Village', 483022009), #58571bb7-9503-48c7-a212-01c06bb77296-2_C-Village

    ACTLocationData('Barbed Hook (Flotsam Vale - Ledge Near Main Entrance)', 'Flotsam Vale', 483022038), #17ac32ac-f0fc-4613-9e02-5ffdf4eecb63-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Rocks Near Main Entrance)', 'Flotsam Vale', 483022039), #7aa4931c-e44f-4531-9b5e-eb1a01418fdd-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Beach North of Main Entrance)', 'Flotsam Vale', 483022043), #60c9e9de-af79-4068-a7bf-7005ac760f4b-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Butane Tank Island East of Main Entrance)', 'Flotsam Vale', 483022049), #c3ff376c-5f53-4401-a52a-1515dba2a2a3-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Upper Flotsam Vale Near Snail Shell)', 'Flotsam Vale', 483022056), #2fd87610-e95f-4b28-9521-d3b59fb718f0-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Wooden Deck Above Propane Tank)', 'Flotsam Vale', 483022058), #125b1086-fa58-45bf-a42f-e715781feffa-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Wooden Platform Above Sludge Steamroller 1)', 'Flotsam Vale', 483022062), #cf30643f-5b43-4e94-af5d-c879e6531d14-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Wooden Platform Above Sludge Steamroller 2)', 'Flotsam Vale', 483022064), #ecbaf918-3632-496e-9598-a9e5da91f495-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Butane Tanks South of Sludge Steamroller)', 'Flotsam Vale', 483022070), #0337dc3e-fcf7-4f30-8759-bef7afeb04ca-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Butane Tanks Southwest of Mailbox)', 'Flotsam Vale', 483022078), #90422b9d-ec1b-4be4-a606-54f196dc1f1e-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Air Pocket Cave Underwater 1)', 'Flotsam Vale', 483022085), #442a694b-ba12-4f08-ad49-f2a5697d3c19-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Air Pocket Cave Underwater 2)', 'Flotsam Vale', 483022087), #8480a51d-bd34-43bb-a348-a3bf69040248-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Air Pocket Cave Above Water)', 'Flotsam Vale', 483022091), #54f7c579-6ea7-402d-b1eb-9ee67d2bbe9a-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Behind Shipping Port Snail Shell)', 'Flotsam Vale', 483022098), #1abd8a20-f2cc-488b-8e0a-00b12c305667-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Butane Tank at Shipping Port)', 'Flotsam Vale', 483022099), #a76a0b9b-6307-4b71-be91-da385c17a977-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Trash Pile Past Shipping Dock)', 'Flotsam Vale', 483022102), #a0549711-5560-4b9c-99d5-65e13911413a-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Top of Cage Next to Consortium)', 'Flotsam Vale - Consortium Arena', 483022105), #7e76017e-13fa-4a96-a1f8-6d881b20b372-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - In Front of Consortium)', 'Flotsam Vale - Consortium Arena', 483022108), #b81ed4dc-3b3e-420d-99e9-d676c88fc120-2_B-LowSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Upper Flotsam Vale Fishing Near Snail Shell)', 'Flotsam Vale', 483022113), #cdf2769f-deb3-43dc-841f-a4c1c0081833-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Gunk Lake Fishing West of Sludge Steamroller)', 'Flotsam Vale', 483022120), #698a076c-2661-4731-90c4-211d8b1414c6-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Gunk Fishing Near Dock)', 'Flotsam Vale', 483022311), #3b49cdc6-b609-49b0-a1c2-57307a398920-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Flotsam Vale - Gunk Fishing Near Sludge Steamroller)', 'Flotsam Vale', 483022312), #a6a69a65-21fa-4bdd-8940-e1f1f6c226a0-2_A-HighSwamp

    ACTLocationData('Barbed Hook (Flotsam Vale - Behind Cubby)', 'Scuttleport', 483022305), #5b786881-414b-41d4-97ea-b3a850d3633a-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Scuttleport - Cubby in First Room)', 'Scuttleport', 483022129), #a91e708c-89a8-4ef0-bf21-870cd56e652e-2_A-HighSwamp
    ACTLocationData('Barbed Hook (Scuttleport - Platform Next to First Magnet)', 'Scuttleport', 483022134), #6b8cd4a1-7a84-4148-837a-75369a25511d-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - In Front of Sorting Chamber Snail Shell)', 'Scuttleport', 483022139), #944f517e-6c6b-40f2-88ec-a5490dd08ab0-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Platform Under Second Magnet Dropoff 1)', 'Scuttleport', 483022142), #cb37f39c-6d87-4151-bbc0-11029c60ebbc-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Trash Island Under Second Magnet Dropoff)', 'Scuttleport', 483022145), #931eb344-1b24-4995-947b-4e56674151a5-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Platform Under Second Magnet Dropoff 2)', 'Scuttleport', 483022148), #e2b1726c-2622-4dbc-930b-72e296ec9ceb-2_C-Facilities
    ACTLocationData("Barbed Hook (Scuttleport - Top of Trash Block on Survivor's Camp Rooftop)", 'Scuttleport', 483022153), #75fef681-50e5-4e53-a61e-d2014e9e44f2-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Mag-Rail Platform Building 1)', 'Scuttleport', 483022159), #b757dc2e-1d8b-4263-9718-93d78d86d98b-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Mag-Rail Platform Building 2)', 'Scuttleport', 483022160), #7ab018f0-a203-4746-8ef0-4452cc6b8cd0-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Mag-Rail Platform Building Rooftop)', 'Scuttleport', 483022165), #3ae12d7f-a589-4f70-8d1b-2d445ad8f34e-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Mag-Rail Platform Building 3)', 'Scuttleport', 483022171), #264db2a2-8767-40b3-a9e9-1b87669e7fc0-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Inside Propane Tank Bridge)', 'Scuttleport', 483022174), #ad1f2eed-11dc-4980-be85-139863b3f4e8-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Past Propane Tank Bridge)', 'Scuttleport', 483022176), #085e9638-f3e8-4fee-b725-7879ecbc8b04-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Rooftop Past Propane Tank Bridge 1)', 'Scuttleport', 483022177), #d18b2837-c335-4535-9ce7-e7b9b44af347-2_C-Facilities
    ACTLocationData('Barbed Hook (Scuttleport - Rooftop Past Propane Tank Bridge 2)', 'Scuttleport', 483022178), #095af59b-ebcd-4dc6-87fc-71239d3e2c98-2_C-Facilities
    
    ACTLocationData('Barbed Hook (Pinbarge 1)', 'Pinbarge', 483022185), #8edddc0a-8caf-48a1-975e-4167e728a4c3-1_A-PinBargeRunup
    ACTLocationData('Barbed Hook (Pinbarge 2)', 'Pinbarge', 483022189), #898633d3-36c1-4f61-88b5-8cd4ca33ec2b-2_B-PinBargeArena

    ACTLocationData('Barbed Hook (The Unfathom - Left of First Mimic)', 'The Unfathom', 483022192), #98535001-699c-4e64-a07d-74e610f04528-2_B-DarkCanyon
    ACTLocationData('Barbed Hook (The Unfathom - On a Hill After First Mimic)', 'The Unfathom', 483022193), #54a8f869-ff96-45b2-93de-fb1eeeec313f-2_B-DarkCanyon

    ACTLocationData('Barbed Hook (The Old Ocean - Styrofoam House Northwest of Snail Shell)', 'The Old Ocean', 483022242), #9da554ca-25f7-4f4f-a914-0276899663cc-2_A-BleachedCopse
    ACTLocationData('Barbed Hook (The Old Ocean - Styrofoam House South of Second Island)', 'The Old Ocean', 483022250), #e83d3323-c371-4358-bd76-372285b083ba-2_A-BleachedCopse
    ACTLocationData('Barbed Hook (The Old Ocean - Middle of Second Island)', 'The Old Ocean', 483022252), #0317b352-75a3-4ac5-8f23-f44c5170a5af-2_A-BleachedCopse
    ACTLocationData('Barbed Hook (The Old Ocean - On Broken Bridge to City 1)', 'The Old Ocean', 483022254), #80dadb0e-6347-4c6d-b7e2-bbc8041bed96-2_A-BleachedCopse
    ACTLocationData('Barbed Hook (The Old Ocean - On Broken Bridge to City 2)', 'The Old Ocean', 483022257), #35c3ce0a-a17b-4ca1-b9b5-9b5c32b1a531-2_A-BleachedCopse
    ACTLocationData('Barbed Hook (The Old Ocean - East of City Entrance)', 'The Old Ocean', 483022264), #f94fbed4-a90c-46e8-a6a3-343f81728eba-2_B-GrandCourtyard
    ACTLocationData('Barbed Hook (The Old Ocean - Platform Past City Gates Snail Shell)', 'The Old Ocean', 483022265), #20dffb0a-e6b1-4c00-8f25-d66aefedcc22-2_B-GrandCourtyard
    ACTLocationData('Shark Egg (The Old Ocean - Southeast of City Gates Snail Shell)', 'The Old Ocean', 483022270), #f8ef34b2-f3b7-44d6-84b6-63749adc075f-2_B-GrandCourtyard
    ACTLocationData('Barbed Hook (The Old Ocean - Southeast of Snail Shell Nearby Chitan)', 'The Old Ocean', 483022273), #b2789002-2749-482b-b64e-4cbba29c6a08-2_B-GrandCourtyard
    ACTLocationData('Barbed Hook (The Old Ocean - East of Snail Shell)', 'The Old Ocean', 483022284), #082d38e1-09cc-496a-9909-ffe96cc80cb8-2_B-GrandCourtyard
    ACTLocationData('Barbed Hook (The Old Ocean - Outside Eastern Building)', 'The Old Ocean', 483022291), #824a5720-5565-4804-9838-a674ebd3b1f1-2_B-GrandCourtyard
    ACTLocationData('Barbed Hook (The Old Ocean - Outside Middle Building)', 'The Old Ocean', 483022295), #56826edb-20cf-4f5a-bd85-4c4e71ca3fee-2_B-GrandCourtyard

    ##### stowaway locations
    ACTLocationData('Siphonophore (Central Shallows - Along West Wall)', 'Central Shallows', 483021731),#4d4ac114-06e4-400f-b888-b500a7348cc9-2_B-ShallowsBigSand
    ACTLocationData('Seastar (Central Shallows - East Ledge Behind Comb Crab)', 'Central Shallows', 483021732), #e9a5a6cf-2a19-4db5-bb0d-d85b260f3e2b-2_B-ShallowsBigSand
    ACTLocationData('Sponge (Central Shallows - East Ledge Near Pufferfish)', 'Central Shallows - Items Behind Grapple', 483021733), #95c0077d-518f-4ab7-85e2-ac1e0c1bb0b9-2_B-ShallowsBigSand
    ACTLocationData('Another Crab (Central Shallows - Tall Pillar Near Royal Shellsplitter)', 'Central Shallows', 483021734), #924670c2-839f-4e42-9cf5-8c081b17f946-2_B-ShallowsBigSand
    ACTLocationData('Sand Dollar (Central Shallows - South Arch Wall)', 'Central Shallows', 483021735), #804d3848-3e86-474f-8622-547d020c4cc4-2_B-ShallowsBigSand
    ACTLocationData('Mussel (Central Shallows - Dig Spot Near Southwest Sandcastle)', 'Central Shallows', 483021825), #41a6780e-55a2-4a0a-96a9-bb279a3b1ec3-2_B-ShallowsBigSand
    ACTLocationData('Anemone (Central Shallows - Hidden Fishing on South-Eastern Wall of Castle on South-Western Plateau)', 'Central Shallows', 483021827), #daaa6ab6-8aac-4713-942f-f322e918dd55-2_B-ShallowsBigSand
    ACTLocationData('Razor Blade (Central Shallows - Fishing South West of Slacktide Near Bottles)', 'Central Shallows', 483021828), #728b3da1-5b4b-4a7f-885c-b5ed9abfadbc-2_B-ShallowsBigSand
    ACTLocationData('Anemone [Stowaway] (Central Shallow - Fishing West of Umbrella)', 'Central Shallows', 483021829), #b29c140a-08c2-44c6-81c3-5f91e5621e47-2_B-ShallowsBigSand

    ACTLocationData('Seastar (Slacktide - Top of Fishing Line Room)', 'Fort Slacktide - Before Destruction', 483021737), #35603032-802e-4811-ae95-8e8eb11c1dfa-2_B-ShallowsBigSand
    ACTLocationData('Barnacle (Slacktide - After Big Urchin Spiral Staircase)', 'Fort Slacktide - Before Destruction', 483021738), #98329dde-9889-4cbb-a656-61f83dca2eca-2_B-ShallowsBigSand
    ACTLocationData('Rusty Nail (Slacktide - Big Urchin Staircase Grapple Point)', 'Fort Slacktide - Before Destruction', 483022017), #87e60901-5489-437e-82c2-d70ca2390364-2_B-ShallowsBigSand

    ACTLocationData("Limpet (Moon Snail's Cave - Ride the First Moon Jelly)", "Moon Snail's Cave", 483021739), #c1a31dc1-9ec5-42e9-8dcf-291f7cdc8a26-2_D-MoonSnailShellCave

    ACTLocationData('Mussel (Slacktide - Southwest Fort Entrance)', 'Fort Slacktide - After Destruction', 483021740), #694c4c66-fefc-4539-962f-a343e13b044b-2_C-Slacktide2
    ACTLocationData('Anemone (Slacktide - South Fort Wall)', 'Fort Slacktide - After Destruction', 483021741), #557546a8-096b-49cd-b63b-452fb751a8bf-2_C-Slacktide2
    ACTLocationData('Whelk (Slacktide - Center Castle Turret Top)', 'Fort Slacktide - After Destruction', 483021742), #e1848736-945b-406d-853e-d213f7c80f14-2_C-Slacktide2
    ACTLocationData('Limpet (Slacktide - Stairs Left of Main Hallway)', 'Fort Slacktide - After Destruction', 483021736), #b5e751fb-8ff5-440e-aa9c-9d9c75977be7-2_B-ShallowsBigSand

    ACTLocationData("Seastar (Reef's Edge - Surrounded by Crabs)", "Reef's Edge - Items Behind Grapple", 483021768), #d93f0715-7c15-4f74-b376-34468705093c-2_A-NCTradeRoute
    ACTLocationData("Sea Star+ (Reef's Edge - Top of Large Hammer Crab Pole)", "Reef's Edge", 483021770), #3473ed8f-db06-4bb7-9932-862f92258542-2_A-NCTradeRoute
    ACTLocationData("Whelk+ (Reef's Edge - Near Orange Coral and Sponge)", "Reef's Edge", 483021773), #5e8a3fb6-f3b1-42a0-a8b8-10b57b340138-2_A-NCTradeRoute

    ACTLocationData('Limpet (New Carcinia - Top of Cardboard Buildings Near Entrance)', 'New Carcinia', 483021775), #e7b4c4fc-6208-4326-847e-ee34113f7fe0-2_B-NCCity
    ACTLocationData('Rusty Nail (New Carcinia - On Top of Hammerhead Toolbox)', 'New Carcinia', 483021777), #f2105767-2544-4acc-9703-a47fbe97c3dc-2_B-NCCity

    ACTLocationData('Sand Dollar (New Carcinia - Flat Coral Near/Above Hammerhead)', 'New Carcinia', 483021786), #a1194e18-4659-4ac9-aa73-744a6df42fe3-2_B-NCCity

    ACTLocationData('Phytoplankton (The Sands Between - Central Vista Center Tunnel)', 'The Sands Between', 483021789), #3197c269-c43d-4bff-b388-a6c3d3e4b5f3-2_A-OOGroveRadius
    ACTLocationData('Anemone (The Sands Between - Central Vista Top)', 'The Sands Between', 483021790), #73aec841-ee9a-411b-8919-53eeeb33ec59-2_A-OOGroveRadius
    ACTLocationData('Anemone (The Sands Between - Sinkhole filled with Crabs near Playground Town)', 'The Sands Between', 483021792), #bd3a89be-89f5-4029-ac76-c1966c70299d-2_A-OOGroveRadius
    ACTLocationData('Rusty Nail (The Sands Between - Near Fence and Rock West of Playground Town)', 'The Sands Between', 483021793), #8778ffd7-a95d-4021-bb90-4a116de9894a-2_A-OOGroveRadius
    ACTLocationData('Googly Eye (The Sands Between - Microplastics near Southern Pizza Box)', 'The Sands Between', 483021796), #52821431-a6c7-458a-b54f-d42196919993-2_A-OOGroveRadius
    ACTLocationData('Siphonophore (The Sands Between - Rocks Southwest of Cooler aka Old Pag Quick Kill Spot)', 'The Sands Between', 483021800), #8d4c2499-b344-4e0f-b4e4-dc2a3e7ccf74-2_A-OOGroveRadius
    ACTLocationData('Limpet (The Sands Between - Near Two Bobbit Worms on East Side near Anchor)', 'The Sands Between', 483021801), #1f5bc2e0-a613-4afd-bdf6-5ed4805edf29-2_A-OOGroveRadius
    ACTLocationData('Anemone (The Sands Between - Sinkhole by West Chains)', 'The Sands Between', 483021803), #57559d1c-80ce-4396-afdf-7d7e6af71ff6-2_A-OOGroveRadius
    ACTLocationData("Fredrick (The Sands Between - Fredrick's Grave by West Chains)", 'The Sands Between', 483021804), #6f1f751a-b27c-4eb0-b95c-a89d66dd242a-2_A-OOGroveRadius
    ACTLocationData('Another Crab (The Sands Between - Under Chain on West Side)', 'The Sands Between', 483021805), #03ba104a-efe3-4294-b378-b2aeff7aa9e3-2_A-OOGroveRadius
    ACTLocationData('Mussel (The Sands Between - Rocks Below Anchor on West Side)', 'The Sands Between', 483021810), #a08ac116-549b-4691-8e88-79daf965dff8-2_A-OOGroveRadius
    ACTLocationData('Barnacle (The Sands Between - Rocks Northeast of Central Vista)', 'The Sands Between', 483021813), #234f3d49-7fc5-4039-949f-8d95f38d7c79-2_A-OOGroveRadius
    ACTLocationData('Salp (The Sands Between - Sinkhole near Rocks Northeast of Central Vista)', 'The Sands Between', 483021814), #2dc13e33-724d-41a7-983b-5f3bf010ce89-2_A-OOGroveRadius
    ACTLocationData('Rusty Nail+ (The Sands Between - Mantis Block near Central Vista)', 'The Sands Between', 483021816), #fc6e8558-9515-40a7-9857-9584a196a1ec-2_A-OOGroveRadius
    ACTLocationData('Sea Star+ (The Sands Between - Mantis Block near Flotsam Vale Entrance)', 'The Sands Between', 483021817), #d19ac393-ea1d-4237-9d31-b620c3a2617d-2_A-OOGroveRadius
    ACTLocationData('Sea Slug (The Sands Between - Mantis Block below Crab Rave)', 'The Sands Between', 483021818), #bceed85e-5560-4a77-a498-749af9f76780-2_A-OOGroveRadius
    ACTLocationData('Sea Slug (The Sands Between - Mantis Block below Crab Rave)', 'The Sands Between', 483021819), #63b93466-f406-492e-ac12-f243fe6a8165-2_A-OOGroveRadius
    ACTLocationData('Sinker+ (The Sands Between - Mantis Block North of Secluded Ridge)', 'The Sands Between', 483021841), #a8e01dfb-5dd9-4da0-92b1-39a7b18e8d83-2_A-OOGroveRadius
    ACTLocationData('Limpet+ (The Sands Between - Mantis Block at Grove Entrance)', 'The Sands Between', 483021842), #56e45097-4ffa-41b0-ac56-cdd6c93b5e88-2_A-OOGroveRadius
    ACTLocationData('Lumpsucker+ (The Sands Between - On the anchor, after the electric crab)', 'The Sands Between', 483021844), #859c746b-c52f-4887-aa96-bb19bd7e25dd-2_A-OOGroveRadius
    ACTLocationData('Sinker+ (The Sands Between - South Eelectrocute Path)', 'Southern Town Ridge', 483021848), #ae4a7ac6-5eb0-4590-a3c7-5d5f236a978d-2_A-OOGroveRadius
    ACTLocationData('Mussel+ (The Sands Between - South Eelectrocute Path First Jump)', 'Southern Town Ridge', 483021849), #7111735c-772e-4c1f-b255-183e62760ae2-2_A-OOGroveRadius
    ACTLocationData('Oyster (The Sands Between - South Eelectrocute Path Large Island Ashtray)', 'Southern Town Ridge', 483021853), #2ccd3299-d207-4d4d-b5a5-d777c4e8aa29-2_A-OOGroveRadius
    ACTLocationData('Mussel (The Sands Between - Fishing Near Bobbit Hill)', 'The Sands Between', 483021859), #da5f126f-e470-432c-b5b0-8eca9918ed77-2_A-OOGroveRadius
    ACTLocationData('Barnacle (The Sands Between - Fishing On Bobbit Hill 2nd Layer)', 'The Sands Between', 483021861), #15cf7503-de68-4475-b39c-fe687f85c448-2_A-OOGroveRadius
    ACTLocationData('Whelk++ (The Sands Between - South Eelectrocute Path First Island Peak)', 'The Sands Between', 483021866), #d61a21a2-c27d-45d7-8e11-75fcd11e8b78-2_A-OOGroveRadius
    ACTLocationData('Salp+ (The Sands Between - Eelectrocute Path Near Grove Small Island)', 'The Sands Between - Grapple to East of Grove', 483021867), #7faef89f-c78a-4002-9454-c20bf5098229-2_A-OOGroveRadius
    ACTLocationData('Used Bandage (The Sands Between - Eelectrocute Path Near Grove)', 'The Sands Between - Grapple to East of Grove', 483021868), #3123f8ec-3548-41f5-a777-c10268e06b8b-2_A-OOGroveRadius

    ACTLocationData('Limpet (Secluded Ridge - North Cliff Hidden in Kelp)', 'Secluded Ridge', 483021891), #fcb1f0bb-2ebf-449c-b5fd-ebb7d515c7af-2_A-OOGroveRadius
    ACTLocationData('Sanddollar (Secluded Ridge - Near Broom)', 'Secluded Ridge', 483021894), #42686eee-4b9f-4d44-a52d-569d2c814f13-2_A-OOGroveRadius
    ACTLocationData('Mussel+ (Secluded Ridge - Western Cliff To Go Box)', 'Secluded Ridge', 483021896), #a59b9d02-9711-48e3-8296-e2164c79f1f2-2_A-OOGroveRadius
    ACTLocationData('Siphonophore+ (Secluded Ridge - Pitfall)', 'Secluded Ridge', 483021903), #e2a1e3e1-8ee4-4539-ab81-98c4d6d99630-2_A-OOGroveRadius
    ACTLocationData('Anemone+ (Secluded Ridge - Eelectrocute)', 'Secluded Ridge - Past Eelectrocute', 483021904), #1b6f2070-3ff2-4f48-b061-0a41990013e1-2_A-OOGroveRadius
    ACTLocationData('Cockle (Secluded Ridge - Fishing on Eelectrocute Path)', 'Secluded Ridge - Past Eelectrocute', 483021908), #d32ade52-c34e-4cb7-957c-df605339ee4c-2_A-OOGroveRadius
    ACTLocationData('Bobber (Secluded Ridge - Broom Spire Climb)', 'Secluded Ridge', 483021911), #fc2cf7ed-6ff6-40bb-987a-936da0afa93b-2_A-OOGroveRadius

    ACTLocationData('Cockle (Trashbin Plateau - Peak)', 'Trashbin Plateau', 483021899), #ca4c297f-e9fd-4a78-b89a-811d2394406b-2_A-OOGroveRadius
    ACTLocationData('Sinker (Trashbin Plateau - Peak)', 'Trashbin Plateau', 483021900), #36611427-18cc-45f3-ad50-a51cc02ccb1d-2_A-OOGroveRadius
    ACTLocationData('Small Battery (Trashbin Plateau - Mantis Block)', 'Trashbin Plateau', 483021901), #0d86fe0e-ae41-4fb2-beb2-9bb5e558429a-2_A-OOGroveRadius
    ACTLocationData('Googly Eye (Trashbin Plateau - Pineapple)', 'Trashbin Plateau', 483021902), #7935fe1e-318c-4f90-901b-fa001de6e4dc-2_A-OOGroveRadius

    ACTLocationData('Barnacle (Expired Grove - On Top of Colander)', 'Expired Grove', 483021913), #09fbd30a-ce33-45a9-bffd-8b4f24c35559-2_A-GroveForestLow
    ACTLocationData('Seastar (Expired Grove - East Circular Rock)', 'Expired Grove', 483021918), #f429fad9-bbb8-4eaf-a154-80164a6550c3-2_A-GroveForestLow
    ACTLocationData('Puffer Quill (Expired Grove - Cross Sponge Islands)', 'Expired Grove', 483021920), #36499157-9a63-42c2-b3b2-644546520db0-2_A-GroveForestLow
    ACTLocationData('Limpet (Expired Grove - Soda Can Stepping Stones)', 'Expired Grove', 483021936), #0eed5053e-c3f5-4c95-868b-86d92ba3d9a1-2_A-GroveForestLow
    ACTLocationData('Lumpsucker (Expired Grove - Carton Canopy)', 'Expired Grove - Raised Platforms', 483021947), #d1bd4b15-62ca-4363-94ec-59b9abbff10b-2_A-GroveForestLow
    ACTLocationData('Another Crab (Expired Grove - Beginning of Sniper Path)', 'Expired Grove', 483022319), #8e4714bf-cc7f-4bde-9c88-7fcdbf8d0afe-2_A-GroveForestLow
    ACTLocationData('Shark Tooth (Expired Grove - Under Pizza Box)', 'Expired Grove', 483021951), #8e34f6a5-5844-4767-ab15-4fbaf6c147dc-2_B-GroveForestHigh
    ACTLocationData('Contact Lens (Expired Grove - Behind Shopping Cart Buildings)', 'Expired Grove', 483021962), #ac0843c0-17cd-4af2-a11c-d1d42bd0ccea-2_A-GroveForestLow
    ACTLocationData('Cotton Ball (Expired Grove - Mantis Block on Oil Drum Path)', 'Expired Grove', 483021963), #fa3cfc64-4f87-452c-bf59-4f599cb3f6fa-2_A-GroveForestLow
    ACTLocationData('Mussel (Expired Grove - Fishing by Entrance)', 'Expired Grove', 483021964), #96c16da5-97e3-44db-bca9-8a4990c2707b-2_A-GroveForestLow
    ACTLocationData('Sponge (Expired Grove - Fishing by Crystal Parkour)', 'Expired Grove', 483021965), #a8310c1f-205c-42cf-bcbd-66b0636e8901-2_A-GroveForestLow
    ACTLocationData('Oyster (Expired Grove - River Fishing Under Bridge)', 'Expired Grove', 483021966), #5480f8db-7801-4ca6-bbca-71dd0876785a-2_A-GroveForestLow
    ACTLocationData('Limpet (Expired Grove - River Fishing Before Lichenthrope)', 'Expired Grove', 483021967), #622cbc21-fcd5-44d1-8e95-c6fcaacc2dcb-2_A-GroveForestLow

    ACTLocationData('Anemone (Expired Grove Village - River Fishing Near Cart Mantis Block)', 'Expired Grove - Village', 483021974), #5e81380f-3e8f-4d44-a0ef-ebbad0f23fdb-2_B-GroveForestHigh
    ACTLocationData('Phytoplankton+ (Expired Grove Village - Top of Upside Down village)', 'Expired Grove - Village', 483022000), #5e1cd261-5882-4737-a524-e27b267b61b0-2_C-Village
    ACTLocationData('Wad of Gum (Expired Grove Village - Gum Pile in Hammer Crab Cave)', 'Expired Grove - Village', 483022006), #ab2ba852-edf4-467f-a1f5-1825341b7596-2_E-Cliffs
    ACTLocationData('Anemone (Expired Grove Village - Near Seahorse)', 'Expired Grove - Village', 483022008), #32841813-148d-45f7-8c4e-4464f157200d-2_E-Cliffs
    ACTLocationData('Mussel (Expired Grove Village - Dock Fishing Spot 2)', 'Expired Grove - Village', 483022010), #26a3a961-1a29-4d56-a5b3-5612b84d6241-2_C-Village
    ACTLocationData('Earthworm (Expired Grove Village - Dock Fishing Spot 5)', 'Expired Grove - Village', 483022013), #70ae97d9-a424-4c98-85f4-150815ea3dd2-2_C-Village

    ACTLocationData('Anemone (Flotsam Vale - Butane Tank Island East of Main Entrance)', 'Flotsam Vale', 483022046), #76b9b9ce-875c-4136-a6da-dabdfc70d40e-2_B-LowSwamp
    ACTLocationData('Rusty Nail (Flotsam Vale - In Gunk Under Broken Butane Tank)', 'Flotsam Vale', 483022050), #d656b2e6-15ec-4e24-bebb-94c1ed7f6c30-2_B-LowSwamp
    ACTLocationData('Sinker (Flotsam Vale - Wooden Platform Above Sludge Steamroller)', 'Flotsam Vale', 483022060), #19c7932e-9133-4dbc-bc25-9f71aa29c271-2_A-HighSwamp
    ACTLocationData('Mussel (Flotsam Vale - Wooden Platform Above Sludge Steamroller)', 'Flotsam Vale', 483022063), #e5b02de1-7cb7-4a4d-98a9-369c44302cac-2_A-HighSwamp
    ACTLocationData('Rusty Nail (Flotsam Vale - In Gunk Near Sludge Steamroller)', 'Flotsam Vale', 483022067), #f8d826c0-7319-4f95-ab90-bf28a7218dfb-2_A-HighSwamp
    ACTLocationData('Limpet (Flotsam Vale - Trash Pile Near Sludge Steamroller)', 'Flotsam Vale', 483022068), #855a1efa-0f38-4e6b-a68d-24a991dcac42-2_A-HighSwamp
    ACTLocationData('Barnacle (Flotsam Vale - On Roof Above Sludge Steamroller)', 'Flotsam Vale - Post Ceviche Sisters', 483022307), #9545c7d7-0ea6-457b-ad4d-c744984f0d79-2_A-HighSwamp
    ACTLocationData('Fruit Sticker (Flotsam Vale - Butane Tanks West of Sludge Steamroller)', 'Flotsam Vale', 483022071), #0ad3895d-4612-4856-a6ed-7a7b48f2c36f-2_A-HighSwamp
    ACTLocationData('Sea Cucumber (Flotsam Vale - Butane Tanks West of Sludge Steamroller)', 'Flotsam Vale', 483022072), #5ccf4e25-ff98-4a9a-9e31-2eea57589809-2_A-HighSwamp
    ACTLocationData('Lumpsucker (Flotsam Vale - Ledge Below Shortcut to Map Piece)', 'Flotsam Vale', 483022075), #a569d9f6-d930-4a9b-8041-8eb8621532ac-2_A-HighSwamp
    ACTLocationData('Oyster (Flotsam Vale - Butane Tanks Southwest of Mailbox)', 'Flotsam Vale', 483022077), #235d8af5-0add-4509-b33c-dd3e3dbd27ff-2_A-HighSwamp
    ACTLocationData('Seastar (Flotsam Vale - Butane Tanks Southwest of Mailbox)', 'Flotsam Vale', 483022079), #2f19d3b2-03ae-4fbe-8821-2dd01f007d11-2_A-HighSwamp
    ACTLocationData('Anemone (Flotsam Vale - Air Pocket Cave Underwater)', 'Flotsam Vale', 483022082), #cce99207-a255-4e12-ba19-51b5048ac64b-2_A-HighSwamp
    ACTLocationData('Cockle (Flotsam Vale - Air Pocket Cave Above Water)', 'Flotsam Vale', 483022090), #aeb3f185-eb51-4e68-a0cc-6dafc4b48a11-2_A-HighSwamp
    ACTLocationData('Sand Dollar (Flotsam Vale - Air Pocket Cave Above Water)', 'Flotsam Vale', 483022092), #812367fb-0264-4113-9da5-104ba61d368b-2_A-HighSwamp
    ACTLocationData('Anemone+ (Flotsam Vale - Air Pocket Cave Underwater)', 'Flotsam Vale', 483022093), #35d5823c-2da6-48c4-b8f1-074221917090-2_A-HighSwamp
    ACTLocationData('Another Crab (Flotsam Vale - Clam Leading Up to Mailbox)', 'Flotsam Vale - Post Ceviche Sisters', 483022095), #daf9fa57-89d6-481f-8a6d-c32c9e8ecb5a-2_A-HighSwamp
    ACTLocationData('Sponge (Flotsam Vale - Crane Grapple Up Toward Expired Grove)', 'Flotsam Vale', 483022107), #2cb7f595-94fa-4b7b-a7c6-602808292c48-2_A-HighSwamp
    ACTLocationData('Seastar+ (Flotsam Vale - Submerged Butane Tank Southwest of Sludge Steamroller)', 'Flotsam Vale', 483022110), #89d10f86-fcf2-483a-b145-f1576682520c-2_A-HighSwamp
    ACTLocationData('Lamprey (Flotsam Vale - Small Island Fishing East of Entrance)', 'Flotsam Vale', 483022111), #5a5395f1-e087-4a30-b3ea-b055fd328d40-2_B-LowSwamp
    ACTLocationData('Mussel (Flotsam Vale - Elevated Island Fishing)', 'Flotsam Vale', 483022112), #e863acfd-d4ee-4d2b-a868-6fe2420f1eda-2_B-LowSwamp
    ACTLocationData('Siphonophore+ (Flotsam Vale - Fishing Near Waterfall)', 'Flotsam Vale', 483022114), #491e2dc3-ab0b-4da4-b36d-a3c2e60ea2a3-2_B-LowSwamp
    ACTLocationData('Whelk (Flotsam Vale - West Gunk Lake Fishing)', 'Flotsam Vale', 483022116), #aecd0ac5-352e-4ae3-ae6a-3b810e8588d6-2_B-LowSwamp
    ACTLocationData('Anemone+ (Flotsam Vale - Gunk Lake Fishing Northwest of Sludge Steamroller)', 'Flotsam Vale', 483022121), #f29c22d3-4459-4d21-b76d-dbdd514fe09a-2_A-HighSwamp
    ACTLocationData('Turtle Shell Shard (Flotsam Vale - Gunk Fishing by Priest)', 'Flotsam Vale', 483022309), #584ec079-5ecc-409b-bcac-7197b1d04a1c-2_A-HighSwamp
    ACTLocationData("Lil' Isopod (Flotsam Vale - Gunk Fishing on Docks)", 'Flotsam Vale', 483022313), #6709552a-af26-4b87-a69e-97830fd645be-2_A-HighSwamp
    ACTLocationData('Rusty Nail (Scuttleport - Gunk Fishing Near Blue Tower)', 'Scuttleport', 483022316), #dbcacde0-7803-42c7-8894-026826e23a67-2_C-Facilities
    ACTLocationData('Barnacle (Scuttleport - Gunk Fishing Near Middle Tower)', 'Scuttleport', 483022317), #670ead0c-1985-4d91-a259-3ab2d5162376-2_C-Facilities

    ACTLocationData('Googly Eye (Scuttleport - Top of Cubbies in First Room)', 'Scuttleport', 483022127), #5736e238-67d5-4215-823d-a0c3b3d60b2a-2_A-HighSwamp
    ACTLocationData('Seastar (Scuttleport - Top of Cubbies in First Room)', 'Scuttleport', 483022128), #69c1d4c5-c467-4127-a12a-6277376c47f0-2_A-HighSwamp
    ACTLocationData('Sand Dollar (Scuttleport - Path to First Magnet)', 'Scuttleport', 483022132), #bfa268ed-5df9-410b-a71e-fc8f0f711655-2_C-Facilities
    ACTLocationData('Mussel (Scuttleport - Fishing Next to First Magnet)', 'Scuttleport', 483022133), #3d0db077-a9de-4725-92ac-8c4cd24d3b73-2_C-Facilities
    ACTLocationData('Limpet (Scuttleport - Platform Next to Electrical Boxes)', 'Scuttleport', 483022137), #416129a7-73dc-49db-884e-dd39081c159f-2_C-Facilities
    ACTLocationData('Rubber Band (Scuttleport - Ledge Before Second Magnet Dropoff)', 'Scuttleport', 483022140), #37f09b48-7c2f-447e-9c87-5c29f6d0685f-2_C-Facilities
    ACTLocationData('Limpet (Scuttleport - Path to Left After First Magnet)', 'Scuttleport', 483022141), #09cdcb1f-cb62-4a7c-a9a1-04aba76325c4-2_C-Facilities
    ACTLocationData('Anemone+ (Scuttleport - Platform Under Second Magnet Dropoff)', 'Scuttleport', 483022143), #89d87d3d-1e06-4fd4-8def-17aff3474b11-2_C-Facilities
    ACTLocationData('Lumpsucker (Scuttleport - Trash Island Under Second Magnet Dropoff)', 'Scuttleport', 483022144), #5c2d7cbb-1040-4e43-9aee-fac430ece31d-2_C-Facilities
    ACTLocationData('Sinker++ (Scuttleport - Clam Next to Stationary Magnet)', 'Scuttleport', 483022151), #4f0723b9-506c-4bcd-a86a-817c5394c800-2_C-Facilities
    ACTLocationData("Seastar (Scuttleport - Inside Survivor's Camp Building)", 'Scuttleport', 483022155), #a503e8bd-3fb8-4b51-840b-927469510cdf-2_C-Facilities
    ACTLocationData("Puffer Quill (Scuttleport - Inside Survivor's Camp Building)", 'Scuttleport', 483022156), #060c2ec3-888a-42ad-afd2-e33f45c409a9-2_C-Facilities
    ACTLocationData("Turtle Shell Shard (Scuttleport - Side Platform After Survivor's Camp Magnet)", 'Scuttleport', 483022158), #dc30d0d1-3ea2-4b93-9871-2169630e22ef-2_C-Facilities
    ACTLocationData('Rusty Nail+ (Scuttleport - Mag-Rail Platform Building Rooftop)', 'Scuttleport', 483022164), #f8e6d62e-3276-4643-a0f4-f403be5c6fbb-2_C-Facilities
    ACTLocationData('Barnacle+ (Scuttleport - Rooftop Past Propane Tank Bridge)', 'Scuttleport', 483022179), #30faa811-16e1-433a-977c-d18e5352e0f9-2_C-Facilities
    ACTLocationData('Salp (Scuttleport - Rooftop Past Propane Tank Bridge)', 'Scuttleport', 483022180), #7fe50500-c6e8-4846-a313-b44f426fb6a3-2_C-Facilities
    ACTLocationData('Mussel+ (Scuttleport - Outside Voltai Arena)', 'Scuttleport', 483022182), #5d4e293b-0bc2-489d-8965-f7caba1c762c-2_C-Facilities

    ACTLocationData('Barnacle (Pinbarge)', 'Pinbarge', 483022184), #98b0e1e4-2548-4b28-948d-b3a05147286a-2_A-PinBargeRunup
    ACTLocationData('Mussel+ (Pinbarge)', 'Pinbarge', 483022187), #29dab0bb-a195-47d3-b553-ebc5a4f03154-2_A-PinBargeRunup

    ACTLocationData('Mussel+ (The Unfathom - Next to Telephone by First Mimic)', 'The Unfathom', 483022191), #87b99366-1eb6-4cd3-af8e-a454cc3c0172-2_B-DarkCanyon
    ACTLocationData('Seastar+ (The Unfathom - Past Blue Glowstick)', 'The Unfathom', 483022196), #bf3b5664-5805-403b-af6f-98f4557c532b-2_B-DarkCanyon
    ACTLocationData('Lanternfish (The Unfathom - Styrofoam Box Near Pinbarge Shipwreck)', 'The Unfathom', 483022203), #9de638f7-ee53-4b14-8b12-8880c9a11631-2_B-DarkCanyon
    ACTLocationData('Lamprey+ (The Unfathom - Clam Northeast of Pinbarge)', 'The Unfathom', 483022209), #fa136387-6988-46e4-9915-fc0a6f11ec6a-2_B-DarkCanyon
    ACTLocationData('Limpet (The Unfathom - Ledge Far Northeast of Pinbarge)', 'The Unfathom', 483022210), #ecc7eed3-27e2-4168-8f6e-6733375b7c99-2_B-DarkCanyon
    ACTLocationData('Siphonophore+ (The Unfathom - Ledge North of Second Shortcut)', 'The Unfathom', 483022212), #75e64603-4664-467d-b2d4-579448396fd4-2_B-DarkCanyon
    ACTLocationData('Salp (The Unfathom - Fishing Near Red Glowstick)', 'The Unfathom', 483022217), #e9fe66b6-b7db-492a-9b64-66f19bfda0c1-2_B-DarkCanyon
    ACTLocationData('Barnacle+ (The Unfathom - Fishing Near Pinbarge Shipwreck)', 'The Unfathom', 483022204), #8ed2ebbb-d383-43ab-8530-f3c1cd714763-2_B-DarkCanyon

    ACTLocationData('Sinker+ (Abyssal Plains - Path East of Petroch)', 'Abyssal Plains', 483022219), #41d32998-d9d9-4b64-bedd-23889b575ec4-2_C-HermitCave
    ACTLocationData('Puffer Quill (Abyssal Plains - Southwest of Inkerton Arena)', 'Abyssal Plains', 483022223), #ce72bf4f-67a6-4ce9-b094-08abfd7fb973-2_D-SilentFlats
    ACTLocationData('Rusty Nail+ (Abyssal Plains - Next to Shortcut)', 'Abyssal Plains', 483022225), #a348d1db-7fb6-460a-b327-a09b3effacd9-2_D-SilentFlats
    ACTLocationData('Limpet+ (Abyssal Plains - Southwest of Inkerton Arena)', 'Abyssal Plains', 483022226), #a36e3443-c030-4021-8022-df892e62328b-2_D-SilentFlats
    ACTLocationData('Whelk (Abyssal Plains - Southeast of Shortcut)', 'Abyssal Plains', 483022227), #b3cc9d26-0b24-438b-ba96-084ba135230a-2_D-SilentFlats
    ACTLocationData('Zooplankton+ (Abyssal Plains - East of Shortcut)', 'Abyssal Plains', 483022228), #42a14e36-7015-455e-a2b9-95fc02893e1f-2_D-SilentFlats
    ACTLocationData('Salp+ (Abyssal Plains - Above Entrance)', 'Abyssal Plains', 483022229), #09879ffa-ec2f-4723-b157-6efbef8f364b-2_D-SilentFlats
    ACTLocationData('Another Crab (Abyssal Plains - Clam On Ledge East of Shortcut)', 'Abyssal Plains', 483022230), #689ac44f-d0f2-4c33-9aad-686823303bff-2_D-SilentFlats
    ACTLocationData('Sea Cucumber (Abyssal Plains - North of Entrance)', 'Abyssal Plains', 483022231), #82554ff8-c8f1-42b3-8018-f84f5ec94c55-2_D-SilentFlats
    ACTLocationData('Fruit Sticker (Abyssal Plains - North of Entrance)', 'Abyssal Plains', 483022233), #fda1ad5d-5abb-4351-b682-8e91036ccddd-2_D-SilentFlats

    ACTLocationData('Sand Dollar (The Old Ocean - Ledge North of Second Island)', 'The Old Ocean', 483022244), #7b965ee1-f184-45d5-ac62-0dbc2c6800ac-2_A-BleachedCopse
    ACTLocationData('Barnacle++ (The Old Ocean - Across Styrofoam Block Hooks)', 'The Old Ocean', 483022245), #411d984e-413e-4167-bb8c-c9e52572874e-2_A-BleachedCopse
    ACTLocationData('Seastar++ (The Old Ocean - Clam On Building North of City Entrance)', 'The Old Ocean', 483022261), #6df4f101-e0f2-4147-94e8-54235e8b803f-2_B-GrandCourtyard
    ACTLocationData('Sponge+ (The Old Ocean - North of City Entrance)', 'The Old Ocean', 483022263), #9cd5413b-91c2-421a-92de-8a703922f888-2_B-GrandCourtyard
    ACTLocationData('Sand Dollar (The Old Ocean - Inside City Walls)', 'The Old Ocean', 483022271), #b27f8f08-2a6d-4f78-8ef5-ca01d2b968ef-2_B-GrandCourtyard
    ACTLocationData('Used Bandage+ (The Old Ocean - Drop Off Onto City Wall)', 'The Old Ocean', 483022279), #5988e9dd-dc40-4f00-af63-66da9db0e7b4-2_B-GrandCourtyard
    ACTLocationData('Cockle+ (The Old Ocean - In Building East of Snail Shell)', 'The Old Ocean', 483022282), #3e336fbb-9830-4772-a1b3-55dc039380dd-2_B-GrandCourtyard
    ACTLocationData('Another Crab (The Old Ocean - Under Large Elevator)', 'The Old Ocean', 483022288), #b7757de2-ce70-474e-a332-cef609bdf42f-2_B-GrandCourtyard
    ACTLocationData('Sand Dollar (The Old Ocean - Inside Eastern Building)', 'The Old Ocean', 483022292), #4babc398-17b9-4197-958e-c6bebc12a6c6-2_B-GrandCourtyard
    ACTLocationData('Phytoplankton+ (The Old Ocean - Clam Inside Eastern Building)', 'The Old Ocean', 483022300), #a9ac0a98-889e-4138-a62b-0d59f63af118-2_B-GrandCourtyard
    ACTLocationData('Mussel++ (The Old Ocean - Clam in Secret Area Under Wooden Planks)', 'The Old Ocean', 483022301), #df538a5c-9108-4210-8b9d-89e777116ec4-2_B-GrandCourtyard
    ACTLocationData('Whelk++ (The Old Ocean - Behind Mantis Punch Wall)', 'The Old Ocean', 483022304), #21387127-4e04-4017-bb58-3aafb9537876-2_B-GrandCourtyard
    ACTLocationData('Fruit Sticker+ (The Old Ocean - Beyond Lone House on Floating Island)', 'The Old Ocean', 483022325), #602a241b-4901-4542-bd7b-f5bce8a9e383-2_A-BleachedCopse

    ##### costume locations
    ACTLocationData('Captain Costume (Central Shallows - Near Nephro Spawn)', 'Central Shallows', 483021743), #7c307763-a7b4-4e81-88d6-e1baf1b04608-2_B-ShallowsBigSand
    ACTLocationData('Clown Costume (The Sands Between - Path of the Clown)', 'The Sands Between', 483021840), #cd2d0535-6c06-4530-bf60-afbffc2d5086-2_A-OOGroveRadius
    ACTLocationData('Sunlight Costume (Secluded Ridge - Southern Bonfire)', 'Secluded Ridge', 483021898), #35aa72f2-fa50-4efc-b600-b597382ed877-2_A-OOGroveRadius
    ACTLocationData('Intern Costume (Expired Grove Village - Intern Costume)', 'Expired Grove - Village', 483021996), #57a328a3-94f4-406c-90de-bdcd1be7d69b-2_C-Village
    ACTLocationData('CowFishBoy Costume (Flotsam Vale - Butane Tank Island East of Main Entrance)', 'Flotsam Vale', 483022048), #b1f8794b-d43d-41b9-827a-75bb4c7a57bf-NickGym
    ACTLocationData('Blue-Collar Costume (Scuttleport - Cubby in First Room)', 'Scuttleport', 483022130), #f37cb96e-df05-4aed-b2b5-7d8d5af32483-NickGym
    ACTLocationData('Krillionaire Costume (The Unfathom - Next to Nemma)', 'The Unfathom', 483022190), #c762c7f8-33b6-4701-9f4c-7ad7938a5d11-2_B-DarkCanyon
    ACTLocationData('Exiled Flame Costume (The Unfathom - Path North of Blue Glowstick)', 'The Unfathom', 483022207), #1b7cb531-3a0a-4957-ab59-da5c9f1da705-2_B-DarkCanyon
    ACTLocationData('Dr. Kril Costume (The Old Ocean - Between Pill Bottles)', 'The Old Ocean', 483022251), #ecc223b8-902c-4d66-b01b-24728ccb7d4e-2_A-BleachedCopse

    ##### non-boss adaptation locations
    ACTLocationData('Urchin Toss Adaptation (New Carcinia - Hug Erich Too Much)', 'New Carcinia', 483021785), #AUTO NEEDS TO MAKE A CUSTOM SCRIPT
    ACTLocationData('Bobbit Trap (The Sands Between - Top of the Bobbit Den)', 'The Sands Between', 483021809), #3bb06349-c151-4333-8305-ba0eb7512bc3-2_A-OOGroveRadius

    ##### skill locations
    ACTLocationData('Shelleport Skill (Moon Snail)', "Moon Snail's Cave", 483021954, ["Moon Snail Skills"]),
    ACTLocationData('Skedaddle Skill (Moon Snail)', "Moon Snail's Cave", 483021955, ["Moon Snail Skills"]),
    ACTLocationData('Parry Skill (Moon Snail)', "Moon Snail's Cave", 483022018, ["Moon Snail Skills"]),
    ACTLocationData('Riposte Skill (Moon Snail)', "Moon Snail's Cave", 483022019, ["Moon Snail Skills"]),
    ACTLocationData('Natural Defenses (Moon Snail)', "Moon Snail's Cave", 483022020, ["Moon Snail Skills"]),
    ACTLocationData('Aggravation Skill (Moon Snail)', "Moon Snail's Cave", 483022021, ["Moon Snail Skills"]),
    ACTLocationData('Self-Repair Skill (Moon Snail)', "Moon Snail's Cave", 483022022, ["Moon Snail Skills"]),
    ACTLocationData('Kintsugi Skill (Moon Snail)', "Moon Snail's Cave", 483022023, ["Moon Snail Skills"]),
    ACTLocationData('Skewer Skill (Moon Snail)', "Moon Snail's Cave", 483022024, ["Moon Snail Skills"]),
    ACTLocationData('Plunge Skill (Moon Snail)', "Moon Snail's Cave", 483022025, ["Moon Snail Skills"]),
    ACTLocationData('Scrap Hammer Skill (Moon Snail)', "Moon Snail's Cave", 483022026, ["Moon Snail Skills"]),
    ACTLocationData('Dispatch Skill (Moon Snail)', "Moon Snail's Cave", 483022027, ["Moon Snail Skills"]),
    ACTLocationData('Spearfishing Skill (Moon Snail)', "Moon Snail's Cave", 483022028, ["Moon Snail Skills"]),
    ACTLocationData('Wave Breaker Skill (Moon Snail)', "Moon Snail's Cave", 483022029, ["Moon Snail Skills"]),
    ACTLocationData('Streamline Skill (Moon Snail)', "Moon Snail's Cave", 483022030, ["Moon Snail Skills"]),
    ACTLocationData('Housewarming Skill (Moon Snail)', "Moon Snail's Cave", 483022031, ["Moon Snail Skills"]),
    ACTLocationData('Circle of Life Skill (Moon Snail)', "Moon Snail's Cave", 483022032, ["Moon Snail Skills"]),
    ACTLocationData('Elusive Prey Skill (Moon Snail)', "Moon Snail's Cave", 483022033, ["Moon Snail Skills"]),
    ACTLocationData('Ebb and Flow Skill (Moon Snail)', "Moon Snail's Cave", 483022034, ["Moon Snail Skills"]),
    ACTLocationData('Umami Training 1 Skill (Moon Snail)', "Moon Snail's Cave", 483022035, ["Moon Snail Skills"]),
    ACTLocationData('Umami Training 2 Skill (Moon Snail)', "Moon Snail's Cave", 483022036, ["Moon Snail Skills"]),
    ACTLocationData('Umami Training 3 Skill (Moon Snail)', "Moon Snail's Cave", 483022037, ["Moon Snail Skills"]),
]

shell_locations_data: List[ACTLocationData] = [
    # shell region is the first possible place it could be acquired
    # add a Shell region to the regions.py if a shell can be acquired in multiple regions first.
    ACTLocationData("Soda Can", "Central Shallows", None, ["Shells"]),
    ACTLocationData("Bottle Cap", "Moon Snail's Cave", None, ["Shells"]),
    ACTLocationData("Tin Can", "Fort Slacktide - Before Destruction", None, ["Shells"]),
    ACTLocationData("Shot Glass", "Moon Snail's Cave", None, ["Shells"]),
    ACTLocationData("Banana Peel", "Fort Slacktide - Before Destruction", None, ["Shells"]),
    ACTLocationData("Party Hat", "Moon Snail's Cave", None, ["Shells"]),
    ACTLocationData("Coconut", "Fort Slacktide - Before Destruction", None, ["Shells"]),
    ACTLocationData("Teacup", "Fort Slacktide - After Destruction", None, ["Shells"]),
    ACTLocationData("Sauce Nozzle", "Reef's Edge", None, ["Shells"]),
    ACTLocationData("Thimble", "Reef's Edge - Items Behind Grapple", None, ["Shells"]),
    ACTLocationData("Bebop Cup", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Tennis Ball", "Reef's Edge - Items Behind Grapple", None, ["Shells"]),
    ACTLocationData("F Key", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Mason Jar", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Salt Shaker", "Shell - Salt Shaker", None, ["Shells"]),
    ACTLocationData("Conchiglie", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Bartholomew", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Disco Ball", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Baby Shoe", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Lil' Bro", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Matryoshka Large", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Shuttlecock", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Felix Cube", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Piggy Bank", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Trophy", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Imposter", "New Carcinia", None, ["Shells"]),
    ACTLocationData("Lil' Red Cup", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Wafer Cone", "Expired Grove", None, ["Shells"]),
    ACTLocationData("Yoccult", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Coffee Pod", "Shell - Coffee Pod", None, ["Shells"]),
    ACTLocationData("Egg Shell", "Expired Grove", None, ["Shells"]),
    ACTLocationData("Coffee Mug", "Expired Grove", None, ["Shells"]),
    ACTLocationData("Cascadia Roll", "Expired Grove", None, ["Shells"]),
    ACTLocationData("Ham Tin", "Expired Grove - Village", None, ["Shells"]),
    ACTLocationData("Skull", "Expired Grove - Village", None, ["Shells"]),
    ACTLocationData("Crab Husk", "Expired Grove - Village", None, ["Shells"]),
    ACTLocationData("Legal Brick", "Shell - Legal Brick", None, ["Shells"]),
    ACTLocationData("Spring", "Shell - Spring", None, ["Shells"]),
    ACTLocationData("Shotgun Shell", "Shell - Shotgun Shell", None, ["Shells"]),
    ACTLocationData("Rubber Duck", "Shell - Rubber Duck", None, ["Shells"]),
    ACTLocationData("Boxing Glove", "Flotsam Vale", None, ["Shells"]),
    ACTLocationData("Cardboard Box", "Flotsam Vale", None, ["Shells"]),
    ACTLocationData("Tissue Box", "Flotsam Vale", None, ["Shells"]),
    ACTLocationData("Valve", "The Sands Between", None, ["Shells"]),
    ACTLocationData("Dumptruck", "Scuttleport", None, ["Shells"]),
    ACTLocationData("Ink Cartridge", "Shell - Ink Cartridge", None, ["Shells"]),
    ACTLocationData("Gacha Capsule", "Pinbarge", None, ["Shells"]),
    ACTLocationData("Lightbulb", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Mouse", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Going Under 64", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Sock", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Doll Head", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Service Bell", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Party Popper", "The Unfathom", None, ["Shells"]),
    ACTLocationData("Scrub Aggy", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Dentures", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Pill Bottle", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Detergent Cap", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("UltraSoft", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Champagne Flute", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Dish Scrubber", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Snow Globe", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Knight's Helmet", "The Old Ocean", None, ["Shells"]),
    ACTLocationData("Plug Fuse", "Shell - Plug Fuse", None, ["Shells"])
    #ACTLocationData("Spirit Conch", "Shell - Spirit Conch", None, "Shells"), #has its own location
    #ACTLocationData("Matryoshka Medium", None, None, "Shells"),
    #ACTLocationData("Matryoshka Small", None, None, "Shells"),
    #ACTLocationData("Home", None, None, "Shells"),
    #ACTLocationData("Gun", None, None, "Shells"),
]

location_table: Dict[str, ACTLocationData] = {location_data.name: location_data for location_data in locations_data + shell_locations_data}

def get_location_groups(location_name: str) -> List[str]:
    return location_table[location_name].location_group

shell_locations: List[str] = [name for name, data in location_table.items() if "Shells" in data.location_group]

temp_loc_total: int = 0

location_name_groups: Dict[str, Set[str]] = {}

for loc_name, loc_data in location_table.items():
    if "Shells" not in loc_data.location_group:
        temp_loc_total += 1

    for location_group in loc_data.location_group:
        location_name_groups.setdefault(location_group, set()).add(loc_name)

location_total: int = temp_loc_total