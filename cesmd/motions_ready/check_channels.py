import sys

def check_channels(lines):

    locations = {}

    for line in lines.split('\n')[:-1]:

        if len(line.split('.')[0]) == 6:
            offset = -1
        else:
            offset = 0

        loc_name = line[48+offset:]
        if "Not Installed" in loc_name:
            print("Channel not installed     <", line)
            continue

        dir = line[20+offset:27+offset]
        
        try:
            v2 = int(line[4:7+offset])
        except ValueError:
            print("got ValueError when parsing v2     <", line)
            continue
        
        sta_chan = line[39+offset:41+offset]
        if sta_chan == '  ':
            true_channel = v2
        else:
            try:
                true_channel = int(sta_chan)
            except ValueError:
                print("got ValueError when parsing Sta Chn     <", line)
                continue

        # chan = int(line[16:18])
        
        if loc_name in locations.keys():
            if dir in locations[loc_name].keys():
                if locations[loc_name][dir] != true_channel:
                    print("Inconsistent Location for Channel Number", true_channel, "     <", line)
            else:
                locations[loc_name][dir] = true_channel
        else:
            locations[loc_name] = {}
            locations[loc_name][dir] = true_channel

    return(locations)


if __name__ == "__main__":

    lines = sys.stdin.read()
    check_channels(lines)