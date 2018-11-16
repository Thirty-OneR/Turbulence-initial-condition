import Turbulence_velocity_field_initializer

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
