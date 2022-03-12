data = {"colors": [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    },
    {
        "color": "cyan",
        "value": "#0ff"
    },
    {
        "color": "magenta",
        "value": "#f0f"
    },
    {
        "color": "yellow",
        "value": "#ff0"
    },
    {
        "color": "black",
        "value": "#000"
    }
],

    "example_one": {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5007", "type": "Powdered Sugar"},
                {"id": "5006", "type": "Chocolate with Sprinkles"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
    },
    "example_two": [
        {
            "id": "0001",
            "type": "donut",
            "name": "Cake",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"},
                            {"id": "1002", "type": "Chocolate"},
                            {"id": "1003", "type": "Blueberry"},
                            {"id": "1004", "type": "Devil's Food"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5005", "type": "Sugar"},
                    {"id": "5007", "type": "Powdered Sugar"},
                    {"id": "5006", "type": "Chocolate with Sprinkles"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        },
        {
            "id": "0002",
            "type": "donut",
            "name": "Raised",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5005", "type": "Sugar"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        },
        {
            "id": "0003",
            "type": "donut",
            "name": "Old Fashioned",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"},
                            {"id": "1002", "type": "Chocolate"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        }
    ],

    "example_three": {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "image":
            {
                "url": "images/0001.jpg",
                "width": 200,
                "height": 200
            },
        "thumbnail":
            {
                "url": "images/thumbnails/0001.jpg",
                "width": 32,
                "height": 32
            }
    },

    "example_four": {
        "items":
            {
                "item":
                    [
                        {
                            "id": "0001",
                            "type": "donut",
                            "name": "Cake",
                            "ppu": 0.55,
                            "batters":
                                {
                                    "batter":
                                        [
                                            {"id": "1001", "type": "Regular"},
                                            {"id": "1002", "type": "Chocolate"},
                                            {"id": "1003", "type": "Blueberry"},
                                            {"id": "1004", "type": "Devil's Food"}
                                        ]
                                },
                            "topping":
                                [
                                    {"id": "5001", "type": "None"},
                                    {"id": "5002", "type": "Glazed"},
                                    {"id": "5005", "type": "Sugar"},
                                    {"id": "5007", "type": "Powdered Sugar"},
                                    {"id": "5006", "type": "Chocolate with Sprinkles"},
                                    {"id": "5003", "type": "Chocolate"},
                                    {"id": "5004", "type": "Maple"}
                                ]
                        }

                    ]
            }
    }
}


def get_f():
    for i in range(len("colors")):
        if data["colors"][i]["value"].__contains__("#f"):
            print(data["colors"][i]["color"])
    print()


def get_maple_topping_id():
    for i in range(len["topping"]):
        if data["example_one"]["topping"][i]["type"].__contains__("Maple"):
            print(data["example_one"]["topping"][i]["id"])
    print()


def get_batter_in_old_fashioned_donut():
    for i in range(len(data["example_two"])):
        if data["example_two"][i]["name"] == "Old Fashioned":
            for x in range(2):
                print(data["example_two"][i]["batters"]["batter"][x]["type"])
    print()


def get_all_toppings_available():
    for i in range(len(data["example_four"])):
        for k in range(len(data["example_four"]["items"]["item"][i]["topping"])):
            print(data["example_four"]["items"]["item"][i]["topping"][k]["type"])


get_f()
get_maple_topping_id()
get_batter_in_old_fashioned_donut()
get_all_toppings_available()
