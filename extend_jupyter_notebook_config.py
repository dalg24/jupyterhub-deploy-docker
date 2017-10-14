import yaml

user_config_file = '/home/jovyan/work/config.yml'
if os.path.isfile(user_config_file):
    with open(user_config_file, 'r') as f:
      user_config = yaml.load(f)
      ld_library_path = user_config.get('LD_LIBRARY_PATH')
      if ld_library_path:
          os.environ['LD_LIBRARY_PATH'] = ld_library_path
          c.Spawner.env_keep.append('LD_LIBRARY_PATH')
