import farm_land as fm
import numpy as np


def main():
    farmLand = fm.createMatrix()
    farmLandDim = farmLand.shape

    with open('farm_land_matrix.txt', 'w') as file: 
        for line in farmLand:
            line2=' '.join([str(x) for x in line])
#           line2=','.join([str(x) for x in line]) ### CSV
            file.write(line2+'\n')

    print(f"{'-'*(farmLandDim[1] - 4)} FARM LAND {'-'*(farmLandDim[1] - 4)}")
    print(farmLand)
    print()
    print(f"The largest farmable square dimension in this {farmLandDim} farm land is: {fm.findLargestSqr(fm.findFarmableLand(farmLand))}")


main()