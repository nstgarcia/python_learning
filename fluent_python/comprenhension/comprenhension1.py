symbols = '$¢£¥€¤'
codes = []
print("traditional way of generating a list")
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


print("using list comprehension")
codes = [ord(s) for s in symbols]
print(codes)
