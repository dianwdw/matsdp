# -*- coding: utf-8 -*-
import os
import sys
package_path = './'
sys.path.insert(0, os.path.abspath(package_path))

from matsdp import funcs
from matsdp import convert
from matsdp.vasp import vasp_read
from matsdp.vasp import vasp_plot
from matsdp.vasp import vasp_analyze
from matsdp.vasp import vasp_build
from matsdp.vasp import vasp_write
from matsdp.vasp import vasp_default
from matsdp.vasp import vasp_help
from matsdp.apt import apt_read
from matsdp.apt import apt_plot
from matsdp.dvm import dvm_read
from matsdp.dvm import dvm_build
from matsdp.dvm import dvm_analyze
from matsdp.dvm import dvm_write
from matsdp.dvm import dvm_default
from matsdp.dvm import dvm_help

run_nn_map = True
run_simple_cna = True
run_substitute = True
run_replace_elmt = True
run_selection_sphere = True
run_get_doscar = True
run_plot_dos = True
run_plot_poscar = False
run_plot_poscar_for_workdir = True
run_overlap_peak_analyzer = True
run_estruct = True
run_write_poscar_with_force = True
run_plot_concentration_profile = True
run_create_multiple_dvm_jobs = True
run_poscar2dvmincar = True

###############
# nn_map_Calc
###############
if run_nn_map == True:
    vasp_analyze.nn_map(
        poscar_file_path = './tests/vasp/POSCAR',
        a0 = 3.545,
        n_shell = 2,
        )
