def Close_string(source, symbol_open = '{', symbol_close = '}'):
    open_brackets = 0
    stop_index = min(source.find(symbol_open), source.find(symbol_close))
    while open_brackets > 0 or source.find(symbol_open ,stop_index + 1) != -1:
        if source[stop_index] == symbol_open:
            open_brackets += 1
        else:
            open_brackets -= 1
        stop_index = min(source.find(symbol_open, stop_index + 1), source.find(symbol_close, stop_index + 1))
    open_brackets += 1
    for i in range(open_brackets):
        if stop_index != -1:
            stop_index = source.find(symbol_close, stop_index + 1)
    return stop_index