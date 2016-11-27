def gas_stations(distance, tank_size, stations):
    stations_list = []
    temp_tank_size = tank_size-stations[0]
    stations.append(distance)

    for indx in range(1, len(stations)):
        if(temp_tank_size < (stations[indx]-stations[indx-1])):
            temp_tank_size = tank_size
            stations_list.append(stations[indx-1])
        temp_tank_size -= (stations[indx]-stations[indx-1])

    return stations_list
