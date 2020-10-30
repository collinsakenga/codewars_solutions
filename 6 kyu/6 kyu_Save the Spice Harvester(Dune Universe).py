def harvester_rescue(data):
    carry_distance = sum(abs((i-j)**2)
                         for i, j in zip(data['harvester'], data['carryall'][0]))
    worm_distance = sum(abs((i-j)**2)
                        for i, j in zip(data['harvester'], data['worm'][0]))
    return "Damn the spice! I'll rescue the miners!" if (carry_distance**0.5/data['carryall'][1]+1) >= worm_distance**0.5/data['worm'][1] else 'The spice must flow! Rescue the harvester!'
