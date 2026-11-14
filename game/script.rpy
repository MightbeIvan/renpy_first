
# CHARACTER DEFINITIONS

define l = Character("Luffy")
define z = Character("Zoro")
define c = Character("Café Manager")


# IMAGE DEFINITIONS

image bg cafe = "images/backgrounds/cafe_interior.png"
image luffy = "images/characters/luffy.png"
image zoro = "images/characters/zoro.png"


# MAIN STORY

label start:

    scene black

    "A quiet afternoon..."

    "A modern bubble tea shop sits on the corner of a busy street."

    "Inside, a certain pirate is about to start his new job."

    scene bg cafe

    show luffy at left

    l "I'M HUNGRY!"

    c "LUFFY! You're supposed to be working!"

    l "But I'm hungry!"

    c "You haven't even served your first customer yet..."

    "The café door suddenly opens."

    "Someone has arrived."

    l "OH! A CUSTOMER!"

    show zoro at right

    "A green-haired swordsman walks through the door."

    l "HEY! YOU LOOK STRONG!"

    "Zoro looks around the café."

    l "Welcome! What do you want to drink?"

    z "Do you serve sake?"

    l "What's that?"

    return
