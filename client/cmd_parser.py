def parse(options) -> {}:
    option_map = {}
    for i in range(0, len(options), 2): 
        option_map[options[i][1:]] = options[i+1]

    return option_map

