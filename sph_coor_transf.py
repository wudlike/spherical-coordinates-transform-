import numpy as np

def point_change(init_lon, w_e, init_lat, s_n, r, psi):
    psi = np.deg2rad(psi)
    ang_c = np.pi/2-np.deg2rad(init_lat)
    cos_a = np.cos(r)*np.cos(ang_c)+np.sin(r)*np.sin(ang_c)*np.cos(psi)
    new_lati = np.abs(90-np.rad2deg(np.arccos(cos_a)))
    ang_B = np.rad2deg(np.arcsin(np.sin(psi)*np.sin(r)/np.sqrt(1-cos_a**2)))
    a_val = abs(np.arccos(cos_a))
    new_longi = np.abs(
        init_lon-np.rad2deg(np.arcsin(np.sin(psi)*np.sin(r)/np.sqrt(1-cos_a**2))))
    # East or west longitude
    if w_e is 'W':
        if (init_lon + ang_B) <= 180 and (init_lon + ang_B) > 0:
            new_longi = init_lon + ang_B
            W_E = 'W'
        elif init_lon + ang_B > 180:
            new_longi = abs(init_lon + ang_B - 360)
            W_E = 'E'
        elif init_lon + ang_B < 0:
            new_longi = abs(init_lon + ang_B)
            W_E = 'E'
    elif w_e is 'E':
        if (init_lon - ang_B) <= 180 and (init_lon - ang_B) > 0:
            new_longi = init_lon - ang_B
            W_E = 'E'
        elif init_lon - ang_B > 180:
            new_longi = abs(init_lon - ang_B - 360)
            W_E = 'E'
        elif init_lon - ang_B < 0:
            new_longi = abs(init_lon - ang_B)
            W_E = 'W'
    # South or north latitude
    if (np.pi/2 - a_val) > 0:
        S_N = 'N'
    else:
        S_N = 'S'
    angle_change = np.rad2deg(
        np.arccos((np.cos(ang_c)-cos_a*np.cos(r))/(np.sqrt(1-cos_a**2)*np.sin(r))))
    angle_change = 180 - angle_change
    return angle_change, new_longi, W_E, new_lati, S_N


if __name__ == "__main__":
    # The unit of r is rad
    # The moving step_size should be less than 90*pi/180
    '''
    # input from terminal
    init_longitude, w_e_input, init_latitude, s_n_input, move_step_size, init_included_angle = \
    map(str,input('Enter initial_longitude, latitude, moving step_size and angular separation,\n, e.g., 60 E 30 N 1 120 >>> ').split())
    init_longitude = float(init_longitude)
    init_latitude = float(init_latitude)
    move_step_size = float(move_step_size)
    init_included_angle = float(init_included_angle)
    included_angle, new_longi, w_e, new_lati, s_n = \
    point_change(init_longitude, w_e_input, init_latitude, s_n_input, move_step_size, init_included_angle)
    '''

    #input from code
    included_angle, new_longi, w_e, new_lati, s_n = point_change(
        0, 'W', 0, 'N', 60*np.pi/180, 90)
    print(('new angular separation = %.2f\nnew position = (%.2f' +
           w_e+', %.2f'+s_n+')') % (included_angle, new_longi, new_lati))

