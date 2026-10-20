"""
Pan-India Destinations Benchmark Dataset for AI Travel Planning Agent.
Covers all 28 States of India with curated tourist destinations and attractions.
Clearly labeled as sample benchmark data for academic planning demonstrations.
"""

from typing import Dict, List, Any, Tuple

ALL_28_INDIAN_STATES: Tuple[str, ...] = (
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
)

SAMPLE_DESTINATIONS: Dict[str, Dict[str, Any]] = {
    # -------------------------------------------------------------
    # 1. ANDHRA PRADESH
    # -------------------------------------------------------------
    "Visakhapatnam (Vizag), Andhra Pradesh": {
        "city_code": "VTZ",
        "state": "Andhra Pradesh",
        "tagline": "The City of Destiny - Coastal Hills and Pristine Beaches",
        "description": "Port city nestled between the Eastern Ghats and the Bay of Bengal.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "VTZ_01",
                "name": "INS Kursura Submarine Museum",
                "category": "Culture & Science",
                "entry_fee": 70,
                "duration_hours": 1.5,
                "zone": "Beach Road Corridor",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Decommissioned Russian-built submarine preserved on the sands of RK Beach.",
                "pro_tip": "Visit around 9:00 AM before lines form at the narrow hatch entrance."
            },
            {
                "id": "VTZ_02",
                "name": "Kailasagiri Hilltop Park & Ropeway",
                "category": "Viewpoint & Nature",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Kailasagiri Ridge",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Hilltop park featuring giant Shiva-Parvati statues and sweeping sea views.",
                "pro_tip": "Take the cable car ropeway up for panoramic views of Vizag coastline."
            },
            {
                "id": "VTZ_03",
                "name": "Rushikonda Beach Watersports",
                "category": "Adventure & Nature",
                "entry_fee": 100,
                "duration_hours": 2.5,
                "zone": "Bheemili Coastal",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "Golden sand beach famed for surfing, sea kayaking, and green hill backdrops.",
                "pro_tip": "Sun protection is essential during noon sessions."
            },
            {
                "id": "VTZ_04",
                "name": "Simhachalam Hilltop Temple",
                "category": "Spiritual & Heritage",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Simhachalam",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "11th-century temple dedicated to Varaha Narasimha with ornate stone carvings.",
                "pro_tip": "Traditional Indian dress code is required for inner sanctum darshan."
            }
        ]
    },
    "Tirupati, Andhra Pradesh": {
        "city_code": "TPT",
        "state": "Andhra Pradesh",
        "tagline": "Spiritual Capital of Andhra - Sacred Seshachalam Hills",
        "description": "One of the most visited pilgrimage destinations on earth.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 240,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "TPT_01",
                "name": "Sri Venkateswara Swamy Temple (Tirumala)",
                "category": "Spiritual",
                "entry_fee": 300,
                "duration_hours": 3.5,
                "zone": "Tirumala Hills",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "World-famous hilltop shrine of Lord Venkateswara (Balaji).",
                "pro_tip": "Pre-book Special Entry Darshan tokens online 60 days in advance."
            },
            {
                "id": "TPT_02",
                "name": "Chandragiri Fort & Light Show",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Chandragiri Valley",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "11th-century fort palace associated with the Vijayanagara Empire.",
                "pro_tip": "Attend the sound-and-light show recounting emperor Krishna Deva Raya."
            },
            {
                "id": "TPT_03",
                "name": "Silathoranam Natural Geological Arch",
                "category": "Nature & Science",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "Tirumala Hills",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Rare pre-Cambrian natural rock formation resembling a serpent's hood.",
                "pro_tip": "Located just 1 km from the main Tirumala temple complex."
            }
        ]
    },

    # -------------------------------------------------------------
    # 2. ARUNACHAL PRADESH
    # -------------------------------------------------------------
    "Tawang, Arunachal Pradesh": {
        "city_code": "TWN",
        "state": "Arunachal Pradesh",
        "tagline": "Land of Dawn-Lit Mountains & Sacred Monasteries",
        "description": "High-altitude Himalayan fortress town perched at 10,000 ft near Tibet border.",
        "avg_intra_zone_transit_cost": 120,
        "avg_inter_zone_transit_cost": 350,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 1.0,
        "attractions": [
            {
                "id": "TWN_01",
                "name": "Tawang Monastery (Galden Namgyal Lhatse)",
                "category": "Heritage & Spiritual",
                "entry_fee": 20,
                "duration_hours": 2.5,
                "zone": "Monastery Ridge",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Second largest Buddhist monastery in the world, founded in 1680.",
                "pro_tip": "Witness morning prayers and butter lamp lighting ceremonies."
            },
            {
                "id": "TWN_02",
                "name": "Sela Pass & Frozen Sela Lake",
                "category": "Nature & Adventure",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Sela Mountain Corridor",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Breathtaking mountain pass at 13,700 ft adorned with Tibetan prayer flags.",
                "pro_tip": "Carry warm thermal windcheaters as icy winds blow throughout the day."
            },
            {
                "id": "TWN_03",
                "name": "Madhuri Lake (Sangetsar Tso)",
                "category": "Nature",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Border Valley",
                "rating": 4.8,
                "preferred_time": "Afternoon",
                "description": "Stunning glacial lake formed by an earthquake with dead pine trunks rising from water.",
                "pro_tip": "Sip piping hot butter tea and momos at the army canteen."
            },
            {
                "id": "TWN_04",
                "name": "Nuranang Falls (Jang Falls)",
                "category": "Nature",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Jang Valley",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Colossal 100-meter roaring white-water cascades surrounded by deodar forest.",
                "pro_tip": "Great stop between Dirang and Tawang."
            }
        ]
    },
    "Ziro Valley, Arunachal Pradesh": {
        "city_code": "ZRO",
        "state": "Arunachal Pradesh",
        "tagline": "UNESCO Cultural Pine Haven - Land of the Apatanis",
        "description": "Pristine highland valley celebrated for unique paddy-cum-pisciculture farming.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 250,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "ZRO_01",
                "name": "Apatani Heritage Village Walk (Hong & Hari)",
                "category": "Culture & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Central Valley",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Traditional bamboo houses and sustainable organic paddy farming terraces.",
                "pro_tip": "Engage a local guide to respectfully learn about ancestral Apatani traditions."
            },
            {
                "id": "ZRO_02",
                "name": "Tarin Fish Farm & Pine Groves",
                "category": "Nature & Science",
                "entry_fee": 20,
                "duration_hours": 1.5,
                "zone": "Tarin Valley",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "High-altitude fish breeding sanctuary bordered by pine trees.",
                "pro_tip": "Walk around the surrounding bamboo orchards."
            },
            {
                "id": "ZRO_03",
                "name": "Kardo Giant Natural Shiva Lingam",
                "category": "Spiritual & Nature",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Kardo Forest",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "25-foot natural monolith discovered inside deep evergreen forests.",
                "pro_tip": "Wear comfortable walking shoes for the forest path."
            }
        ]
    },

    # -------------------------------------------------------------
    # 3. ASSAM
    # -------------------------------------------------------------
    "Kaziranga National Park, Assam": {
        "city_code": "KZR",
        "state": "Assam",
        "tagline": "Sanctuary of the Great Indian One-Horned Rhinoceros",
        "description": "UNESCO World Heritage floodplains bordering the mighty Brahmaputra river.",
        "avg_intra_zone_transit_cost": 150,
        "avg_inter_zone_transit_cost": 400,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.9,
        "attractions": [
            {
                "id": "KZR_01",
                "name": "Kohora Central Range Jeep Safari",
                "category": "Adventure & Nature",
                "entry_fee": 450,
                "duration_hours": 3.0,
                "zone": "Kohora Zone",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Open jeep safari through tall elephant grass to spot rhinos, wild buffalos, and tigers.",
                "pro_tip": "Opt for the earliest morning shift at 7:00 AM for maximum wildlife sightings."
            },
            {
                "id": "KZR_02",
                "name": "Kaziranga National Orchid & Biodiversity Park",
                "category": "Nature & Culture",
                "entry_fee": 120,
                "duration_hours": 2.0,
                "zone": "Durgapur",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Over 500 species of wild Himalayan orchids and Assamese folk dance performances.",
                "pro_tip": "Sample the authentic 30-dish traditional Assamese thali for lunch."
            },
            {
                "id": "KZR_03",
                "name": "Bagori Western Range Safari",
                "category": "Adventure & Nature",
                "entry_fee": 450,
                "duration_hours": 3.0,
                "zone": "Bagori Zone",
                "rating": 4.8,
                "preferred_time": "Evening",
                "description": "Water bodies attracting river otters, migratory birds, and swamp deer.",
                "pro_tip": "Carry binoculars and telephoto lenses."
            }
        ]
    },
    "Guwahati, Assam": {
        "city_code": "GAU",
        "state": "Assam",
        "tagline": "Gateway to the North East - Brahmaputra & Sacred Shrines",
        "description": "Sprawling river metropolis blending ancient tantric temples and tea heritage.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "GAU_01",
                "name": "Maa Kamakhya Shaktipeeth Temple",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Nilachal Hills",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Legendary tantric shrine perched atop Nilachal Hill overlooking the river.",
                "pro_tip": "Expect queue wait times; early morning VIP passes are available."
            },
            {
                "id": "GAU_02",
                "name": "Umananda River Island Temple & Ferry",
                "category": "Spiritual & Nature",
                "entry_fee": 60,
                "duration_hours": 2.0,
                "zone": "Brahmaputra Riverfront",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Smallest inhabited river island in the world, home to golden langurs.",
                "pro_tip": "Catch the inland water transport ferry from Sukreswar Ghat."
            },
            {
                "id": "GAU_03",
                "name": "Brahmaputra Sunset River Cruise",
                "category": "Relaxation & Nature",
                "entry_fee": 400,
                "duration_hours": 1.5,
                "zone": "Brahmaputra Riverfront",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Golden sunset voyage with live folk Bihu music and river breeze.",
                "pro_tip": "Book 5:00 PM slot for unobstructed crimson dusk views."
            }
        ]
    },

    # -------------------------------------------------------------
    # 4. BIHAR
    # -------------------------------------------------------------
    "Bodh Gaya, Bihar": {
        "city_code": "BDG",
        "state": "Bihar",
        "tagline": "The Cradle of Buddhism - Enlightenment & World Peace",
        "description": "The sacred ground where Gautama Buddha attained supreme enlightenment.",
        "avg_intra_zone_transit_cost": 70,
        "avg_inter_zone_transit_cost": 160,
        "transit_time_same_zone_hr": 0.25,
        "transit_time_cross_zone_hr": 0.5,
        "attractions": [
            {
                "id": "BDG_01",
                "name": "Mahabodhi Temple Complex & Sacred Bodhi Tree",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Temple Sanctuary",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "UNESCO World Heritage brick monument and the descendant of the original Bodhi Tree.",
                "pro_tip": "Phones are deposited in lockers; peaceful morning meditation is deeply revitalising."
            },
            {
                "id": "BDG_02",
                "name": "The Great Buddha Statue (80-Foot)",
                "category": "Spiritual & Culture",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "International Monastery Row",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Majestic red granite Buddha meditating on a lotus pedestal in open air.",
                "pro_tip": "Carved by 12,000 skilled stonemasons over seven years."
            },
            {
                "id": "BDG_03",
                "name": "International Buddhist Monasteries Trail",
                "category": "Culture & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "International Monastery Row",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Thai, Japanese, Bhutanese, and Tibetan monasteries showcasing unique native architecture.",
                "pro_tip": "Thai temple features a 24-carat gold leaf Buddha inside."
            }
        ]
    },
    "Nalanda & Rajgir, Bihar": {
        "city_code": "NLN",
        "state": "Bihar",
        "tagline": "Ancient Seat of Universal Learning & Hot Springs",
        "description": "Home to the world's first residential university and capital of the Magadha empire.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 180,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.6,
        "attractions": [
            {
                "id": "NLN_01",
                "name": "Nalanda Mahavihara Ancient Ruins",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Nalanda Heritage Zone",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "5th-century UNESCO World Heritage ruins of the ancient international monastic university.",
                "pro_tip": "Inspect the red brick stupas and ancient hostel dormitories."
            },
            {
                "id": "NLN_02",
                "name": "Vishwa Shanti Stupa & Rajgir Ropeway",
                "category": "Spiritual & Viewpoint",
                "entry_fee": 100,
                "duration_hours": 2.0,
                "zone": "Rajgir Hills",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Peace pagoda crowning Ratnagiri Hill accessed via chairlift ropeway.",
                "pro_tip": "Single-seater chairlift ride offers breathtaking views of the rugged hills."
            },
            {
                "id": "NLN_03",
                "name": "Venuvana & Brahmakund Hot Springs",
                "category": "Nature & Spiritual",
                "entry_fee": 20,
                "duration_hours": 1.5,
                "zone": "Rajgir Hills",
                "rating": 4.4,
                "preferred_time": "Evening",
                "description": "Bamboo grove gifted to Buddha and natural therapeutic hot sulphur springs.",
                "pro_tip": "Very soothing during cool morning or evening hours."
            }
        ]
    },

    # -------------------------------------------------------------
    # 5. CHHATTISGARH
    # -------------------------------------------------------------
    "Bastar & Jagdalpur, Chhattisgarh": {
        "city_code": "BST",
        "state": "Chhattisgarh",
        "tagline": "Tribal Heartland - Waterfalls, Caves & Bell Metal Art",
        "description": "Lush eco-tourism haven famous for roaring cascades and dhokra tribal craft.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 260,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "BST_01",
                "name": "Chitrakote Waterfall ('Niagara of India')",
                "category": "Nature",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Indravati Riverfront",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Horseshoe-shaped 300-meter wide cataract on the Indravati river.",
                "pro_tip": "Local boatmen offer exhilarating rides right up to the spray mist."
            },
            {
                "id": "BST_02",
                "name": "Tirathgarh Cascades & Kanger Valley",
                "category": "Nature & Adventure",
                "entry_fee": 25,
                "duration_hours": 2.0,
                "zone": "Kanger Valley National Park",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Tiered block waterfall flowing over rugged crags inside dense sal woods.",
                "pro_tip": "Climb down the stone steps to the pool base for photography."
            },
            {
                "id": "BST_03",
                "name": "Kotumsar Subterranean Limestone Caves",
                "category": "Adventure & Science",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Kanger Valley National Park",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Deep limestone cavern featuring giant stalactite pillars and blind cave fish.",
                "pro_tip": "Carry a flashlight and hire a park guide with petromax lamps."
            }
        ]
    },
    "Raipur & Sirpur, Chhattisgarh": {
        "city_code": "RPR",
        "state": "Chhattisgarh",
        "tagline": "Ancient Temple Capitals & Craft Heritage",
        "description": "Rapidly modernizing capital bordered by 7th-century archaeological wonders.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 200,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "RPR_01",
                "name": "Sirpur Laxman Temple Archaeological Complex",
                "category": "Heritage",
                "entry_fee": 25,
                "duration_hours": 2.5,
                "zone": "Sirpur Heritage Zone",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "7th-century red brick temple with exquisitely carved doorway lintels.",
                "pro_tip": "Visit the adjacent Buddhist Vihara ruins where Xuanzang once studied."
            },
            {
                "id": "RPR_02",
                "name": "Purkhouti Muktangan Cultural Open-Air Park",
                "category": "Culture & Nature",
                "entry_fee": 30,
                "duration_hours": 2.0,
                "zone": "Naya Raipur",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "200-acre open-air museum preserving folk habitats, dances, and sculptures.",
                "pro_tip": "Pleasant evening stroll; golf carts available for elders."
            },
            {
                "id": "RPR_03",
                "name": "Vivekananda Sarovar (Budha Talab)",
                "category": "Relaxation",
                "entry_fee": 20,
                "duration_hours": 1.5,
                "zone": "Raipur City Center",
                "rating": 4.4,
                "preferred_time": "Evening",
                "description": "Urban lake featuring a 37-foot bronze statue of Swami Vivekananda.",
                "pro_tip": "Musical water fountain show runs daily after sunset."
            }
        ]
    },

    # -------------------------------------------------------------
    # 6. GOA
    # -------------------------------------------------------------
    "Goa (North & South)": {
        "city_code": "GOA",
        "state": "Goa",
        "tagline": "Sun, Sand, Portuguese Heritage & Tropical Vibes",
        "description": "India's coastal paradise blending historic Latin quarters, serene backwaters, and golden beaches.",
        "avg_intra_zone_transit_cost": 150,
        "avg_inter_zone_transit_cost": 450,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 1.0,
        "attractions": [
            {
                "id": "GOA_01",
                "name": "Aguada Fort & Lighthouse",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "North Goa - Candolim",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "17th-century Portuguese fort overlooking the Arabian Sea and Sinquerim beach.",
                "pro_tip": "Climb up near the jail museum for uninterrupted ocean vistas."
            },
            {
                "id": "GOA_02",
                "name": "Basilica of Bom Jesus & Old Goa",
                "category": "Heritage & Spiritual",
                "entry_fee": 25,
                "duration_hours": 2.0,
                "zone": "Central Goa - Old Goa",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "UNESCO World Heritage baroque church enshrining the mortal remains of St. Francis Xavier.",
                "pro_tip": "Modest clothing required inside ecclesiastical grounds."
            },
            {
                "id": "GOA_03",
                "name": "Baga Beach Watersports & Shacks",
                "category": "Adventure & Nature",
                "entry_fee": 500,
                "duration_hours": 3.0,
                "zone": "North Goa - Coastal",
                "rating": 4.4,
                "preferred_time": "Afternoon",
                "description": "Energetic coastline packed with parasailing, jet skiing, banana rides, and vibrant beach shacks.",
                "pro_tip": "Always verify life jacket safety protocols before embarking on boat rides."
            },
            {
                "id": "GOA_04",
                "name": "Fontainhas Latin Quarter Heritage Walk",
                "category": "Culture & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Panaji / Central",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Narrow picturesque streets lined with vibrant pastel Portuguese villas, tiled roofs, and art cafes.",
                "pro_tip": "Great spot for street photography; try traditional Bebinca in a heritage cafe."
            },
            {
                "id": "GOA_05",
                "name": "Chapora Fort (Dil Chahta Hai Fort)",
                "category": "Viewpoint & Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "North Goa - Vagator",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Red laterite cliff-top fort overlooking Vagator Beach and the Ozran coastline.",
                "pro_tip": "Wear sturdy footwear for the 10-minute incline trek up the ramparts."
            },
            {
                "id": "GOA_06",
                "name": "Mandovi River Sunset Cruise",
                "category": "Relaxation & Culture",
                "entry_fee": 600,
                "duration_hours": 2.0,
                "zone": "Panaji / Central",
                "rating": 4.3,
                "preferred_time": "Evening",
                "description": "1-hour river journey featuring Goan folk dances (Dekhni, Fugdi) and live music.",
                "pro_tip": "Book the 5:45 PM slot to catch the golden sunset into the horizon."
            },
            {
                "id": "GOA_07",
                "name": "Anjuna Flea Market / Curlies Sunset",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "North Goa - Coastal",
                "rating": 4.2,
                "preferred_time": "Evening",
                "description": "Bohemian beachfront atmosphere with handicrafts, musicians, and sunset views.",
                "pro_tip": "Wednesdays host the full flea market; lively shacks open daily."
            },
            {
                "id": "GOA_08",
                "name": "Se Cathedral & Church of St. Francis of Assisi",
                "category": "Heritage & Spiritual",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Central Goa - Old Goa",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "One of the largest churches in Asia, famed for its Golden Bell and Portuguese-Manueline architecture.",
                "pro_tip": "Located directly across from Basilica of Bom Jesus."
            }
        ]
    },
    "South Goa & Coastal Serenity, Goa": {
        "city_code": "SGO",
        "state": "Goa",
        "tagline": "Tranquil Sands, Dolphin Coves & Cabo Forts",
        "description": "The calmer, greener half of Goa boasting secluded bays and waterfalls.",
        "avg_intra_zone_transit_cost": 160,
        "avg_inter_zone_transit_cost": 480,
        "transit_time_same_zone_hr": 0.45,
        "transit_time_cross_zone_hr": 1.1,
        "attractions": [
            {
                "id": "SGO_01",
                "name": "Palolem Beach & Butterfly Island Boat Trip",
                "category": "Nature & Adventure",
                "entry_fee": 250,
                "duration_hours": 2.5,
                "zone": "Canacona Coastal",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Crescent beach shaded by swaying palms with calm swimming waters.",
                "pro_tip": "Hire a traditional boat in early morning for dolphin spotting."
            },
            {
                "id": "SGO_02",
                "name": "Cabo de Rama Cliff Fort",
                "category": "Heritage & Viewpoint",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Cabo Promontory",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Ancient sea fort perched on high cliffs where Lord Rama is said to have sheltered.",
                "pro_tip": "Breathtaking sunset vistas over the Arabian Sea."
            },
            {
                "id": "SGO_03",
                "name": "Dudhsagar Falls Jungle Safari Excursion",
                "category": "Adventure & Nature",
                "entry_fee": 500,
                "duration_hours": 3.5,
                "zone": "Bhagwan Mahavir Reserve",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Four-tiered sea of milk waterfall cascading 310 meters down Western Ghats.",
                "pro_tip": "Government registered 4x4 jeeps ferry visitors through riverbed tracks."
            }
        ]
    },

    # -------------------------------------------------------------
    # 7. GUJARAT
    # -------------------------------------------------------------
    "Ahmedabad, Gujarat": {
        "city_code": "AMD",
        "state": "Gujarat",
        "tagline": "India's First UNESCO Heritage City - Textile & Freedom Legacy",
        "description": "Vibrant metropolis on the Sabarmati famed for carved stepwells, mosques, and street food.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "AMD_01",
                "name": "Sabarmati Ashram (Gandhi Smarak Sangrahalaya)",
                "category": "Heritage & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Sabarmati Riverfront",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Historic headquarters of Mahatma Gandhi during the epic Dandi Salt March.",
                "pro_tip": "Browse the museum gallery and peaceful river-facing prayer grounds."
            },
            {
                "id": "AMD_02",
                "name": "Adalaj Stepwell (Rudabai Vav)",
                "category": "Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Northern Corridor",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Five-storey deep subterranean sandstone stepwell featuring Solanki architectural filigree.",
                "pro_tip": "The temperature inside the stepwell is 5 degrees cooler than surface levels."
            },
            {
                "id": "AMD_03",
                "name": "Sidi Saiyyed Mosque ('Tree of Life' Jali)",
                "category": "Heritage & Culture",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "Old Walled City",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "16th-century mosque famous for its intricate marble tracery jali of intertwined tree branches.",
                "pro_tip": "The design serves as the official insignia of IIM Ahmedabad."
            },
            {
                "id": "AMD_04",
                "name": "Manek Chowk Night Food Trail",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Old Walled City",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Jewellery market by day converting into an energetic street culinary carnival by night.",
                "pro_tip": "Try Gwalior Dosa, chocolate sandwiches, and Kulfi Falooda."
            }
        ]
    },
    "Rann of Kutch & Bhuj, Gujarat": {
        "city_code": "KTC",
        "state": "Gujarat",
        "tagline": "The Great White Desert & Royal Kutchi Crafts",
        "description": "Vast endless salt flats, vibrant tribal embroidery, and historic royal palaces.",
        "avg_intra_zone_transit_cost": 140,
        "avg_inter_zone_transit_cost": 400,
        "transit_time_same_zone_hr": 0.45,
        "transit_time_cross_zone_hr": 1.1,
        "attractions": [
            {
                "id": "KTC_01",
                "name": "Great Rann of Kutch White Salt Desert",
                "category": "Nature & Viewpoint",
                "entry_fee": 100,
                "duration_hours": 3.0,
                "zone": "Dhordo Desert Zone",
                "rating": 4.9,
                "preferred_time": "Evening",
                "description": "World's largest seasonal salt marsh shimmering like snow under moonlight.",
                "pro_tip": "Obtain entry permits online or at the Bhirandiyara checkpoint."
            },
            {
                "id": "KTC_02",
                "name": "Kala Dungar (Black Hill) Summit",
                "category": "Viewpoint & Nature",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Northern Ridge",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Highest point in Kutch offering sweeping panoramic views of the white desert horizon.",
                "pro_tip": "Visit the 400-year-old Dattatreya Temple where jackals are fed daily."
            },
            {
                "id": "KTC_03",
                "name": "Aina Mahal & Prag Mahal Palaces",
                "category": "Heritage",
                "entry_fee": 60,
                "duration_hours": 2.0,
                "zone": "Bhuj Heritage Core",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "18th-century hall of mirrors and Venetian gothic palace with clock tower.",
                "pro_tip": "Climb the 45m bell tower for 360-degree views of Bhuj city."
            }
        ]
    },

    # -------------------------------------------------------------
    # 8. HARYANA
    # -------------------------------------------------------------
    "Kurukshetra, Haryana": {
        "city_code": "KRK",
        "state": "Haryana",
        "tagline": "Land of the Mahabharata & Gita Jayanti",
        "description": "Historic holy city where Lord Krishna imparted the teachings of the Bhagavad Gita.",
        "avg_intra_zone_transit_cost": 75,
        "avg_inter_zone_transit_cost": 180,
        "transit_time_same_zone_hr": 0.25,
        "transit_time_cross_zone_hr": 0.6,
        "attractions": [
            {
                "id": "KRK_01",
                "name": "Brahma Sarovar Sacred Water Body",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Brahma Sarovar Enclosure",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "One of Asia's largest man-made sacred tanks with broad granite ghats.",
                "pro_tip": "Grand evening aarti is performed at sunset with floating diyas."
            },
            {
                "id": "KRK_02",
                "name": "Jyotisar (Birthplace of Bhagavad Gita)",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Jyotisar Sanctuary",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Sacred banyan tree site where Krishna delivered the eternal sermon to Arjuna.",
                "pro_tip": "Laser light and sound show brings the Mahabharata epic to life."
            },
            {
                "id": "KRK_03",
                "name": "Sheikh Chilli's Tomb & Archaeological Museum",
                "category": "Heritage",
                "entry_fee": 25,
                "duration_hours": 1.5,
                "zone": "Thanesar Heritage",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "Mughal-era Persian style white marble mausoleum with symmetrical charbagh gardens.",
                "pro_tip": "Museum displays rare Harappan seals excavated nearby."
            }
        ]
    },
    "Gurugram & Sultanpur, Haryana": {
        "city_code": "GGM",
        "state": "Haryana",
        "tagline": "Modern Millennium City & Migratory Bird Havens",
        "description": "High-tech skyscraper hub complemented by premier transport museums and wetlands.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 250,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "GGM_01",
                "name": "Sultanpur National Bird Sanctuary",
                "category": "Nature & Adventure",
                "entry_fee": 40,
                "duration_hours": 2.5,
                "zone": "Sultanpur Wetlands",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Wetland habitat welcoming over 250 species of Siberian and European migratory birds.",
                "pro_tip": "Four watchtowers provide birdwatching vantage points across the lake."
            },
            {
                "id": "GGM_02",
                "name": "Heritage Transport Museum",
                "category": "Culture & Science",
                "entry_fee": 400,
                "duration_hours": 2.5,
                "zone": "Tauru Corridor",
                "rating": 4.8,
                "preferred_time": "Afternoon",
                "description": "World-class 90,000 sq ft museum showcasing vintage cars, locomotives, and aviation.",
                "pro_tip": "Fully air-conditioned; great family experience with interactive displays."
            },
            {
                "id": "GGM_03",
                "name": "CyberHub & Leisure Valley Evening Stroll",
                "category": "Food & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "DLF CyberCity",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Gourmet dining plaza and open-air boulevard celebrating global culinary cultures.",
                "pro_tip": "Directly connected via the modern Rapid Metro system."
            }
        ]
    },

    # -------------------------------------------------------------
    # 9. HIMACHAL PRADESH
    # -------------------------------------------------------------
    "Manali, Himachal Pradesh": {
        "city_code": "MNL",
        "state": "Himachal Pradesh",
        "tagline": "Himalayan Gateway - Snow Peaks, Pines & Adventures",
        "description": "High-altitude resort town tucked in the Beas River Valley, surrounded by snow-capped Pir Panjal peaks.",
        "avg_intra_zone_transit_cost": 150,
        "avg_inter_zone_transit_cost": 500,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 1.2,
        "attractions": [
            {
                "id": "MNL_01",
                "name": "Solang Valley Adventure Arena",
                "category": "Adventure & Nature",
                "entry_fee": 600,
                "duration_hours": 3.5,
                "zone": "Upper Valley / Solang",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Side valley offering paragliding, zorbing, quad biking, and winter ski slopes.",
                "pro_tip": "Start before 8 AM to avoid highway traffic bottleneck towards the Atal Tunnel."
            },
            {
                "id": "MNL_02",
                "name": "Hadimba Devi Ancient Wooden Temple",
                "category": "Heritage & Spiritual",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Central Manali",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Four-tiered pagoda-style cedar wood temple built in 1553 amid dense Dhungri deodar forests.",
                "pro_tip": "Respect local custom; photography inside the sanctum sanctorum is prohibited."
            },
            {
                "id": "MNL_03",
                "name": "Old Manali Cafe Trail & Apple Orchards Walk",
                "category": "Culture & Food",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Old Manali",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Quaint village vibe with indie cafes, live acoustic music, wooden houses, and mountain views.",
                "pro_tip": "Try trout fish delicacies and hot spiced apple cider at local cafes."
            },
            {
                "id": "MNL_04",
                "name": "Jogini Waterfall Short Trek",
                "category": "Adventure & Nature",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Vashisht / North",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Scenic 3 km pine-trail hike starting from Vashisht village ending at cascading mountain falls.",
                "pro_tip": "Wear hiking shoes with good grip on wet granite steps."
            },
            {
                "id": "MNL_05",
                "name": "Vashisht Hot Water Springs & Temple",
                "category": "Spiritual & Relaxation",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Vashisht / North",
                "rating": 4.4,
                "preferred_time": "Afternoon",
                "description": "Natural sulfur mineral springs with therapeutic qualities and an ancient stone temple.",
                "pro_tip": "Separate bathing tanks exist for men and women."
            },
            {
                "id": "MNL_06",
                "name": "Mall Road & Tibetan Monastery Evening Stroll",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Central Manali",
                "rating": 4.3,
                "preferred_time": "Evening",
                "description": "Lively pedestrian boulevard with woollen shawls, Himachali caps, hot momos, and handicrafts.",
                "pro_tip": "Strictly no vehicles permitted; great for leisurely post-dinner strolls."
            },
            {
                "id": "MNL_07",
                "name": "Atal Tunnel & Sissu Valley Day Excursion",
                "category": "Sightseeing & Nature",
                "entry_fee": 250,
                "duration_hours": 4.0,
                "zone": "Lahaul Valley / Solang",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "World's longest highway tunnel above 10,000 ft connecting to stark Lahaul alpine landscapes.",
                "pro_tip": "Carry warm thermals as temperatures drop abruptly past the north portal."
            }
        ]
    },
    "Shimla, Himachal Pradesh": {
        "city_code": "SML",
        "state": "Himachal Pradesh",
        "tagline": "Queen of the Hills - Colonial Architecture & Mountain Vistas",
        "description": "Former summer capital of British India perched gracefully across seven Himalayan ridges.",
        "avg_intra_zone_transit_cost": 120,
        "avg_inter_zone_transit_cost": 300,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "SML_01",
                "name": "The Ridge & Mall Road Promenade",
                "category": "Heritage & Culture",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Central Mall",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Pedestrian hub home to the neo-Gothic Christ Church and scenic mountain views.",
                "pro_tip": "Stop at the Indian Coffee House for nostalgic filter coffee and mutton cutlets."
            },
            {
                "id": "SML_02",
                "name": "Jakhoo Hill & Giant Hanuman Statue",
                "category": "Spiritual & Viewpoint",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Jakhoo Peak",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Highest peak in Shimla (8,000 ft) crowned by a 108-foot saffron Hanuman statue.",
                "pro_tip": "A fast ropeway gondola connects the Ridge to Jakhoo in 6 minutes."
            },
            {
                "id": "SML_03",
                "name": "Viceregal Lodge (Indian Institute of Advanced Study)",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Observatory Hill",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Magnificent Jacobethan manor where the historic Shimla Conference of 1945 was held.",
                "pro_tip": "Guided indoor tours depart every 30 minutes."
            }
        ]
    },

    # -------------------------------------------------------------
    # 10. JHARKHAND
    # -------------------------------------------------------------
    "Ranchi, Jharkhand": {
        "city_code": "RNC",
        "state": "Jharkhand",
        "tagline": "City of Waterfalls - Forest Valleys & Plateaus",
        "description": "Capital set on the Chota Nagpur plateau surrounded by thunderous cataracts.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 230,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "RNC_01",
                "name": "Hundru Waterfalls Cascade",
                "category": "Nature",
                "entry_fee": 20,
                "duration_hours": 2.5,
                "zone": "Subarnarekha Valley",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Subarnarekha river plummeting 98 meters over jagged rock formations.",
                "pro_tip": "Wear footwear with solid grip; rock steps can be damp."
            },
            {
                "id": "RNC_02",
                "name": "Patratu Valley Scenic Drive & Lake",
                "category": "Nature & Viewpoint",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Patratu Valley",
                "rating": 4.8,
                "preferred_time": "Evening",
                "description": "Dramatic winding serpentine mountain road cutting through dense forested ravines.",
                "pro_tip": "Catch sunset from the designated valley view pavilion."
            },
            {
                "id": "RNC_03",
                "name": "Tagore Hill & Bramho Cultural Retreat",
                "category": "Culture & Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Morabadi",
                "rating": 4.4,
                "preferred_time": "Morning",
                "description": "Hilltop hermitage where Jyotirindranath Tagore wrote plays and poetry.",
                "pro_tip": "Provides sweeping views across Ranchi city horizon."
            }
        ]
    },
    "Jamshedpur, Jharkhand": {
        "city_code": "IXW",
        "state": "Jharkhand",
        "tagline": "The Steel City - Planned Green Avenues & Wildlife",
        "description": "India's first planned industrial city blessed with expansive rose gardens and lake sanctuaries.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 210,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "JMP_01",
                "name": "Jubilee Park & Musical Fountains",
                "category": "Nature & Relaxation",
                "entry_fee": 30,
                "duration_hours": 2.0,
                "zone": "Sakchi Civic Core",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "200-acre park modeled after Mysore's Brindavan Gardens.",
                "pro_tip": "Illuminated fountains operate on Tuesdays and Saturdays."
            },
            {
                "id": "JMP_02",
                "name": "Dalma Wildlife Sanctuary & Hilltop",
                "category": "Adventure & Nature",
                "entry_fee": 100,
                "duration_hours": 3.5,
                "zone": "Dalma Range",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Forested elephant corridor situated at 3,000 ft altitude overlooking the plateau.",
                "pro_tip": "Forest department rest houses offer overnight wildlife camping."
            },
            {
                "id": "JMP_03",
                "name": "Dimna Lake & Dam Catchment",
                "category": "Nature",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Dalma Foothills",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "Clear water reservoir tucked right at the base of the Dalma hills.",
                "pro_tip": "Ideal tranquil spot for morning photography."
            }
        ]
    },

    # -------------------------------------------------------------
    # 11. KARNATAKA
    # -------------------------------------------------------------
    "Bengaluru & Mysuru, Karnataka": {
        "city_code": "BLR",
        "state": "Karnataka",
        "tagline": "Royal Heritage Palaces & Silicon Valley Innovation",
        "description": "From the grand royal court of the Wodeyars to lush botanical glasshouses.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 260,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.85,
        "attractions": [
            {
                "id": "BLR_01",
                "name": "Mysore Royal Palace (Amba Vilas)",
                "category": "Heritage",
                "entry_fee": 100,
                "duration_hours": 2.5,
                "zone": "Mysuru Heritage Core",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Indo-Saracenic royal masterpiece with stained glass domes and golden thrones.",
                "pro_tip": "Witness 100,000 incandescent bulbs illuminate the palace every Sunday night."
            },
            {
                "id": "BLR_02",
                "name": "Lalbagh Botanical Gardens & Glass House",
                "category": "Nature",
                "entry_fee": 30,
                "duration_hours": 2.0,
                "zone": "South Bengaluru",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Historic 240-acre garden established by Hyder Ali featuring century-old trees.",
                "pro_tip": "Walk up the peninsular gneiss rock hillock dating back 3,000 million years."
            },
            {
                "id": "BLR_03",
                "name": "Chamundi Hill & Giant Nandi Bull",
                "category": "Spiritual & Viewpoint",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Mysuru Hills",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Historic Dravidian temple perched 1,000 meters above sea level.",
                "pro_tip": "Stop at the monolithic 16-foot Nandi statue halfway down."
            }
        ]
    },
    "Hampi, Karnataka": {
        "city_code": "HMP",
        "state": "Karnataka",
        "tagline": "UNESCO Open-Air Museum - Vijayanagara Boulder Empire",
        "description": "Surreal boulder-strewn wonderland housing the ruins of the medieval Vijayanagara Empire.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 200,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.6,
        "attractions": [
            {
                "id": "HMP_01",
                "name": "Vijaya Vittala Temple & Stone Chariot",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 2.5,
                "zone": "Vittala Complex",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Iconic monolithic stone chariot and 56 musical pillars that chime notes.",
                "pro_tip": "Battery operated buggies are available from the outer parking gate."
            },
            {
                "id": "HMP_02",
                "name": "Virupaksha Temple & Hampi Bazaar",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Sacred Centre",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Continuously active 7th-century temple dedicated to Lord Shiva with 50m gopuram.",
                "pro_tip": "Greet Lakshmi the resident temple elephant during morning hours."
            },
            {
                "id": "HMP_03",
                "name": "Lotus Mahal & Royal Elephant Stables",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 2.0,
                "zone": "Royal Enclosure",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Indo-Islamic secular palace featuring lotus bud dome arches and vaulted stables.",
                "pro_tip": "Ticket is composite and covers Vittala Temple on the same date."
            }
        ]
    },

    # -------------------------------------------------------------
    # 12. KERALA
    # -------------------------------------------------------------
    "Kochi, Kerala": {
        "city_code": "COK",
        "state": "Kerala",
        "tagline": "Queen of the Arabian Sea - Spice Route & Colonial Charm",
        "description": "Historic coastal spice port influenced by Dutch, Portuguese, British, and Chinese traders.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 280,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "COK_01",
                "name": "Fort Kochi Chinese Fishing Nets & Beach Promenade",
                "category": "Heritage & Sightseeing",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Fort Kochi",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Iconic cantilevered shore nets introduced by 14th-century Chinese traders.",
                "pro_tip": "Watch local fishermen operate the heavy counterweights during high tide."
            },
            {
                "id": "COK_02",
                "name": "Mattancherry Palace (Dutch Palace) & Murals",
                "category": "Heritage",
                "entry_fee": 20,
                "duration_hours": 1.5,
                "zone": "Mattancherry",
                "rating": 4.5,
                "preferred_time": "Morning",
                "description": "Colonial palace renowned for extraordinary Hindu mythological wall murals.",
                "pro_tip": "Closed on Fridays and national holidays."
            },
            {
                "id": "COK_03",
                "name": "Jew Town & Paradesi Synagogue",
                "category": "Culture & Heritage",
                "entry_fee": 30,
                "duration_hours": 2.0,
                "zone": "Mattancherry",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Oldest active synagogue in the Commonwealth, featuring hand-painted Chinese tiles and antique stores.",
                "pro_tip": "Browse aroma-rich cardamom and ginger wholesale spice shops along the lane."
            },
            {
                "id": "COK_04",
                "name": "Kerala Kathakali Centre Classical Performance",
                "category": "Culture & Performance",
                "entry_fee": 450,
                "duration_hours": 2.0,
                "zone": "Fort Kochi",
                "rating": 4.8,
                "preferred_time": "Evening",
                "description": "Traditional drama performance with live makeup demonstration and mudra explanations.",
                "pro_tip": "Arrive at 5:00 PM to watch the elaborate face painting transformation."
            },
            {
                "id": "COK_05",
                "name": "Kochi Harbor Ferry / Sunset Water Cruise",
                "category": "Relaxation & Nature",
                "entry_fee": 300,
                "duration_hours": 1.5,
                "zone": "Marine Drive / Ernakulam",
                "rating": 4.4,
                "preferred_time": "Evening",
                "description": "Scenic sail on backwater channels passing merchant ship docks, Bolgatty Palace, and islands.",
                "pro_tip": "Government water metro offers modern air-conditioned rides at nominal tariffs."
            },
            {
                "id": "COK_06",
                "name": "Santa Cruz Cathedral Basilica",
                "category": "Heritage & Spiritual",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "Fort Kochi",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Majestic gothic basilica built originally by Portuguese in 1505 with frescoed ceilings.",
                "pro_tip": "Very peaceful sanctuary right in the heart of Fort Kochi village."
            },
            {
                "id": "COK_07",
                "name": "Hill Palace Museum, Tripunithura",
                "category": "Culture & Heritage",
                "entry_fee": 60,
                "duration_hours": 2.5,
                "zone": "Ernakulam / Outer",
                "rating": 4.4,
                "preferred_time": "Afternoon",
                "description": "Largest archaeological palace complex in Kerala with royal crown jewels and deer park.",
                "pro_tip": "Closed on Mondays; huge 54-acre heritage campus."
            }
        ]
    },
    "Munnar & Alleppey, Kerala": {
        "city_code": "MNR",
        "state": "Kerala",
        "tagline": "Misty Tea Slopes & Emerald Backwater Lagoons",
        "description": "The quintessential God's Own Country journey from high tea hills to lazy houseboat lagoons.",
        "avg_intra_zone_transit_cost": 120,
        "avg_inter_zone_transit_cost": 350,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 1.0,
        "attractions": [
            {
                "id": "MNR_01",
                "name": "Eravikulam National Park (Nilgiri Tahr)",
                "category": "Nature & Adventure",
                "entry_fee": 200,
                "duration_hours": 3.0,
                "zone": "Munnar Highlands",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Rolling grassland slopes home to endangered mountain goats and Anamudi peak.",
                "pro_tip": "Book safari mini-bus tickets online in advance."
            },
            {
                "id": "MNR_02",
                "name": "Mattupetty Dam & Tea Plantation Trail",
                "category": "Nature",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Munnar Highlands",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "Reservoir surrounded by tea estates, popular for speedboating and echo points.",
                "pro_tip": "Sample fresh handmade chocolates and strawberry dips near the dam."
            },
            {
                "id": "MNR_03",
                "name": "Alappuzha Backwater Houseboat Day Cruise",
                "category": "Relaxation & Nature",
                "entry_fee": 650,
                "duration_hours": 3.5,
                "zone": "Alleppey Backwaters",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Kettuvallam boat glide through canals, coconut palm shores, and paddy fields.",
                "pro_tip": "Enjoy onboard lunch featuring Karimeen Pollichathu (pearl spot fish)."
            }
        ]
    },

    # -------------------------------------------------------------
    # 13. MADHYA PRADESH
    # -------------------------------------------------------------
    "Khajuraho, Madhya Pradesh": {
        "city_code": "HJR",
        "state": "Madhya Pradesh",
        "tagline": "UNESCO Architectural Poetry in Sandstone",
        "description": "Chandela dynasty temple marvels famed worldwide for expressive sculptural mastery.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 180,
        "transit_time_same_zone_hr": 0.25,
        "transit_time_cross_zone_hr": 0.6,
        "attractions": [
            {
                "id": "HJR_01",
                "name": "Western Group of Temples (Kandariya Mahadeva)",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 3.0,
                "zone": "Western Complex",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Masterpieces of Nagara temple architecture featuring 800 celestial sculptures.",
                "pro_tip": "Hire an ASI licensed guide to decode the intricate symbolism of the friezes."
            },
            {
                "id": "HJR_02",
                "name": "Eastern & Jain Temple Enclosure",
                "category": "Heritage & Spiritual",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Eastern Village Zone",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Parsvanatha and Adinatha temples boasting intricate sandstone filigree.",
                "pro_tip": "Quiet and contemplative compared to the busier western complex."
            },
            {
                "id": "HJR_03",
                "name": "Raneh Falls & Ken River Canyon",
                "category": "Nature",
                "entry_fee": 100,
                "duration_hours": 2.5,
                "zone": "Ken River Sanctuary",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Volcanic crystalline rock canyon with multicolored granite chasms.",
                "pro_tip": "Spot Indian gharials basking on the river islands."
            }
        ]
    },
    "Bhopal & Sanchi, Madhya Pradesh": {
        "city_code": "BHO",
        "state": "Madhya Pradesh",
        "tagline": "City of Lakes & Ancient Ashokan Stupas",
        "description": "Sprawling lake capital connected to 2,300-year-old Buddhist monuments.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "BHO_01",
                "name": "Great Stupa of Sanchi",
                "category": "Heritage & Spiritual",
                "entry_fee": 40,
                "duration_hours": 2.5,
                "zone": "Sanchi Hilltop",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Oldest stone structure in India commissioned by Emperor Ashoka in 3rd century BCE.",
                "pro_tip": "Inspect the four monumental Torana gateways depicting Jataka tales."
            },
            {
                "id": "BHO_02",
                "name": "Bhimbetka Prehistoric Rock Shelters",
                "category": "Heritage & Science",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Bhimbetka Forest",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "UNESCO World Heritage site with 30,000-year-old Paleolithic cave art.",
                "pro_tip": "Look for the famous rock 'Auditorium' and vivid hunting scenes."
            },
            {
                "id": "BHO_03",
                "name": "Upper Lake (Bhojtal) & Van Vihar",
                "category": "Nature & Relaxation",
                "entry_fee": 40,
                "duration_hours": 2.0,
                "zone": "Lakefront Promenade",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Huge 11th-century artificial lake and adjoining open-zoo nature sanctuary.",
                "pro_tip": "Bicycle rentals available for exploring the waterfront drive."
            }
        ]
    },

    # -------------------------------------------------------------
    # 14. MAHARASHTRA
    # -------------------------------------------------------------
    "Mumbai, Maharashtra": {
        "city_code": "BOM",
        "state": "Maharashtra",
        "tagline": "City of Dreams - Colonial Heritage & Arabian Sea Coastline",
        "description": "India's financial capital blending Victorian Gothic monuments, sea drives, and Bollywood.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 280,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.85,
        "attractions": [
            {
                "id": "BOM_01",
                "name": "Gateway of India & Taj Mahal Palace Hotel",
                "category": "Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Colaba / South Mumbai",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "26m basalt arch monument overlooking Mumbai harbour, built in 1911.",
                "pro_tip": "Board harbour catamarans right from the jetty behind the arch."
            },
            {
                "id": "BOM_02",
                "name": "Elephanta Caves UNESCO Rock-Cut Temples",
                "category": "Heritage & Spiritual",
                "entry_fee": 260,
                "duration_hours": 3.5,
                "zone": "Elephanta Island",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Ancient island cave temples featuring the celebrated 20-foot Trimurti sculpture of Shiva.",
                "pro_tip": "One-hour scenic ferry ride departs every 30 minutes from Gateway of India."
            },
            {
                "id": "BOM_03",
                "name": "Marine Drive Promenade ('Queen's Necklace')",
                "category": "Viewpoint & Relaxation",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Colaba / South Mumbai",
                "rating": 4.8,
                "preferred_time": "Evening",
                "description": "3.6-kilometer C-shaped boulevard along the natural bay with sunset breeze.",
                "pro_tip": "Grab roasted spicy corn (bhutta) and sit along the tetrapods at dusk."
            },
            {
                "id": "BOM_04",
                "name": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya",
                "category": "Culture & Science",
                "entry_fee": 150,
                "duration_hours": 2.5,
                "zone": "Fort / Kala Ghoda",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Premier Indo-Saracenic museum holding 70,000 ancient artifacts, miniature paintings, and armory.",
                "pro_tip": "Audio guides in 7 languages are available at the entrance."
            }
        ]
    },
    "Chhatrapati Sambhajinagar (Aurangabad), Maharashtra": {
        "city_code": "IXU",
        "state": "Maharashtra",
        "tagline": "Tourism Capital of Maharashtra - Ajanta & Ellora Wonders",
        "description": "Gateway to the world-renowned monolithic rock-cut cave architectures.",
        "avg_intra_zone_transit_cost": 110,
        "avg_inter_zone_transit_cost": 320,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.9,
        "attractions": [
            {
                "id": "IXU_01",
                "name": "Ellora Caves & Monolithic Kailasa Temple",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 3.5,
                "zone": "Ellora Complex",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Largest single rock-cut monolithic structure on earth carved top-down from a basalt cliff.",
                "pro_tip": "Cave 16 (Kailasa) alone deserves at least 1.5 hours of dedicated study."
            },
            {
                "id": "IXU_02",
                "name": "Bibi Ka Maqbara ('Dakkhani Taj')",
                "category": "Heritage",
                "entry_fee": 25,
                "duration_hours": 1.5,
                "zone": "Aurangabad City",
                "rating": 4.4,
                "preferred_time": "Afternoon",
                "description": "17th-century Mughal mausoleum built by prince Azam Shah in memory of his mother.",
                "pro_tip": "Striking architectural resemblance to the Taj Mahal of Agra."
            },
            {
                "id": "IXU_03",
                "name": "Daulatabad (Devagiri) Hill Fort",
                "category": "Heritage & Adventure",
                "entry_fee": 25,
                "duration_hours": 2.5,
                "zone": "Daulatabad Ridge",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Impregnable triangular fortress featuring an ingenious dark maze (Andhari) passageway.",
                "pro_tip": "Carry water bottles for the 750-step climb to the summit cannon."
            }
        ]
    },

    # -------------------------------------------------------------
    # 15. MANIPUR
    # -------------------------------------------------------------
    "Imphal & Loktak Lake, Manipur": {
        "city_code": "IMF",
        "state": "Manipur",
        "tagline": "Jewel of India - Floating Phumdis & Sangai Deer",
        "description": "Enchanting eastern valley housing the world's only floating national park.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 240,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "IMF_01",
                "name": "Keibul Lamjao Floating National Park",
                "category": "Nature & Adventure",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Loktak Lake Sanctuary",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "World's only floating wildlife park on circular biomass rings (phumdis), sanctuary of brow-antlered deer.",
                "pro_tip": "Climb the watchtower at Sendra Island for a bird's eye view."
            },
            {
                "id": "IMF_02",
                "name": "Kangla Fort & Royal Palace Complex",
                "category": "Heritage",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Imphal City Center",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Historic royal power seat of Manipur kingdom surrounded by deep moats.",
                "pro_tip": "Bicycles are available at the entrance to tour the large fort grounds."
            },
            {
                "id": "IMF_03",
                "name": "Ima Keithel (Mother's Market)",
                "category": "Shopping & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Imphal City Center",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Centuries-old commercial market operated exclusively by 5,000+ licensed women traders.",
                "pro_tip": "Fabulous place to purchase handloom shawls, bamboo crafts, and local spices."
            }
        ]
    },

    # -------------------------------------------------------------
    # 16. MEGHALAYA
    # -------------------------------------------------------------
    "Shillong & Cherrapunji (Sohra), Meghalaya": {
        "city_code": "SHL",
        "state": "Meghalaya",
        "tagline": "Abode of Clouds - Living Root Bridges & Giant Waterfalls",
        "description": "Scotland of the East renowned for pristine rivers, rolling pine meadows, and bio-engineering marvels.",
        "avg_intra_zone_transit_cost": 120,
        "avg_inter_zone_transit_cost": 360,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 1.0,
        "attractions": [
            {
                "id": "SHL_01",
                "name": "Double Decker Living Root Bridge",
                "category": "Adventure & Nature",
                "entry_fee": 50,
                "duration_hours": 4.0,
                "zone": "Nongriat Valley",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Centuries-old bio-engineering wonder made by weaving aerial rubber fig roots over river valleys.",
                "pro_tip": "Involves climbing 3,500 stone steps; carry water and energy bars."
            },
            {
                "id": "SHL_02",
                "name": "Nohkalikai Falls Viewpoint",
                "category": "Nature & Viewpoint",
                "entry_fee": 20,
                "duration_hours": 1.5,
                "zone": "Cherrapunji / Sohra",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "India's tallest plunge waterfall (1,115 ft) plummeting into a turquoise mountain pool.",
                "pro_tip": "Visit before noon before rising valley mist obscures the gorge."
            },
            {
                "id": "SHL_03",
                "name": "Umiam Lake (Barapani Watersports)",
                "category": "Relaxation & Nature",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Shillong Outskirts",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Picturesque hill reservoir offering kayaking, water scooters, and pine shores.",
                "pro_tip": "Ideal scenic stop when driving from Guwahati to Shillong."
            }
        ]
    },

    # -------------------------------------------------------------
    # 17. MIZORAM
    # -------------------------------------------------------------
    "Aizawl & Reiek, Mizoram": {
        "city_code": "AZL",
        "state": "Mizoram",
        "tagline": "Land of the Rolling Hills - Bamboo Forests & Warm Hospitality",
        "description": "Picturesque cliffside capital celebrated for high-altitude mist and Mizo cultural warmth.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 250,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "AZL_01",
                "name": "Reiek Mountain Peak & Heritage Village",
                "category": "Adventure & Culture",
                "entry_fee": 20,
                "duration_hours": 3.0,
                "zone": "Reiek Ridge",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Dramatic cliff summit at 5,000 ft with traditional Mizo village models.",
                "pro_tip": "Trek up the grassy ridge on clear days to see Bangladesh plains in distance."
            },
            {
                "id": "AZL_02",
                "name": "Solomon's Temple (White Marble Shrine)",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Chawlhhmun",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Grand white marble cathedral built in the verdant western hills of Aizawl.",
                "pro_tip": "Surrounded by landscaped poly-greenhouses and flower gardens."
            },
            {
                "id": "AZL_03",
                "name": "Durtlang Hills Sunset Viewpoint",
                "category": "Viewpoint & Relaxation",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Durtlang Ridge",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Panoramic mountain perch looking over the layered tiers of Aizawl city lights.",
                "pro_tip": "Great evening cafe spots along the ridge."
            }
        ]
    },

    # -------------------------------------------------------------
    # 18. NAGALAND
    # -------------------------------------------------------------
    "Kohima & Dzukou Valley, Nagaland": {
        "city_code": "KHM",
        "state": "Nagaland",
        "tagline": "Land of Festivals - Dzukou Lily Valley & Naga Heritage",
        "description": "Historic hill capital renowned for the annual Hornbill Festival and emerald valleys.",
        "avg_intra_zone_transit_cost": 95,
        "avg_inter_zone_transit_cost": 260,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.85,
        "attractions": [
            {
                "id": "KHM_01",
                "name": "Kisama Heritage Village (Hornbill Venue)",
                "category": "Culture & Heritage",
                "entry_fee": 30,
                "duration_hours": 2.5,
                "zone": "Kisama Valley",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Open-air preservation of 16 distinct Naga tribal morung pavilions and wood carvings.",
                "pro_tip": "Fabulous place to learn Naga tribal history even outside festival dates."
            },
            {
                "id": "KHM_02",
                "name": "Kohima War Memorial & Cemetery",
                "category": "Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Garrison Hill",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Immaculately terraced Commonwealth war memorial of the pivotal 1944 Battle of Kohima.",
                "pro_tip": "Reads the famous epitaph: 'When you go home, tell them of us and say...'"
            },
            {
                "id": "KHM_03",
                "name": "Dzukou Valley Alpine Trail",
                "category": "Adventure & Nature",
                "entry_fee": 100,
                "duration_hours": 4.0,
                "zone": "Dzukou Border Range",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Dreamscape valley of rolling velvet green hills and rare Dzukou lilies at 8,000 ft.",
                "pro_tip": "Engage a local guide for the trail from Jakhama or Viswema villages."
            }
        ]
    },

    # -------------------------------------------------------------
    # 19. ODISHA
    # -------------------------------------------------------------
    "Puri & Konark, Odisha": {
        "city_code": "PURI",
        "state": "Odisha",
        "tagline": "The Golden Triangle - Sun Temple, Jagannath & Chilika",
        "description": "Sacred coastal circuit showcasing Kalinga architectural wonders and marine lagoons.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "PURI_01",
                "name": "Konark Sun Temple (Black Pagoda)",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 2.5,
                "zone": "Konark Corridor",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "UNESCO World Heritage 13th-century colossal chariot of the Sun God with 24 carved stone wheels.",
                "pro_tip": "Examine the sundial spokes which indicate time accurately to the minute."
            },
            {
                "id": "PURI_02",
                "name": "Shree Jagannath Holy Temple",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Puri Grand Road",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "One of the holy Char Dhams renowned for the annual Ratha Yatra and Anand Bazaar mahaprasad.",
                "pro_tip": "Taste Khaja sweets and Mahaprasad cooked in earthen pots."
            },
            {
                "id": "PURI_03",
                "name": "Golden Beach Promenade (Blue Flag)",
                "category": "Relaxation & Nature",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Puri Coastal",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Clean, eco-certified Blue Flag beach with golden sands and safety lifelines.",
                "pro_tip": "Enjoy cool coastal breeze and evening sand art displays."
            }
        ]
    },
    "Bhubaneswar, Odisha": {
        "city_code": "BBI",
        "state": "Odisha",
        "tagline": "Temple City of India - Lingaraj & Ancient Rock Edits",
        "description": "Ancient capital of Kalinga boasting over 500 historic sandstone temples.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 200,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.65,
        "attractions": [
            {
                "id": "BBI_01",
                "name": "Lingaraj 11th-Century Temple Complex",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Old Town Temples",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Magnificent 55-meter tower representing Kalinga stone architecture at its zenith.",
                "pro_tip": "A viewing platform outside the perimeter wall offers elevated photo views."
            },
            {
                "id": "BBI_02",
                "name": "Udayagiri & Khandagiri Twin Cave Hills",
                "category": "Heritage & Adventure",
                "entry_fee": 25,
                "duration_hours": 2.5,
                "zone": "Cave Hills",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "2nd-century BCE rock-cut Jain monastic cells featuring the famous Hathigumpha inscription.",
                "pro_tip": "Rani Gumpha (Queen's Cave) displays double-storeyed sculpted friezes."
            },
            {
                "id": "BBI_03",
                "name": "Nandankanan Zoological Park & White Tiger Safari",
                "category": "Nature & Adventure",
                "entry_fee": 50,
                "duration_hours": 3.0,
                "zone": "Barang Sanctuary",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Renowned sanctuary known for successful breeding of white tigers and Indian pangolins.",
                "pro_tip": "Hop on the tiger safari electric shuttle."
            }
        ]
    },

    # -------------------------------------------------------------
    # 20. PUNJAB
    # -------------------------------------------------------------
    "Amritsar, Punjab": {
        "city_code": "ATQ",
        "state": "Punjab",
        "tagline": "The Golden City - Spiritual Solace & Patriotic Fervour",
        "description": "Cultural heart of Punjab renowned for the Harmandir Sahib, brave history, and kulchas.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 200,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "ATQ_01",
                "name": "Golden Temple (Sri Harmandir Sahib) & Langar",
                "category": "Spiritual & Culture",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Heritage Core",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Gilded central gurdwara floating on the Amrit Sarovar, serving 100,000 free meals daily.",
                "pro_tip": "Cover your head with a scarf; nighttime illumination reflected in the water is magical."
            },
            {
                "id": "ATQ_02",
                "name": "Wagah Border Beating Retreat Ceremony",
                "category": "Culture & Heritage",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Attari Border",
                "rating": 4.9,
                "preferred_time": "Evening",
                "description": "Electrifying military drill conducted jointly by Indian BSF and Pakistan Rangers at sunset.",
                "pro_tip": "Reach the border stadium by 3:30 PM to secure prime grandstand seats."
            },
            {
                "id": "ATQ_03",
                "name": "Jallianwala Bagh Memorial & Flame",
                "category": "Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Heritage Core",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Sacred national memorial garden marking the 1919 historic independence sacrifice.",
                "pro_tip": "Preserves bullet marks still visible on red brick boundary walls."
            }
        ]
    },
    "Chandigarh, Punjab": {
        "city_code": "IXC",
        "state": "Punjab",
        "tagline": "The City Beautiful - Le Corbusier's Modernist Marvel",
        "description": "India's best planned green capital, famed for sculptures, rose parks, and lake walks.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.65,
        "attractions": [
            {
                "id": "IXC_01",
                "name": "Nek Chand's Rock Garden",
                "category": "Culture & Art",
                "entry_fee": 30,
                "duration_hours": 2.5,
                "zone": "Sector 1 Civic Belt",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Visionary 40-acre wonderland crafted entirely from domestic and industrial scrap ceramics.",
                "pro_tip": "Wander through the narrow stone corridors opening up to giant cascading courtyards."
            },
            {
                "id": "IXC_02",
                "name": "Sukhna Lake Promenade & Boating",
                "category": "Nature & Relaxation",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Sector 1 Civic Belt",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Scenic 3-sq-km rainfed reservoir at the foothills of the Shivaliks.",
                "pro_tip": "Rent a paddle boat for sunset lake views."
            },
            {
                "id": "IXC_03",
                "name": "Zakir Hussain Rose Garden",
                "category": "Nature",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Sector 16",
                "rating": 4.5,
                "preferred_time": "Morning",
                "description": "Asia's largest rose sanctuary housing 1,600 distinct varieties and medicinal trees.",
                "pro_tip": "Peak flowering season occurs between February and March."
            }
        ]
    },

    # -------------------------------------------------------------
    # 21. RAJASTHAN
    # -------------------------------------------------------------
    "Jaipur, Rajasthan": {
        "city_code": "JPR",
        "state": "Rajasthan",
        "tagline": "The Pink City - Majestic Palaces and Heritage",
        "description": "Capital of Rajasthan, famed for historic forts, vibrant bazaars, and royal architecture.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "JPR_01",
                "name": "Amber Fort & Palace",
                "category": "Heritage",
                "entry_fee": 200,
                "duration_hours": 3.0,
                "zone": "Amer / North",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "16th-century hilltop fort known for artistic Hindu style elements and Sheesh Mahal.",
                "pro_tip": "Visit early morning around 8:30 AM to beat tourist crowds and scorching sun."
            },
            {
                "id": "JPR_02",
                "name": "Hawa Mahal (Palace of Winds)",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 1.5,
                "zone": "Old City / Walled City",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Five-storey pink sandstone palace featuring 953 intricate jharokhas (casements).",
                "pro_tip": "Best photographed from the Wind View Cafe across the street."
            },
            {
                "id": "JPR_03",
                "name": "City Palace & Museum",
                "category": "Heritage",
                "entry_fee": 300,
                "duration_hours": 2.5,
                "zone": "Old City / Walled City",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Royal residence blending Rajput, Mughal, and European architectural wonders.",
                "pro_tip": "Composite ticket includes Jaigarh Fort access within 2 days."
            },
            {
                "id": "JPR_04",
                "name": "Jantar Mantar Astronomical Observatory",
                "category": "Culture & Science",
                "entry_fee": 200,
                "duration_hours": 1.5,
                "zone": "Old City / Walled City",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "UNESCO World Heritage site with nineteen architectural astronomical instruments.",
                "pro_tip": "Hiring a registered audio guide makes the sundials truly come alive."
            },
            {
                "id": "JPR_05",
                "name": "Nahargarh Fort & Sunset Viewpoint",
                "category": "Viewpoint & Heritage",
                "entry_fee": 100,
                "duration_hours": 2.5,
                "zone": "Amer / North",
                "rating": 4.7,
                "preferred_time": "Evening",
                "description": "Perched on the edge of the Aravalli Hills, offering sweeping panoramic sunset views of Jaipur.",
                "pro_tip": "Arrive 1 hour before sunset to grab a spot near the Padao restaurant ramparts."
            },
            {
                "id": "JPR_06",
                "name": "Jal Mahal (Water Palace)",
                "category": "Sightseeing",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "Amer / North",
                "rating": 4.3,
                "preferred_time": "Evening",
                "description": "Poetic palace floating gracefully in the middle of Man Sagar Lake.",
                "pro_tip": "Entry inside is restricted; enjoy evening strolls along the illuminated promenade."
            },
            {
                "id": "JPR_07",
                "name": "Albert Hall State Museum",
                "category": "Culture & Science",
                "entry_fee": 150,
                "duration_hours": 2.0,
                "zone": "Central Jaipur",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Oldest museum of Rajasthan boasting Indo-Saracenic architecture and night illumination.",
                "pro_tip": "Night view with exterior golden floodlights is stunning."
            },
            {
                "id": "JPR_08",
                "name": "Johari Bazaar & Bapu Bazaar Walk",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Old City / Walled City",
                "rating": 4.4,
                "preferred_time": "Evening",
                "description": "Bustling traditional markets for bandhani sarees, mojris, jewelry, and kachoris.",
                "pro_tip": "Keep cash handy and polite bargaining is culturally customary."
            },
            {
                "id": "JPR_09",
                "name": "Birla Mandir (Laxmi Narayan Temple)",
                "category": "Spiritual",
                "entry_fee": 0,
                "duration_hours": 1.0,
                "zone": "Central Jaipur",
                "rating": 4.6,
                "preferred_time": "Morning",
                "description": "Pure white marble temple dedicated to Lord Vishnu and Goddess Lakshmi.",
                "pro_tip": "Serene gardens provide a calm break from city traffic."
            },
            {
                "id": "JPR_10",
                "name": "Chokhi Dhani Ethnic Resort Experience",
                "category": "Culture & Food",
                "entry_fee": 950,
                "duration_hours": 3.5,
                "zone": "South Jaipur",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Immersive Rajasthani village fair with folk dances, camel rides, and unlimited royal thali.",
                "pro_tip": "Plan this on a relaxed evening; starts at 5:30 PM."
            }
        ]
    },
    "Udaipur, Rajasthan": {
        "city_code": "UDR",
        "state": "Rajasthan",
        "tagline": "City of Lakes & Venice of the East",
        "description": "Romantic lakeside kingdom set against the Aravalli Hills with grand palaces and boat rides.",
        "avg_intra_zone_transit_cost": 95,
        "avg_inter_zone_transit_cost": 230,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "UDR_01",
                "name": "City Palace Complex & Crystal Gallery",
                "category": "Heritage",
                "entry_fee": 300,
                "duration_hours": 3.0,
                "zone": "Pichola East Bank",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Rajasthan's largest palace complex perched atop Lake Pichola featuring peacock mosaics.",
                "pro_tip": "Board lake boats directly from Rameshwar Ghat inside the palace."
            },
            {
                "id": "UDR_02",
                "name": "Lake Pichola Sunset Boat Cruise",
                "category": "Relaxation & Viewpoint",
                "entry_fee": 450,
                "duration_hours": 1.5,
                "zone": "Lake Pichola",
                "rating": 4.9,
                "preferred_time": "Evening",
                "description": "Spectacular cruise circling Jag Mandir Island and the floating white Lake Palace.",
                "pro_tip": "Book the 5:00 PM sunset slot for ethereal golden hour reflections."
            },
            {
                "id": "UDR_03",
                "name": "Saheliyon Ki Bari (Garden of Royal Maids)",
                "category": "Nature & Heritage",
                "entry_fee": 50,
                "duration_hours": 1.5,
                "zone": "Fateh Sagar Belt",
                "rating": 4.5,
                "preferred_time": "Afternoon",
                "description": "Ornate historic gardens featuring lotus pools, marble pavilions, and elephant fountains.",
                "pro_tip": "Fountains operate purely on natural water gravity from Fateh Sagar Lake."
            }
        ]
    },

    # -------------------------------------------------------------
    # 22. SIKKIM
    # -------------------------------------------------------------
    "Gangtok & Tsomgo Lake, Sikkim": {
        "city_code": "GTK",
        "state": "Sikkim",
        "tagline": "Himalayan Shangri-La - Monasteries, Glacial Lakes & Kanchenjunga",
        "description": "Clean, eco-conscious mountain capital overlooking snow peaks and prayer flags.",
        "avg_intra_zone_transit_cost": 120,
        "avg_inter_zone_transit_cost": 380,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 1.0,
        "attractions": [
            {
                "id": "GTK_01",
                "name": "Tsomgo (Changu) Lake & Baba Mandir",
                "category": "Nature & Adventure",
                "entry_fee": 150,
                "duration_hours": 3.5,
                "zone": "Nathula Pass Highway",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Glacial lake at 12,300 ft reflecting changing hues according to seasons.",
                "pro_tip": "Special protected area permits (PAP) are required; carry passport photos and ID."
            },
            {
                "id": "GTK_02",
                "name": "Rumtek Dharma Chakra Centre",
                "category": "Spiritual & Heritage",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Rumtek Ridge",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Seat of the Karmapa Lama housing priceless Tibetan religious artwork and golden stupa.",
                "pro_tip": "Admire the monastery courtyard surrounded by monks' study quarters."
            },
            {
                "id": "GTK_03",
                "name": "MG Marg Pedestrian Boulevard & Cable Ropeway",
                "category": "Shopping & Street Food",
                "entry_fee": 120,
                "duration_hours": 2.0,
                "zone": "Central Gangtok",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Litter-free, vehicle-free paved mall with benches, cafes, and momo parlours.",
                "pro_tip": "Take the 1-km bi-cable ropeway from Deorali for bird's-eye views."
            }
        ]
    },
    "Pelling, Sikkim": {
        "city_code": "PLG",
        "state": "Sikkim",
        "tagline": "Closest Views of Kanchenjunga & Glass Skywalks",
        "description": "Peaceful West Sikkim mountain hamlet facing the majestic Mt. Kanchenjunga massif.",
        "avg_intra_zone_transit_cost": 110,
        "avg_inter_zone_transit_cost": 300,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "PLG_01",
                "name": "Pelling Glass Skywalk & Chenrezig Colossus",
                "category": "Viewpoint & Spiritual",
                "entry_fee": 50,
                "duration_hours": 2.0,
                "zone": "Sanga Choeling Ridge",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "India's first glass skywalk hovering over mountain cliffs beneath a 137-ft statue.",
                "pro_tip": "Early morning offers cloudless views of the Kanchenjunga peaks."
            },
            {
                "id": "PLG_02",
                "name": "Pemayangtse Ancient Monastery",
                "category": "Spiritual & Heritage",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Pemayangtse",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "One of Sikkim's oldest premier Nyingma monasteries, built in 1705.",
                "pro_tip": "Houses the famous 7-tiered hand-carved wooden model of Guru Rinpoche's palace."
            },
            {
                "id": "PLG_03",
                "name": "Rabdentse Ruins Ancient Capital Walk",
                "category": "Heritage & Nature",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Rabdentse Forest",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Atmospheric ruins of the second capital of the Kingdom of Sikkim, surrounded by chestnut woods.",
                "pro_tip": "Delightful 15-minute nature walk through bird-filled forest trails."
            }
        ]
    },

    # -------------------------------------------------------------
    # 23. TAMIL NADU
    # -------------------------------------------------------------
    "Chennai & Mahabalipuram, Tamil Nadu": {
        "city_code": "MAA",
        "state": "Tamil Nadu",
        "tagline": "Gateway to the South - Classical Temples & Monolithic Rock Art",
        "description": "Vibrant Dravidian metropolis and 7th-century UNESCO Pallava coastal monuments.",
        "avg_intra_zone_transit_cost": 95,
        "avg_inter_zone_transit_cost": 260,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "MAA_01",
                "name": "Mahabalipuram Shore Temple & Pancha Rathas",
                "category": "Heritage",
                "entry_fee": 40,
                "duration_hours": 3.0,
                "zone": "Mahabalipuram Coastal",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "7th-century UNESCO rock-cut monoliths carved from single granite boulders along the sea.",
                "pro_tip": "Examine 'Arjuna's Penance', one of the world's largest open-air stone bas-reliefs."
            },
            {
                "id": "MAA_02",
                "name": "Kapaleeshwarar Temple (Mylapore)",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Mylapore Core",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Towering rainbow-colored Dravidian gopuram dedicated to Lord Shiva in ancient Mylapore.",
                "pro_tip": "Sip legendary filter coffee and crispy ghee roast dosas at nearby traditional messes."
            },
            {
                "id": "MAA_03",
                "name": "Marina Beach Promenade & Lighthouse",
                "category": "Relaxation",
                "entry_fee": 20,
                "duration_hours": 2.0,
                "zone": "Marina Beachfront",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "World's second longest urban beach buzzing with sea breeze, carousel rides, and sundal snacks.",
                "pro_tip": "Climb up the lighthouse lift for panoramic coastline vistas."
            }
        ]
    },
    "Madurai & Rameswaram, Tamil Nadu": {
        "city_code": "IXM",
        "state": "Tamil Nadu",
        "tagline": "Temple Towers, Pamban Sea Bridge & Holy Confluence",
        "description": "The soul of Tamil heritage from ancient Madurai streets to ocean-swept Rameswaram.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 250,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "IXM_01",
                "name": "Madurai Meenakshi Amman Temple",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Madurai Temple Core",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Historic architectural marvel with 14 monumental gopurams and Hall of 1,000 Pillars.",
                "pro_tip": "Attend the 9:00 PM evening procession when Lord Sundareswarar is escorted to Meenakshi's shrine."
            },
            {
                "id": "IXM_02",
                "name": "Ramanathaswamy Temple & 22 Sacred Wells",
                "category": "Spiritual & Heritage",
                "entry_fee": 25,
                "duration_hours": 2.5,
                "zone": "Rameswaram Island",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Char Dham coastal temple holding the world's longest pillared corridor measuring 1,220 meters.",
                "pro_tip": "Pilgrims bathe in the 22 holy water theerthams inside the temple grounds."
            },
            {
                "id": "IXM_03",
                "name": "Dhanushkodi Ghost Town & Pamban Sea Bridge",
                "category": "Viewpoint & Heritage",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Dhanushkodi Promontory",
                "rating": 4.8,
                "preferred_time": "Evening",
                "description": "Surreal land's end where the Bay of Bengal meets the Indian Ocean, 20 km from Sri Lanka.",
                "pro_tip": "Take the scenic ocean road built right over the sand spit."
            }
        ]
    },

    # -------------------------------------------------------------
    # 24. TELANGANA
    # -------------------------------------------------------------
    "Hyderabad, Telangana": {
        "city_code": "HYD",
        "state": "Telangana",
        "tagline": "City of Pearls - Nizami Grandeur, Biryani & Tech Hub",
        "description": "Historic royal capital of the Qutb Shahis and Nizams, famed for Golconda and pearls.",
        "avg_intra_zone_transit_cost": 95,
        "avg_inter_zone_transit_cost": 240,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.8,
        "attractions": [
            {
                "id": "HYD_01",
                "name": "Charminar & Laad Bazaar Bangles Walk",
                "category": "Heritage & Shopping",
                "entry_fee": 25,
                "duration_hours": 2.0,
                "zone": "Old Walled City",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "1591 iconic four-minaret monument surrounded by traditional pearl and lacquer bangle markets.",
                "pro_tip": "Sample authentic Osmania biscuits and Irani chai at Nimrah Cafe right opposite."
            },
            {
                "id": "HYD_02",
                "name": "Golconda Fort & Acoustic Echo Wonder",
                "category": "Heritage",
                "entry_fee": 25,
                "duration_hours": 3.0,
                "zone": "Golconda Ridge",
                "rating": 4.8,
                "preferred_time": "Afternoon",
                "description": "Massive medieval fortress renowned for the Koh-i-Noor diamond trade and acoustic sound engineering.",
                "pro_tip": "A handclap under the portico dome can be heard clearly a kilometer away at Bala Hissar."
            },
            {
                "id": "HYD_03",
                "name": "Salar Jung Art Museum",
                "category": "Culture & Science",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Old City / Musi",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "One of the world's largest one-man antique collections, home to the Veiled Rebecca sculpture.",
                "pro_tip": "Gather near the 19th-century musical bracket clock at 12:00 noon to watch the mechanical bell striker."
            },
            {
                "id": "HYD_04",
                "name": "Hussain Sagar Lake & Monolithic Buddha Cruise",
                "category": "Relaxation & Viewpoint",
                "entry_fee": 100,
                "duration_hours": 1.5,
                "zone": "Necklace Road",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Heart-shaped 1563 artificial lake with an 18m white granite monolithic Buddha statue in its center.",
                "pro_tip": "Speedboats and ferry launches connect Lumbini Park to the island."
            }
        ]
    },
    "Warangal, Telangana": {
        "city_code": "WGL",
        "state": "Telangana",
        "tagline": "Kakatiya Realm - Carved Gateways & Ramappa Temple",
        "description": "Ancient medieval capital famed for UNESCO temple architecture and carved granite arches.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 190,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.65,
        "attractions": [
            {
                "id": "WGL_01",
                "name": "Ramappa Temple (UNESCO World Heritage Site)",
                "category": "Heritage & Spiritual",
                "entry_fee": 30,
                "duration_hours": 2.5,
                "zone": "Palampet Sanctuary",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "13th-century Kakatiya temple built with floating bricks and carved black basalt bracket figures.",
                "pro_tip": "Described by Marco Polo as the 'brightest star in the galaxy of medieval temples'."
            },
            {
                "id": "WGL_02",
                "name": "Thousand Pillar Temple (Rudreswara Swamy)",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 1.5,
                "zone": "Hanamkonda",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Star-shaped architectural marvel with richly carved monolithic stone pillars.",
                "pro_tip": "Houses a large 6-foot monolithic carved basalt Nandi bull."
            },
            {
                "id": "WGL_03",
                "name": "Warangal Fort & Kakatiya Kala Thoranam",
                "category": "Heritage",
                "entry_fee": 25,
                "duration_hours": 2.0,
                "zone": "Fort Core",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Medieval ruins featuring the four iconic carved stone gateways that form Telangana's emblem.",
                "pro_tip": "Surrounded by tranquil gardens; visit during golden late afternoon."
            }
        ]
    },

    # -------------------------------------------------------------
    # 25. TRIPURA
    # -------------------------------------------------------------
    "Agartala & Neermahal, Tripura": {
        "city_code": "IXA",
        "state": "Tripura",
        "tagline": "Palaces, Lakes & Ancient Rock Relics",
        "description": "Tranquil north-eastern princely kingdom boasting floating lake palaces and giant rock carvings.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "IXA_01",
                "name": "Ujjayanta Royal Palace & State Museum",
                "category": "Heritage & Culture",
                "entry_fee": 20,
                "duration_hours": 2.5,
                "zone": "Agartala City Core",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Stately 1901 Indo-Saracenic palace with Mughal gardens and fountains, named by Rabindranath Tagore.",
                "pro_tip": "Museum displays rare tribal artifacts and royal coronation thrones."
            },
            {
                "id": "IXA_02",
                "name": "Neermahal Floating Water Palace",
                "category": "Heritage & Nature",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Rudrasagar Lake",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Eastern India's only water palace, erected gracefully in the middle of Rudrasagar Lake.",
                "pro_tip": "Motorized boats transfer visitors across the lake to the palace steps."
            },
            {
                "id": "IXA_03",
                "name": "Unakoti Ancient Rock-Cut Shaivite Bas-Reliefs",
                "category": "Heritage & Spiritual",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "Kailashahar Hills",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Sublime 7th-century forest mountain cliffs carved with thousands of colossal Shiva bas-reliefs.",
                "pro_tip": "The central Shiva head (Unakotiswara Kal Bhairava) stands 30 ft tall."
            }
        ]
    },

    # -------------------------------------------------------------
    # 26. UTTAR PRADESH
    # -------------------------------------------------------------
    "Varanasi, Uttar Pradesh": {
        "city_code": "VNS",
        "state": "Uttar Pradesh",
        "tagline": "The Spiritual Heart - Ancient Ghats & Living Traditions",
        "description": "One of the world's oldest continuously inhabited cities on the sacred banks of the River Ganges.",
        "avg_intra_zone_transit_cost": 80,
        "avg_inter_zone_transit_cost": 200,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.6,
        "attractions": [
            {
                "id": "VNS_01",
                "name": "Subah-e-Banaras Morning Boat Tour (Assi to Manikarnika)",
                "category": "Spiritual & Culture",
                "entry_fee": 300,
                "duration_hours": 2.5,
                "zone": "Ghats / Riverside",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Dawn boat rowing along 84 ghats witnessing morning rituals, sunrise prayers, and old palaces.",
                "pro_tip": "Be at Assi Ghat by 5:15 AM to catch the classical music and Vedic chants."
            },
            {
                "id": "VNS_02",
                "name": "Kashi Vishwanath Jyotirlinga Temple & Corridor",
                "category": "Spiritual",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Old City / Godowlia",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Revered golden temple of Lord Shiva and newly modernized grand river corridor.",
                "pro_tip": "Cell phones and leather items are strictly prohibited inside locker counters."
            },
            {
                "id": "VNS_03",
                "name": "Dashashwamedh Ghat Grand Evening Ganga Aarti",
                "category": "Spiritual & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Ghats / Riverside",
                "rating": 4.9,
                "preferred_time": "Evening",
                "description": "Hypnotic synchronised ritual with towering brass multi-tiered lamps, incense, and bells.",
                "pro_tip": "Secure a wooden boat seat facing the ghat 45 minutes prior to 6:30 PM."
            },
            {
                "id": "VNS_04",
                "name": "Sarnath Buddhist Sacred Complex & Museum",
                "category": "Heritage & Spiritual",
                "entry_fee": 50,
                "duration_hours": 3.0,
                "zone": "Sarnath / Outer",
                "rating": 4.7,
                "preferred_time": "Afternoon",
                "description": "Site where Lord Buddha delivered his first sermon; home to the Lion Capital of Ashoka.",
                "pro_tip": "Museum is closed on Fridays; plan accordingly."
            },
            {
                "id": "VNS_05",
                "name": "Old Alleyways Silk Weaving & Food Trail",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Old City / Godowlia",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Wandering through labyrinthine galis for kachori-jalebi, Banarasi paan, and authentic weavers.",
                "pro_tip": "Try famous Malaiyo (winter milk froth dessert) or creamy blue lassi."
            },
            {
                "id": "VNS_06",
                "name": "Ramnagar Fort & Vintage Royal Car Museum",
                "category": "Heritage",
                "entry_fee": 100,
                "duration_hours": 2.0,
                "zone": "Across River / Ramnagar",
                "rating": 4.2,
                "preferred_time": "Afternoon",
                "description": "18th-century sandstone fortress home of the Kashi Naresh, displaying antique armory.",
                "pro_tip": "Stop at the adjacent centuries-old Shiv Prasad Lassi stall outside the gate."
            }
        ]
    },
    "Agra, Uttar Pradesh": {
        "city_code": "AGR",
        "state": "Uttar Pradesh",
        "tagline": "City of Taj - Timeless Mughal Architectural Grandeur",
        "description": "Historic capital of the Mughal Empire housing three UNESCO World Heritage jewels.",
        "avg_intra_zone_transit_cost": 90,
        "avg_inter_zone_transit_cost": 240,
        "transit_time_same_zone_hr": 0.3,
        "transit_time_cross_zone_hr": 0.7,
        "attractions": [
            {
                "id": "AGR_01",
                "name": "Taj Mahal (UNESCO World Heritage Site)",
                "category": "Heritage",
                "entry_fee": 250,
                "duration_hours": 3.0,
                "zone": "Taj Ganj",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "White marble mausoleum built by Emperor Shah Jahan in memory of Mumtaz Mahal.",
                "pro_tip": "Enter from East Gate at sunrise (6:00 AM) to experience ethereal soft dawn light. Closed Fridays."
            },
            {
                "id": "AGR_02",
                "name": "Agra Fort (Red Fort)",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Civil Lines / Fort",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Massive 16th-century red sandstone fortress that served as the principal imperial residence.",
                "pro_tip": "Musamman Burj pavilion gives a spectacular framed view of the Taj across the Yamuna."
            },
            {
                "id": "AGR_03",
                "name": "Mehtab Bagh (Moonlight Garden Sunset)",
                "category": "Viewpoint & Nature",
                "entry_fee": 25,
                "duration_hours": 1.5,
                "zone": "Across River / Mehtab",
                "rating": 4.5,
                "preferred_time": "Evening",
                "description": "Charbagh complex aligned directly across the Yamuna river offering reflection views of the Taj.",
                "pro_tip": "The ultimate sunset photo spot without the inner monument crowds."
            },
            {
                "id": "AGR_04",
                "name": "Fatehpur Sikri Royal Complex & Buland Darwaza",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 3.5,
                "zone": "Outer Agra / Sikri",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Emperor Akbar's abandoned utopian red sandstone capital city and colossal 54m gateway.",
                "pro_tip": "Located 36 km west of Agra; allow 1 hour travel each way."
            },
            {
                "id": "AGR_05",
                "name": "Tomb of I'timād-ud-Daulah (Baby Taj)",
                "category": "Heritage",
                "entry_fee": 30,
                "duration_hours": 1.5,
                "zone": "Across River / Mehtab",
                "rating": 4.4,
                "preferred_time": "Afternoon",
                "description": "Delicate jewel-box marble tomb featuring the first extensive pietra dura inlay in India.",
                "pro_tip": "Much quieter and more intimate than the primary monuments."
            },
            {
                "id": "AGR_06",
                "name": "Sadar Bazaar Walking & Petha Tasting",
                "category": "Shopping & Street Food",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Civil Lines / Fort",
                "rating": 4.3,
                "preferred_time": "Evening",
                "description": "Lively downtown bazaar famous for leather handicrafts, Mughlai chaat, and Panchhi Petha.",
                "pro_tip": "Sample unique varieties: Kesar, Angoori, and Chocolate petha."
            }
        ]
    },

    # -------------------------------------------------------------
    # 27. UTTARAKHAND
    # -------------------------------------------------------------
    "Rishikesh & Haridwar, Uttarakhand": {
        "city_code": "RSK",
        "state": "Uttarakhand",
        "tagline": "Yoga Capital of the World & Gateway to Garhwal Himalayas",
        "description": "Holy riverbanks where the emerald Ganges emerges from the Himalayan foothills.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 220,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "RSK_01",
                "name": "Har Ki Pauri Evening Grand Ganga Aarti",
                "category": "Spiritual & Culture",
                "entry_fee": 0,
                "duration_hours": 2.5,
                "zone": "Haridwar Ghats",
                "rating": 4.9,
                "preferred_time": "Evening",
                "description": "Celebrated sacred river ghat where priests wave colossal flaming multi-tiered brass lamps.",
                "pro_tip": "Arrive by 5:15 PM on the opposite bank steps for the best viewing angle."
            },
            {
                "id": "RSK_02",
                "name": "Laxman Jhula & Ram Jhula Suspension Bridges",
                "category": "Heritage & Sightseeing",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Tapovan / Swargashram",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Iconic iron suspension bridges suspended across the emerald Ganges.",
                "pro_tip": "Cross on foot while observing local sadhus and mountain reflections."
            },
            {
                "id": "RSK_03",
                "name": "Shivpuri White Water River Rafting",
                "category": "Adventure & Nature",
                "entry_fee": 650,
                "duration_hours": 3.5,
                "zone": "Shivpuri Valley",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Thrilling Grade III+ river rapids like Roller Coaster, Golf Course, and Club House.",
                "pro_tip": "Strictly follow certified river instructor safety gear guidelines."
            },
            {
                "id": "RSK_04",
                "name": "The Beatles Ashram (Chaurasi Kutia)",
                "category": "Culture & Art",
                "entry_fee": 150,
                "duration_hours": 2.0,
                "zone": "Swargashram Forest",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "Forest meditation retreat where The Beatles composed over 40 songs in 1968.",
                "pro_tip": "Explore the stone meditation igloos and psychedelic wall murals."
            }
        ]
    },
    "Nainital & Corbett, Uttarakhand": {
        "city_code": "NNT",
        "state": "Uttarakhand",
        "tagline": "Emerald Lakes & Royal Bengal Tiger Safari",
        "description": "Eye-shaped Himalayan lake hill station paired with India's oldest national park.",
        "avg_intra_zone_transit_cost": 100,
        "avg_inter_zone_transit_cost": 280,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.9,
        "attractions": [
            {
                "id": "NNT_01",
                "name": "Naini Lake Boating & Mall Road",
                "category": "Relaxation & Nature",
                "entry_fee": 210,
                "duration_hours": 2.0,
                "zone": "Nainital Lakefront",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Natural pear-shaped mountain lake surrounded by pine-covered hills.",
                "pro_tip": "Hire colorful wooden rowing boats and visit Naina Devi Temple by the northern shore."
            },
            {
                "id": "NNT_02",
                "name": "Jim Corbett National Park Safari",
                "category": "Adventure & Nature",
                "entry_fee": 750,
                "duration_hours": 3.5,
                "zone": "Corbett Tiger Reserve",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Oldest national park in India, renowned for Royal Bengal tigers, wild elephants, and sal forests.",
                "pro_tip": "Book jeep safari permits well in advance for Bijrani or Jhirna zones."
            },
            {
                "id": "NNT_03",
                "name": "Snow View Point & Ropeway Cable Car",
                "category": "Viewpoint & Nature",
                "entry_fee": 200,
                "duration_hours": 2.0,
                "zone": "Nainital Ridge",
                "rating": 4.6,
                "preferred_time": "Afternoon",
                "description": "High ridge offering sweeping panoramic vistas of Nanda Devi and Trishul peaks.",
                "pro_tip": "Aerial ropeway departs near Mallital."
            }
        ]
    },

    # -------------------------------------------------------------
    # 28. WEST BENGAL
    # -------------------------------------------------------------
    "Kolkata, West Bengal": {
        "city_code": "CCU",
        "state": "West Bengal",
        "tagline": "City of Joy - Colonial Splendour, Culture & Tram Heritage",
        "description": "Grand cultural capital on the Hooghly famed for art, literature, and street gastronomy.",
        "avg_intra_zone_transit_cost": 85,
        "avg_inter_zone_transit_cost": 210,
        "transit_time_same_zone_hr": 0.35,
        "transit_time_cross_zone_hr": 0.75,
        "attractions": [
            {
                "id": "CCU_01",
                "name": "Victoria Memorial Hall & Gardens",
                "category": "Heritage",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Maidan / Central",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Colossal white Makrana marble monument dedicated to Queen Victoria, surrounded by 64 acres of gardens.",
                "pro_tip": "Inspect the royal gallery housing rare colonial paintings and Queen's piano."
            },
            {
                "id": "CCU_02",
                "name": "Howrah Bridge & Mullick Ghat Flower Market",
                "category": "Heritage & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Hooghly Riverfront",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "Iconic cantilever truss bridge over the Hooghly river and Asia's largest fragrant flower bazaar.",
                "pro_tip": "Early morning (6:30 AM) reveals vibrant cascades of marigold garlands and wrestlers practicing."
            },
            {
                "id": "CCU_03",
                "name": "Dakshineswar Kali Temple & Belur Math Ferry",
                "category": "Spiritual & Heritage",
                "entry_fee": 0,
                "duration_hours": 3.0,
                "zone": "North Riverfront",
                "rating": 4.8,
                "preferred_time": "Afternoon",
                "description": "19th-century Navaratna temple where Ramakrishna Paramahamsa served as priest.",
                "pro_tip": "Take the local river ferry across to Belur Math (Ramakrishna Mission headquarters)."
            },
            {
                "id": "CCU_04",
                "name": "Park Street Cultural Dining & Heritage Coffee House",
                "category": "Food & Culture",
                "entry_fee": 0,
                "duration_hours": 2.0,
                "zone": "Park Street",
                "rating": 4.6,
                "preferred_time": "Evening",
                "description": "Celebrated boulevard featuring legendary colonial tearooms, chelo kebabs, and live jazz.",
                "pro_tip": "Visit Flurys for English breakfast and Peter Cat for Chelo Kababs."
            }
        ]
    },
    "Darjeeling & Sundarbans, West Bengal": {
        "city_code": "DAJ",
        "state": "West Bengal",
        "tagline": "Queen of the Hills & Royal Bengal Mangrove Delta",
        "description": "From world-famous orthodox black tea gardens to the UNESCO tidal mangrove delta.",
        "avg_intra_zone_transit_cost": 110,
        "avg_inter_zone_transit_cost": 320,
        "transit_time_same_zone_hr": 0.4,
        "transit_time_cross_zone_hr": 0.9,
        "attractions": [
            {
                "id": "DAJ_01",
                "name": "Tiger Hill Sunrise over Mount Kanchenjunga",
                "category": "Viewpoint & Nature",
                "entry_fee": 50,
                "duration_hours": 2.5,
                "zone": "Darjeeling Ridge",
                "rating": 4.9,
                "preferred_time": "Morning",
                "description": "Witness the first golden rays of sunlight illuminate the world's 3rd highest mountain peak.",
                "pro_tip": "Depart hotel by 4:00 AM; bring warm gloves and caps."
            },
            {
                "id": "DAJ_02",
                "name": "Darjeeling Himalayan Railway (UNESCO Toy Train)",
                "category": "Heritage & Experience",
                "entry_fee": 500,
                "duration_hours": 2.0,
                "zone": "Darjeeling Ridge",
                "rating": 4.8,
                "preferred_time": "Morning",
                "description": "Chugging steam locomotive journey looping around the Batasia Loop and Ghoom station.",
                "pro_tip": "Book the 10:00 AM steam joyride round trip."
            },
            {
                "id": "DAJ_03",
                "name": "Sundarbans Mangrove Delta & Tiger Watchtower Boat Safari",
                "category": "Adventure & Nature",
                "entry_fee": 450,
                "duration_hours": 4.0,
                "zone": "Sundarbans Biosphere",
                "rating": 4.7,
                "preferred_time": "Morning",
                "description": "UNESCO World Heritage tidal halophytic mangrove forest, home to estuarine crocodiles and tigers.",
                "pro_tip": "Board motorized boats from Godkhali to Sajnekhali watchtower."
            }
        ]
    }
}

