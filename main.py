from os import path
import click
import os
from distutils.dir_util import copy_tree

@click.command()
@click.option('-p', '--project', required=True, help='This is for set project name')
@click.option('-b', '--bootstrap', prompt="Bootstrap elave edilsinmi? Y/N", type=bool)
@click.option('-ph', '--path', prompt="path where create folder", type=str)

def create_project(project, bootstrap, path):
    project_path = os.getcwd()

    # if not os.path.isdir(project):
    #     os.mkdir(project)
    os.chdir(f'{path}')
    src = f'{project_path}/project_internal'
    dist = f'{project}'
    copy_tree(src, dist)
    
    if not bootstrap:
        print(os.getcwd(),'sfsfsfscfcscs')
        with open(f'{project_path}/{project}/index.html', 'r') as f:
            lines = f.readlines()
        del lines[7]
        with open(f'{project_path}/{project}/index.html', 'w') as f:
            for line in lines:
                f.write(line)

    
if __name__ == '__main__':
    create_project()


# ishlek variantdi asagidaki
# @click.command()
# @click.option('-p', '--project', required=True, help='This is for set project name')
# @click.option('-b', '--bootstrap', prompt="Bootstrap elave edilsinmi? Y/N", type=bool)

# def create_project(project, bootstrap):
#     project_path = os.getcwd()

#     if not os.path.isdir(project):
#         os.mkdir(project)
#     os.system(f'cp -r project_internal/* {project_path}/{project}')
#     if not bootstrap:
#         with open(f'{project_path}/{project}/index.html', 'r') as f:
#             lines = f.readlines()
#         del lines[7]
#         with open(f'{project_path}/{project}/index.html', 'w') as f:
#             for line in lines:
#                 f.write(line)
