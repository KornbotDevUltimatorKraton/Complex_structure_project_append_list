data = {"category_component": "Navigation_system","component_selected": "Intel_Realsense_RPLIDAR_A2", "components_spec_data": "Serial", "email": "kornbot380@hotmail.com", "project_name": "Roboreactor_devian_8"}
data2 = {"category_component": "Navigation_system", "component_selected": "SIM900", "components_spec_data": "UART", "email": "kornbot380@hotmail.com", "project_name": "Roboreactor_devian_8"}
data3 = {"category_component": "Navigation_system", "component_selected": "SIM900", "components_spec_data": "UART", "email": "mimic380@hotmail.com", "project_name": "Roboreactor_d1"}
data4 = {"category_component": "Vision_system", "component_selected": "Fish_eyes_lens_camera", "components_spec_data": "8MPX", "email": "kornbot380@hotmail.com", "project_name": "Roboreactor_devian_8"}
list_info = [data,data2,data3]
#Select the component seprately inside the project data 
project_components = {}
#append data inside the list  check the email and generate predata insert 
if data.get('email') not in list(project_components):
                  project_components[data.get('email')] = {data.get('project_name'):{data.get('category_component'):[{data.get('component_selected'):data.get('components_spec_data')}]}}
print('Append first datao',project_components)
if data.get('email') in list(project_components):
                  
            if data2.get('project_name') in list(project_components.get(data.get('email'))):   
                  print(data2)
                  if data2.get('category_component') in list(project_components.get('kornbot380@hotmail.com').get(data2.get('project_name'))): 
                             project_components.get('kornbot380@hotmail.com').get(data2.get('project_name')).get(data2.get('category_component'))[0][data2.get('component_selected')] = data2.get('components_spec_data')  
                  if data4.get('category_component') not in list(project_components.get('kornbot380@hotmail.com').get(data4.get('project_name'))):
                            project_components.get('kornbot380@hotmail.com').get(data4.get('project_name'))[data4.get('category_component')] = [{data4.get('component_selected'):data4.get('components_spec_data')}]
                              
            if data2.get('project_name') not in list(project_components.get(data.get('email'))):
                  project_components.get('kornbot380@hotmail.com')[data2.get('project_name')] = {data2.get('project_name'):{data2.get('category_component'):[data2.get('component_selected')]}} 
print("Result from new input",project_components)
