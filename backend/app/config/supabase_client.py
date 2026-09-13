from supabase import create_client, Client

from app.config.settings import settings

# This client is used by the FastAPI backend only (never shipped to the
# browser). The backend does its own JWT-based authorization in the API layer
# before it ever touches Supabase, so it must use the service_role key and
# bypass Row Level Security — RLS is what protects the anon key that IS public
# (bundled into the frontend build). If RLS is enabled on the app tables with
# no anon-role policies (the recommended setup here), running this client on
# the anon key instead would make every backend query fail.
#
# Set SUPABASE_SERVICE_KEY in the backend's .env / deployment env vars.
_key = settings.supabase_service_key or settings.supabase_key
supabase: Client = create_client(settings.supabase_url, _key)
