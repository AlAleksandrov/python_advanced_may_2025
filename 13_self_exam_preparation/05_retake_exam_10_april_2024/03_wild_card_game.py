def sort_collections(current_name, current_card, spell_lst, monster_lst):
    if current_card == "spell":
        if current_name not in spell_lst:
            spell_lst.append(current_name)

    elif current_card == "monster":
        if current_name not in monster_lst:
            monster_lst.append(current_name)

    return spell_lst, monster_lst


def draw_cards(*args, **kwargs):
    spell = []
    monster = []
    result = ""
    for name, card_type in args:
        spell, monster = sort_collections(name, card_type, spell, monster)

    for name, card_type in kwargs.items():
        spell, monster = sort_collections(name, card_type, spell, monster)

    if monster:
        monster = sorted(monster, reverse=True)
        monster_lines = '\n  ***'.join(x for x in monster)
        result = f"Monster cards:\n  ***{monster_lines}"
    if spell:
        spell = sorted(spell)
        spell_lines = '\n  $$$'.join(x for x in spell)
        if result:
            result += f"\nSpell cards:\n  $$${spell_lines}"
        else:
            result = f"Spell cards:\n  $$${spell_lines}"

    return result


print(draw_cards(("cyber dragon", "monster"), ("celtic guardian", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))