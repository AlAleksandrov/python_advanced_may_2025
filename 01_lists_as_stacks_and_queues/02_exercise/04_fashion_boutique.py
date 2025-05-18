stack_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_counter = 0

while stack_clothes:
    racks_counter += 1
    current_rack_capacity = rack_capacity
    while stack_clothes and stack_clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= stack_clothes.pop()


print(racks_counter)