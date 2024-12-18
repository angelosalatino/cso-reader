import configparser
import os



class Config:
    """ A simple abstraction layer for the configuration file """

    def __init__(self):
        """ Initialising the config class
        """
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.config_file = os.path.join(self.dir, "config.ini")
        self.config = configparser.ConfigParser()
        self.read_config_file()


# =============================================================================
#     ONTOLOGY
# =============================================================================
    def get_cso_path(self):
        """ Returns the path of the local version of CSO """
        return os.path.join(self.dir, self.config['ontology']['cso_path'])

    def get_cso_pickle_path(self):
        """ Returns the path of the local pickle version of CSO """
        return os.path.join(self.dir, self.config['ontology']['cso_pickle_path'])

    def get_cso_graph_path(self):
        """ Returns the path of the local pickle version of CSO (GRAPH) """
        return os.path.join(self.dir, self.config['ontology']['cso_graph_path'])

    def get_cso_remote_url(self):
        """ Returns the remote url where the latest version of CSO is located """
        return self.config['ontology']['cso_remote_url']

    def get_ontology_version(self):
        """ Return the ontology version """
        return self.config['ontology']['cso_version']

    def get_cso_version_logger_url(self):
        """ Returns the url of the version logger of CSO """
        return self.config['ontology']['cso_versions_logger_url']

    def set_cso_version(self, version):
        """ Sets the CSO version """
        self.config['ontology']['cso_version'] = version
        self.write_config_file()


# =============================================================================
#     READ AND WRITE CONFIG FILE
# =============================================================================
    def read_config_file(self):
        """ Reads the config file """
        self.config.read(self.config_file)

    def write_config_file(self):
        """ Writes the config file """
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
