import Turbulence_velocity_field_initializer
import Power_Spectrum
import Density_field_initializer
import analyze_output

def task_write_velocity():

    return {
            'actions': [
                (Turbulence_velocity_field_initializer.run_generator,),],
            'params':[
                {'name':'N', 'short':'N', 'type':int, 'default':64},
                {'name':'index', 'short':'index', 'type':float, 'default':1.5},
                {'name':'seed', 'short':'seed', 'type':int,
                    'default':0x4d3d3d3},
                {'name':'output_fn', 'short':'output_fn', 'type':str,
                    'default':'vel_init'},
                {'name':'binary', 'short':'binary', 'type':int,
                    'default':'False'}
                ],
            }

def task_write_denisty():

    return {
            'actions': [
                (Density_field_initializer.run_generator,),],
            'params':[
                {'name':'N', 'short':'N', 'type':int, 'default':64},
                {'name':'mu', 'short':'mu', 'type':float, 'default':1.0},
                {'name':'sigma', 'short':'sigma', 'type':float, 'default':0.1},
                {'name':'seed', 'short':'seed', 'type':int,
                    'default':0x4d3d3d3},
                {'name':'output_fn', 'short':'output_fn', 'type':str,
                    'default':'den_init'},
                {'name':'binary', 'short':'binary', 'type':int,
                    'default':'False'}
                ],
            }


def task_draw_power_spectrum():

    return {
            'actions': [
                (Power_Spectrum.draw_power_spectrum,),],
            'params':[
                {'name':'N', 'short':'N', 'type':int, 'default':64},
                {'name':'bins', 'short':'bins', 'type':int, 'default':32},
                {'name':'figname', 'short':'fig', 'type':str,
                    'default':'power_spectrum'}
                ],
            }


def task_make_slice():
    return {
            'actions': [
                (analyze_output.run_slice,),],
            'params':[]
            }

def task_combine_data():
    return {'actions':[['python','combine.py']]}


