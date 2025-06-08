from collections import deque


suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]
target_value = int(input())
final_feed = []

while suggested_links and featured_articles:

    if suggested_links[0] == featured_articles[-1]:
        final_feed.append(0)
        featured_articles.pop()
        suggested_links.popleft()


    elif suggested_links[0] > featured_articles[-1]:
        remainder = suggested_links.popleft() % featured_articles.pop()
        final_feed.append(-remainder)
        if remainder == 0:
            continue
        suggested_links.append(remainder * 2)



    elif suggested_links[0] < featured_articles[-1]:
        remainder = featured_articles.pop() % suggested_links.popleft()
        final_feed.append(remainder)
        if remainder == 0:
            continue
        featured_articles.append(remainder * 2)



total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(str(x) for x in final_feed)}")

if total_engagement_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")