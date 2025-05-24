from collections import deque


boxes_with_materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
present = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
magic_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while boxes_with_materials and magic_level:
    magic_level_toy = boxes_with_materials[-1] * magic_level[0]
    if magic_level_toy in magic_presents:
        boxes_with_materials.pop()
        magic_level.popleft()
        present[magic_presents[magic_level_toy]] += 1
    else:
        if magic_level_toy < 0:
            result = boxes_with_materials.pop() + magic_level.popleft()
            boxes_with_materials.append(result)
        elif magic_level_toy > 0:
            magic_level.popleft()
            boxes_with_materials[-1] += 15
        else:
            if magic_level[0] == 0 and boxes_with_materials[-1] == 0:
                boxes_with_materials.pop()
                magic_level.popleft()
                continue
            if magic_level[0] == 0:
                magic_level.popleft()
                continue
            if boxes_with_materials[-1] == 0:
                boxes_with_materials.pop()
                continue


if (present["Doll"] >= 1  and present["Wooden train"] >= 1) or (present["Teddy bear"] >= 1 and present["Bicycle"] >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in boxes_with_materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
for toy_name, amount in sorted(present.items()):
    if amount == 0:
        continue
    else:
        print(f"{toy_name}: {amount}")