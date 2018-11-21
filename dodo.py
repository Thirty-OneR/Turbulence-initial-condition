import Turbulence_velocity_field_initializer
import Power_Spectrum

def task_write_binary():

    return {
            'actions': [
                (Turbulence_velocity_field_initializer.run_generator,),],
            'params':[
                {'name':'N', 'short':'N', 'type':int, 'default':64},
                {'name':'index', 'short':'index', 'type':float, 'default':1.5},
                {'name':'seed', 'short':'seed', 'type':int,
                    'default':0x4d3d3d3},
                {'name':'output_fn', 'short':'output_fn', 'type':str,
                    'default':'vel_init'}
                ],
            }

def draw_power_spectrum():

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

