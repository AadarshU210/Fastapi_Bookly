from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config
import ssl as ssl_module

def get_database_config():
    """Get database URL and connect_args with proper SSL configuration"""
    database_url = Config.DATABASE_URL
    
    # Remove any existing query parameters from URL
    base_url = database_url.split('?')[0]
    
    # Check if this is local Docker/localhost database
    if "@db:" in base_url or "localhost" in base_url or "@127.0.0.1" in base_url:
        # Local database - explicitly disable SSL
        print(f"🔧 Using LOCAL database (SSL disabled): {base_url}")
        return base_url, {"ssl": False}
    
    # Production database - enable SSL with proper context
    print(f"Using PRODUCTION database (SSL enabled): {base_url.split('@')[0]}@***")
    
    # Create SSL context for production
    ssl_context = ssl_module.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl_module.CERT_NONE
    
    return base_url, {"ssl": ssl_context}


# Get database configuration
database_url, connect_args = get_database_config()

# Create async engine with better connection pool settings
async_engine = create_async_engine(
    url=database_url,
    echo=False,  # Turn off for production
    connect_args = connect_args,
    pool_size=10,              # Number of connections to maintain
    max_overflow=10,           # Don't create extra connections
    pool_pre_ping=True,       # Test connections before use
    future=True,
    pool_recycle=3600
)

async def init_db():

    async with async_engine.begin() as conn:

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind = async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False, 
        autoflush=False
    )

    async with Session() as session:
        yield session
