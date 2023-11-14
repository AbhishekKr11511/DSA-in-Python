def spanOfStock(stocks):
    spans = []
    for i in range(len(stocks)):
        count = 0
        for j in range(i,-1,-1):
            if(stocks[j]<=stocks[i]):
                count+=1
            else:
                break
        spans.append(str(count))

    return " ".join(spans)

result = spanOfStock([15,10,8,9,12,17])
print(result)
