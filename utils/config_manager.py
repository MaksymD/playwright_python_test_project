import os
import yaml


class ConfigurationManager:
    def __init__(self, base_directory="configs"):
        self.base_directory = base_directory

    @staticmethod
    def load_config(config_file_path):
        with open(config_file_path, "r") as config_file:
            return yaml.safe_load(config_file)

    def get_config(self, config_filename):
        # if 'JENKINS_HOME' in os.environ:
        #     base_config_files_directory = os.path.join(os.path.dirname(os.getcwd()), "Proc_Tests_cc1-server", "configs")
        # else:
        base_config_files_directory = os.path.join(os.getcwd(), "configs")

        config_file_path = os.path.join(base_config_files_directory, config_filename)

        try:
            return self.load_config(config_file_path)
        except FileNotFoundError:
            print(f"Error: Config file not found at path {config_file_path}")
            return None
