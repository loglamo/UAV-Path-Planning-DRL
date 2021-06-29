import numpy as np
import pandas as pd
import math

class env:
    # on the ground
    "Class env definites components in UAV-assisted wireless such as set of devices, set of resources "
    N_users = 50 # the number users according to the number of users at the configs
    N_agents = 5 # the number of UAVs
    N_subcarriers = 64 # the number of subchannels
    N_powerlevels = 3 # the number of power levels
    energy_list = [12, 23, 21]  # list of total energy at time t of every egent
    # in sky
    maximum_altitude = 200 # maximum altitude of each UAV with the unit m
    minimum_altitude = 150 # minimum altitude of each UAV
    maximum_energy = 1000 #wat at a time step
    minimum_energy = 0 # need to be recalculated based on status of UAV (moving, hover)
    maximum_average_total_energy = 22
    #coords_UAV_first_step = [(np.random.randint(0, 1000), np.random.randint(0, 1000), np.random.randint(150,200)) for _ in range(N_agents)]# create the initial position of UAVs
    # print(coords_UAV_first_step)
    # pd.DataFrame(coords_UAV_first_step).to_csv("coord_v1_UAV.csv")
    kapka1 = 0.6
    kapka2 = 0.4

    def return_mobility_energy(time_moving, time_transmission):
        UAV_weight = 1  # unit of kgs
        g = 9.8 #the earth gravity m/s2
        air_dense = 1.225
        r = 0.04 #the radius of propellers
        n = 5 #the number of propellers
        v_average = 10 #m/s
        v_max = 15
        P_full = 5 #W
        P_s = 0 #W
        hov_energy = math.sqrt((UAV_weight*g)**3/(2*math.pi*(r)**2*n*air_dense)) #hover power
        transition_energy = (P_full-P_s)*v_average/v_max + P_s #transition power
        mobility_energy = (hov_energy + transition_energy)*time_moving + (hov_energy + P_s)*time_transmission
        return mobility_energy

    def return_tranmission_energy_UAV_m(index_UAV, indicator_users, indicator_subchannels, level_transmit_power, informations, locations_of_UAVs):#information from other UAVs
        channel_power_gain_reference_distance = 60 #dB
        alpha = 2 #pathloss coefficient
        location_users = [[1,2,3][2,2,2]]
        channel_power_gain = []
        for i in range(indicator_users):
            if indicator_users[i] == 1:
               channel_power_gain_i = (channel_power_gain_reference_distance)/(((abs(math.dist(location_users[i][0:1],locations_of_UAVs[index_UAV][0:1])))**2 + locations_of_UAVs[index_UAV][2]**2)**(alpha/2))
               channel_power_gain.append(channel_power_gain_i)
            elif indicator_users[i] == 0:
               channel_power_gain_i = 0
               channel_power_gain.append(channel_power_gain_i)
            

        transmission_power = 0
        return transmission_power
    def return_state(obs, recent_action):

        satisfied_users_ratio = 0
        return satisfied_users_ratio
    def return_reward(self, recent_state):
        energy_list = [12, 23, 21]  # list of total energy at time t of every egent
        satified_users_ratio = 0.6  # take from a function
        normalized_value = self.normalize_value(energy_list)
        reward = self.kapka1 * normalized_value + self.kapka2 * satified_users_ratio
        return reward
    def normalize_value(self, energy_list):
        min_value = 0 #min value of energy take from common information
        max_value = 30 #max value of energy at each time step taken from common information
        value = self.maximum_average_total_energy - (sum(energy_list)/len(energy_list))
        normalized_value = (value - min_value)/(max_value - min_value)
        return normalized_value

