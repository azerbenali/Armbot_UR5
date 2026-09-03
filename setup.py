from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'armbot_ur5'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
          glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'worlds'),
          glob('worlds/*.sdf')),
        (os.path.join('share',package_name,'urdf'),
          glob('urdf/*.xacro')),
        (os.path.join('share',package_name,'config'),
          glob('config/*.yaml')),
        (os.path.join('share',package_name,'srdf'),
          glob('srdf/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Azer Ben Ali',
    author_email='azerbenali5017@gmail.com',
    
    description=(
        'Armbot_UR5 autonomous pick-and-place controller for a UR5 arm '
        'with a Robotiq gripper in ROS 2 and Gazebo.'
    ),
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'move_to_pose = armbot_ur5.move_to_pose:main',
            'pick_and_place = armbot_ur5.pick_and_place:main',
            'box_pose_bridge = armbot_ur5.box_pose_bridge:main',
            'detect_box = armbot_ur5.detect_box:main',
            'pixel_to_world = armbot_ur5.pixel_to_world:main',
            'detect_objects = armbot_ur5.detect_objects:main',
        ],
    },
)