########################
# simple_common_neighbor
########################
if run_simple_cna == True:
    vasp_analyze.simple_cna(
        poscar_file_path = './tests/vasp/POSCAR',
        a0 = 3.545,
        common_neighbor_elmt_list = ['Re', 'W', 'Ta','Ni']
        )
    vasp_plot.plot_poscar(
        poscar_file_path = './outputs/POSCAR_simple_common_neighbor_pair_count_ReNi.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 2,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )
    vasp_plot.plot_poscar(
        poscar_file_path = './outputs/POSCAR_simple_common_neighbor_pair_count_ReNi.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 2,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'horizontal'
        )

#################
# run_substitute
#################
if run_substitute == True:
    vasp_build.substitution(
        substitution_list_file = './tests/vasp/example.subst',
        poscar_file_path = './tests/vasp/POSCAR_NoDope',
        )
###################
# run_replace_elmt
###################
if run_replace_elmt == True:
    vasp_build.rep_elmt(
        substitution_list_file = './tests/vasp/example.subst',
        poscar_file_path = './tests/vasp/POSCAR_NoDope',
        old_elmt= 'Re',
        elmt_group = ['W','Cr'],
        )
#################################
# atom selection -- sphere
#################################
if run_selection_sphere == True:
    vasp_build.selection_sphere(
        poscar_file_path = './tests/vasp/CONTCAR',
        origin_atom_name = 'Re1',
        radius = 7,
        include_mirror_atoms = False,
        output_file_name = 'example'
        )
###########
#plot_dos
###########
if run_plot_dos == True:
    dos1_file_path = './tests/vasp/DOSCAR'
    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path],
        atom_sysname_list = ['C5'],
        atom_indx_list = ['Ni1'],
        atom_palette_list = ['black'],
        atom_subplot_arg_list = [111],
        subplot_arg_list = [111],
        subplot_xlo_list = [-6.5],
        subplot_xhi_list = [4.0],
        subplot_ylo_list = [None],
        subplot_yhi_list = [None],
        subplot_xtick_list = [True],
        subplot_ytick_list = [True],
        subplot_xlabel_list = [False],
        subplot_ylabel_list = [False],
        subplot_share_xy_list = [False, False],
        mainplot_axis_label_list = [True, True],
        dos_mode = None,
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [13.0, 9.5],
        fig_dpi = 600,
        )
    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path, dos1_file_path],
        atom_sysname_list = ['C1', 'C1'],
        atom_indx_list = ['Ni1', 'Re1'],
        atom_palette_list = ['black', 'red'],
        atom_subplot_arg_list = [111, 111],
        subplot_arg_list = [111],
        subplot_xlo_list = [-6.5],
        subplot_xhi_list = [4.0],
        subplot_ylo_list = [None],
        subplot_yhi_list = [None],
        subplot_xtick_list = [True],
        subplot_ytick_list = [True],
        subplot_xlabel_list = [False],
        subplot_ylabel_list = [False],
        subplot_share_xy_list = [False, False],
        mainplot_axis_label_list = [True, True],
        dos_mode = {'Ni':['d'], 'Re':['d']},
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [11.0, 9.5],
        fig_dpi = 600,
        )

    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path, dos1_file_path],
        atom_sysname_list = ['C1', 'C1'],
        atom_indx_list = ['Ni2', 'Re1'],
        atom_palette_list = ['black', 'red'],
        atom_subplot_arg_list = [211, 212],
        subplot_arg_list = [211, 212],
        subplot_xlo_list = [-6.5, -6.5],
        subplot_xhi_list = [4.0, 4.0],
        subplot_ylo_list = [None, None],
        subplot_yhi_list = [None, None],
        subplot_xtick_list = [True, True],
        subplot_ytick_list = [True, True],
        subplot_xlabel_list = [False, False],
        subplot_ylabel_list = [False, False],
        subplot_share_xy_list = [False, False],
        mainplot_axis_label_list = [True, True],
        dos_mode = {'Ni':['d'], 'Re':['d']},
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [11.0, 9.5],
        fig_dpi = 600,
        )

    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path, dos1_file_path],
        atom_sysname_list = ['C1', 'C1'],
        atom_indx_list = ['Ni2', 'Re1'],
        atom_palette_list = ['black', 'red'],
        atom_subplot_arg_list = [211, 212],
        subplot_arg_list = [211, 212],
        subplot_xlo_list = [-6.5, -6.5],
        subplot_xhi_list = [4.0, 4.0],
        subplot_ylo_list = [None, None],
        subplot_yhi_list = [None, None],
        subplot_xtick_list = [False, True],
        subplot_ytick_list = [True, True],
        subplot_xlabel_list = [False, False],
        subplot_ylabel_list = [False, False],
        subplot_share_xy_list = [True, False],
        mainplot_axis_label_list = [True, True],
        dos_mode = {'Ni':['d'], 'Re':['d']},
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [11.0, 9.5],
        fig_dpi = 600,
        )


    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path, dos1_file_path, dos1_file_path, dos1_file_path],
        atom_sysname_list = ['C1', 'C1', 'C1', 'C1'],
        atom_indx_list = ['Ni2', 'Re1', 'Ni1', 'Ni5'],
        atom_palette_list = ['black', 'red', 'blue', 'green'],
        atom_subplot_arg_list = [221, 222, 223, 224],
        subplot_arg_list = [221, 222, 223, 224],
        subplot_xlo_list = [-4.5, -6.5, -4.5, -6.5],
        subplot_xhi_list = [4.0, 4.0, 4.0, 4.0],
        subplot_ylo_list = [None, None, None, None],
        subplot_yhi_list = [None, None, None, None],
        subplot_xtick_list = [True, True, True, True],
        subplot_ytick_list = [True, True, True, True],
        subplot_xlabel_list = [False, False, False, False],
        subplot_ylabel_list = [False, False, False, False],
        subplot_share_xy_list = [False, False],
        mainplot_axis_label_list = [True, True],
        dos_mode = {'Ni':['d'], 'Re':['d']},
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [11.0, 9.5],
        fig_dpi = 600,
        )
    vasp_plot.plot_dos(
        atom_doscar_file_path_list = [dos1_file_path, dos1_file_path, dos1_file_path, dos1_file_path],
        atom_sysname_list = ['C1', 'C1', 'C1', 'C1'],
        atom_indx_list = ['Ni2', 'Re1', 'Ni1', 'Ni5'],
        atom_palette_list = ['black', 'red', 'blue', 'green'],
        atom_subplot_arg_list = [221, 222, 223, 224],
        subplot_arg_list = [221, 222, 223, 224],
        subplot_xlo_list = [-4.5, -6.5, -4.5, -6.5],
        subplot_xhi_list = [4.0, 4.0, 4.0, 4.0],
        subplot_ylo_list = [-2.3, -2.3, -2.3, -2.3],
        subplot_yhi_list = [2.5, 2.5, 2.5, 2.5],
        subplot_xtick_list = [False, False, True, True],
        subplot_ytick_list = [True, False, True, False],
        subplot_xlabel_list = [False, False, False, False],
        subplot_ylabel_list = [False, False, False, False],
        subplot_share_xy_list = [True, True],
        mainplot_axis_label_list = [True, True],
        dos_mode = {'Ni':['d'], 'Re':['d']},
        fermi_shift_zero = True,
        peak_analyzer = False,
        fig_format = 'png',
        fig_size = [11.0, 9.5],
        fig_dpi = 600,
        )    
