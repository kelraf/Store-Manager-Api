class Config(object):

    """ base config """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """ Development configuration """
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    """ Testing Configurations """
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """ Production Configurations """
    DEBUG = False
    TESTING = False

app_config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}