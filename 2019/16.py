data = open('16.input', 'r').readline().strip() 


base = [ 0 , 1 , 0 , -1 ]
signal = map(int, data)
signal = [1,2,3,4,5,6,7,8]

def repeater(arr, n):
    res = []
    for i in arr:
        res += [i for _ in range(n)]
    return res

def calc(signal, base):
    res = 0
    for pos, s in enumerate(signal):
        res += s * base[(pos+1) % len(base)] 
    return abs(res) % 10




def fft(signal, base):
    new_signal = []
    for i in range(len(signal)):
        b = repeater(base, i+1)
        res = calc(signal,b)
        new_signal.append(res)
    return new_signal


def transformer(signal, iterations):
    s = signal
    for i in range(iterations):
        s = fft(s, base) 
    return s

def transformer_2(signal, iterations):
    for i in range(iterations):
        arr = []
        summing = sum(signal)
        arr.append(abs(summing % 10))

        for s in signal: 
            summing -= s
            arr.append(abs(summing % 10))

        signal = arr

    return signal



signal = map(int, '80871224585914546619083218645595') 

# Part 1
signal = map(int, data)
res = transformer(signal, 100)
res = "".join(map(str,res))
print("Part 1 result: %s" % res[:8])


pos = 5976809

# Part 2
signal = map(int, data*10000)
res = transformer_2(signal[pos:], 100)
res = "".join(map(str,res))
print("Part 2 result: %s" % res[:8])

