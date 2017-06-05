'''
Class in charge of controling the input files for NASQM
'''
from sed import sed_inplace, sed_global
from periodic_table import periodic_table

class InputCeon:
    """
    NAESMD always uses the input.ceon file, so that will be used for the naesmd input file.
    AMBER can use any input file name, so we require it.
    """
    def __init__(self, amber_input):
        self.amber_input = amber_input
        self.naesmd_init = open('input.ceon', 'r').read()
        self.amber_init = open(amber_input, 'r').read()
        self.log = ''

    def set_n_steps(self, n_steps):
        '''
        Sets the number of time-steps to do the simulation
        '''
        sed_inplace('input.ceon', 'n_class_steps=\d+', 'n_class_steps=' + str(n_steps))
        sed_inplace(self.amber_input, 'nstlim\s*=\s*\d+\.?\d*', 'nstlim='+str(n_steps))
        if n_steps == 0:
            sed_inplace(self.amber_input, 'irest\s*=\s*\d+', 'irest=0')
            sed_inplace(self.amber_input, 'ntx\s*=\s*\d+', 'ntx=1')

    def set_n_steps_to_print(self, n_steps_to_print):
        '''
        Set the number of steps between print outs
        '''
        sed_inplace('input.ceon', 'out_data_steps=\d*', 'out_data_steps=' + str(n_steps_to_print))
        sed_inplace(self.amber_input, 'ntwx=\s*\d*', 'ntwx=' + str(n_steps_to_print))
        sed_inplace(self.amber_input, 'ntpr=\s*\d*', 'ntpr=' + str(n_steps_to_print))

    def write_log(self):
        '''
        Write a log of all our changes
        '''
        open('input_ceon.log', 'w').write(self.log)

    def write_backup(self):
        '''
        Write the backup the original input files overriding any changes we made during the
        process
        '''
        open('input.ceon', 'w').write(self.naesmd_init)
        open(self.amber_input, 'w').write(self.amber_init)


    def set_exc_state_propagate(self, n_exc_states_propagate):
        '''
        Set the number of exciteds states to propagate
        '''
        sed_inplace('input.ceon', 'n_exc_states_propagate=\d*', 'n_exc_states_propagate='
                    + str(n_exc_states_propagate))

    def set_coordinates(self, coordinates):
        '''
        Set the coordinates for input.ceon
        '''
        sed_global('input.ceon', '&coord(.|\s|\n)*?&endcoord', '&coord\n' + coordinates + '&endcoord')

    def set_exc_state_init(self, exc_state_init):
        """
        Set the initial excited state
        """
        sed_inplace('input.ceon', 'exc_state_init=\d*', 'exc_state_init=' + str(exc_state_init))

    def set_verbosity(self, verbosity):
        """
        Set the verbosity for both amber and naesmd
        """
        sed_inplace('input.ceon', 'verbosity=\d*', 'verbosity=' + str(verbosity))
        sed_inplace(self.amber_input, 'verbosity\s*=\s*\d*', 'verbosity=' + str(verbosity))

    def set_periodic(self, periodic):
        '''
        Sets the appropriate boundary condition values for priodic or non-periodic conditions
        '''
        if periodic is True:
            sed_inplace(self.amber_input, 'ntb\s*=\s*\d+', 'ntb=2')
            sed_inplace(self.amber_input, 'ntp\s*=\s*\d+', 'ntp=1')
        if periodic is False:
            sed_inplace(self.amber_input, 'ntb\s*=\s*\d+', 'ntb=0')
            sed_inplace(self.amber_input, 'ntp\s*=\s*\d+', 'ntp=0')

    def set_time_step(self, time_step):
        """
        Sets the timestep of the simulation
        """
        sed_inplace(self.amber_input, 'dt=\s*\d+\.?\d*', 'dt=' +str(time_step/1000))

    def set_random_velocities(self, is_random_velocities):
        '''
        Sets the appropriate values for random velocities
        '''
        if is_random_velocities is False:
            sed_inplace(self.amber_input, 'ntx=\s*\d+\.?\d*', 'ntx=1')
        if is_random_velocities is True:
            sed_inplace(self.amber_input, 'ntx=\s*\d+\.?\d*', 'ntx=5')

    def log_inputceon(self):
        '''
        log the inputceon file
        '''
        self.log += open('input.ceon', 'r').read()


def set_inpcrd(coordinates, file_name):
    '''
    Sets the inpcrd coordinates of amber. The input coordinates are in the format
    of an XYZ file. Coordinates are written to file name.
    '''
    temp_list = coordinates.split()
    c_list = []
    for i, coord in enumerate(temp_list):
        if i % 4 != 0:
            c_list.append(float(coord))
    n_atoms = int(len(c_list) / 3)
    inpcrd = "MOL\n"
    inpcrd += "    " + str(n_atoms) + "\n"
    n_full_lines = int(n_atoms / 2)
    for i in range(n_full_lines):
        inpcrd += '{: 12.7f}{: 12.7f}{: 12.7f}{: 12.7f}{: 12.7f}{: 12.7f}'.format(c_list[i*6],
                                                                                  c_list[i*6+1],
                                                                                  c_list[i*6+2],
                                                                                  c_list[i*6+3],
                                                                                  c_list[i*6+4],
                                                                                  c_list[i*6+5])
        inpcrd += '\n'
    open(file_name, 'w').write(inpcrd)


def get_xyz_coordinates(file_stream):
    '''
    Obtain the xyz file_string from the xyz file_stream
    '''
    number_atoms = int(file_stream.readline())
    file_stream.readline()
    coords = ""
    for _ in range(number_atoms):
        l_coords = file_stream.readline().split()
        try:
            l_coords[0] = periodic_table(l_coords[0])
        except KeyError:
            l_coords[0] = l_coords[0]
        coords += "{:>2}{: 16.10f}{: 16.10f}{: 16.10f}\n".format(l_coords[0], float(l_coords[1]),
                                                                 float(l_coords[2]),
                                                                 float(l_coords[3]))
    return coords