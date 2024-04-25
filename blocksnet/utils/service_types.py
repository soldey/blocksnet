"""
Default service types used in ``City`` model
"""

SERVICE_TYPES = [
    {
        "code": "3.5.1",
        "name": "school",
        "demand": 120,
        "accessibility": 15,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 250, "area": 12000, "is_integrated": False, "parking_area": 0},
            {"capacity": 300, "area": 11000, "is_integrated": False, "parking_area": 0},
            {"capacity": 600, "area": 13000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1100, "area": 18000, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 2000, "is_integrated": True, "parking_area": 200},
            {"capacity": 300, "area": 3600, "is_integrated": True, "parking_area": 300},
            {"capacity": 600, "area": 8000, "is_integrated": True, "parking_area": 600},
            {"capacity": 1100, "area": 11000, "is_integrated": True, "parking_area": 1000},
        ],
    },
    {
        "code": "3.5.1",
        "name": "kindergarten",
        "demand": 61,
        "accessibility": 7,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 180, "area": 7200, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 14400, "is_integrated": False, "parking_area": 0},
            {"capacity": 280, "area": 11000, "is_integrated": False, "parking_area": 0},
            {"capacity": 180, "area": 5400, "is_integrated": True, "parking_area": 250},
            {"capacity": 250, "area": 7600, "is_integrated": True, "parking_area": 300},
            {"capacity": 280, "area": 8400, "is_integrated": True, "parking_area": 320},
        ],
    },
    {
        "code": "3.4.2",
        "name": "hospital",
        "demand": 9,
        "accessibility": 60,
        "land_use": ["residential", "business", "special"],
        "bricks": [
            {"capacity": 110, "area": 3000, "is_integrated": False, "parking_area": 0},
            {"capacity": 400, "area": 25000, "is_integrated": False, "parking_area": 0},
            {"capacity": 925, "area": 62000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1200, "area": 58000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "3.4.1",
        "name": "polyclinic",
        "demand": 13,
        "accessibility": 10,
        "land_use": ["residential", "business", "special", "industrial"],
        "bricks": [
            {"capacity": 100, "area": 1500, "is_integrated": False, "parking_area": 0},
            {"capacity": 150, "area": 2100, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 3400, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 6500, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 1200, "is_integrated": True, "parking_area": 125},
            {"capacity": 150, "area": 1700, "is_integrated": True, "parking_area": 150},
            {"capacity": 250, "area": 2600, "is_integrated": True, "parking_area": 200},
            {"capacity": 500, "area": 5000, "is_integrated": True, "parking_area": 250},
        ],
    },
    {
        "code": "5.1.3",
        "name": "pitch",
        "demand": 10,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 10, "area": 150, "is_integrated": False, "parking_area": 0},
            {"capacity": 32, "area": 6000, "is_integrated": False, "parking_area": 0},
            {"capacity": 48, "area": 8000, "is_integrated": False, "parking_area": 0},
            {"capacity": 10, "area": 80, "is_integrated": True, "parking_area": 50},
            {"capacity": 32, "area": 5000, "is_integrated": True, "parking_area": 150},
            {"capacity": 48, "area": 7000, "is_integrated": True, "parking_area": 250},
        ],
    },
    {
        "code": "5.1.2",
        "name": "swimming_pool",
        "demand": 8,
        "accessibility": 30,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 50, "area": 7000, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 12000, "is_integrated": False, "parking_area": 0},
            {"capacity": 300, "area": 32000, "is_integrated": False, "parking_area": 0},
            {"capacity": 30, "area": 2000, "is_integrated": True, "parking_area": 125},
            {"capacity": 50, "area": 3000, "is_integrated": True, "parking_area": 220},
            {"capacity": 100, "area": 7000, "is_integrated": True, "parking_area": 500},
        ],
    },
    {
        "code": "5.1.1",
        "name": "stadium",
        "demand": 10,
        "accessibility": 30,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 2000, "area": 127500, "is_integrated": False, "parking_area": 0},
            {"capacity": 21000, "area": 283000, "is_integrated": False, "parking_area": 0},
            {"capacity": 62300, "area": 701000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "3.6.1",
        "name": "theatre",
        "demand": 6,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 800, "area": 5000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1200, "area": 7000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1600, "area": 11000, "is_integrated": False, "parking_area": 0},
            {"capacity": 890, "area": 4000, "is_integrated": True, "parking_area": 3250},
            {"capacity": 1600, "area": 7000, "is_integrated": True, "parking_area": 6000},
            {"capacity": 1400, "area": 11000, "is_integrated": True, "parking_area": 5000},
        ],
    },
    {
        "code": "3.6.1",
        "name": "museum",
        "demand": 3,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 1000, "area": 12000, "is_integrated": False, "parking_area": 0},
            {"capacity": 3500, "area": 132000, "is_integrated": False, "parking_area": 0},
            {"capacity": 10000, "area": 233000, "is_integrated": False, "parking_area": 0},
            {"capacity": 200, "area": 500, "is_integrated": True, "parking_area": 3250},
            {"capacity": 700, "area": 2500, "is_integrated": True, "parking_area": 1870},
            {"capacity": 1000, "area": 8000, "is_integrated": True, "parking_area": 2750},
        ],
    },
    {
        "code": "3.6.1",
        "name": "cinema",
        "demand": 9,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 680, "area": 2500, "is_integrated": False, "parking_area": 0},
            {"capacity": 560, "area": 2000, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 1500, "is_integrated": True, "parking_area": 1300},
            {"capacity": 760, "area": 2500, "is_integrated": True, "parking_area": 2000},
            {"capacity": 1000, "area": 3200, "is_integrated": True, "parking_area": 2800},
        ],
    },
    {
        "code": "4.2",
        "name": "mall",
        "demand": 8,
        "accessibility": 30,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 7000, "area": 17000, "is_integrated": False, "parking_area": 0},
            {"capacity": 10000, "area": 22000, "is_integrated": False, "parking_area": 0},
            {"capacity": 18000, "area": 37000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1000, "area": 800, "is_integrated": True, "parking_area": 500},
            {"capacity": 4000, "area": 4000, "is_integrated": True, "parking_area": 2500},
            {"capacity": 10000, "area": 13000, "is_integrated": True, "parking_area": 8100},
        ],
    },
    {
        "code": "4.4",
        "name": "convenience",
        "demand": 180,
        "accessibility": 5,
        "land_use": ["residential", "business", "industrial"],
        "bricks": [
            {"capacity": 50, "area": 30, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 65, "is_integrated": False, "parking_area": 0},
            {"capacity": 160, "area": 80, "is_integrated": False, "parking_area": 0},
            {"capacity": 50, "area": 25, "is_integrated": True, "parking_area": 50},
            {"capacity": 100, "area": 50, "is_integrated": True, "parking_area": 50},
            {"capacity": 180, "area": 75, "is_integrated": True, "parking_area": 50},
        ],
    },
    {
        "code": "4.4",
        "name": "supermarket",
        "demand": 900,
        "accessibility": 15,
        "land_use": ["residential", "business", "industrial"],
        "bricks": [
            {"capacity": 200, "area": 150, "is_integrated": False, "parking_area": 0},
            {"capacity": 1500, "area": 300, "is_integrated": False, "parking_area": 0},
            {"capacity": 1000, "area": 700, "is_integrated": False, "parking_area": 0},
            {"capacity": 3500, "area": 2500, "is_integrated": False, "parking_area": 0},
            {"capacity": 200, "area": 150, "is_integrated": True, "parking_area": 75},
            {"capacity": 500, "area": 300, "is_integrated": True, "parking_area": 125},
            {"capacity": 1000, "area": 700, "is_integrated": True, "parking_area": 250},
        ],
    },
    {
        "code": "12.1",
        "name": "cemetery",
        "demand": 96,
        "accessibility": 40,
        "land_use": ["special"],
        "bricks": [
            {"capacity": 3200, "area": 86000, "is_integrated": False, "parking_area": 0},
            {"capacity": 10800, "area": 270000, "is_integrated": False, "parking_area": 0},
            {"capacity": 21000, "area": 510000, "is_integrated": False, "parking_area": 0},
            {"capacity": 280000, "area": 700000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "3.7.1",
        "name": "religion",
        "demand": 10,
        "accessibility": 30,
        "land_use": ["residential", "business", "special"],
        "bricks": [
            {"capacity": 1300, "area": 18000, "is_integrated": False, "parking_area": 0},
            {"capacity": 2700, "area": 46500, "is_integrated": False, "parking_area": 0},
            {"capacity": 3000, "area": 53000, "is_integrated": False, "parking_area": 0},
            {"capacity": 6000, "area": 100000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "4.3",
        "name": "market",
        "demand": 800,
        "accessibility": 30,
        "land_use": ["residential", "business", "industrial", "agriculture"],
        "bricks": [
            {"capacity": 15000, "area": 11000, "is_integrated": False, "parking_area": 0},
            {"capacity": 21000, "area": 30000, "is_integrated": False, "parking_area": 0},
            {"capacity": 35000, "area": 50000, "is_integrated": False, "parking_area": 0},
            {"capacity": 50000, "area": 140000, "is_integrated": False, "parking_area": 0},
            {"capacity": 2500, "area": 270, "is_integrated": True, "parking_area": 170},
            {"capacity": 9100, "area": 10000, "is_integrated": True, "parking_area": 625},
            {"capacity": 29200, "area": 32000, "is_integrated": True, "parking_area": 2000},
        ],
    },
    {
        "code": "4.8.1",
        "name": "bowling_alley",
        "demand": 9,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 80, "area": 700, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 2000, "is_integrated": False, "parking_area": 0},
            {"capacity": 900, "area": 7000, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 700, "is_integrated": True, "parking_area": 250},
            {"capacity": 300, "area": 2000, "is_integrated": True, "parking_area": 750},
            {"capacity": 1000, "area": 7000, "is_integrated": True, "parking_area": 2500},
        ],
    },
    {
        "code": "3.5.2",
        "name": "university",
        "demand": 13,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 500, "area": 14000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1000, "area": 25000, "is_integrated": False, "parking_area": 0},
            {"capacity": 2500, "area": 65000, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 5500, "is_integrated": True, "parking_area": 350},
            {"capacity": 400, "area": 10000, "is_integrated": True, "parking_area": 390},
            {"capacity": 700, "area": 14000, "is_integrated": True, "parking_area": 7600},
        ],
    },
    {
        "code": "2.1.1",
        "name": "playground",
        "demand": 2,
        "accessibility": 4,
        "land_use": ["residential"],
        "bricks": [
            {"capacity": 20, "area": 50, "is_integrated": False, "parking_area": 0},
            {"capacity": 28, "area": 70, "is_integrated": False, "parking_area": 0},
            {"capacity": 45, "area": 100, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "4.2",
        "name": "pharmacy",
        "demand": 15,
        "accessibility": 15,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 30, "area": 40, "is_integrated": False, "parking_area": 0},
            {"capacity": 50, "area": 63, "is_integrated": False, "parking_area": 0},
            {"capacity": 70, "area": 85, "is_integrated": False, "parking_area": 0},
            {"capacity": 20, "area": 25, "is_integrated": True, "parking_area": 50},
            {"capacity": 40, "area": 40, "is_integrated": True, "parking_area": 95},
            {"capacity": 60, "area": 60, "is_integrated": True, "parking_area": 140},
        ],
    },
    {
        "code": "4.9.1.1",
        "name": "fuel",
        "demand": 33,
        "accessibility": 60,
        "land_use": ["residential", "business", "special", "industrial", "agriculture", "transport"],
        "bricks": [
            {"capacity": 30, "area": 40, "is_integrated": False, "parking_area": 0},
            {"capacity": 50, "area": 63, "is_integrated": False, "parking_area": 0},
            {"capacity": 70, "area": 85, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "1.11",
        "name": "beach",
        "demand": 1000,
        "accessibility": 60,
        "land_use": ["recreation"],
        "bricks": [
            {"capacity": 480, "area": 1440, "is_integrated": False, "parking_area": 0},
            {"capacity": 1000, "area": 3100, "is_integrated": False, "parking_area": 0},
            {"capacity": 2400, "area": 7300, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "7.12",
        "name": "train_building",
        "demand": 33,
        "accessibility": 60,
        "land_use": ["business", "recreation", "industrial", "transport"],
        "bricks": [
            {"capacity": 25000, "area": 10600, "is_integrated": False, "parking_area": 0},
            {"capacity": 16000, "area": 17200, "is_integrated": False, "parking_area": 0},
            {"capacity": 37000, "area": 20000, "is_integrated": False, "parking_area": 0},
            {"capacity": 68000, "area": 22000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "4.5",
        "name": "bank",
        "demand": 20,
        "accessibility": 30,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 250, "area": 450, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 800, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 400, "is_integrated": True, "parking_area": 325},
            {"capacity": 500, "area": 750, "is_integrated": True, "parking_area": 580},
        ],
    },
    {
        "code": "4.1",
        "name": "lawyer",
        "demand": 14,
        "accessibility": 30,
        "land_use": ["residential", "business", "industrial"],
        "bricks": [
            {"capacity": 250, "area": 450, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 800, "is_integrated": False, "parking_area": 0},
            {"capacity": 250, "area": 400, "is_integrated": True, "parking_area": 125},
            {"capacity": 500, "area": 700, "is_integrated": True, "parking_area": 250},
        ],
    },
    {
        "code": "4.6",
        "name": "cafe",
        "demand": 25,
        "accessibility": 15,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 25, "area": 1500, "is_integrated": False, "parking_area": 200},
            {"capacity": 45, "area": 750, "is_integrated": False, "parking_area": 375},
            {"capacity": 90, "area": 380, "is_integrated": False, "parking_area": 1100},
            {"capacity": 65, "area": 280, "is_integrated": False, "parking_area": 875},
            {"capacity": 30, "area": 1500, "is_integrated": True, "parking_area": 200},
            {"capacity": 50, "area": 750, "is_integrated": True, "parking_area": 375},
            {"capacity": 100, "area": 380, "is_integrated": True, "parking_area": 1100},
            {"capacity": 70, "area": 280, "is_integrated": True, "parking_area": 875},
        ],
    },
    {
        "code": "7.6",
        "name": "subway_entrance",
        "demand": 408,
        "accessibility": 15,
        "land_use": ["residential", "business", "recreation", "industrial", "agriculture", "transport"],
        "bricks": [
            {"capacity": 30000, "area": 14000, "is_integrated": False, "parking_area": 0},
            {"capacity": 50000, "area": 15000, "is_integrated": False, "parking_area": 0},
            {"capacity": 65000, "area": 17000, "is_integrated": False, "parking_area": 0},
            {"capacity": 30000, "area": 14000, "is_integrated": True, "parking_area": 500},
            {"capacity": 50000, "area": 15000, "is_integrated": True, "parking_area": 2500},
            {"capacity": 65000, "area": 17000, "is_integrated": True, "parking_area": 8100},
        ],
    },
    {
        "code": "3.2.2",
        "name": "multifunctional_center",
        "demand": 408,
        "accessibility": 15,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 80, "area": 700, "is_integrated": True, "parking_area": 400},
            {"capacity": 100, "area": 1000, "is_integrated": True, "parking_area": 600},
            {"capacity": 200, "area": 1200, "is_integrated": True, "parking_area": 700},
        ],
    },
    {
        "code": "3.3",
        "name": "hairdresser",
        "demand": 10,
        "accessibility": 15,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 20, "area": 600, "is_integrated": False, "parking_area": 0},
            {"capacity": 40, "area": 1000, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 3000, "is_integrated": False, "parking_area": 0},
            {"capacity": 20, "area": 400, "is_integrated": True, "parking_area": 250},
            {"capacity": 40, "area": 800, "is_integrated": True, "parking_area": 300},
            {"capacity": 100, "area": 2000, "is_integrated": True, "parking_area": 400},
        ],
    },
    {
        "code": "4.6",
        "name": "restaurant",
        "demand": 71,
        "accessibility": 30,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 45, "area": 200, "is_integrated": False, "parking_area": 0},
            {"capacity": 65, "area": 270, "is_integrated": False, "parking_area": 0},
            {"capacity": 90, "area": 400, "is_integrated": False, "parking_area": 0},
            {"capacity": 185, "area": 800, "is_integrated": False, "parking_area": 0},
            {"capacity": 50, "area": 200, "is_integrated": True, "parking_area": 250},
            {"capacity": 70, "area": 270, "is_integrated": True, "parking_area": 340},
            {"capacity": 100, "area": 400, "is_integrated": True, "parking_area": 500},
            {"capacity": 200, "area": 800, "is_integrated": True, "parking_area": 1000},
        ],
    },
    {
        "code": "4.6",
        "name": "bar",
        "demand": 25,
        "accessibility": 15,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 30, "area": 600, "is_integrated": False, "parking_area": 0},
            {"capacity": 50, "area": 100, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 350, "is_integrated": False, "parking_area": 0},
            {"capacity": 30, "area": 400, "is_integrated": True, "parking_area": 150},
            {"capacity": 50, "area": 90, "is_integrated": True, "parking_area": 25},
            {"capacity": 100, "area": 250, "is_integrated": True, "parking_area": 90},
        ],
    },
    {
        "code": "3.6.2",
        "name": "park",
        "demand": 150,
        "accessibility": 30,
        "land_use": ["recreation"],
        "bricks": [
            {"capacity": 270, "area": 120000, "is_integrated": False, "parking_area": 0},
            {"capacity": 2100, "area": 680000, "is_integrated": False, "parking_area": 0},
            {"capacity": 5500, "area": 1680000, "is_integrated": False, "parking_area": 0},
            {"capacity": 5480, "area": 960000, "is_integrated": False, "parking_area": 0},
            {"capacity": 17800, "area": 1750000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "3.8.1",
        "name": "government",
        "demand": 1,
        "accessibility": 60,
        "land_use": ["business", "residential"],
        "bricks": [
            {"capacity": 100, "area": 800, "is_integrated": False, "parking_area": 0},
            {"capacity": 150, "area": 1350, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 3800, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "4.1",
        "name": "recruitment",
        "demand": 15,
        "accessibility": 30,
        "land_use": ["residential", "business", "industrial"],
        "bricks": [
            {"capacity": 460, "area": 2300, "is_integrated": True, "parking_area": 125},
            {"capacity": 540, "area": 3100, "is_integrated": True, "parking_area": 168},
            {"capacity": 600, "area": 4000, "is_integrated": True, "parking_area": 220},
        ],
    },
    {
        "code": "4.7",
        "name": "hotel",
        "demand": 9,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 300, "area": 24000, "is_integrated": False, "parking_area": 0},
            {"capacity": 500, "area": 27000, "is_integrated": False, "parking_area": 0},
            {"capacity": 900, "area": 32000, "is_integrated": False, "parking_area": 0},
            {"capacity": 1500, "area": 40000, "is_integrated": False, "parking_area": 0},
            {"capacity": 2200, "area": 77000, "is_integrated": False, "parking_area": 0},
            {"capacity": 300, "area": 24000, "is_integrated": True, "parking_area": 150},
            {"capacity": 500, "area": 27000, "is_integrated": True, "parking_area": 170},
            {"capacity": 900, "area": 32000, "is_integrated": True, "parking_area": 200},
            {"capacity": 1500, "area": 40000, "is_integrated": True, "parking_area": 250},
        ],
    },
    {
        "code": "3.6.3",
        "name": "zoo",
        "demand": 2,
        "accessibility": 60,
        "land_use": ["business"],
        "bricks": [
            {"capacity": 2975, "area": 72000, "is_integrated": False, "parking_area": 0},
            {"capacity": 100, "area": 3500, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "3.6.3",
        "name": "circus",
        "demand": 1,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation", "special"],
        "bricks": [
            {"capacity": 400, "area": 50, "is_integrated": True, "parking_area": 50},
            {"capacity": 480, "area": 60, "is_integrated": True, "parking_area": 600},
            {"capacity": 800, "area": 100, "is_integrated": True, "parking_area": 100},
        ],
    },
    {
        "code": "3.2.3",
        "name": "post",
        "demand": 933,
        "accessibility": 10,
        "land_use": ["residential", "business", "recreation", "special"],
        "bricks": [
            {"capacity": 400, "area": 50, "is_integrated": True, "parking_area": 50},
            {"capacity": 480, "area": 60, "is_integrated": True, "parking_area": 600},
            {"capacity": 800, "area": 100, "is_integrated": True, "parking_area": 100},
        ],
    },
    {
        "code": "8.3",
        "name": "police",
        "demand": 5,
        "accessibility": 10,
        "land_use": [
            "residential",
            "business",
            "recreation",
            "special",
            "industrial",
            "agriculture",
            "transport",
        ],
        "bricks": [
            {"capacity": 60, "area": 700, "is_integrated": False, "parking_area": 0},
            {"capacity": 90, "area": 1100, "is_integrated": False, "parking_area": 0},
            {"capacity": 450, "area": 5500, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "12.0.2",
        "name": "dog_park",
        "demand": 53,
        "accessibility": 15,
        "land_use": [
            "residential",
            "business",
            "recreation",
            "special",
            "industrial",
            "agriculture",
            "transport",
        ],
        "bricks": [
            {"capacity": 106, "area": 400, "is_integrated": False, "parking_area": 0},
            {"capacity": 159, "area": 600, "is_integrated": False, "parking_area": 0},
            {"capacity": 265, "area": 1000, "is_integrated": False, "parking_area": 0},
        ],
    },
    {
        "code": "4.7",
        "name": "hostel",
        "demand": 9,
        "accessibility": 60,
        "land_use": ["residential", "business", "recreation"],
        "bricks": [
            {"capacity": 200, "area": 1600, "is_integrated": False, "parking_area": 0},
            {"capacity": 20, "area": 100, "is_integrated": True, "parking_area": 125},
            {"capacity": 40, "area": 200, "is_integrated": True, "parking_area": 250},
            {"capacity": 60, "area": 350, "is_integrated": True, "parking_area": 400},
        ],
    },
    {
        "code": "4.6",
        "name": "bakery",
        "demand": 8,
        "accessibility": 10,
        "land_use": ["residential", "business"],
        "bricks": [
            {"capacity": 150, "area": 70, "is_integrated": True, "parking_area": 50},
            {"capacity": 200, "area": 90, "is_integrated": True, "parking_area": 60},
            {"capacity": 300, "area": 120, "is_integrated": True, "parking_area": 80},
        ],
    },
    {
        "code": "2.7.1",
        "name": "parking",
        "demand": 378,
        "accessibility": 7,
        "land_use": ["residential"],
        "bricks": [
            {"capacity": 50, "area": 1250, "is_integrated": False, "parking_area": 0},
            {"capacity": 190, "area": 4750, "is_integrated": False, "parking_area": 0},
            {"capacity": 330, "area": 8250, "is_integrated": False, "parking_area": 0},
        ],
    },
]
