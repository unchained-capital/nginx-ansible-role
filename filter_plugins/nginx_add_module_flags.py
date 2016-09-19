from os.path import basename

def nginx_add_module_flags(list_, directory):
    return ["--add-module=%s/%s" % (directory, basename(str(element))) for element in list_]

class FilterModule(object):
    
    def filters(self):
        return {
            'nginx_add_module_flags': nginx_add_module_flags,
        }
