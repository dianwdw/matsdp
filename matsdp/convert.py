# -*- coding: utf-8 -*-
def atomname2indx(poscar_dir,atom_name):
    '''Convert atom name to atom index according to POSCAR file of vasp'''
    from .vasp import vasp_read as RFV
    poscar_dict = RFV.read_poscar(poscar_dir)
    atom_indx = poscar_dict['atomname_list'].index(atom_name) + 1
    return atom_indx

def POSCAR2lmp_datafile(poscar_dir):
    '''
    Description:
        Convert POSCAR file to LAMMPS data file
    '''
    import os
    import numpy as np
    from .vasp import vasp_read as RFV
    
    poscar_dir = os.path.abspath(poscar_dir)
    poscar_path = os.path.dirname(poscar_dir)
    poscar_filename = os.path.split(poscar_dir)[-1]
    lmp_datafile = poscar_path + '/' + poscar_filename + '.lmpdata'
    
    # Extract information from the input POSCAR file
    poscar_dict = RFV.read_poscar(poscar_dir)
    n_atoms = np.sum(poscar_dict['elmt_num_arr'])

    #Generate element name index\
    elmtname_indx = []
    indx = 0
    for i_type in range(len(poscar_dict['ElmtSpeciesArr'])):
        indx += 1
        for i in range(poscar_dict['elmt_num_arr'][i_type]):
            elmtname_indx.append(indx)        
    #Generate position part
    pos_str = ''
    for i_atom in range(n_atoms):
        pos_str = pos_str +  str(i_atom + 1) + ' ' + str(poscar_dict['elmtname_indx'][i_atom]) + ' ' + ' '.join(str(i) for i in poscar_dict['pos_arr'][i_atom,3:6]) + '\n'
    #Write lammps data file
    with open(lmp_datafile, 'w') as f:
        f.write('# LAMMPS data file generated by vaspToolkitPy\n' +
                str(sum(poscar_dict['elmt_num_arr'])) + ' atoms\n' +
                str(len(poscar_dict['ElmtSpeciesArr'])) + ' atom types\n' +
                '0.0 ' + str(poscar_dict['l_arr'][0,0]) + ' xlo xhi\n' +
                '0.0 ' + str(poscar_dict['l_arr'][1,1]) + ' ylo yhi\n' +
                '0.0 ' + str(poscar_dict['l_arr'][2,2]) + ' zlo zhi\n\nAtoms # atomic\n\n' +
                str(pos_str)
                )

def unitconvert(A,B):
    '''convert unit of physical quantity'''
    if A == 'a.u.' and B == 'eV':
        result = 27.211396 
    return result
