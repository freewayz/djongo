from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    supports_transactions = False
    # djongo doesn't seem to support this currently
    has_bulk_insert = False
    has_native_uuid_field = True