#########################
# overlap_peak_analyzer
#########################
if run_overlap_peak_analyzer == True:
    vasp_analyze.overlap_peak_analyzer(
        doscar_file_path = './tests/vasp/DOSCAR',
        sysname = 'DOS1',
        atom_indx_list = ['Ni1','Re1'],
        n_shell = 2,
        a0 = 3.52,
        dos_mode = {'Ni':['d'],'Re':['d']},
        fermi_shift_zero = True,
        )
#############################
#Get DOS files with DOS info
#############################
if run_get_doscar == True:
    poscar_file_path = './tests/vasp/POSCAR'
    poscar_dict = vasp_read.read_poscar(poscar_file_path)  
    for atom_indx in range(0, len(poscar_dict['atom_species_arr']) + 1):
        vasp_read.read_doscar(
            doscar_file_path = './tests/vasp/DOSCAR',
            atom_indx = atom_indx,
            save_dos_arr = True,
            )

#########################
#Visualization of POSCAR
#########################
if run_plot_poscar == True:
    vasp_plot.plot_poscar(
        poscar_file_path = './tests/vasp/POSCAR',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = False,
        colormap_column_indx = 1,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )

##########################
# write_poscar_with_force
##########################
if run_write_poscar_with_force == True:
    # write_poscar_with_force
    vasp_write.write_poscar_with_force(
        outcar_file_path = './tests/vasp/OUTCAR',
        ionic_step = 'last',
        output_poscar_file_name = None
        )
    vasp_plot.plot_poscar(
        poscar_file_path = './tests/vasp/POSCAR_with_force_step_1.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 1,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )
    vasp_plot.plot_poscar(
        poscar_file_path = './tests/vasp/POSCAR_with_force_step_1_absforce.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 1,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )

################################################
#run_plot_poscar for the POSCARs in a directory
################################################
if run_plot_poscar_for_workdir == True:    
    vasp_plot.plot_poscar_for_workdir(
        workdir = './outputs/example/',
        euler_angle_type = 'zyx',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = None,
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        poscar_or_contcar = 'POSCAR',
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = False,
        colormap_column_indx = 1,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )
##############
# run_estruct
##############
if run_estruct == True:
    vasp_analyze.estruct(
        doscar_file_path = './tests/vasp/DOSCAR',
        sysname = 'DOS1',
        )
    vasp_plot.plot_poscar(
        poscar_file_path = './outputs/POSCAR_estruct_DOS1_Ef-7.0888.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 1,
        colormap_vmin = None,
        colormap_vmax = None,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )

    vasp_plot.plot_poscar(
        poscar_file_path = './outputs/POSCAR_estruct_DOS1_Ef-7.0888.vasp',
        euler_angle_type = 'zyz',
        phi = -3,
        theta = 5,
        psi = 0,
        elmt_color = {'Ni':'red','Re':'blue'},
        draw_mirror_atom = True,
        box_on = True,
        axis_indicator =True,
        plot_cell_basis_vector_label = True,
        plot_atom_label = True,
        fig_format = 'png',
        fig_dpi = 100,
        draw_colormap = True,
        colormap_column_indx = 1,
        colormap_vmin = -80,
        colormap_vmax = -40,
        vmin_color = 'blue',
        vmax_color = 'red',
        colorbar_alignment = 'vertical'
        )

#################################
#apt- plot concentration profile
#################################
if run_plot_concentration_profile == True:    
    apt_plot.plot_proxigram_csv(
        proxigram_csv_file_path = './tests/apt/profile-interface0.csv',
        sysname = 'M2',
        visible_elmt_list = ['Ni','Al'],
        interplation_on = False,
        fig_width = 6,
        fig_height = 5,
        fig_dpi = 600,
        fig_format = 'png',
        )

#################################
# create multiple dvm jobs
#################################
if run_create_multiple_dvm_jobs == True:
    poscar_file_path_dict = {}
    poscar_file_path_dict['dvm_example'] = './tests/vasp/CONTCAR'
    dvm_build.create_multiple_dvm_jobs(
        poscar_file_path_dict = poscar_file_path_dict,
        elmt_ind_file_dir = './tests/dvm/',
        origin_atom_name_list = ['Re1', 'Ni5'],
        radius = 8,
        include_mirror_atoms = True
        )

#################################
# poscar2dvmincar
#################################
if run_poscar2dvmincar == True:
    convert.poscar2dvmincar(
        poscar_path = './tests/vasp/CONTCAR'
        )
