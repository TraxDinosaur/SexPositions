import json
from .funcs import positions


def DumpJson():
    print('Dumping data to positions.json...')
    all_positions_data = []
    positionNumber = 1
    limit = 3

    while positionNumber <= limit:
        print(f"Dumped Position: {positionNumber}")
        position_data = positions(positionNumber)
        all_positions_data.append(position_data)
        positionNumber += 1

        with open('positions.json', 'w') as json_file:
            json.dump(all_positions_data, json_file, indent=4)
    print('Positions dumped successfully!')

if __name__ == '__main__':
    ...
