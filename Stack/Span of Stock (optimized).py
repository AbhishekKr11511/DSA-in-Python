def spanOfStock(stocks):
    spans = []
    for i in range(len(stocks)):
        if max(stocks[0:i+1])>stocks[i]:
            span = i-stocks.index(max(stocks[0:i+1]))
            spans.append(span)
        else:
            spans.append(i+1)
    return spans

result = spanOfStock([15,10,8,9,12,17])
print(result)