# -------------------------------------------------------------
# Mapping of all 28 States to their Destinations
# -------------------------------------------------------------
STATE_DESTINATIONS_MAP: Dict[str, List[str]] = {state: [] for state in ALL_28_INDIAN_STATES}

for dest_name, details in SAMPLE_DESTINATIONS.items():
    state_name = details.get("state")
    if state_name and state_name in STATE_DESTINATIONS_MAP:
        STATE_DESTINATIONS_MAP[state_name].append(dest_name)


def validate_all_28_states_present() -> Dict[str, Any]:
    """
    Validates that:
    1. Exactly all 28 official Indian States are represented in the dataset.
    2. Each state has at least one tourist destination.
    3. Each destination contains at least 3 attractions with required fields.
    Returns validation summary dictionary or raises ValueError.
    """
    missing_states = [state for state in ALL_28_INDIAN_STATES if state not in STATE_DESTINATIONS_MAP]
    if missing_states:
        raise ValueError(f"Validation Failed: Missing states in map: {missing_states}")

    empty_states = [state for state, dests in STATE_DESTINATIONS_MAP.items() if len(dests) == 0]
    if empty_states:
        raise ValueError(f"Validation Failed: The following states have zero destinations: {empty_states}")

    total_destinations = len(SAMPLE_DESTINATIONS)
    total_attractions = sum(len(d["attractions"]) for d in SAMPLE_DESTINATIONS.values())

    # Validate destination properties
    for dest_name, data in SAMPLE_DESTINATIONS.items():
        if "state" not in data or data["state"] not in ALL_28_INDIAN_STATES:
            raise ValueError(f"Destination '{dest_name}' has invalid or missing state: {data.get('state')}")
        if len(data.get("attractions", [])) < 3:
            raise ValueError(f"Destination '{dest_name}' must have at least 3 attractions for valid planning.")
        for req_field in ["avg_intra_zone_transit_cost", "avg_inter_zone_transit_cost", "transit_time_same_zone_hr", "transit_time_cross_zone_hr"]:
            if req_field not in data:
                raise ValueError(f"Destination '{dest_name}' is missing required transit field: {req_field}")

    return {
        "status": "VALID",
        "total_states": len(ALL_28_INDIAN_STATES),
        "total_destinations": total_destinations,
        "total_attractions": total_attractions,
        "states": list(ALL_28_INDIAN_STATES)
    }


STANDARD_DAILY_COSTS = {
    "food": {
        "Budget (Local / Street / Thali)": 400,
        "Moderate (Casual Cafes & Dhabas)": 750,
        "Comfort (Fine Dining & Multi-Cuisine)": 1400
    },
    "accommodation": {
        "Backpacker Hostel / Dorm": 600,
        "Budget Guesthouse / 2-Star": 1300,
        "Comfort Boutique / 3-Star": 2600,
        "Skip Lodging (Already booked / Day Trip)": 0
    },
    "safety_buffer_pct": 0.10  # 10% emergency buffer
}
