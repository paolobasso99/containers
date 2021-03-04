#DBTYPE = "mariadb"  # Uncomment this to enable an external DB instead of local SQLite, refer to Papermerge docs
DBUSER = "root"
DBPASS = "root"
DBHOST = "mariadb"
DBNAME = "papermerge"

MEDIA_DIR = "/data/media"
STATIC_DIR = "/app/papermerge/static"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

OCR_DEFAULT_LANGUAGE = "eng"

OCR_LANGUAGES = {
    "eng": "English",
    "ita": "Italiano",
}

IMPORTER_DIR = "/import"