#print('#GCOS')
# If structure is high-relief (> or = 3 times higher than seismic accuracy) And low structural complexity
# (4-way) ENTER A
# Medium structure (1-3 times higher than seismic accuracy) Or high relief structure and high structural complexity
# 3 Way, stratigraphic ENTER B
# Low-relief structure (lower than seismic accuracy) OR high uncertainty of depth conversion
# (sub-salt, below lava flow) OR areas with rapidly changing lateral velocities in the overburden ENTER C
# Low-relief structure (lower than seismic accuracy) AND either high uncertainty of depth conversion
# (sub-salt, below lava flow) OR areas with rapidly changing lateral velocities in the overburden ENTER D

prob = 0
#Data Availability
print("Specify Data Availability. \n~If 3D Seismic is availble. \n ENTER \"A\" \n~If 2D SEISMIC and dense lines (7 lines or more per structure). \n ENTER \"B\" \n~If 2D SEISMIC and sparse lines (3-6 lines per structure).\n ENTER \"C\" \n~If 2D SEISMIC and very sparse lines (2 lines (lead)).\n ENTER \"D\" ")
data_ext = input('Enter Answer: ')
#Structure Relief
print("~If structure is high-relief (> or = 3 times higher than seismic accuracy) And low structural complexity (4-way).\n ENTER \"A\" \n~If structure is medium structure (1-3 times higher than seismic accuracy) Or high relief structure and high structural complexity 3 Way, stratigraphic.\n ENTER \"B\"\n~If structure is low-relief structure (lower than seismic accuracy) OR high uncertainty of depth conversion (sub-salt, below lava flow) OR areas with rapidly changing lateral velocities in the overburden.\n ENTER \"C\"\n~If structure is low-relief structure (lower than seismic accuracy) AND either high uncertainty of depth conversion (sub-salt, below lava flow) OR areas with rapidly changing lateral velocities in the overburden.\n ENTER \"D\" ")

struc = input('Enter: ')
if struc == 'A':
    print("~If it is easy to interpret, reliable correlations based on nearby (<50km) wells.\n ENTER \"A\" \n~Uncertain correlation (horizons are interrupted laterally) Or based on remote (> 50km) wells.\n ENTER \"B\"\n~Difficult to interpret, unreliable correlation (horizons are interrupted by thrust faults, diapirs etc) OR model developed using analogues without wells in the basin.\n ENTER \"C\" ")
    struc_v1 = input('Enter Answer: ')
    if struc_v1 == 'A':
        if data_ext == 'A':
            prob = 1
        elif data_ext == 'B':
            prob = 0.9
        elif data_ext == 'C':
            prob = 0.8
        else:
            prob = 0.6
    elif struc_v1 == 'B':
        if data_ext == 'A':
            prob = 0.95
        elif data_ext == 'B':
            prob = 0.85
        elif data_ext == 'C':
            prob = 0.75
        else:
            prob = 0.55
    elif struc_v1 == 'C':
        if data_ext == 'A':
            prob = 0.85
        elif data_ext == 'B':
            prob = 0.75
        elif data_ext == 'C':
            prob = 0.70
        else:
            prob = 0.45
#if high_relief:
elif struc == 'B':
    print(" If it is easy to interpret, reliable correlations based on nearby (<50km) wells.\n ENTER \"A\" \nUncertain correlation (horizons are interrupted laterally) Or based on remote (> 50km) wells.\n ENTER \"B\"\nDifficult to interpret, unreliable correlation (horizons are interrupted by thrust faults, diapirs etc) OR model developed using analogues without wells in the basin.\n ENTER \"C\" ")
    struc_v1 = input('Enter: ')
    if struc_v1 == 'A':
        if data_ext == 'A':
            prob = 0.8
        elif data_ext == 'B':
            prob = 0.7
        elif data_ext == 'C':
            prob = 0.6
        else:
            prob = 0.35
    elif struc_v1 == 'B':
        if data_ext == 'A':
            prob = 0.75
        elif data_ext == 'B':
            prob = 0.65
        elif data_ext == 'C':
            prob = 0.50
        else:
            prob = 0.25
    elif struc_v1 == 'C':
        if data_ext == 'A':
            prob = 0.70
        elif data_ext == 'B':
            prob = 0.55
        elif data_ext == 'C':
            prob = 0.45
        else:
            prob = 0.20
elif struc == 'C':
    print(" If it is easy to interpret, reliable correlations based on nearby (<50km) wells. ENTER \"A\" \nUncertain correlation (horizons are interrupted laterally) Or based on remote (> 50km) wells ENTER \"B\"\nDifficult to interpret, unreliable correlation (horizons are interrupted by thrust faults, diapirs etc) OR model developed using analogues without wells in the basin. ENTER \"C\" ")
    struc_v1 = input('Enter: ')
    if struc_v1 == 'A':
        if data_ext == 'A':
            prob = 0.55
        elif data_ext == 'B':
            prob = 0.45
        elif data_ext == 'C':
            prob = 0.35
        else:
            prob = 0.15
    elif struc_v1 == 'B':
        if data_ext == 'A':
            prob = 0.50
        elif data_ext == 'B':
            prob = 0.40
        elif data_ext == 'C':
            prob = 0.25
        else:
            prob = 0.10
    elif struc_v1 == 'C':
        if data_ext == 'A':
            prob = 0.40
        elif data_ext == 'B':
            prob = 0.30
        elif data_ext == 'C':
            prob = 0.20
        else:
            prob = 0.05
else: 
    struc = 'D'
    if data_ext == 'A':
        prob = 0.35

    elif data_ext == 'B':
        prob = 0.25
    elif data_ext == 'C':
        prob = 0.15
    else:
        prob = 0.05

print('Probability of Structure Presence is', prob)
    