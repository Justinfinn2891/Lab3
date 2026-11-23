import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/c/Users/justi/OneDrive/Desktop/hw10_data/hw10_data/Lab3/metafly_tf_pub/install/metafly_tf_pub'
