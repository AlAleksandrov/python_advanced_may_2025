def sorting(current_name, current_game, console, pc):
    if current_name == "console":
        if current_game not in console:
            console[current_game] = ""

    elif current_name == "pc":
        if current_game not in pc:
            pc[current_game] = ""

    else:
        if current_game in console:
            console[current_game] = current_name[:-4:]

        elif current_game in pc:
            pc[current_game] = current_name[:-4:]

    return console, pc


def sort_games(*args, **kwargs):
    console_games = {}
    pc_games = {}
    result = ""
    for console, game in args:
        console_games, pc_games = sorting(console, game, console_games, pc_games)

    for release_date, release_game in kwargs.items():
        console_games, pc_games = sorting(release_date, release_game, console_games, pc_games)

    if console_games:
        result = "Console Games:\n"
        sorted_console = sorted(console_games.items(), key=lambda kvp: (kvp[1], kvp[0]))
        for game_title, release in sorted_console:
            result += f">>>{release}: {game_title}\n"

    if pc_games:
        result += "PC Games:\n"
        sorted_pc = sorted(pc_games.items(), key=lambda kvp: kvp[1], reverse=True)
        for game_title, release in sorted_pc:
            result += f"<<<{release}: {game_title}\n"

    return result

print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))
print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
print(sort_games(
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("console", "Blade Echo"),
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
))
print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
