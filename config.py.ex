def get_config():
    return dict(
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
