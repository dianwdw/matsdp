# -*- coding: utf-8 -*-
import os
import sys
package_path = '/user/specified/path/to/matsdp/'
sys.path.insert(0, os.path.abspath(package_path))

def test_plot_poscar_for_workdir():
    from matsdp.vasp import vasp_plot

    retn_val = vasp_plot.plot_poscar_for_workdir(
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
    assert retn_val == 0
