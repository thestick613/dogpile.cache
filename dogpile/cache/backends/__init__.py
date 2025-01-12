from ...util import PluginLoader

_backend_loader = PluginLoader("dogpile.cache")
register_backend = _backend_loader.register

register_backend(
    "dogpile.cache.null", "dogpile.cache.backends.null", "NullBackend"
)
register_backend(
    "dogpile.cache.dbm", "dogpile.cache.backends.file", "DBMBackend"
)
register_backend(
    "dogpile.cache.pylibmc",
    "dogpile.cache.backends.memcached",
    "PylibmcBackend",
)
register_backend(
    "dogpile.cache.bmemcached",
    "dogpile.cache.backends.memcached",
    "BMemcachedBackend",
)
register_backend(
    "dogpile.cache.memcached",
    "dogpile.cache.backends.memcached",
    "MemcachedBackend",
)
register_backend(
    "dogpile.cache.memory", "dogpile.cache.backends.memory", "MemoryBackend"
)
register_backend(
    "dogpile.cache.memory_pickle",
    "dogpile.cache.backends.memory",
    "MemoryPickleBackend",
)
register_backend(
    "dogpile.cache.redis", "dogpile.cache.backends.redis", "RedisBackend"
)
register_backend(
    "dogpile.cache.mongo", "dogpile.cache.backends.mongodb", "MongoBackend"
)
