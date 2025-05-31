def separate_and_sum(*args):
    positive_sum = sum([x for x in args if x > 0])
    negative_sum = sum([x for x in args if x < 0])
    
    if abs(negative_sum) > positive_sum:
        result = f"{negative_sum}\n{positive_sum}\nThe negatives are stronger than the positives"
    else:
        result = f"{negative_sum}\n{positive_sum}\nThe positives are stronger than the negatives"
    return result


nums = [int(x) for x in input().split()]
print(separate_and_sum(*nums))